"""Topic 11 — Data Validation and Quality Layer.

Completeness, accuracy and integrity validation, freshness and
timestamp checks, duplicate/missing/invalid detection, anomaly
severity, confidence scoring, and reject/quarantine/recover handling.
"""

from .engine import (
    QualityEngine,
    confidence_score,
    detect_duplicates,
    is_complete,
    is_fresh,
    is_valid_timestamp,
    quarantine_record,
    reject_record,
    severity_grade,
)

__all__ = [
    "QualityEngine",
    "confidence_score",
    "detect_duplicates",
    "is_complete",
    "is_fresh",
    "is_valid_timestamp",
    "quarantine_record",
    "reject_record",
    "severity_grade",
]
