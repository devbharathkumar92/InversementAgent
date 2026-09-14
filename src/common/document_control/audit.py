"""Topic 1.12 — structured, machine-readable audit trail."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class AuditEvent:
    """A single immutable audit event.

    Fields (REQ 1.12): event identity via ``(timestamp, action, actor,
    object_id)``; ``result`` records the outcome where applicable.
    """

    action: str
    actor: str
    object_id: str
    result: str | None = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not self.action:
            raise ValueError("Audit event requires an action")
        if not self.actor:
            raise ValueError("Audit event requires an actor")
        if not self.object_id:
            raise ValueError("Audit event requires an object ID")


@dataclass
class AuditLog:
    """An ordered, queryable collection of audit events (REQ 1.12)."""

    _events: list[AuditEvent] = field(default_factory=list)

    def record(
        self,
        action: str,
        actor: str,
        object_id: str,
        result: str | None = None,
    ) -> AuditEvent:
        event = AuditEvent(
            action=action,
            actor=actor,
            object_id=object_id,
            result=result,
        )
        self._events.append(event)
        return event

    def events(self) -> list[AuditEvent]:
        """Return events in insertion order (chronological)."""
        return list(self._events)
