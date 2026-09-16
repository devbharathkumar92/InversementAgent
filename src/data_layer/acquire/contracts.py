"""Topic 10 — acquisition boundary contracts.

Typed, deterministic contracts for the data-acquisition boundary that sits
between a *source* and the Topic 11 quality layer:

    SOURCE -> ACQUISITION -> NORMALIZATION -> [Topic 11 VALIDATION] -> downstream

These are pure data/validation types. They contain no network access, no
credentials, and no provider-specific logic; providers live in
`src.data_layer.acquire.providers`.

The control *rules* (approval criteria, latency, rate budgets, provenance
shaping) are intentionally not re-implemented here: they are reused from
`src.common.acquisition.engine`, which is the existing Topic 10 control
implementation.
"""

from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from src.common.acquisition.engine import rate_limit_exceeded
from src.common.quality.engine import is_valid_timestamp

#: The market-data fields a normalized record must carry (REQ 10.9.1).
DEFAULT_MARKET_FIELDS: tuple[str, ...] = (
    "asset",
    "price",
    "volume",
    "timestamp",
    "timestamp_utc",
    "source_id",
    "acquisition_id",
)


class AcquisitionStatus(StrEnum):
    """The terminal status of one acquisition attempt."""

    ACQUIRED = "ACQUIRED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


class FailureClass(StrEnum):
    """Classification of every acquisition outcome (REQ 10.18)."""

    NONE = "NONE"
    UNAPPROVED_SOURCE = "UNAPPROVED_SOURCE"
    MISSING_LICENSE = "MISSING_LICENSE"
    DISABLED_SOURCE = "DISABLED_SOURCE"
    RATE_LIMITED = "RATE_LIMITED"
    BAD_TIMESTAMP = "BAD_TIMESTAMP"
    STALE_DATA = "STALE_DATA"
    MISSING_PROVENANCE = "MISSING_PROVENANCE"
    MALFORMED_RESPONSE = "MALFORMED_RESPONSE"
    PROVIDER_ERROR = "PROVIDER_ERROR"


@dataclass(frozen=True)
class DataSource:
    """A declared data source under approval/licensing control (10.3)."""

    id: str
    kind: str
    authority: str
    license: str
    enabled: bool = True


@dataclass
class SourceRegistry:
    """The set of sources that may be acquired from (REQ 10.3/10.19)."""

    name: str = ""
    sources: dict[str, DataSource] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def register(self, source: DataSource) -> str:
        """Register a source; returns its id."""
        self.sources[source.id] = source
        return source.id

    def get(self, source_id: str) -> DataSource:
        """Return a registered source, raising `KeyError` if unknown."""
        return self.sources[source_id]


@dataclass(frozen=True)
class RateLimitPolicy:
    """Configured call budget for a source (REQ 10.17).

    `max_calls` of `None` means the budget is not enforced. `window_s` is
    the declared window from the SRS; enforcement is budget-based, matching
    the existing `rate_limit_exceeded` control, so it stays deterministic
    and free of wall-clock state.
    """

    max_calls: int | None = None
    window_s: float = 60.0


@dataclass
class RateLimiter:
    """Deterministic call-budget enforcement (REQ 10.17)."""

    policy: RateLimitPolicy = field(default_factory=RateLimitPolicy)
    calls: int = 0

    def allow(self) -> bool:
        """Consume one call; return whether it is within budget."""
        if self.policy.max_calls is None:
            return True
        if rate_limit_exceeded(self.calls, self.policy.max_calls):
            return False
        self.calls += 1
        return True


@dataclass(frozen=True)
class AcquisitionRequest:
    """A fully-specified acquisition request. Carries no credentials."""

    source_id: str
    asset: str
    kind: str
    timestamp: str
    as_of: str
    max_age_s: float = 3600.0


@dataclass(frozen=True)
class MarketDataRecord:
    """A normalized market-data record (REQ 10.9.1/10.21).

    `timestamp` preserves the source's own time semantics exactly as
    received; `timestamp_utc` is the explicit UTC representation.
    """

    asset: str
    price: float
    volume: float
    timestamp: str
    timestamp_utc: str
    source_id: str
    acquisition_id: str


@dataclass(frozen=True)
class AcquisitionEvidence:
    """Preserved, inspectable evidence of one acquisition (REQ 10.20/10.21)."""

    acquisition_id: str
    source_id: str
    asset: str
    status: str
    failure_class: str
    attempts: int
    detail: str
    provenance: dict[str, Any]
    raw_payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        """Return a deterministic, serialisable representation."""
        return asdict(self)


@dataclass(frozen=True)
class AcquisitionResult:
    """The bounded outcome of one acquisition attempt."""

    status: AcquisitionStatus
    failure_class: FailureClass
    acquisition_id: str
    record: MarketDataRecord | None
    provenance: dict[str, Any]
    evidence: AcquisitionEvidence
    attempts: int
    detail: str = ""


@dataclass(frozen=True)
class ProductionProviderStatus:
    """Explicit status of production market-data sourcing.

    `approved` is False because no approval/licensing decision for a
    production vendor exists in the repository. This makes the blocked
    state inspectable instead of implicitly inventing authorization.
    """

    approved: bool
    reason: str
    candidates: tuple[str, ...]


def production_provider_status() -> ProductionProviderStatus:
    """Return the current production-provider status: not authorized."""
    return ProductionProviderStatus(
        approved=False,
        reason=(
            "No production market-data vendor is authorized: REQ 10.3.1/10.3.4 require an "
            "explicit approval and licensing decision, and none exists in this repository."
        ),
        candidates=("yfinance",),
    )


def build_acquisition_id(
    source_id: str, asset: str, timestamp: str, price: float, volume: float
) -> str:
    """Return the deterministic acquisition id for an acquisition (10.21.2).

    Derived purely from the acquisition inputs, so repeated acquisition of
    identical data yields an identical id and no clock/randomness is used.
    """
    payload = "|".join((source_id, asset, timestamp, repr(float(price)), repr(float(volume))))
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return f"acq-{digest[:16]}"


def to_utc_iso(timestamp: str) -> str:
    """Return the UTC ISO-8601 representation of a source timestamp."""
    parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return parsed.astimezone(UTC).isoformat()


def is_usable_timestamp(timestamp: object) -> bool:
    """Return whether a payload timestamp is a valid ISO-8601 string."""
    return isinstance(timestamp, str) and is_valid_timestamp(timestamp)


def to_quality_record(record: MarketDataRecord) -> dict[str, Any]:
    """Adapt an acquired record into the Topic 11 validation input shape."""
    return {name: getattr(record, name) for name in DEFAULT_MARKET_FIELDS}


#: The runtime input fields that an acquired record can supply directly.
RUNTIME_MARKET_FIELDS: tuple[str, ...] = ("asset", "price", "volume", "fetched_at")


def runtime_market_fields(record: MarketDataRecord) -> dict[str, Any]:
    """Map an acquired record onto the runtime input fields it owns.

    Only market-observation fields are mapped. The analytics fields the
    runtime also needs (volatility, projected return, capital, ...) are
    *not* invented here: they stay the caller's explicit responsibility,
    so acquired data is never silently dressed up as analysis.
    """
    return {
        "asset": record.asset,
        "price": record.price,
        "volume": record.volume,
        "fetched_at": record.timestamp_utc,
    }
