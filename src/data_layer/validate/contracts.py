"""Topic 11 — validation boundary contracts.

Typed, deterministic contracts for the validation boundary that consumes
Topic 10 acquisition output and decides whether it may proceed:

    ACQUIRED -> VALIDATION -> ACCEPTED | REJECTED | QUARANTINED
                           -> RECOVERY / REVALIDATION

**Threshold policy.** `srs/topics/TOPIC_11.md` requires thresholds to exist
as version-controlled controls (11.2.2, 11.20.2, 11.21) but never states a
numeric value. Every threshold here is therefore caller-supplied
configuration carried in `QualityRules`, and a *required* check whose
threshold was not configured fails closed (`THRESHOLD_UNCONFIGURED`) rather
than having a magic value invented for it.
"""

from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any

from src.common.quality.engine import is_valid_timestamp


class CheckName(StrEnum):
    """The validation checks the boundary can execute (11.2-11.21)."""

    COMPLETENESS = "COMPLETENESS"
    MISSING_THRESHOLD = "MISSING_THRESHOLD"
    INTEGRITY = "INTEGRITY"
    PROVENANCE = "PROVENANCE"
    INVALID_TYPE = "INVALID_TYPE"
    TIMESTAMP = "TIMESTAMP"
    CONSISTENCY = "CONSISTENCY"
    FRESHNESS = "FRESHNESS"
    DUPLICATES = "DUPLICATES"
    ACCURACY = "ACCURACY"
    ANOMALY = "ANOMALY"
    OUTLIER = "OUTLIER"
    CROSS_SOURCE = "CROSS_SOURCE"
    CONFIDENCE = "CONFIDENCE"


#: Checks that always run: they express invariants the SRS forbids
#: bypassing (identity, provenance, timestamps, integrity, completeness).
CORE_CHECKS: tuple[CheckName, ...] = (
    CheckName.COMPLETENESS,
    CheckName.INTEGRITY,
    CheckName.PROVENANCE,
    CheckName.INVALID_TYPE,
    CheckName.TIMESTAMP,
    CheckName.CONSISTENCY,
)


class ValidationStatus(StrEnum):
    """The terminal status of one validation (11.22)."""

    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    QUARANTINED = "QUARANTINED"


class ValidationFailure(StrEnum):
    """Classification of every validation outcome (11.22)."""

    NONE = "NONE"
    UNSUPPORTED_DOMAIN = "UNSUPPORTED_DOMAIN"
    INVALID_TYPE = "INVALID_TYPE"
    PROVENANCE_MISSING = "PROVENANCE_MISSING"
    PROVENANCE_MISMATCH = "PROVENANCE_MISMATCH"
    VERSION_MISMATCH = "VERSION_MISMATCH"
    BAD_TIMESTAMP = "BAD_TIMESTAMP"
    MISSING_FIELDS = "MISSING_FIELDS"
    INCOMPLETE = "INCOMPLETE"
    INTEGRITY_FAILURE = "INTEGRITY_FAILURE"
    STALE = "STALE"
    DUPLICATE = "DUPLICATE"
    INCONSISTENT = "INCONSISTENT"
    THRESHOLD_UNCONFIGURED = "THRESHOLD_UNCONFIGURED"
    CONFIDENCE_BELOW_THRESHOLD = "CONFIDENCE_BELOW_THRESHOLD"
    UNVERIFIABLE = "UNVERIFIABLE"
    CONFLICT = "CONFLICT"
    ACCURACY_OUT_OF_TOLERANCE = "ACCURACY_OUT_OF_TOLERANCE"
    ANOMALOUS = "ANOMALOUS"
    OUTLIER = "OUTLIER"


#: Failures that definitively invalidate data -> REJECTED (11.22.1).
REJECTING_FAILURES: tuple[ValidationFailure, ...] = (
    ValidationFailure.INVALID_TYPE,
    ValidationFailure.PROVENANCE_MISSING,
    ValidationFailure.PROVENANCE_MISMATCH,
    ValidationFailure.VERSION_MISMATCH,
    ValidationFailure.BAD_TIMESTAMP,
    ValidationFailure.MISSING_FIELDS,
    ValidationFailure.INCOMPLETE,
    ValidationFailure.INTEGRITY_FAILURE,
    ValidationFailure.STALE,
    ValidationFailure.DUPLICATE,
    ValidationFailure.INCONSISTENT,
)

#: Failures that leave correctness uncertain -> QUARANTINED (11.22.2).
QUARANTINE_FAILURES: tuple[ValidationFailure, ...] = (
    ValidationFailure.UNSUPPORTED_DOMAIN,
    ValidationFailure.THRESHOLD_UNCONFIGURED,
    ValidationFailure.CONFIDENCE_BELOW_THRESHOLD,
    ValidationFailure.CONFLICT,
    ValidationFailure.UNVERIFIABLE,
    ValidationFailure.ACCURACY_OUT_OF_TOLERANCE,
    ValidationFailure.ANOMALOUS,
    ValidationFailure.OUTLIER,
)

#: Used to pick the single reported failure_class, most severe first.
FAILURE_PRECEDENCE: tuple[ValidationFailure, ...] = (
    *REJECTING_FAILURES,
    *QUARANTINE_FAILURES,
    ValidationFailure.NONE,
)


class ReconciliationStatus(StrEnum):
    """Outcome of comparing a record with its declared peers (11.19)."""

    NOT_ATTEMPTED = "NOT_ATTEMPTED"
    RECONCILED = "RECONCILED"
    CONFLICT = "CONFLICT"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


@dataclass(frozen=True)
class QualityRules:
    """Explicit, versioned validation configuration (11.21/11.30).

    Every threshold is optional. `None` means "not configured", which is
    distinct from a configured value: a required-but-unconfigured check
    fails closed instead of silently defaulting.
    """

    version: str
    schema_version: str = ""
    required_fields: tuple[str, ...] = ()
    required_checks: frozenset[CheckName] = field(default_factory=frozenset)
    max_missing: int | None = None
    max_age_s: float | None = None
    accuracy_tolerance: float | None = None
    anomaly_tolerance: float | None = None
    outlier_tolerance: float | None = None
    min_confidence: float | None = None

    def __post_init__(self) -> None:
        if not self.version.strip():
            raise ValueError("rules version must be non-empty")
        if self.max_missing is not None and self.max_missing < 0:
            raise ValueError("max_missing must be >= 0")
        for label, value in (
            ("max_age_s", self.max_age_s),
            ("accuracy_tolerance", self.accuracy_tolerance),
            ("anomaly_tolerance", self.anomaly_tolerance),
            ("outlier_tolerance", self.outlier_tolerance),
        ):
            if value is not None and value < 0:
                raise ValueError(f"{label} must be >= 0")
        if self.min_confidence is not None and not 0.0 <= self.min_confidence <= 100.0:
            raise ValueError("min_confidence must be within 0..100")

    def threshold_for(self, check: CheckName) -> float | int | None:
        """Return the configured threshold for a check, or None."""
        return {
            CheckName.MISSING_THRESHOLD: self.max_missing,
            CheckName.FRESHNESS: self.max_age_s,
            CheckName.ACCURACY: self.accuracy_tolerance,
            CheckName.ANOMALY: self.anomaly_tolerance,
            CheckName.OUTLIER: self.outlier_tolerance,
            CheckName.CONFIDENCE: self.min_confidence,
        }.get(check)


@dataclass(frozen=True)
class ValidationRequest:
    """A fully-specified validation input. Carries no credentials.

    `source_timestamp` preserves the source's own time semantics;
    `timestamp_utc` is the normalized representation. `as_of` is the
    caller-supplied reference time - never a wall clock.
    """

    record: dict[str, Any]
    asset: str
    source_id: str
    kind: str
    acquisition_id: str
    source_timestamp: str
    timestamp_utc: str
    provenance: dict[str, Any]
    as_of: str
    reference: float | None = None
    peers: tuple[dict[str, Any], ...] = ()
    baseline: tuple[float, ...] = ()
    schema_version: str = ""


@dataclass(frozen=True)
class AnomalyFinding:
    """One anomaly (or outlier) finding with its severity (11.10/11.11)."""

    field: str
    kind: str
    deviation: float
    tolerance: float
    severity: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class QuarantineRecord:
    """A quarantined record with its reason and evidence (11.23)."""

    acquisition_id: str
    source_id: str
    asset: str
    reason: str
    failure_class: str
    rules_version: str
    schema_version: str
    provenance: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationEvidence:
    """Preserved, inspectable evidence of one validation (11.27)."""

    validation_id: str
    trace_id: str
    acquisition_id: str
    source_id: str
    asset: str
    status: str
    disposition: str
    failure_class: str
    passed_checks: tuple[str, ...]
    failed_checks: tuple[str, ...]
    missing_fields: tuple[str, ...]
    duplicate_count: int
    quality_score: float
    rules_version: str
    schema_version: str
    timestamps: dict[str, str]
    provenance: dict[str, Any]
    detail: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationReport:
    """A structured quality report (11.25)."""

    validation_id: str
    trace_id: str
    acquisition_id: str
    source_id: str
    asset: str
    status: str
    disposition: str
    failure_class: str
    quality_score: float
    passed_checks: tuple[str, ...]
    failed_checks: tuple[str, ...]
    rules_version: str
    schema_version: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationResult:
    """The bounded, deterministic outcome of one validation."""

    validation_id: str
    status: ValidationStatus
    disposition: str
    failure_class: ValidationFailure
    quality_score: float
    passed_checks: tuple[CheckName, ...]
    failed_checks: tuple[CheckName, ...]
    anomalies: tuple[AnomalyFinding, ...]
    conflicts: tuple[dict[str, Any], ...]
    reconciliation: ReconciliationStatus
    downstream_usable: bool
    quarantine: QuarantineRecord | None
    report: ValidationReport
    evidence: ValidationEvidence
    rules_version: str
    schema_version: str
    detail: str = ""


@dataclass(frozen=True)
class DomainApplicability:
    """Whether a data domain can be validated today (11.14-11.16).

    `applicable` is False when the repository holds no approved schema or
    contract for the domain. That is a controlled blocker, not a silent
    pass and not fabricated domain data.
    """

    kind: str
    applicable: bool
    reason: str = ""


def domain_applicability(kind: str) -> DomainApplicability:
    """Return whether validation is supported for a data `kind`."""
    if kind == "market":
        return DomainApplicability(kind=kind, applicable=True)
    return DomainApplicability(
        kind=kind,
        applicable=False,
        reason=(
            f"no approved {kind!r} schema or contract exists in the repository, so "
            f"{kind!r} data cannot be validated without fabricating domain rules"
        ),
    )


def _parse(timestamp: str) -> datetime | None:
    """Parse an ISO-8601 timestamp, returning None when invalid."""
    if not is_valid_timestamp(timestamp):
        return None
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))


def same_instant(left: str, right: str) -> bool:
    """Return whether two timestamps denote the same instant."""
    a, b = _parse(left), _parse(right)
    if a is None or b is None:
        return False
    return a == b


def build_validation_id(
    source_id: str, asset: str, acquisition_id: str, timestamp: str, rules_version: str
) -> str:
    """Return the deterministic validation id (11.27/11.30).

    Derived purely from stable inputs and the rule version, so repeated
    validation of identical input under identical rules is identical. No
    clock, randomness, or UUID is involved.
    """
    payload = "|".join((source_id, asset, acquisition_id, timestamp, rules_version))
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return f"val-{digest[:16]}"


def trace_id_for(validation_id: str) -> str:
    """Return the deterministic trace id for a validation (11.27)."""
    return f"trace-{validation_id.removeprefix('val-')}"


def disposition_for(status: ValidationStatus) -> str:
    """Map a validation status onto its disposition vocabulary."""
    return {
        ValidationStatus.ACCEPTED: "accepted",
        ValidationStatus.REJECTED: "rejected",
        ValidationStatus.QUARANTINED: "quarantined",
    }[status]


def select_failure(failures: set[ValidationFailure]) -> ValidationFailure:
    """Return the most severe reported failure from a set of failures."""
    for candidate in FAILURE_PRECEDENCE:
        if candidate in failures:
            return candidate
    return ValidationFailure.NONE


def status_for(failures: set[ValidationFailure]) -> ValidationStatus:
    """Derive the status from the failures found (fail closed otherwise)."""
    if any(failure in REJECTING_FAILURES for failure in failures):
        return ValidationStatus.REJECTED
    if any(failure in QUARANTINE_FAILURES for failure in failures):
        return ValidationStatus.QUARANTINED
    return ValidationStatus.ACCEPTED
