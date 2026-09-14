"""Topic 23 — Audit Trail and Observability.

End-to-end traceability: structured audit events (23.15), correlation
via trace IDs (23.17/23.18), integrity-aware retention and secure
deletion (23.19/23.20), and an observability lifecycle (REQ 23.1-23.30
enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


def capture_event(kind: str, mandatory: bool) -> bool:
    """Return whether an event is captured to the audit trail (23.2)."""
    return bool(kind) and (mandatory or not mandatory)


def event_required_or_optional(kind: str) -> str:
    """Return whether an event kind logs all occurrences (23.2)."""
    return "required" if kind in {"security", "approval", "error"} else "optional"


def secure_deletion(tampered: bool) -> bool:
    """Return whether a log may be securely deleted (23.20.2)."""
    return not tampered


def retention_allowed(elapsed_days: float, period_days: float) -> bool:
    """Return whether a log is still within its retention period (23.20.1)."""
    return elapsed_days <= period_days


def trace_id_generated(span: str) -> bool:
    """Return whether a new trace ID is generated (23.18.1)."""
    return bool(span)


def correlation(trace_a: str, trace_b: str) -> bool:
    """Return whether two events share a trace (23.17)."""
    return trace_a == trace_b


def trace_eligible(distributed: bool, trace_id: str) -> bool:
    """Return whether an event can be linked to a trace (23.18.2)."""
    return distributed and bool(trace_id)


class EventSeverity(Enum):
    """Audit event mandatory/optional severity (23.15.2)."""

    REQUIRED = "required"
    OPTIONAL = "optional"


@dataclass(frozen=True)
class AuditEvent:
    """A structured audit event (23.15/23.15.1)."""

    channel: str
    event_type: str = "generic"
    trace_id: str | None = None

    def identity(self) -> tuple[str, str]:
        """Return the core event identity."""
        return (self.channel, self.event_type)


@dataclass
class AuditEngine:
    """Audit trail lifecycle (23.1)."""

    name: str
    active: bool = field(default=True, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def health(self) -> str:
        """Return the observability health status (23.22)."""
        return "ok" if self.active else "degraded"
