"""Topic 10 — Data Acquisition Layer (executable boundary).

The repository previously held only control-oriented helpers in
`src.common.acquisition.engine`; this package turns them into an
executable, isolated acquisition boundary:

    SOURCE -> ACQUISITION -> NORMALIZATION -> [Topic 11 VALIDATION] -> downstream

It is deterministic and offline: the only registered provider is
`DeterministicProvider`, there are no credentials, and no live vendor is
authorized (see `production_provider_status()`).

Usage:

    service = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    result = service.acquire(request)
"""

from src.data_layer.acquire.contracts import (
    DEFAULT_MARKET_FIELDS,
    RUNTIME_MARKET_FIELDS,
    AcquisitionEvidence,
    AcquisitionRequest,
    AcquisitionResult,
    AcquisitionStatus,
    DataSource,
    FailureClass,
    MarketDataRecord,
    ProductionProviderStatus,
    RateLimiter,
    RateLimitPolicy,
    SourceRegistry,
    build_acquisition_id,
    is_usable_timestamp,
    production_provider_status,
    runtime_market_fields,
    to_quality_record,
    to_utc_iso,
)
from src.data_layer.acquire.providers import (
    DeterministicProvider,
    ProviderAdapter,
    ProviderError,
)
from src.data_layer.acquire.service import (
    SYNTHETIC_SOURCE_ID,
    AcquisitionService,
    default_source_registry,
)

__all__ = [
    "DEFAULT_MARKET_FIELDS",
    "RUNTIME_MARKET_FIELDS",
    "SYNTHETIC_SOURCE_ID",
    "AcquisitionEvidence",
    "AcquisitionRequest",
    "AcquisitionResult",
    "AcquisitionService",
    "AcquisitionStatus",
    "DataSource",
    "DeterministicProvider",
    "FailureClass",
    "MarketDataRecord",
    "ProductionProviderStatus",
    "ProviderAdapter",
    "ProviderError",
    "RateLimitPolicy",
    "RateLimiter",
    "SourceRegistry",
    "build_acquisition_id",
    "default_source_registry",
    "is_usable_timestamp",
    "production_provider_status",
    "runtime_market_fields",
    "to_quality_record",
    "to_utc_iso",
]
