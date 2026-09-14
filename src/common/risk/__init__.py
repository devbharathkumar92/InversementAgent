"""Topic 16 — Risk and Safety Engine.

Exposure, loss, drawdown, stop-loss, concentration and counterparty
controls; kill switch; emergency stop; human approval gates; risk
escalation; and ongoing risk monitoring.
"""

from .engine import (
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

__all__ = [
    "RiskEngine",
    "approval_required",
    "concentration_exceeded",
    "drawdown_within_limit",
    "exposes_within_limit",
    "kill_switch_triggered",
    "loss_within_limit",
    "returns_below_drawdown",
    "stop_loss_breached",
]
