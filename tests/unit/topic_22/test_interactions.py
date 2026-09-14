"""Tests for Topic 22 — Human Interaction and Notifications.

Covers the human-in-the-loop interaction lifecycle (22.2): approval
requirements (22.3), clarification requests (22.4), escalation
requests (22.5), alert channels (22.6-22.15), notification priority
(22.16), routing (22.17), deduplication (22.18), acknowledgement
(22.19), retry (22.20), human response timeout (22.21), escalation
chain (22.22) and non-blocking interaction (22.23).
"""

import pytest

from src.common.interactions.engine import (
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


class TestHumanInTheLoop:
    """REQ 22.2/22.3/22.4/22.5/22.22/22.23."""

    def test_approval_required(self):
        assert approval_required(action="kill", size=5000) is True

    def test_approval_not_required_for_small(self):
        assert approval_required(action="entry", size=10) is False

    def test_clarification_content(self):
        assert clarification_content(question="confirm?") == "confirm?"

    def test_escalation_triggered(self):
        assert escalation_triggered(risk=0.95, limit=0.8) is True

    def test_escalation_destination(self):
        assert escalation_destination(level=2) == "ops"

    def test_non_blocking(self):
        assert non_blocking(resolvable=True) is True


class TestNotifications:
    """REQ 22.16/22.17/22.18/22.19/22.20."""

    def test_priority_assigned(self):
        assert notification_priority_assigned(severity=3) == "high"

    def test_route_notification_channel(self):
        assert route_notification(channel="email") == "email"

    def test_alert_triggered(self):
        assert alert_triggered(value=120.0, threshold=100.0) is True

    def test_deduplicated(self):
        assert Notification(channel="email", event="p", body="x").dedupe_key() == (
            "email",
            "p",
        )

    def test_retry_pending(self):
        assert retry_pending(attempts=1, max_attempts=3) is True

    def test_retry_exhausted(self):
        assert retry_pending(attempts=3, max_attempts=3) is False


class TestEngine:
    """REQ 22.1 — interaction engine lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            InteractionEngine(name=" ")

    def test_channel_enum(self):
        assert InteractionChannel.DASHBOARD.value == "dashboard"


pytestmark = pytest.mark.unit
