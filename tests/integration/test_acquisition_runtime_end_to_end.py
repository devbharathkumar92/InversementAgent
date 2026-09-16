"""Integration proof: Topic 10 acquisition boundary -> Topic 11 -> runtime.

This is the executable evidence for the claim that the new acquisition
boundary feeds the *existing* runtime without changing it:

* acquired records are the provenance-bearing INPUT for a bounded run;
* the run stays deterministic and paper-only;
* the default `SyntheticInput` path is untouched (no live data required).

Nothing here touches a network, a broker, or a credential.
"""

import pytest

from src.data_layer.acquire import (
    AcquisitionRequest,
    AcquisitionService,
    AcquisitionStatus,
    DeterministicProvider,
    default_source_registry,
    runtime_market_fields,
    to_quality_record,
)
from src.task_runtime.orchestration import (
    RunStatus,
    RuntimeOrchestrator,
    RuntimePolicy,
    SyntheticInput,
)

pytestmark = pytest.mark.integration

AT = "2026-09-14T09:30:00Z"
AS_OF = "2026-09-14T09:35:00Z"
ASSET = "NSE:TESTCO"


def acquired_record():
    service = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    return service.acquire(
        AcquisitionRequest(
            source_id="synthetic",
            asset=ASSET,
            kind="market",
            timestamp=AT,
            as_of=AS_OF,
            max_age_s=600.0,
        )
    )


def runtime_input(**overrides) -> SyntheticInput:
    data = {
        "asset": ASSET,
        "price": 110.0,
        "prior_price": 100.0,
        "volume": 1_000_000.0,
        "avg_volume": 100_000.0,
        "volatility": 0.40,
        "normal_volatility": 0.20,
        "liquidity": 0.90,
        "regime_ok": True,
        "projected_return": 0.10,
        "risk": 0.15,
        "reward": 4.0,
        "risk_amount": 1.5,
        "signal": "buy",
        "fetched_at": AT,
        "as_of": AS_OF,
        "capital": 100_000.0,
        "virtual_capital": 100_000.0,
    }
    data.update(overrides)
    return SyntheticInput(**data)


def test_acquired_data_validates_then_runs_end_to_end():
    acquired = acquired_record()
    assert acquired.status == AcquisitionStatus.ACQUIRED

    # Topic 11 shape is satisfied by the acquired record...
    quality_record = to_quality_record(acquired.record)
    assert all(value is not None for value in quality_record.values())

    # ...and the acquired market fields are the runtime INPUT provenance.
    market = runtime_market_fields(acquired.record)
    result = RuntimeOrchestrator(name="acquisition-runtime").run(runtime_input(**market))

    assert result.status == RunStatus.COMPLETED
    assert result.input["provenance"]["fetched_at"] == acquired.record.timestamp_utc
    assert result.input["asset"] == ASSET
    assert result.paper_only is True


def test_acquired_run_is_deterministic():
    acquired = acquired_record()
    market = runtime_market_fields(acquired.record)

    first = RuntimeOrchestrator(name="r").run(runtime_input(**market)).to_dict()
    second = RuntimeOrchestrator(name="r").run(runtime_input(**market)).to_dict()
    assert first == second


def test_default_synthetic_runtime_path_is_unchanged():
    # The pre-existing contract: a synthetic run needs no acquisition at all.
    result = RuntimeOrchestrator(name="r", policy=RuntimePolicy()).run(runtime_input())
    assert result.status == RunStatus.COMPLETED
    assert result.input["source"] == "synthetic"
    assert result.input["provenance"]["source_id"] == "synthetic"
    assert result.stage_order[0] == "INPUT"


def test_rejected_acquisition_never_reaches_the_runtime():
    service = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    rejected = service.acquire(
        AcquisitionRequest(
            source_id="unregistered",
            asset=ASSET,
            kind="market",
            timestamp=AT,
            as_of=AS_OF,
            max_age_s=600.0,
        )
    )
    assert rejected.status == AcquisitionStatus.REJECTED
    # No record means no runtime input can be constructed from it.
    assert rejected.record is None
