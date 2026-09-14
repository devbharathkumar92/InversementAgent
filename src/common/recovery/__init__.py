"""Topic 24 — Error Detection and Recovery.

Classifies errors, drives automatic recovery, retry/fallback policies
and safe-state transitions, and preserves evidence for root-cause
analysis (REQ 24.1-24.30 subset).
"""

from .engine import (
    RecoveryEngine,
    auto_recoverable,
    classify_error,
    evidence_collected,
    fallback_available,
    retry_condition_allowed,
    retry_exhausted,
    safe_transition,
    severity_action_mapped,
    task_restart_allowed,
    task_rollback_allowed,
)

__all__ = [
    "RecoveryEngine",
    "auto_recoverable",
    "classify_error",
    "evidence_collected",
    "fallback_available",
    "retry_condition_allowed",
    "retry_exhausted",
    "safe_transition",
    "severity_action_mapped",
    "task_restart_allowed",
    "task_rollback_allowed",
]
