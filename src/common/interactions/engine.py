"""Topic 22 — Human Interaction and Notifications.

Coordinates human-in-the-loop approvals, clarifications and
escalations, and delivers prioritized, deduplicated notifications
across channels (REQ 22.1-22.30 enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


def approval_required(action: str, size: float) -> bool:
    """Return whether an action needs human approval (REQ 22.3.1)."""
    return action == "kill" or size >= 1000


def clarification_content(question: str) -> str:
    """Return the clarification request content (REQ 22.4.2)."""
    return question


def escalation_triggered(risk: float, limit: float) -> bool:
    """Return whether an escalation is triggered (REQ 22.5.1)."""
    return risk > limit


def escalation_destination(level: int) -> str:
    """Return the escalation route for a severity level (REQ 22.5.2)."""
    if level <= 1:
        return "level1"
    if level == 2:
        return "ops"
    return "management"


def non_blocking(resolvable: bool) -> bool:
    """Return whether interaction can proceed async (REQ 22.23.1)."""
    return resolvable


def notification_priority_assigned(severity: int) -> str:
    """Assign a priority label from severity (REQ 22.16.2)."""
    if severity >= 3:
        return "high"
    if severity == 2:
        return "medium"
    return "low"


def route_notification(channel: str) -> str:
    """Return the resolved delivery channel (REQ 22.17)."""
    return channel


def alert_triggered(value: float, threshold: float) -> bool:
    """Return whether a metric crossed its alert threshold (REQ 22.6)."""
    return value > threshold


def retry_pending(attempts: int, max_attempts: int) -> bool:
    """Return whether delivery should be retried (REQ 22.20)."""
    return attempts < max_attempts


@dataclass(frozen=True)
class Notification:
    """A deduplicatable notification (REQ 22.18)."""

    channel: str
    event: str
    body: str

    def dedupe_key(self) -> tuple[str, str]:
        """Return the identity used to dedupe notifications."""
        return (self.channel, self.event)


class InteractionChannel(Enum):
    """Notification delivery channels (REQ 22.13/22.14/22.15)."""

    PUSH = "push"
    EMAIL = "email"
    DASHBOARD = "dashboard"


@dataclass
class InteractionEngine:
    """Human interaction lifecycle (REQ 22.1/22.2)."""

    name: str
    _active: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._active = True

    def status(self) -> str:
        """Return the engine state."""
        return "engaged" if self._active else "idle"
