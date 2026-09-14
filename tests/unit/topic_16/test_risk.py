"""Tests for Topic 16 — Risk and Safety Engine.

Covers capital protection (16.2), exposure limits (16.3/16.4), loss
limits (16.5/16.6), drawdown (16.7), stop-loss enforcement (16.8),
concentration/counterparty controls (16.12/16.13), kill switch
(16.18), emergency stop (16.19), human approval gates (16.20), risk
escalation (16.21), and risk monitoring (16.22).
"""

import pytest

from src.common.risk.engine import (
    RiskEngine,
    approval_required,
    concentration_exceeded,
    drawdown_within_limit,
    exposes_within_limit,
    kill_switch_triggered,
    loss_within_limit,
    returns_below_drawdown,
    stop_loss_breached,
)


class TestExposure:
    """REQ 16.3/16.4/16.12 — capital/position exposure and concentration."""

    def test_exposure_within_limit(self):
        assert exposes_within_limit(exposure=0.1, cap=0.5) is True

    def test_exposure_exceeds_limit(self):
        assert exposes_within_limit(exposure=0.6, cap=0.5) is False

    def test_concentration_ok(self):
        assert concentration_exceeded(weight=0.1, cap=0.25) is False

    def test_concentration_exceeded(self):
        assert concentration_exceeded(weight=0.5, cap=0.25) is True


class TestLossAndDrawdown:
    """REQ 16.5/16.6/16.7 — per-trade/daily loss and drawdown limits."""

    def test_loss_within_limit(self):
        assert loss_within_limit(loss=0.05, limit=0.10) is True

    def test_loss_exceeds_limit(self):
        assert loss_within_limit(loss=0.12, limit=0.10) is False

    def test_drawdown_within(self):
        assert drawdown_within_limit(drawdown=0.10, limit=0.25) is True

    def test_drawdown_triggered(self):
        assert returns_below_drawdown(value=80, peak=100) is True


class TestStopLoss:
    """REQ 16.8 — stop-loss enforcement."""

    def test_stop_loss_breached(self):
        assert stop_loss_breached(price=95, stop=100) is True

    def test_no_breach(self):
        assert stop_loss_breached(price=105, stop=100) is False


class TestKillSwitch:
    """REQ 16.18 — kill-switch triggers."""

    def test_kill_switch_triggered(self):
        assert kill_switch_triggered(drawdown=0.4, limit=0.3) is True

    def test_kill_switch_calm(self):
        assert kill_switch_triggered(drawdown=0.1, limit=0.3) is False


class TestApprovalGates:
    """REQ 16.20 — human approval required for flagged actions."""

    def test_approval_required(self):
        assert approval_required(action="kill", sensitive=True) is True

    def test_no_approval_needed(self):
        assert approval_required(action="tick", sensitive=False) is False


class TestRiskEngine:
    """REQ 16.2/16.21.1/16.22 — aggregated engine behaviors."""

    def test_engine_monitors_risk(self):
        eng = RiskEngine(name="r")
        assert eng.monitor() == "nominal"

    def test_engine_escalates(self):
        assert RiskEngine.escalate(threat=0.9, level=0.5) is True

    def test_engine_requires_name(self):
        with pytest.raises(ValueError):
            RiskEngine(name="  ")


pytestmark = pytest.mark.unit
