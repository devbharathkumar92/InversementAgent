"""Topic 10 — the executable acquisition boundary.

`AcquisitionService` is the single entry point through which data enters
the system:

    request -> source vetting -> provider fetch -> normalization
            -> timestamp/freshness checks -> provenance -> evidence
            -> AcquisitionResult (ready for Topic 11 validation)

The stages are strictly ordered and every outcome is classified, so the
boundary fails closed rather than inferring intent.

Outcome classification is deliberate:

* REJECTED — the source or the *data* is not admissible (unapproved,
  unlicensed, disabled, rate-limited, bad timestamp, stale, no
  provenance). The system declines to admit it and never substitutes.
* FAILED — the provider itself could not deliver a well-formed payload
  (raised an error, or violated the payload contract).

Source vetting and the call-budget control reuse the existing
`src.common.acquisition.engine` implementations rather than duplicating
them.
"""

from __future__ import annotations

from typing import Any

from src.common.acquisition.engine import (
    SUPPORTED_KINDS,
    AcquisitionEngine,
    approve_source,
)
from src.common.quality.engine import is_fresh
from src.data_layer.acquire.contracts import (
    AcquisitionEvidence,
    AcquisitionRequest,
    AcquisitionResult,
    AcquisitionStatus,
    DataSource,
    FailureClass,
    MarketDataRecord,
    RateLimiter,
    SourceRegistry,
    build_acquisition_id,
    is_usable_timestamp,
    to_utc_iso,
)
from src.data_layer.acquire.providers import ProviderAdapter, ProviderError

SYNTHETIC_SOURCE_ID = "synthetic"

#: Fields a provider payload must contain to satisfy the provider contract.
_REQUIRED_PAYLOAD_FIELDS: tuple[str, ...] = ("price", "volume", "timestamp", "provenance")


def default_source_registry() -> SourceRegistry:
    """Return the default registry: the synthetic source only (REQ 10.3)."""
    registry = SourceRegistry(name="default")
    registry.register(
        DataSource(
            id=SYNTHETIC_SOURCE_ID,
            kind="market",
            authority="synthetic",
            license="internal-test",
            enabled=True,
        )
    )
    return registry


class AcquisitionService:
    """The controlled boundary through which market data is acquired."""

    def __init__(
        self,
        *,
        name: str,
        registry: SourceRegistry,
        provider: ProviderAdapter,
        rate_limiter: RateLimiter | None = None,
        engine: AcquisitionEngine | None = None,
    ) -> None:
        if not name.strip():
            raise ValueError("name must be non-empty")
        self.name = name
        self.registry = registry
        self.provider = provider
        self.rate_limiter = rate_limiter
        self.engine = engine or AcquisitionEngine(name=name)
        self._evidence: list[AcquisitionEvidence] = []

    # -- public API ---------------------------------------------------------

    def evidence_log(self) -> list[dict[str, Any]]:
        """Return the preserved acquisition evidence (REQ 10.20)."""
        return [item.to_dict() for item in self._evidence]

    def acquire(self, request: AcquisitionRequest) -> AcquisitionResult:
        """Acquire, normalize, prove and record one market-data record."""
        # 1. Source control: an unvetted source never reaches the provider.
        rejected = self._vet(request)
        if rejected is not None:
            return self._outcome(
                request,
                AcquisitionStatus.REJECTED,
                rejected[0],
                rejected[1],
                attempts=0,
            )

        if self.rate_limiter is not None and not self.rate_limiter.allow():
            return self._outcome(
                request,
                AcquisitionStatus.REJECTED,
                FailureClass.RATE_LIMITED,
                "configured call budget exhausted",
                attempts=0,
            )

        # 2. Fetch across the provider boundary.
        try:
            payload = self.provider.fetch(request)
        except ProviderError as exc:
            return self._outcome(
                request,
                AcquisitionStatus.FAILED,
                FailureClass.PROVIDER_ERROR,
                str(exc),
                attempts=1,
            )

        # 3. Provider contract: a response the provider could not shape.
        if not isinstance(payload, dict):
            return self._outcome(
                request,
                AcquisitionStatus.FAILED,
                FailureClass.MALFORMED_RESPONSE,
                "provider returned a non-mapping payload",
                attempts=1,
            )
        missing = [field for field in _REQUIRED_PAYLOAD_FIELDS if field not in payload]
        if missing:
            return self._outcome(
                request,
                AcquisitionStatus.FAILED,
                FailureClass.MALFORMED_RESPONSE,
                f"provider payload missing fields: {missing}",
                attempts=1,
            )
        price, volume = payload["price"], payload["volume"]
        if not isinstance(price, (int, float)) or not isinstance(volume, (int, float)):
            return self._outcome(
                request,
                AcquisitionStatus.FAILED,
                FailureClass.MALFORMED_RESPONSE,
                "price and volume must be numeric",
                attempts=1,
            )

        # 4. Admissibility of the delivered data: reject, never substitute.
        provenance = payload["provenance"]
        if not isinstance(provenance, dict) or not provenance.get("source_id"):
            return self._outcome(
                request,
                AcquisitionStatus.REJECTED,
                FailureClass.MISSING_PROVENANCE,
                "delivered data carries no traceable provenance (REQ 10.21)",
                attempts=1,
            )

        timestamp = payload["timestamp"]
        if not is_usable_timestamp(timestamp):
            return self._outcome(
                request,
                AcquisitionStatus.REJECTED,
                FailureClass.BAD_TIMESTAMP,
                f"delivered timestamp is not ISO-8601: {timestamp!r}",
                attempts=1,
            )

        timestamp_utc = to_utc_iso(timestamp)
        if not is_fresh(timestamp_utc, request.max_age_s, request.as_of):
            return self._outcome(
                request,
                AcquisitionStatus.REJECTED,
                FailureClass.STALE_DATA,
                f"data is older than {request.max_age_s}s as of {request.as_of}",
                attempts=1,
            )

        # 5. Normalize and attach provenance.
        acquisition_id = build_acquisition_id(
            request.source_id, request.asset, timestamp, float(price), float(volume)
        )
        record = MarketDataRecord(
            asset=request.asset,
            price=float(price),
            volume=float(volume),
            timestamp=timestamp,
            timestamp_utc=timestamp_utc,
            source_id=request.source_id,
            acquisition_id=acquisition_id,
        )
        full_provenance: dict[str, Any] = {
            "source_id": request.source_id,
            "fetched_at": provenance.get("fetched_at", timestamp),
            "acquisition_id": acquisition_id,
            "lineage": "source",
        }
        evidence = AcquisitionEvidence(
            acquisition_id=acquisition_id,
            source_id=request.source_id,
            asset=request.asset,
            status=AcquisitionStatus.ACQUIRED.value,
            failure_class=FailureClass.NONE.value,
            attempts=1,
            detail="",
            provenance=full_provenance,
            raw_payload=dict(payload),
        )
        self._evidence.append(evidence)
        return AcquisitionResult(
            status=AcquisitionStatus.ACQUIRED,
            failure_class=FailureClass.NONE,
            acquisition_id=acquisition_id,
            record=record,
            provenance=full_provenance,
            evidence=evidence,
            attempts=1,
        )

    # -- internals ----------------------------------------------------------

    def _vet(self, request: AcquisitionRequest) -> tuple[FailureClass, str] | None:
        """Apply the existing source-approval controls; fail closed."""
        try:
            source = self.registry.get(request.source_id)
        except KeyError:
            return FailureClass.UNAPPROVED_SOURCE, f"source {request.source_id!r} is not registered"

        if source.kind not in SUPPORTED_KINDS:
            return FailureClass.UNAPPROVED_SOURCE, f"unsupported source kind {source.kind!r}"

        decision = approve_source(
            {
                "id": source.id,
                "kind": source.kind,
                "authority": source.authority,
                "license": source.license,
                "primary": True,
            }
        )
        if decision["status"] != "approved":
            if not str(source.license).strip():
                return FailureClass.MISSING_LICENSE, f"source {source.id!r} has no usable license"
            return FailureClass.UNAPPROVED_SOURCE, f"source {source.id!r} is not approved"

        if not source.enabled:
            return FailureClass.DISABLED_SOURCE, f"source {source.id!r} is disabled"

        if source.kind != request.kind:
            return (
                FailureClass.UNAPPROVED_SOURCE,
                f"request kind {request.kind!r} does not match source kind {source.kind!r}",
            )
        return None

    def _outcome(
        self,
        request: AcquisitionRequest,
        status: AcquisitionStatus,
        failure_class: FailureClass,
        detail: str,
        *,
        attempts: int,
    ) -> AcquisitionResult:
        """Record and return a non-acquired outcome with preserved evidence."""
        evidence = AcquisitionEvidence(
            acquisition_id=build_acquisition_id(
                request.source_id, request.asset, request.as_of, 0.0, 0.0
            ),
            source_id=request.source_id,
            asset=request.asset,
            status=status.value,
            failure_class=failure_class.value,
            attempts=attempts,
            detail=detail,
            provenance={},
            raw_payload={},
        )
        self._evidence.append(evidence)
        return AcquisitionResult(
            status=status,
            failure_class=failure_class,
            acquisition_id=evidence.acquisition_id,
            record=None,
            provenance={},
            evidence=evidence,
            attempts=attempts,
            detail=detail,
        )
