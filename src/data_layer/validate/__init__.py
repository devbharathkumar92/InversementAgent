"""Topic 11 — Data Validation & Quality Layer (executable boundary).

The repository previously held only primitives in
`src/common/quality/engine.py`, with `src/data_layer/validate/` containing
nothing but an empty `__init__.py`. This package turns them into an
executable validation boundary that consumes Topic 10 acquisition output:

    ACQUIRED -> VALIDATION -> ACCEPTED | REJECTED | QUARANTINED
                           -> RECOVERY / REVALIDATION

It is deterministic and offline: no network, no credentials, no live data.

**Thresholds.** `srs/topics/TOPIC_11.md` requires thresholds to be
version-controlled controls (11.2.2, 11.20.2, 11.21) but states no numeric
values. Every threshold is therefore caller-supplied in `QualityRules`, and
a required-but-unconfigured threshold fails closed
(`THRESHOLD_UNCONFIGURED` -> QUARANTINED) rather than being invented.

Usage:

    rules = QualityRules(version="t11-rules-v1", required_fields=(...))
    service = ValidationService(name="validation", rules=rules)
    result = service.validate(request)
"""

from src.data_layer.validate.contracts import (
    CORE_CHECKS,
    QUARANTINE_FAILURES,
    REJECTING_FAILURES,
    AnomalyFinding,
    CheckName,
    DomainApplicability,
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
    same_instant,
    select_failure,
    status_for,
    trace_id_for,
)
from src.data_layer.validate.service import (
    QualityMonitor,
    ValidationService,
    request_from_acquisition,
)

__all__ = [
    "CORE_CHECKS",
    "QUARANTINE_FAILURES",
    "REJECTING_FAILURES",
    "AnomalyFinding",
    "CheckName",
    "DomainApplicability",
    "QualityMonitor",
    "QualityRules",
    "QuarantineRecord",
    "ReconciliationStatus",
    "ValidationEvidence",
    "ValidationFailure",
    "ValidationReport",
    "ValidationRequest",
    "ValidationResult",
    "ValidationService",
    "ValidationStatus",
    "build_validation_id",
    "disposition_for",
    "domain_applicability",
    "request_from_acquisition",
    "same_instant",
    "select_failure",
    "status_for",
    "trace_id_for",
]
