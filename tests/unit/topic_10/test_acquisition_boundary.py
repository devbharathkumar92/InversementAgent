"""Topic 10 — executable data-acquisition boundary (evidence-first TDD).

These tests define the *missing* behaviour: the repository previously held
only control-oriented helpers in `src/common/acquisition/engine.py`, with
`src/data_layer/acquire/` containing nothing but an empty `__init__.py`.
There was no way to actually acquire, normalize, prove, or preserve a
market-data record.

Scope is deliberately synthetic/deterministic: no live provider, no
credentials, no network. Source vetting reuses the existing engine
controls rather than reimplementing them.
"""

import socket

import pytest

from src.common.acquisition.engine import SUPPORTED_KINDS
from src.common.quality.engine import QualityEngine, is_fresh, is_valid_timestamp
from src.data_layer.acquire import (
    DEFAULT_MARKET_FIELDS,
    AcquisitionRequest,
    AcquisitionService,
    AcquisitionStatus,
    DataSource,
    DeterministicProvider,
    FailureClass,
    MarketDataRecord,
    RateLimiter,
    RateLimitPolicy,
    SourceRegistry,
    build_acquisition_id,
    default_source_registry,
    production_provider_status,
    to_quality_record,
)

pytestmark = pytest.mark.unit

SOURCE_ID = "synthetic"
ASSET = "NSE:TESTCO"
AT = "2026-09-14T09:30:00Z"
AS_OF = "2026-09-14T09:35:00Z"


def registry_with(**overrides) -> SourceRegistry:
    base = {
        "id": SOURCE_ID,
        "kind": "market",
        "authority": "exchange",
        "license": "commercial",
        "enabled": True,
    }
    base.update(overrides)
    reg = SourceRegistry(name="test-registry")
    reg.register(DataSource(**base))
    return reg


def service(provider=None, registry=None, limiter=None) -> AcquisitionService:
    return AcquisitionService(
        name="acquisition",
        registry=registry if registry is not None else default_source_registry(),
        provider=provider if provider is not None else DeterministicProvider(),
        rate_limiter=limiter,
    )


def request(**overrides) -> AcquisitionRequest:
    base = {
        "source_id": SOURCE_ID,
        "asset": ASSET,
        "kind": "market",
        "timestamp": AT,
        "as_of": AS_OF,
        "max_age_s": 600.0,
    }
    base.update(overrides)
    return AcquisitionRequest(**base)


def walk_keys(value) -> list[str]:
    """Collect every mapping key anywhere in a nested structure."""
    keys: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            keys.append(str(key).lower())
            keys.extend(walk_keys(item))
    elif isinstance(value, (list, tuple)):
        for item in value:
            keys.extend(walk_keys(item))
    return keys


class TestSourceRegistrationAndControl:
    """A/B — an executable boundary that refuses unapproved sources."""

    def test_source_registration(self):
        reg = registry_with()
        assert reg.get(SOURCE_ID).id == SOURCE_ID

    def test_unapproved_kind_rejected(self):
        # `kind` is not one of the SRS-approved source classes.
        result = service(registry=registry_with(kind="unclassified")).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.UNAPPROVED_SOURCE

    def test_unknown_authority_rejected(self):
        result = service(registry=registry_with(authority="")).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.UNAPPROVED_SOURCE

    def test_missing_license_rejected(self):
        result = service(registry=registry_with(license="")).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.MISSING_LICENSE

    def test_disabled_source_rejected(self):
        result = service(registry=registry_with(enabled=False)).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.DISABLED_SOURCE

    def test_unregistered_source_rejected(self):
        reg = SourceRegistry(name="empty")
        result = service(registry=reg).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.UNAPPROVED_SOURCE

    def test_rejection_never_reaches_the_provider(self):
        poisoned = DeterministicProvider(error="should not be called")
        result = service(provider=poisoned, registry=registry_with(license="")).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.attempts == 0

    def test_default_registry_registers_only_synthetic(self):
        reg = default_source_registry()
        assert set(reg.sources) == {SOURCE_ID}
        assert reg.get(SOURCE_ID).kind in SUPPORTED_KINDS


class TestDeterministicAcquisition:
    """D/E — a deterministic provider producing a typed, normalized record."""

    def test_deterministic_synthetic_acquisition(self):
        result = service().acquire(request())
        assert result.status == AcquisitionStatus.ACQUIRED
        assert result.failure_class == FailureClass.NONE
        assert result.record is not None
        assert result.attempts == 1

    def test_normalized_schema_is_typed(self):
        result = service().acquire(request())
        rec = result.record
        assert isinstance(rec, MarketDataRecord)
        assert isinstance(rec.price, float)
        assert isinstance(rec.volume, float)
        assert isinstance(rec.timestamp_utc, str)
        for name in DEFAULT_MARKET_FIELDS:
            assert hasattr(rec, name), name

    def test_record_carries_explicit_identifiers(self):
        result = service().acquire(request())
        assert result.record.source_id == SOURCE_ID
        assert result.record.asset == ASSET
        assert result.acquisition_id.startswith("acq-")

    def test_no_live_network_provider_is_registered(self):
        # Only the deterministic provider exists; nothing fetches a live feed.
        assert DeterministicProvider().name == "deterministic-synthetic"
        assert production_provider_status().approved is False


class TestTimeHandling:
    """F — source time semantics retained, UTC representation explicit."""

    def test_source_and_utc_timestamps_are_both_present(self):
        result = service().acquire(request(timestamp="2026-09-14T15:00:00+05:30"))
        rec = result.record
        assert rec.timestamp == "2026-09-14T15:00:00+05:30"
        assert rec.timestamp_utc == "2026-09-14T09:30:00+00:00"
        assert is_valid_timestamp(rec.timestamp_utc)

    def test_bad_timestamp_rejected(self):
        result = service(provider=DeterministicProvider(timestamp="not-a-timestamp")).acquire(
            request()
        )
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.BAD_TIMESTAMP

    def test_stale_data_rejected(self):
        result = service().acquire(request(as_of="2026-09-14T12:00:00Z", max_age_s=60.0))
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.STALE_DATA

    def test_fresh_data_within_window_accepted(self):
        result = service().acquire(request(as_of=AS_OF, max_age_s=600.0))
        assert result.status == AcquisitionStatus.ACQUIRED


class TestProvenanceAndEvidence:
    """G/H — traceable provenance and preservable evidence."""

    def test_provenance_is_attached(self):
        result = service().acquire(request())
        prov = result.provenance
        assert prov["source_id"] == SOURCE_ID
        assert prov["fetched_at"] == AT
        assert prov["acquisition_id"] == result.acquisition_id
        assert prov["lineage"] == "source"

    def test_missing_provenance_rejected(self):
        provider = DeterministicProvider(payload_override={"provenance": None})
        result = service(provider=provider).acquire(request())
        assert result.status == AcquisitionStatus.REJECTED
        assert result.failure_class == FailureClass.MISSING_PROVENANCE

    def test_evidence_is_preserved_and_inspectable(self):
        svc = service()
        result = svc.acquire(request())
        assert svc.evidence_log(), "evidence must be recorded"
        ev = result.evidence
        assert ev.acquisition_id == result.acquisition_id
        assert ev.source_id == SOURCE_ID
        assert ev.status == AcquisitionStatus.ACQUIRED.value
        assert ev.attempts == 1
        assert ev.raw_payload, "raw payload must be preserved (REQ 10.21)"
        assert ev.provenance["source_id"] == SOURCE_ID

    def test_failed_acquisition_still_records_evidence(self):
        svc = service(provider=DeterministicProvider(error="boom"))
        result = svc.acquire(request())
        assert result.status == AcquisitionStatus.FAILED
        assert svc.evidence_log()[0]["failure_class"] == FailureClass.PROVIDER_ERROR.value


class TestDeterminism:
    """Repeated acquisition with identical input is byte-identical."""

    def test_acquisition_id_is_deterministic(self):
        a = build_acquisition_id(SOURCE_ID, ASSET, AT, 110.0, 1_000_000.0)
        b = build_acquisition_id(SOURCE_ID, ASSET, AT, 110.0, 1_000_000.0)
        assert a == b
        assert a.startswith("acq-")

    def test_acquisition_id_changes_with_input(self):
        a = build_acquisition_id(SOURCE_ID, ASSET, AT, 110.0, 1_000_000.0)
        b = build_acquisition_id(SOURCE_ID, ASSET, AT, 111.0, 1_000_000.0)
        assert a != b

    def test_repeated_acquisition_is_identical(self):
        first = service().acquire(request()).evidence
        second = service().acquire(request()).evidence
        assert first == second

    def test_distinct_services_agree(self):
        left = service().acquire(request())
        right = service().acquire(request())
        assert left.acquisition_id == right.acquisition_id
        assert left.record == right.record


class TestRateLimits:
    """I — configured rate limits are enforced (REQ 10.17)."""

    def test_rate_limit_enforced(self):
        limiter = RateLimiter(policy=RateLimitPolicy(max_calls=2, window_s=60.0))
        svc = service(limiter=limiter)
        assert svc.acquire(request()).status == AcquisitionStatus.ACQUIRED
        assert svc.acquire(request()).status == AcquisitionStatus.ACQUIRED
        third = svc.acquire(request())
        assert third.status == AcquisitionStatus.REJECTED
        assert third.failure_class == FailureClass.RATE_LIMITED

    def test_under_limit_is_allowed(self):
        limiter = RateLimiter(policy=RateLimitPolicy(max_calls=5, window_s=60.0))
        svc = service(limiter=limiter)
        for _ in range(5):
            assert svc.acquire(request()).status == AcquisitionStatus.ACQUIRED


class TestFailureClassification:
    """J — failures are classified and propagated safely."""

    def test_provider_failure_classified(self):
        result = service(provider=DeterministicProvider(error="upstream unavailable")).acquire(
            request()
        )
        assert result.status == AcquisitionStatus.FAILED
        assert result.failure_class == FailureClass.PROVIDER_ERROR
        assert "upstream unavailable" in result.detail
        assert result.record is None

    def test_malformed_response_classified(self):
        provider = DeterministicProvider(payload_override={"price": None})
        result = service(provider=provider).acquire(request())
        assert result.status == AcquisitionStatus.FAILED
        assert result.failure_class == FailureClass.MALFORMED_RESPONSE

    def test_failure_carries_no_record(self):
        result = service(provider=DeterministicProvider(error="x")).acquire(request())
        assert result.record is None
        assert result.provenance == {}

    def test_every_outcome_has_a_failure_class(self):
        ok = service().acquire(request())
        bad = service(provider=DeterministicProvider(error="x")).acquire(request())
        assert ok.failure_class == FailureClass.NONE
        assert bad.failure_class != FailureClass.NONE


class TestSecurity:
    """M — no secrets anywhere in the boundary or its evidence."""

    FORBIDDEN = ("api_key", "apikey", "secret", "password", "token", "authorization", "credential")

    def test_no_secret_fields_in_evidence(self):
        svc = service()
        result = svc.acquire(request())
        for blob in (result.evidence.to_dict(), result.provenance, svc.evidence_log()[0]):
            keys = walk_keys(blob)
            for forbidden in self.FORBIDDEN:
                assert forbidden not in keys, f"{forbidden} leaked into evidence"
            assert "authorization" not in repr(blob).lower()

    def test_no_credential_inputs_on_the_request(self):
        fields = set(AcquisitionRequest.__dataclass_fields__)
        for forbidden in self.FORBIDDEN:
            assert forbidden not in fields

    def test_deterministic_provider_needs_no_credentials(self):
        # A provider that required credentials could not run fully offline.
        result = service().acquire(request())
        assert result.status == AcquisitionStatus.ACQUIRED

    def test_deterministic_provider_makes_no_network_calls(self, monkeypatch):
        def deny(*args, **kwargs):
            raise AssertionError("deterministic provider attempted network access")

        monkeypatch.setattr(socket, "socket", deny)
        monkeypatch.setattr(socket, "create_connection", deny)
        result = service().acquire(request())
        assert result.status == AcquisitionStatus.ACQUIRED
        assert result.record is not None


class TestTopic11Integration:
    """K — acquired data flows through the existing Topic 11 validation."""

    def test_acquired_record_passes_quality_validation(self):
        result = service().acquire(request())
        record = to_quality_record(result.record)

        assert all(record.get(name) is not None for name in DEFAULT_MARKET_FIELDS)
        quality = QualityEngine(name="quality")
        assert quality.integrity_ok(record, DEFAULT_MARKET_FIELDS) is True
        assert is_valid_timestamp(record["timestamp_utc"]) is True
        assert is_fresh(record["timestamp_utc"], 600.0, AS_OF.replace("Z", "+00:00")) is True

    def test_quality_validation_rejects_a_stale_record(self):
        # Same contract, stale window: Topic 11 rejects what Topic 10 would too.
        result = service().acquire(request())
        record = to_quality_record(result.record)
        assert is_fresh(record["timestamp_utc"], 1.0, "2026-09-15T00:00:00+00:00") is False


class TestProductionProviderStatus:
    """Production sourcing is explicitly BLOCKED, not invented."""

    def test_production_provider_is_not_approved(self):
        status = production_provider_status()
        assert status.approved is False
        assert status.reason
        assert "yfinance" in status.candidates

    def test_a_candidate_dependency_is_not_an_authorization(self):
        # `yfinance` is only a candidate; approval stays False regardless.
        status = production_provider_status()
        assert "yfinance" in status.candidates
        assert status.approved is False
