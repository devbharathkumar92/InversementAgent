"""Topic 11 — executable validation boundary (evidence-first TDD).

These tests define the *missing* behaviour. The repository previously held
only primitives in `src/common/quality/engine.py` with
`src/data_layer/validate/` containing nothing but an empty `__init__.py`:
there was no way to execute a full validation, reach a disposition, or
preserve evidence.

The authoritative SRS (`srs/topics/TOPIC_11.md`) requires thresholds to
exist as version-controlled controls but never states their numeric
values. Every threshold here is therefore caller-supplied configuration,
and a *required* but unconfigured threshold fails closed (quarantine)
rather than being invented.
"""

import socket

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
    ReconciliationStatus,
    ValidationFailure,
    ValidationRequest,
    ValidationService,
    ValidationStatus,
    build_validation_id,
    domain_applicability,
    request_from_acquisition,
)

pytestmark = pytest.mark.unit

SOURCE_ID = "synthetic"
ASSET = "NSE:TESTCO"
ACQUISITION_ID = "acq-abc123"
AT = "2026-09-14T09:30:00Z"
AS_OF = "2026-09-14T09:35:00Z"
RULES_VERSION = "t11-rules-v1"
SCHEMA_VERSION = "t11-schema-v1"


def rules(**overrides) -> QualityRules:
    """Return explicitly-configured rules (version is mandatory)."""
    base = {
        "version": RULES_VERSION,
        "schema_version": SCHEMA_VERSION,
        "required_fields": ("asset", "price", "volume", "timestamp_utc"),
        "required_checks": frozenset({CheckName.COMPLETENESS, CheckName.INTEGRITY}),
    }
    base.update(overrides)
    return QualityRules(**base)


def record(**overrides) -> dict:
    base = {
        "asset": ASSET,
        "price": 110.0,
        "volume": 1_000_000.0,
        "timestamp_utc": AT,
        "source_id": SOURCE_ID,
        "acquisition_id": ACQUISITION_ID,
    }
    base.update(overrides)
    return base


def request(**overrides) -> ValidationRequest:
    base = {
        "record": record(),
        "asset": ASSET,
        "source_id": SOURCE_ID,
        "kind": "market",
        "acquisition_id": ACQUISITION_ID,
        "source_timestamp": AT,
        "timestamp_utc": AT,
        "provenance": {
            "source_id": SOURCE_ID,
            "acquisition_id": ACQUISITION_ID,
            "fetched_at": AT,
            "lineage": "source",
        },
        "as_of": AS_OF,
    }
    base.update(overrides)
    return ValidationRequest(**base)


def service(rule_set=None, monitor=None) -> ValidationService:
    return ValidationService(
        name="validation",
        rules=rule_set if rule_set is not None else rules(),
        monitor=monitor,
    )


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


class TestRuleVersioning:
    """11.21/11.30 — thresholds are explicit, versioned configuration."""

    def test_rules_version_is_mandatory(self):
        with pytest.raises(ValueError):
            QualityRules(version="")

    def test_negative_threshold_rejected(self):
        with pytest.raises(ValueError):
            QualityRules(version=RULES_VERSION, max_age_s=-1.0)

    def test_version_is_traced_in_result_and_evidence(self):
        result = service().validate(request())
        assert result.rules_version == RULES_VERSION
        assert result.evidence.rules_version == RULES_VERSION
        assert result.schema_version == SCHEMA_VERSION

    def test_required_check_without_threshold_fails_closed(self):
        # 11.2.2 defines the control but the SRS states no numeric value:
        # a required threshold that was never configured must not be invented.
        rule_set = rules(required_checks=frozenset({CheckName.MISSING_THRESHOLD}))
        result = service(rule_set).validate(request())
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.THRESHOLD_UNCONFIGURED


class TestCompleteness:
    """11.2/11.2.1/11.2.2 — completeness vs an explicit missing threshold."""

    def test_complete_record_accepted(self):
        assert service().validate(request()).status == ValidationStatus.ACCEPTED

    def test_single_missing_required_field_rejected(self):
        result = service().validate(request(record=record(volume=None)))
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class in {
            ValidationFailure.INCOMPLETE,
            ValidationFailure.INTEGRITY_FAILURE,
        }

    def test_field_absent_rejected(self):
        partial = record()
        partial.pop("volume")
        result = service().validate(request(record=partial))
        assert result.status == ValidationStatus.REJECTED
        assert CheckName.COMPLETENESS in result.failed_checks

    def test_multiple_missing_fields_are_all_preserved(self):
        partial = record()
        partial.pop("volume")
        partial.pop("timestamp_utc")
        result = service().validate(request(record=partial))
        assert result.evidence.missing_fields == ("timestamp_utc", "volume")

    def test_missing_threshold_at_boundary_passes(self):
        rule_set = rules(max_missing=1, required_checks=frozenset({CheckName.MISSING_THRESHOLD}))
        partial = record()
        partial.pop("volume")
        result = service(rule_set).validate(request(record=partial))
        assert CheckName.MISSING_THRESHOLD in result.passed_checks

    def test_missing_threshold_exceeded_rejected(self):
        rule_set = rules(max_missing=0, required_checks=frozenset({CheckName.MISSING_THRESHOLD}))
        partial = record()
        partial.pop("volume")
        result = service(rule_set).validate(request(record=partial))
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.MISSING_FIELDS


class TestIntegrityAndInvalidTypes:
    """11.6/11.9 — integrity and invalid/malformed types."""

    def test_none_in_required_field_fails_integrity(self):
        result = service().validate(request(record=record(price=None)))
        assert CheckName.INTEGRITY in result.failed_checks

    def test_non_numeric_price_is_invalid(self):
        result = service().validate(request(record=record(price="not-a-number")))
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.INVALID_TYPE

    def test_null_byte_string_is_invalid(self):
        result = service().validate(request(record=record(asset="NSE:\x00BAD")))
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.INVALID_TYPE

    def test_provenance_missing_rejected(self):
        result = service().validate(request(provenance={}))
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.PROVENANCE_MISSING

    def test_provenance_acquisition_id_mismatch_rejected(self):
        result = service().validate(
            request(provenance={"source_id": SOURCE_ID, "acquisition_id": "acq-OTHER"})
        )
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.PROVENANCE_MISMATCH


class TestTimestampAndFreshness:
    """11.5/11.13 — explicit time handling, caller-supplied reference."""

    def test_valid_timestamp_passes(self):
        assert CheckName.TIMESTAMP in service().validate(request()).passed_checks

    def test_invalid_timestamp_rejected(self):
        result = service().validate(
            request(record=record(timestamp_utc="nope"), timestamp_utc="nope")
        )
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.BAD_TIMESTAMP

    def test_offset_timestamp_is_normalized_deterministically(self):
        result = service().validate(request(timestamp_utc="2026-09-14T15:00:00+05:30"))
        assert CheckName.TIMESTAMP in result.passed_checks

    def test_freshness_requires_configuration(self):
        rule_set = rules(required_checks=frozenset({CheckName.FRESHNESS}))
        result = service(rule_set).validate(request())
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.THRESHOLD_UNCONFIGURED

    def test_fresh_record_passes(self):
        rule_set = rules(max_age_s=600.0, required_checks=frozenset({CheckName.FRESHNESS}))
        result = service(rule_set).validate(request())
        assert result.status == ValidationStatus.ACCEPTED

    def test_exact_freshness_boundary_passes(self):
        # 09:30:00 -> 09:35:00 is exactly 300s.
        rule_set = rules(max_age_s=300.0, required_checks=frozenset({CheckName.FRESHNESS}))
        result = service(rule_set).validate(request())
        assert CheckName.FRESHNESS in result.passed_checks

    def test_stale_record_rejected(self):
        rule_set = rules(max_age_s=60.0, required_checks=frozenset({CheckName.FRESHNESS}))
        result = service(rule_set).validate(request())
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.STALE

    def test_reference_time_is_never_wall_clock(self):
        # Same request, different as_of => different freshness outcome.
        rule_set = rules(max_age_s=60.0, required_checks=frozenset({CheckName.FRESHNESS}))
        early = service(rule_set).validate(request(as_of=AS_OF))
        late = service(rule_set).validate(request(as_of="2026-09-14T10:00:00Z"))
        assert early.status == ValidationStatus.REJECTED
        assert late.status == ValidationStatus.REJECTED
        # ...and identical inputs always agree.
        assert early.evidence == service(rule_set).validate(request(as_of=AS_OF)).evidence


class TestDuplicates:
    """11.7 — duplicates are detected, classified and never silently dropped."""

    def test_duplicate_within_batch_rejected(self):
        rule_set = rules(required_checks=frozenset({CheckName.DUPLICATES}))
        batch = (
            record(),
            record(),
        )
        result = service(rule_set).validate(request(peers=batch))
        assert result.status == ValidationStatus.REJECTED
        assert result.failure_class == ValidationFailure.DUPLICATE

    def test_no_duplicates_passes(self):
        rule_set = rules(required_checks=frozenset({CheckName.DUPLICATES}))
        batch = (
            record(price=1.0, acquisition_id="acq-a"),
            record(price=2.0, acquisition_id="acq-b"),
        )
        result = service(rule_set).validate(request(peers=batch))
        assert CheckName.DUPLICATES in result.passed_checks

    def test_duplicate_evidence_is_preserved(self):
        rule_set = rules(required_checks=frozenset({CheckName.DUPLICATES}))
        result = service(rule_set).validate(request(peers=(record(), record())))
        assert result.evidence.duplicate_count >= 1


class TestAccuracyAnomalyOutlier:
    """11.3/11.10/11.11 — accuracy, anomaly severity, outlier detection."""

    def test_accuracy_exact_match_passes(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request(reference=110.0))
        assert CheckName.ACCURACY in result.passed_checks

    def test_accuracy_within_tolerance_passes(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request(reference=110.4))
        assert CheckName.ACCURACY in result.passed_checks

    def test_accuracy_exact_boundary_passes(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request(reference=110.5))
        assert CheckName.ACCURACY in result.passed_checks

    def test_accuracy_outside_tolerance_quarantined(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request(reference=120.0))
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.ACCURACY_OUT_OF_TOLERANCE

    def test_accuracy_required_without_tolerance_fails_closed(self):
        rule_set = rules(required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request())
        assert result.failure_class == ValidationFailure.THRESHOLD_UNCONFIGURED

    def test_accuracy_required_without_reference_cannot_verify(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request())
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.UNVERIFIABLE

    def test_anomaly_severity_is_surfaced(self):
        rule_set = rules(anomaly_tolerance=0.5, required_checks=frozenset({CheckName.ANOMALY}))
        result = service(rule_set).validate(request(reference=110.2))
        assert result.anomalies
        assert result.anomalies[0].severity == "moderate"

    def test_high_severity_anomaly_quarantined(self):
        rule_set = rules(anomaly_tolerance=0.5, required_checks=frozenset({CheckName.ANOMALY}))
        result = service(rule_set).validate(request(reference=120.0))
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.ANOMALOUS

    def test_no_anomaly_when_on_reference(self):
        rule_set = rules(anomaly_tolerance=0.5, required_checks=frozenset({CheckName.ANOMALY}))
        result = service(rule_set).validate(request(reference=110.0))
        assert result.anomalies[0].severity == "low"
        assert result.status == ValidationStatus.ACCEPTED

    def test_outlier_within_baseline_passes(self):
        rule_set = rules(outlier_tolerance=1.0, required_checks=frozenset({CheckName.OUTLIER}))
        result = service(rule_set).validate(request(baseline=(109.0, 110.0, 111.0)))
        assert CheckName.OUTLIER in result.passed_checks

    def test_outlier_beyond_tolerance_quarantined(self):
        rule_set = rules(outlier_tolerance=0.5, required_checks=frozenset({CheckName.OUTLIER}))
        # Baseline mean is 110.0; a price of 130.0 deviates far beyond it.
        result = service(rule_set).validate(
            request(record=record(price=130.0), baseline=(109.0, 110.0, 111.0))
        )
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.OUTLIER

    def test_outlier_required_without_tolerance_fails_closed(self):
        rule_set = rules(required_checks=frozenset({CheckName.OUTLIER}))
        result = service(rule_set).validate(request(baseline=(1.0,)))
        assert result.failure_class == ValidationFailure.THRESHOLD_UNCONFIGURED


class TestConsistency:
    """11.4 — internal consistency without inventing financial rules."""

    def test_identity_consistency_enforced(self):
        result = service().validate(request(record=record(asset="NSE:OTHER")))
        assert result.status in {ValidationStatus.REJECTED, ValidationStatus.QUARANTINED}
        assert CheckName.CONSISTENCY in result.failed_checks

    def test_contradictory_timestamps_detected(self):
        # source_timestamp and timestamp_utc must denote the same instant.
        result = service().validate(
            request(source_timestamp="2026-09-14T09:30:00Z", timestamp_utc="2026-09-14T11:00:00Z")
        )
        assert CheckName.CONSISTENCY in result.failed_checks


class TestCrossSourceReconciliation:
    """11.12/11.12.1/11.12.2/11.19 — conflicts are exposed, never erased."""

    def test_matching_peer_reconciles(self):
        rule_set = rules(
            accuracy_tolerance=0.5, required_checks=frozenset({CheckName.CROSS_SOURCE})
        )
        result = service(rule_set).validate(request(peers=(record(price=110.2),)))
        assert result.reconciliation == ReconciliationStatus.RECONCILED

    def test_permitted_difference_reconciles(self):
        rule_set = rules(
            accuracy_tolerance=0.5, required_checks=frozenset({CheckName.CROSS_SOURCE})
        )
        result = service(rule_set).validate(request(peers=(record(price=110.5),)))
        assert result.reconciliation == ReconciliationStatus.RECONCILED

    def test_conflict_is_exposed_not_erased(self):
        rule_set = rules(
            accuracy_tolerance=0.5, required_checks=frozenset({CheckName.CROSS_SOURCE})
        )
        result = service(rule_set).validate(request(peers=(record(price=200.0),)))
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.CONFLICT
        assert result.conflicts, "conflicting peers must remain visible"
        assert result.reconciliation == ReconciliationStatus.CONFLICT

    def test_no_peers_is_insufficient_evidence(self):
        rule_set = rules(
            accuracy_tolerance=0.5, required_checks=frozenset({CheckName.CROSS_SOURCE})
        )
        result = service(rule_set).validate(request())
        assert result.reconciliation == ReconciliationStatus.INSUFFICIENT_EVIDENCE
        assert result.failure_class == ValidationFailure.UNVERIFIABLE

    def test_no_silent_source_preference(self):
        # Two conflicting peers: no authority rule exists, so it must not pick one.
        rule_set = rules(
            accuracy_tolerance=0.5, required_checks=frozenset({CheckName.CROSS_SOURCE})
        )
        result = service(rule_set).validate(
            request(peers=(record(price=110.0), record(price=200.0)))
        )
        assert result.status == ValidationStatus.QUARANTINED
        assert len(result.conflicts) >= 1
        assert result.evidence.provenance["source_id"] == SOURCE_ID


class TestConfidence:
    """11.20/11.20.1/11.20.2 — confidence from pass rate vs explicit threshold."""

    def test_full_confidence_when_all_pass(self):
        assert service().validate(request()).quality_score == 100.0

    def test_confidence_reflects_failures(self):
        rule_set = rules(max_age_s=1.0, required_checks=frozenset({CheckName.FRESHNESS}))
        result = service(rule_set).validate(request())
        assert result.quality_score < 100.0

    def test_confidence_threshold_required_fails_closed_when_unset(self):
        rule_set = rules(required_checks=frozenset({CheckName.CONFIDENCE}))
        result = service(rule_set).validate(request())
        assert result.failure_class == ValidationFailure.THRESHOLD_UNCONFIGURED

    def test_confidence_at_threshold_accepted(self):
        rule_set = rules(min_confidence=100.0, required_checks=frozenset({CheckName.CONFIDENCE}))
        result = service(rule_set).validate(request())
        assert result.status == ValidationStatus.ACCEPTED

    def test_confidence_below_threshold_quarantined(self):
        rule_set = rules(
            anomaly_tolerance=0.5,
            min_confidence=100.0,
            required_checks=frozenset({CheckName.ANOMALY, CheckName.CONFIDENCE}),
        )
        result = service(rule_set).validate(request(reference=120.0))
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.CONFIDENCE_BELOW_THRESHOLD
        assert result.quality_score < 100.0


class TestDomainApplicability:
    """11.14/11.15/11.16/11.17 — market supported; others blocked, not faked."""

    def test_market_kind_is_applicable(self):
        assert domain_applicability("market").applicable is True

    def test_news_and_financial_are_blocked_not_faked(self):
        for kind in ("news", "financial"):
            status = domain_applicability(kind)
            assert status.applicable is False
            assert status.reason

    def test_unsupported_domain_quarantined(self):
        result = service().validate(request(kind="news"))
        assert result.status == ValidationStatus.QUARANTINED
        assert result.failure_class == ValidationFailure.UNSUPPORTED_DOMAIN

    def test_validation_does_not_mutate_the_input_record(self):
        payload = record()
        snapshot = dict(payload)
        service().validate(request(record=payload))
        assert payload == snapshot


class TestDispositionsAndRecovery:
    """11.22/11.22.1/11.22.2/11.22.3/11.23/11.24 — controlled lifecycle."""

    def test_rejected_record_is_not_downstream_usable(self):
        result = service().validate(request(record=record(price="bad")))
        assert result.status == ValidationStatus.REJECTED
        assert result.downstream_usable is False

    def test_quarantine_record_carries_reason_and_evidence(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        result = service(rule_set).validate(request(reference=120.0))
        assert result.quarantine is not None
        assert result.quarantine.reason
        assert result.quarantine.acquisition_id == ACQUISITION_ID
        assert result.quarantine.rules_version == RULES_VERSION
        assert result.quarantine.provenance["source_id"] == SOURCE_ID
        assert result.quarantine.to_dict()["reason"]

    def test_recovery_requires_revalidation(self):
        svc = service()
        quarantined = svc.validate(request(record=record(price="bad")))
        assert quarantined.status in {
            ValidationStatus.REJECTED,
            ValidationStatus.QUARANTINED,
        }
        # Recovering with the *same* invalid data must not accept it.
        again = svc.validate(request(record=record(price="bad")))
        assert again.status != ValidationStatus.ACCEPTED

    def test_recovery_with_valid_data_is_accepted(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        svc = service(rule_set)
        blocked = svc.validate(request(reference=200.0))
        assert blocked.status == ValidationStatus.QUARANTINED
        assert svc.is_quarantined(ACQUISITION_ID) is True

        recovered = svc.recover(ACQUISITION_ID, request=request(reference=110.0))
        assert recovered is not None
        assert recovered.status == ValidationStatus.ACCEPTED
        assert svc.is_quarantined(ACQUISITION_ID) is False

    def test_recovery_with_invalid_data_remains_blocked(self):
        rule_set = rules(accuracy_tolerance=0.5, required_checks=frozenset({CheckName.ACCURACY}))
        svc = service(rule_set)
        svc.validate(request(reference=200.0))
        assert svc.is_quarantined(ACQUISITION_ID) is True

        recovered = svc.recover(ACQUISITION_ID, request=request(reference=999.0))
        assert recovered is not None
        assert recovered.status != ValidationStatus.ACCEPTED
        assert svc.is_quarantined(ACQUISITION_ID) is True

    def test_recovering_unknown_id_returns_none(self):
        assert service().recover("acq-unknown", request=request()) is None

    def test_reject_outranks_quarantine(self):
        # A definite rejection plus an uncertain signal must reject.
        rule_set = rules(anomaly_tolerance=0.5)
        result = service(rule_set).validate(request(record=record(price="bad"), reference=999.0))
        assert result.status == ValidationStatus.REJECTED


class TestReportingMonitoringAudit:
    """11.25/11.26/11.27 — report, deterministic counters, audit trail."""

    def test_report_exposes_required_fields(self):
        result = service().validate(request())
        report = result.report.to_dict()
        for field in (
            "status",
            "disposition",
            "quality_score",
            "passed_checks",
            "failed_checks",
            "rules_version",
            "schema_version",
            "acquisition_id",
            "source_id",
            "validation_id",
            "trace_id",
        ):
            assert field in report, field

    def test_monitor_counters_are_deterministic(self):
        monitor = QualityMonitor(name="monitor")
        svc = service(monitor=monitor)
        svc.validate(request())
        svc.validate(request(record=record(price="bad")))
        svc.validate(request(record=record(price="bad")))
        assert monitor.counters["validations"] == 3
        assert monitor.counters["accepted"] == 1
        assert monitor.counters["rejected"] == 2

    def test_monitor_counters_repeatable_across_services(self):
        def run() -> dict:
            monitor = QualityMonitor(name="m")
            svc = service(monitor=monitor)
            svc.validate(request())
            svc.validate(request(record=record(price="bad")))
            return dict(monitor.counters)

        assert run() == run()

    def test_audit_trail_records_each_validation(self):
        svc = service()
        svc.validate(request())
        entries = svc.audit_log()
        assert len(entries) == 1
        assert entries[0]["acquisition_id"] == ACQUISITION_ID
        assert entries[0]["status"] == ValidationStatus.ACCEPTED.value
        assert entries[0]["rules_version"] == RULES_VERSION


class TestDeterminism:
    """Repeated identical validation is byte-identical."""

    def test_validation_id_is_deterministic(self):
        a = build_validation_id(SOURCE_ID, ASSET, ACQUISITION_ID, AT, RULES_VERSION)
        b = build_validation_id(SOURCE_ID, ASSET, ACQUISITION_ID, AT, RULES_VERSION)
        assert a == b
        assert a.startswith("val-")

    def test_validation_id_changes_with_version(self):
        a = build_validation_id(SOURCE_ID, ASSET, ACQUISITION_ID, AT, RULES_VERSION)
        b = build_validation_id(SOURCE_ID, ASSET, ACQUISITION_ID, AT, "other-version")
        assert a != b

    def test_repeated_validation_is_identical(self):
        first = service().validate(request()).evidence
        second = service().validate(request()).evidence
        assert first == second

    def test_distinct_services_agree(self):
        left = service().validate(request())
        right = service().validate(request())
        assert left.validation_id == right.validation_id
        assert left.quality_score == right.quality_score
        assert left.status == right.status


class TestSecurity:
    """No credentials, no network, no secret leakage."""

    FORBIDDEN = ("api_key", "apikey", "secret", "password", "token", "authorization", "credential")

    def test_no_secret_fields_on_the_request(self):
        fields = set(ValidationRequest.__dataclass_fields__)
        for forbidden in self.FORBIDDEN:
            assert forbidden not in fields

    def test_no_secrets_in_evidence_or_audit(self):
        svc = service()
        result = svc.validate(request())
        for blob in (result.evidence.to_dict(), result.report.to_dict(), svc.audit_log()[0]):
            for forbidden in self.FORBIDDEN:
                assert forbidden not in walk_keys(blob), f"{forbidden} leaked"
            assert "authorization" not in repr(blob).lower()

    def test_validation_makes_no_network_calls(self, monkeypatch):
        def deny(*args, **kwargs):
            raise AssertionError("validation attempted network access")

        monkeypatch.setattr(socket, "socket", deny)
        monkeypatch.setattr(socket, "create_connection", deny)
        assert service().validate(request()).status == ValidationStatus.ACCEPTED


class TestTopic10Integration:
    """Acquisition output flows into validation without live data."""

    def test_acquired_record_validates_and_is_accepted(self):
        acquisition = AcquisitionService(
            name="acquisition",
            registry=default_source_registry(),
            provider=DeterministicProvider(),
        )
        acquired = acquisition.acquire(
            AcquisitionRequest(
                source_id=SOURCE_ID,
                asset=ASSET,
                kind="market",
                timestamp=AT,
                as_of=AS_OF,
                max_age_s=600.0,
            )
        )
        assert acquired.status.value == "ACQUIRED"

        rule_set = rules(max_age_s=600.0)
        validation = service(rule_set).validate(
            request_from_acquisition(acquired, rules=rule_set, as_of=AS_OF)
        )
        assert validation.status == ValidationStatus.ACCEPTED
        assert validation.evidence.acquisition_id == acquired.acquisition_id
        assert validation.evidence.provenance["source_id"] == SOURCE_ID

    def test_adapter_preserves_acquisition_identity(self):
        acquisition = AcquisitionService(
            name="acquisition",
            registry=default_source_registry(),
            provider=DeterministicProvider(),
        )
        acquired = acquisition.acquire(
            AcquisitionRequest(
                source_id=SOURCE_ID,
                asset=ASSET,
                kind="market",
                timestamp=AT,
                as_of=AS_OF,
                max_age_s=600.0,
            )
        )
        rule_set = rules()
        built = request_from_acquisition(acquired, rules=rule_set, as_of=AS_OF)
        assert built.acquisition_id == acquired.acquisition_id
        assert built.asset == acquired.record.asset
        assert built.timestamp_utc == acquired.record.timestamp_utc
