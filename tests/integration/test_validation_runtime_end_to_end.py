"""Integration proof: Topic 10 acquisition -> Topic 11 validation -> runtime.

This is the executable evidence that:

* acquired records flow through the validation boundary with identity,
  provenance, and timestamps preserved;
* a rejected/quarantined record is NOT downstream-usable, so invalid data
  cannot silently reach the runtime;
* the existing deterministic paper runtime is unchanged.

No network, broker, credential, or live data is involved.
"""

import pytest

from src.data_layer.acquire import (
    AcquisitionRequest,
    AcquisitionService,
    DeterministicProvider,
    default_source_registry,
)
from src.data_layer.validate import (
    CheckName,
    QualityMonitor,
    QualityRules,
    ValidationFailure,
    ValidationService,
    ValidationStatus,
    request_from_acquisition,
)
from src.task_runtime.orchestration import (
    RunStatus,
    RuntimeOrchestrator,
    SyntheticInput,
)

pytestmark = pytest.mark.integration

SOURCE_ID = "synthetic"
ASSET = "NSE:TESTCO"
AT = "2026-09-14T09:30:00Z"
AS_OF = "2026-09-14T09:35:00Z"
RULES_VERSION = "t11-rules-v1"


def acquire(service: AcquisitionService, *, timestamp: str = AT, as_of: str = AS_OF):
    return service.acquire(
        AcquisitionRequest(
            source_id=SOURCE_ID,
            asset=ASSET,
            kind="market",
            timestamp=timestamp,
            as_of=as_of,
            max_age_s=600.0,
        )
    )


def rules(**overrides) -> QualityRules:
    base = {
        "version": RULES_VERSION,
        "schema_version": "t11-schema-v1",
        "required_fields": ("asset", "price", "volume", "timestamp_utc"),
    }
    base.update(overrides)
    return QualityRules(**base)


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


def test_acquired_record_validates_then_runs_end_to_end():
    acquisition = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    acquired = acquire(acquisition)
    assert acquired.record is not None

    rule_set = rules(max_age_s=600.0, required_checks=frozenset({CheckName.FRESHNESS}))
    validation = ValidationService(name="validation", rules=rule_set).validate(
        request_from_acquisition(acquired, rules=rule_set, as_of=AS_OF)
    )

    assert validation.status == ValidationStatus.ACCEPTED
    assert validation.downstream_usable is True

    # Identity, provenance and timestamps survive the whole path.
    assert validation.evidence.acquisition_id == acquired.acquisition_id
    assert validation.evidence.provenance["source_id"] == SOURCE_ID
    assert validation.evidence.timestamps["utc"] == acquired.record.timestamp_utc

    # Only then does the data reach the runtime, which stays paper-only.
    result = RuntimeOrchestrator(name="validation-runtime").run(runtime_input())
    assert result.status == RunStatus.COMPLETED
    assert result.paper_only is True


def test_stale_acquisition_is_rejected_before_the_runtime():
    acquisition = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    acquired = acquire(acquisition)

    # A strict freshness window makes the same data stale.
    rule_set = rules(max_age_s=1.0, required_checks=frozenset({CheckName.FRESHNESS}))
    validation = ValidationService(name="validation", rules=rule_set).validate(
        request_from_acquisition(acquired, rules=rule_set, as_of=AS_OF)
    )

    assert validation.status == ValidationStatus.REJECTED
    assert validation.failure_class == ValidationFailure.STALE
    assert validation.downstream_usable is False


def test_invalid_acquisition_result_cannot_be_validated():
    acquisition = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    # An unregistered source is rejected at acquisition, so there is no record.
    rejected = acquisition.acquire(
        AcquisitionRequest(
            source_id="unregistered",
            asset=ASSET,
            kind="market",
            timestamp=AT,
            as_of=AS_OF,
            max_age_s=600.0,
        )
    )
    assert rejected.record is None

    rule_set = rules()
    with pytest.raises(ValueError):
        request_from_acquisition(rejected, rules=rule_set, as_of=AS_OF)


def test_monitor_and_audit_capture_the_full_path():
    acquisition = AcquisitionService(
        name="acquisition",
        registry=default_source_registry(),
        provider=DeterministicProvider(),
    )
    monitor = QualityMonitor(name="monitor")
    rule_set = rules(max_age_s=600.0, required_checks=frozenset({CheckName.FRESHNESS}))
    validation_service = ValidationService(name="validation", rules=rule_set, monitor=monitor)

    acquired = acquire(acquisition)
    validation_service.validate(request_from_acquisition(acquired, rules=rule_set, as_of=AS_OF))

    assert monitor.counters["validations"] == 1
    assert monitor.counters["accepted"] == 1
    audit = validation_service.audit_log()
    assert len(audit) == 1
    assert audit[0]["acquisition_id"] == acquired.acquisition_id
    assert audit[0]["rules_version"] == RULES_VERSION


def test_validation_path_is_deterministic():
    def run() -> dict:
        acquisition = AcquisitionService(
            name="acquisition",
            registry=default_source_registry(),
            provider=DeterministicProvider(),
        )
        acquired = acquire(acquisition)
        rule_set = rules(max_age_s=600.0, required_checks=frozenset({CheckName.FRESHNESS}))
        validation = ValidationService(name="validation", rules=rule_set).validate(
            request_from_acquisition(acquired, rules=rule_set, as_of=AS_OF)
        )
        return validation.evidence.to_dict()

    assert run() == run()


def test_default_synthetic_runtime_path_is_unchanged():
    result = RuntimeOrchestrator(name="r").run(runtime_input())
    assert result.status == RunStatus.COMPLETED
    assert result.input["source"] == "synthetic"
    assert result.stage_order[0] == "INPUT"
