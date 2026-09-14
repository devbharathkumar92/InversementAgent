"""Topic 24 — Error Detection and Recovery.

Classifies errors by category (24.2), maps severity to actions
(24.15.2), and drives recovery through retry (24.17), fallback
(24.18), safe-state transitions (24.19) and task restore
(24.20-24.22), while collecting evidence (24.25/24.26).
(REQ 24.1-24.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field

_TRANSIENT_KINDS = frozenset({"network", "api", "timeout", "rate"})
_RETRYABLE_KINDS = frozenset({"api", "network", "timeout", "rate", "integration"})


def classify_error(kind: str) -> str:
    """Classify an error severity (24.2/24.2.2)."""
    if kind in _TRANSIENT_KINDS:
        return "transient"
    if kind in _RETRYABLE_KINDS:
        return "recoverable"
    if kind == "logic":
        return "fatal"
    return "critical"


def severity_action_mapped(severity: int) -> str:
    """Map a severity level to its action (24.15.2)."""
    if severity <= 1:
        return "continue"
    if severity == 2:
        return "retry"
    if severity == 3:
        return "fallback"
    return "halt"


def auto_recoverable(kind: str) -> bool:
    """Return whether the error can be auto-recovered (24.16.1)."""
    return kind in _TRANSIENT_KINDS or kind in _RETRYABLE_KINDS


def retry_condition_allowed(kind: str) -> bool:
    """Return whether retry is permitted (24.17.1)."""
    return kind in _RETRYABLE_KINDS


def retry_exhausted(attempts: int, limit: int) -> bool:
    """Return whether retry has reached its limit (24.17.2)."""
    return attempts >= limit


def fallback_available(kind: str, alternate: bool) -> bool:
    """Return whether a fallback exists (24.18.1)."""
    return alternate and (kind in _RETRYABLE_KINDS or kind in _TRANSIENT_KINDS)


def safe_transition(safe: bool) -> bool:
    """Return whether a safe-state transition is allowed (24.19.1)."""
    return safe


def task_rollback_allowed(persisted: bool) -> bool:
    """Return whether a task can be rolled back (24.21)."""
    return persisted


def task_restart_allowed(idempotent: bool) -> bool:
    """Return whether a task can be restarted (24.20)."""
    return idempotent


def evidence_collected(error_id: str, saved: bool) -> bool:
    """Return whether error evidence was preserved (24.25.1)."""
    return bool(error_id) and saved


@dataclass
class RecoveryEngine:
    """Error handling and recovery lifecycle (24.1)."""

    name: str
    _armed: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._armed = True

    def status(self) -> str:
        """Return the recovery engine state."""
        return "armed" if self._armed else "disabled"
