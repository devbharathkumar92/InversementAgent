"""Topic 11 — Data Validation and Quality Layer.

Enforces completeness, accuracy and integrity rules, freshness and
timestamp validation, duplicate/missing/invalid detection, anomaly
severity grading, confidence scoring, and reject/quarantine/recover
handling for invalid data (REQ 11.1-11.30 subset, enforced items).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any


def is_complete(record: dict[str, Any], required: tuple[str, ...]) -> bool:
    """Return whether every required field is present (REQ 11.2)."""
    return all(key in record for key in required)


def detect_duplicates(rows: list[dict[str, Any]], key: str) -> int:
    """Return the number of duplicate rows by key (REQ 11.7)."""
    seen: set[Any] = set()
    duplicate = 0
    for row in rows:
        value = row.get(key)
        if value in seen:
            duplicate += 1
        seen.add(value)
    return duplicate


def is_fresh(timestamp: str, max_age_s: float, now: str) -> bool:
    """Return whether the record's timestamp is within max age (REQ 11.5)."""
    stamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    current = datetime.fromisoformat(now.replace("Z", "+00:00"))
    return (current - stamp) <= timedelta(seconds=max_age_s)


def is_valid_timestamp(timestamp: str) -> bool:
    """Return whether a field parses as an ISO-8601 timestamp (REQ 11.13)."""
    try:
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def severity_grade(tol: float, deviation: float) -> str:
    """Grade an anomaly by deviation vs tolerance (REQ 11.10.2).

    Deviation within 10% of tolerance is low, within tolerance is
    moderate, beyond tolerance is high.
    """
    if deviation <= tol * 0.1:
        return "low"
    if deviation <= tol:
        return "moderate"
    return "high"


def confidence_score(passed: int, total: int) -> float:
    """Return the confidence percentage from validation pass rate
    (REQ 11.20.1)."""
    if total <= 0:
        return 0.0
    return passed / total * 100.0


def reject_record(record_id: str, reason: str) -> str:
    """Disposition: reject a record (REQ 11.22.1)."""
    if not reason.strip():
        raise ValueError("reason must be non-empty")
    return "rejected"


def quarantine_record(record_id: str, reason: str) -> str:
    """Disposition: quarantine a record (REQ 11.22.2)."""
    if not reason.strip():
        raise ValueError("reason must be non-empty")
    return "quarantined"


@dataclass
class QualityEngine:
    """Holds records under quarantine and integrity rules (11.22/11.24)."""

    name: str = ""
    quarantined: dict[str, dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def within_tolerance(self, value: float, reference: float, tol: float) -> bool:
        """Return whether a value is within tolerance of a reference (11.3)."""
        return abs(value - reference) <= tol

    def integrity_ok(self, record: dict[str, Any], required: tuple[str, ...]) -> bool:
        """Return whether required fields are present and non-None (11.6)."""
        return all(record.get(key) is not None for key in required)

    def missing_count(self, record: dict[str, Any]) -> int:
        """Return the number of missing (None-valued) fields (REQ 11.8)."""
        return sum(1 for value in record.values() if value is None)

    def recover(self, record_id: str) -> bool:
        """Release a quarantined record after resolution (REQ 11.24)."""
        if record_id not in self.quarantined:
            return False
        self.quarantined.pop(record_id)
        return True
