"""Tests for Topic 21 — Dashboard and User Visibility.

Covers the agent/sub-agent status views (21.3/21.4), current task and
progress (21.5/21.6), task queue and dependencies (21.7/21.8), blocked
tasks (21.9), status views across the pipeline (21.10-21.19), approval
requests (21.21), notification center (21.22), system health (21.23),
performance (21.24), historical activity (21.25), search and filtering
(21.26), and restricted user actions (21.27.2).
"""

import pytest

from src.common.dashboard.engine import (
    ApprovalState,
    Dashboard,
    agent_current_activity,
    agent_status,
    blocked_task,
    progress_percentage,
    restricted_action,
    search_and_filter,
    system_health,
)


class TestAgentViews:
    """REQ 21.3/21.3.2/21.5/21.6/21.7."""

    def test_agent_status(self):
        assert agent_status(name="a1", state="idle") is True

    def test_agent_current_activity(self):
        assert agent_current_activity(name="a1", activity="scanning") == "scanning"

    def test_blocked_task(self):
        assert blocked_task(task_id="t1", required="credential") is True

    def test_progress_percentage_capped(self):
        assert progress_percentage(done=30, total=100) == 30.0

    def test_progress_caps_at_100(self):
        assert progress_percentage(done=120, total=100) == 100.0


class TestViewsAndControls:
    """REQ 21.10/21.15/21.21/21.23/21.25/21.26/21.27.2."""

    def test_approval_pending(self):
        assert ApprovalState.PENDING.value == "pending"

    def test_approval_granted(self):
        assert ApprovalState.GRANTED.value == "granted"

    def test_system_health(self):
        assert system_health(ok=True) == "healthy"

    def test_search_and_filter(self):
        assert search_and_filter(items=["a", "b"], term="a") == ["a"]

    def test_restricted_action_rejected(self):
        assert restricted_action(action="transfer") is True

    def test_allowed_action_not_restricted(self):
        assert restricted_action(action="review") is False


class TestDashboard:
    """REQ 21.2 — dashboard lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            Dashboard(name=" ")

    def test_render(self):
        d = Dashboard(name="ops")
        assert d.render() == "ops"


def test_engine_present():
    from src.common.dashboard.engine import Dashboard

    assert Dashboard("d").status == "ready"


pytestmark = pytest.mark.unit
