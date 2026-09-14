"""Topic 3 — Proof of Value Definition.

Implements the PoV contract: objectives (functional/technical/outcome),
success conditions, minimum success thresholds, release-blocking
conditions, acceptance criteria, failure classification, and completion
criteria.
"""

from .definition import (
    FailureClass,
    PoVDefinition,
    PoVStatus,
    ReleaseGate,
    completion_status,
    evaluate_release_gate,
    failure_class,
    meets_success_threshold,
    validate_completion,
)

__all__ = [
    "PoVDefinition",
    "PoVStatus",
    "ReleaseGate",
    "FailureClass",
    "completion_status",
    "evaluate_release_gate",
    "failure_class",
    "meets_success_threshold",
    "validate_completion",
]
