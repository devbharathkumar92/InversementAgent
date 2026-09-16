"""Topic 11 — the individual validation checks.

Each check is a pure function over an explicit, versioned rule set. None of
them mutate the input, and none of them invent a threshold: when a check
requires a threshold that `QualityRules` does not carry, it returns
`THRESHOLD_UNCONFIGURED` (fail closed) rather than defaulting.

Existing `src.common.quality.engine` primitives are reused wherever they
already express the rule, so this module adds orchestration and evidence,
not a parallel implementation.
"""

from __future__ import annotations

from typing import Any

from src.common.quality.engine import (
    confidence_score,
    detect_duplicates,
    is_complete,
    is_fresh,
    is_valid_timestamp,
    severity_grade,
)
from src.data_layer.validate.contracts import (
    AnomalyFinding,
    QualityRules,
    ValidationFailure,
    ValidationRequest,
    same_instant,
)

#: Fields whose values must be numeric when present (11.9).
NUMERIC_FIELDS: tuple[str, ...] = ("price", "volume")

#: Characters that indicate a malformed payload rather than a bad value.
_INVALID_CHARS: tuple[str, ...] = ("\x00", "\r")


def check_completeness(
    request: ValidationRequest, rules: QualityRules
) -> tuple[set[ValidationFailure], tuple[str, ...]]:
    """Return completeness failures and the missing field names (11.2)."""
    if is_complete(request.record, rules.required_fields):
        return set(), ()
    missing = tuple(sorted(name for name in rules.required_fields if name not in request.record))
    if rules.max_missing is not None and len(missing) <= rules.max_missing:
        return set(), missing
    return {ValidationFailure.INCOMPLETE}, missing


def check_missing_threshold(
    request: ValidationRequest, rules: QualityRules
) -> set[ValidationFailure]:
    """Enforce an explicitly configured missing-field threshold (11.2.2)."""
    if rules.max_missing is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}
    missing = sum(1 for name in rules.required_fields if name not in request.record)
    if missing > rules.max_missing:
        return {ValidationFailure.MISSING_FIELDS}
    return set()


def check_integrity(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Required fields that are *present* must not be None (11.6).

    Presence itself is owned by `check_completeness`, which honours the
    configured missing-field threshold; keeping the two separate prevents a
    permitted omission from being double-counted here.
    """
    for name in rules.required_fields:
        if name in request.record and request.record[name] is None:
            return {ValidationFailure.INTEGRITY_FAILURE}
    return set()


def check_provenance(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Provenance must exist, identify the source, and match the record (11.21.1)."""
    provenance = request.provenance
    if not provenance or not provenance.get("source_id"):
        return {ValidationFailure.PROVENANCE_MISSING}
    if provenance.get("source_id") != request.source_id:
        return {ValidationFailure.PROVENANCE_MISMATCH}
    recorded = provenance.get("acquisition_id")
    if recorded is not None and recorded != request.acquisition_id:
        return {ValidationFailure.PROVENANCE_MISMATCH}
    return set()


def check_invalid_types(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Detect malformed values: wrong types or invalid characters (11.9)."""
    for name in NUMERIC_FIELDS:
        value = request.record.get(name)
        if value is not None and not isinstance(value, (int, float)):
            return {ValidationFailure.INVALID_TYPE}
    for value in request.record.values():
        if isinstance(value, str) and any(char in value for char in _INVALID_CHARS):
            return {ValidationFailure.INVALID_TYPE}
    return set()


def check_timestamp(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Source and normalized timestamps must both be valid ISO-8601 (11.13)."""
    if not is_valid_timestamp(request.timestamp_utc):
        return {ValidationFailure.BAD_TIMESTAMP}
    if not is_valid_timestamp(request.source_timestamp):
        return {ValidationFailure.BAD_TIMESTAMP}
    return set()


def check_consistency(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Identity and timestamp consistency within the record (11.4).

    Only invariants the repository already expresses are checked: the
    record must agree with the declared asset, acquisition id, and the
    source timestamp must denote the same instant as the normalized one.
    """
    if request.record.get("asset") not in (None, request.asset):
        return {ValidationFailure.INCONSISTENT}
    recorded = request.record.get("acquisition_id")
    if recorded is not None and recorded != request.acquisition_id:
        return {ValidationFailure.INCONSISTENT}
    if not same_instant(request.source_timestamp, request.timestamp_utc):
        return {ValidationFailure.INCONSISTENT}
    return set()


def check_freshness(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Freshness against a configured max age and caller-supplied time (11.5)."""
    if rules.max_age_s is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}
    if not is_valid_timestamp(request.timestamp_utc) or not is_valid_timestamp(request.as_of):
        return {ValidationFailure.BAD_TIMESTAMP}
    if is_fresh(request.timestamp_utc, rules.max_age_s, request.as_of):
        return set()
    return {ValidationFailure.STALE}


def check_duplicates(
    request: ValidationRequest, rules: QualityRules
) -> tuple[set[ValidationFailure], int]:
    """Detect duplicates among the declared peer records (11.7)."""
    if not request.peers:
        return set(), 0
    rows = list(request.peers)
    # Duplicate identity is the acquisition id: the same acquired record
    # appearing more than once. No domain-value heuristic is invented.
    count = detect_duplicates(rows, key="acquisition_id")
    if count:
        return {ValidationFailure.DUPLICATE}, count
    return set(), 0


def check_accuracy(request: ValidationRequest, rules: QualityRules) -> set[ValidationFailure]:
    """Accuracy against an explicitly supplied reference value (11.3)."""
    if rules.accuracy_tolerance is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}
    if request.reference is None:
        return {ValidationFailure.UNVERIFIABLE}
    price = request.record.get("price")
    if not isinstance(price, (int, float)):
        return {ValidationFailure.INVALID_TYPE}
    if abs(price - request.reference) <= rules.accuracy_tolerance:
        return set()
    return {ValidationFailure.ACCURACY_OUT_OF_TOLERANCE}


def check_anomaly(
    request: ValidationRequest, rules: QualityRules
) -> tuple[set[ValidationFailure], tuple[AnomalyFinding, ...]]:
    """Grade deviation against a configured anomaly tolerance (11.10)."""
    if rules.anomaly_tolerance is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}, ()
    if request.reference is None:
        return {ValidationFailure.UNVERIFIABLE}, ()
    price = request.record.get("price")
    if not isinstance(price, (int, float)):
        return {ValidationFailure.INVALID_TYPE}, ()

    tolerance = rules.anomaly_tolerance
    deviation = abs(price - request.reference)
    grade = severity_grade(tolerance, deviation)
    finding = AnomalyFinding(
        field="price",
        kind="anomaly",
        deviation=deviation,
        tolerance=tolerance,
        severity=grade,
    )
    if grade == "high":
        return {ValidationFailure.ANOMALOUS}, (finding,)
    return set(), (finding,)


def check_outlier(
    request: ValidationRequest, rules: QualityRules
) -> tuple[set[ValidationFailure], tuple[AnomalyFinding, ...]]:
    """Detect an outlier against a declared baseline (11.11).

    The baseline is supplied by the caller; no statistical threshold is
    invented. The comparison is against the baseline mean.
    """
    if rules.outlier_tolerance is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}, ()
    if not request.baseline:
        return {ValidationFailure.UNVERIFIABLE}, ()
    price = request.record.get("price")
    if not isinstance(price, (int, float)):
        return {ValidationFailure.INVALID_TYPE}, ()

    mean = sum(request.baseline) / len(request.baseline)
    tolerance = rules.outlier_tolerance
    deviation = abs(price - mean)
    finding = AnomalyFinding(
        field="price",
        kind="outlier",
        deviation=deviation,
        tolerance=tolerance,
        severity=severity_grade(tolerance, deviation),
    )
    if deviation <= tolerance:
        return set(), (finding,)
    return {ValidationFailure.OUTLIER}, (finding,)


def check_cross_source(
    request: ValidationRequest, rules: QualityRules
) -> tuple[set[ValidationFailure], tuple[dict[str, Any], ...]]:
    """Compare against declared peers, exposing conflicts (11.12/11.19).

    Conflicts are returned, never resolved by preferring one source: no
    authoritative precedence rule exists in the repository.
    """
    if rules.accuracy_tolerance is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}, ()
    if not request.peers:
        return {ValidationFailure.UNVERIFIABLE}, ()

    price = request.record.get("price")
    if not isinstance(price, (int, float)):
        return {ValidationFailure.INVALID_TYPE}, ()

    conflicts: list[dict[str, Any]] = []
    for peer in request.peers:
        peer_price = peer.get("price")
        if not isinstance(peer_price, (int, float)):
            continue
        if abs(price - peer_price) > rules.accuracy_tolerance:
            conflicts.append(
                {
                    "source_id": peer.get("source_id", ""),
                    "acquisition_id": peer.get("acquisition_id", ""),
                    "price": peer_price,
                    "deviation": abs(price - peer_price),
                }
            )
    if conflicts:
        return {ValidationFailure.CONFLICT}, tuple(conflicts)
    return set(), ()


def check_confidence(
    request: ValidationRequest,
    rules: QualityRules,
    *,
    passed: int,
    total: int,
) -> tuple[set[ValidationFailure], float]:
    """Confidence from the pass rate against a configured threshold (11.20)."""
    score = confidence_score(passed, total)
    if rules.min_confidence is None:
        return {ValidationFailure.THRESHOLD_UNCONFIGURED}, score
    if score < rules.min_confidence:
        return {ValidationFailure.CONFIDENCE_BELOW_THRESHOLD}, score
    return set(), score
