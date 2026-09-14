"""Topic 34 — SRS Self-Validation.

Validates the SRS for completeness, consistency, ambiguity,
contradiction and traceability, scoring quality against a
threshold before approval (REQ 34.1-34.30 subset).
"""

from .engine import (
    SelfValidationEngine,
    ambiguity_free,
    approval_recommended,
    blocked_detected,
    completeness_ok,
    consistency_ok,
    contradiction_free,
    duplicates_absent,
    quality_score_pass,
    traceability_validated,
)

__all__ = [
    "SelfValidationEngine",
    "ambiguity_free",
    "approval_recommended",
    "blocked_detected",
    "completeness_ok",
    "consistency_ok",
    "contradiction_free",
    "duplicates_absent",
    "quality_score_pass",
    "traceability_validated",
]
