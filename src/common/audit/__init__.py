"""Topic 23 — Audit Trail and Observability.

Immutable, correlated event logging with trace IDs, retention and
secure deletion, plus health/alerting hooks (REQ 23.1-23.30 subset).
"""

from .engine import (
    AuditEngine,
    AuditEvent,
    capture_event,
    correlation,
    event_required_or_optional,
    retention_allowed,
    secure_deletion,
    trace_eligible,
    trace_id_generated,
)

__all__ = [
    "AuditEngine",
    "AuditEvent",
    "capture_event",
    "correlation",
    "event_required_or_optional",
    "retention_allowed",
    "secure_deletion",
    "trace_eligible",
    "trace_id_generated",
]
