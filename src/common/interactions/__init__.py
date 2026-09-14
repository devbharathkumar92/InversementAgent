"""Topic 22 — Human Interaction and Notifications.

Human-in-the-loop touchpoints (approvals, clarifications, escalation),
alert channels, and notification delivery with priority, routing,
deduplication, acknowledgement and retry (REQ 22.1-22.30 subset).
"""

from .engine import (
    InteractionChannel,
    InteractionEngine,
    Notification,
    alert_triggered,
    approval_required,
    clarification_content,
    escalation_destination,
    escalation_triggered,
    non_blocking,
    notification_priority_assigned,
    retry_pending,
    route_notification,
)

__all__ = [
    "InteractionChannel",
    "InteractionEngine",
    "Notification",
    "alert_triggered",
    "approval_required",
    "clarification_content",
    "escalation_destination",
    "escalation_triggered",
    "non_blocking",
    "notification_priority_assigned",
    "retry_pending",
    "route_notification",
]
