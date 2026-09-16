"""Topic 11 — the executable validation boundary.

`ValidationService.validate()` is the single entry point through which
acquired data is judged before it may reach downstream intelligence:

    acquired record -> domain applicability -> ordered checks
                    -> failure classification -> disposition
                    -> evidence + report + audit + counters

Disposition is derived from the failures, never chosen ad hoc:

* REJECTED     - the data is definitively invalid or inadmissible.
* QUARANTINED  - correctness is uncertain or unverifiable; isolated with a
                 reason and evidence until recovery revalidates it.
* ACCEPTED     - every required check passed.

The service consumes Topic 10 output; it never acquires data, never
touches a network, and holds no credentials.
"""

from __future__ import annotations

from typing import Any

from src.common.quality.engine import confidence_score
from src.data_layer.validate import rules as rule_checks
from src.data_layer.validate.contracts import (
    CORE_CHECKS,
    AnomalyFinding,
    CheckName,
    QualityRules,
    QuarantineRecord,
    ReconciliationStatus,
    ValidationEvidence,
    ValidationFailure,
    ValidationReport,
    ValidationRequest,
    ValidationResult,
    ValidationStatus,
    build_validation_id,
    disposition_for,
    domain_applicability,
    select_failure,
    status_for,
    trace_id_for,
)

#: Checks whose failure means the record cannot be verified against a peer.
_DEFAULT_REQUIRED: tuple[CheckName, ...] = CORE_CHECKS


class QualityMonitor:
    """Deterministic quality counters (11.26). No external platform."""

    def __init__(self, *, name: str) -> None:
        if not name.strip():
            raise ValueError("name must be non-empty")
        self.name = name
        self.counters: dict[str, int] = {
            "validations": 0,
            "accepted": 0,
            "rejected": 0,
            "quarantined": 0,
            "stale": 0,
            "invalid": 0,
            "anomalous": 0,
        }

    def observe(self, result: ValidationResult) -> None:
        """Record one validation outcome."""
        self.counters["validations"] += 1
        self.counters[result.status.value.lower()] += 1
        if result.failure_class == ValidationFailure.STALE:
            self.counters["stale"] += 1
        if result.failure_class == ValidationFailure.INVALID_TYPE:
            self.counters["invalid"] += 1
        if result.failure_class == ValidationFailure.ANOMALOUS:
            self.counters["anomalous"] += 1


class ValidationService:
    """The controlled boundary through which data is validated."""

    def __init__(
        self,
        *,
        name: str,
        rules: QualityRules,
        monitor: QualityMonitor | None = None,
    ) -> None:
        if not name.strip():
            raise ValueError("name must be non-empty")
        self.name = name
        self.rules = rules
        self.monitor = monitor
        self._quarantine: dict[str, QuarantineRecord] = {}
        self._audit: list[dict[str, Any]] = []

    # -- public API ---------------------------------------------------------

    def audit_log(self) -> list[dict[str, Any]]:
        """Return the validation audit trail (11.27)."""
        return list(self._audit)

    def is_quarantined(self, acquisition_id: str) -> bool:
        """Return whether an acquisition id is currently quarantined (11.23)."""
        return acquisition_id in self._quarantine

    def quarantine(self) -> dict[str, QuarantineRecord]:
        """Return the current quarantine, keyed by acquisition id."""
        return dict(self._quarantine)

    def validate(self, request: ValidationRequest) -> ValidationResult:
        """Validate one acquired record and return its classified outcome."""
        failures: set[ValidationFailure] = set()
        failed_checks: list[CheckName] = []
        passed_checks: list[CheckName] = []
        anomalies: list[AnomalyFinding] = []
        conflicts: tuple[dict[str, Any], ...] = ()
        reconciliation = ReconciliationStatus.NOT_ATTEMPTED
        detail = ""

        # 11.14-11.16: refuse to validate a domain we have no contract for.
        applicability = domain_applicability(request.kind)
        if not applicability.applicable:
            failures.add(ValidationFailure.UNSUPPORTED_DOMAIN)
            failed_checks.append(CheckName.INTEGRITY)
            detail = applicability.reason
            return self._finalise(
                request,
                failures,
                passed_checks,
                failed_checks,
                anomalies,
                conflicts,
                reconciliation,
                detail,
            )

        required = set(_DEFAULT_REQUIRED) | set(self.rules.required_checks)

        def record(check: CheckName, found: set[ValidationFailure]) -> None:
            if found:
                failures.update(found)
                failed_checks.append(check)
            else:
                passed_checks.append(check)

        missing_fields: tuple[str, ...] = ()
        duplicate_count = 0

        for check in required:
            if check is CheckName.COMPLETENESS:
                found, missing_fields = rule_checks.check_completeness(request, self.rules)
                record(check, found)
            elif check is CheckName.MISSING_THRESHOLD:
                record(check, rule_checks.check_missing_threshold(request, self.rules))
            elif check is CheckName.INTEGRITY:
                record(check, rule_checks.check_integrity(request, self.rules))
            elif check is CheckName.PROVENANCE:
                record(check, rule_checks.check_provenance(request, self.rules))
            elif check is CheckName.INVALID_TYPE:
                record(check, rule_checks.check_invalid_types(request, self.rules))
            elif check is CheckName.TIMESTAMP:
                record(check, rule_checks.check_timestamp(request, self.rules))
            elif check is CheckName.CONSISTENCY:
                record(check, rule_checks.check_consistency(request, self.rules))
            elif check is CheckName.FRESHNESS:
                record(check, rule_checks.check_freshness(request, self.rules))
            elif check is CheckName.DUPLICATES:
                found, duplicate_count = rule_checks.check_duplicates(request, self.rules)
                record(check, found)
            elif check is CheckName.ACCURACY:
                record(check, rule_checks.check_accuracy(request, self.rules))
            elif check is CheckName.ANOMALY:
                found, findings = rule_checks.check_anomaly(request, self.rules)
                anomalies.extend(findings)
                record(check, found)
            elif check is CheckName.OUTLIER:
                found, findings = rule_checks.check_outlier(request, self.rules)
                anomalies.extend(findings)
                record(check, found)

        # Cross-source/peer comparison (11.12/11.19). Runs when peers exist,
        # or when the check is explicitly required (so absence of evidence
        # is recorded as insufficient evidence rather than skipped).
        if request.peers or CheckName.CROSS_SOURCE in required:
            found, conflicts = rule_checks.check_cross_source(request, self.rules)
            if found == {ValidationFailure.UNVERIFIABLE}:
                reconciliation = ReconciliationStatus.INSUFFICIENT_EVIDENCE
            elif conflicts:
                reconciliation = ReconciliationStatus.CONFLICT
            else:
                reconciliation = ReconciliationStatus.RECONCILED
            if CheckName.CROSS_SOURCE in required:
                record(CheckName.CROSS_SOURCE, found)
            else:
                failures.update(found)

        # Confidence (11.20) is evaluated last, from the pass rate so far.
        total = len(passed_checks) + len(failed_checks)
        if total == 0:
            total = 1
        score = 0.0
        if CheckName.CONFIDENCE in required:
            found, score = rule_checks.check_confidence(
                request, self.rules, passed=len(passed_checks), total=total
            )
            record(CheckName.CONFIDENCE, found)
        else:
            score = confidence_score(len(passed_checks), total)

        return self._finalise(
            request,
            failures,
            passed_checks,
            failed_checks,
            anomalies,
            conflicts,
            reconciliation,
            detail,
            missing_fields=missing_fields,
            duplicate_count=duplicate_count,
            score=score,
        )

    def recover(
        self, acquisition_id: str, *, request: ValidationRequest
    ) -> ValidationResult | None:
        """Recover a quarantined record through revalidation (11.22.3/11.24).

        Recovery never implies acceptance: the record is only released when
        revalidating it actually passes. Otherwise it stays blocked.
        """
        if acquisition_id not in self._quarantine:
            return None
        result = self.validate(request)
        if result.status == ValidationStatus.ACCEPTED:
            self._quarantine.pop(acquisition_id, None)
        return result

    # -- internals ----------------------------------------------------------

    def _finalise(
        self,
        request: ValidationRequest,
        failures: set[ValidationFailure],
        passed_checks: list[CheckName],
        failed_checks: list[CheckName],
        anomalies: list[AnomalyFinding],
        conflicts: tuple[dict[str, Any], ...],
        reconciliation: ReconciliationStatus,
        detail: str,
        *,
        missing_fields: tuple[str, ...] = (),
        duplicate_count: int = 0,
        score: float = 0.0,
    ) -> ValidationResult:
        """Classify the failures, build evidence/report, and record state."""
        status = status_for(failures)
        failure_class = select_failure(failures)
        disposition = disposition_for(status)

        validation_id = build_validation_id(
            request.source_id,
            request.asset,
            request.acquisition_id,
            request.timestamp_utc,
            self.rules.version,
        )
        evidence = ValidationEvidence(
            validation_id=validation_id,
            trace_id=trace_id_for(validation_id),
            acquisition_id=request.acquisition_id,
            source_id=request.source_id,
            asset=request.asset,
            status=status.value,
            disposition=disposition,
            failure_class=failure_class.value,
            passed_checks=tuple(sorted(check.value for check in passed_checks)),
            failed_checks=tuple(sorted(check.value for check in failed_checks)),
            missing_fields=missing_fields,
            duplicate_count=duplicate_count,
            quality_score=score,
            rules_version=self.rules.version,
            schema_version=self.rules.schema_version,
            timestamps={"source": request.source_timestamp, "utc": request.timestamp_utc},
            provenance=dict(request.provenance),
            detail=detail,
        )
        report = ValidationReport(
            validation_id=validation_id,
            trace_id=evidence.trace_id,
            acquisition_id=request.acquisition_id,
            source_id=request.source_id,
            asset=request.asset,
            status=status.value,
            disposition=disposition,
            failure_class=failure_class.value,
            quality_score=score,
            passed_checks=evidence.passed_checks,
            failed_checks=evidence.failed_checks,
            rules_version=self.rules.version,
            schema_version=self.rules.schema_version,
        )

        quarantine: QuarantineRecord | None = None
        if status == ValidationStatus.QUARANTINED:
            quarantine = QuarantineRecord(
                acquisition_id=request.acquisition_id,
                source_id=request.source_id,
                asset=request.asset,
                reason=detail or f"{failure_class.value} requires review",
                failure_class=failure_class.value,
                rules_version=self.rules.version,
                schema_version=self.rules.schema_version,
                provenance=dict(request.provenance),
            )
            self._quarantine[request.acquisition_id] = quarantine

        result = ValidationResult(
            validation_id=validation_id,
            status=status,
            disposition=disposition,
            failure_class=failure_class,
            quality_score=score,
            passed_checks=tuple(passed_checks),
            failed_checks=tuple(failed_checks),
            anomalies=tuple(anomalies),
            conflicts=conflicts,
            reconciliation=reconciliation,
            downstream_usable=status == ValidationStatus.ACCEPTED,
            quarantine=quarantine,
            report=report,
            evidence=evidence,
            rules_version=self.rules.version,
            schema_version=self.rules.schema_version,
            detail=detail,
        )
        self._audit.append(
            {
                "validation_id": validation_id,
                "trace_id": evidence.trace_id,
                "acquisition_id": request.acquisition_id,
                "source_id": request.source_id,
                "status": status.value,
                "failure_class": failure_class.value,
                "rules_version": self.rules.version,
            }
        )
        if self.monitor is not None:
            self.monitor.observe(result)
        return result


def request_from_acquisition(
    acquired: Any, *, rules: QualityRules, as_of: str
) -> ValidationRequest:
    """Adapt a Topic 10 `AcquisitionResult` into a validation request.

    Only values the acquisition actually produced are copied. Nothing is
    fabricated: if the acquisition carries no record, a `ValueError` is
    raised rather than inventing one.
    """
    record = acquired.record
    if record is None:
        raise ValueError("acquisition carried no record to validate")

    payload: dict[str, Any] = {
        "asset": record.asset,
        "price": record.price,
        "volume": record.volume,
        "timestamp": record.timestamp,
        "timestamp_utc": record.timestamp_utc,
        "source_id": record.source_id,
        "acquisition_id": record.acquisition_id,
    }
    return ValidationRequest(
        record=payload,
        asset=record.asset,
        source_id=record.source_id,
        kind="market",
        acquisition_id=record.acquisition_id,
        source_timestamp=record.timestamp,
        timestamp_utc=record.timestamp_utc,
        provenance=dict(acquired.provenance),
        as_of=as_of,
        schema_version=rules.schema_version,
    )
