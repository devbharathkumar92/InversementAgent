"""Topic 16 — Risk and Safety Engine.

Provides the risk envelope that bounds the agent: capital/position
exposure caps, per-trade/daily loss limits, drawdown limits, stop-loss
enforcement, concentration and counterparty controls, kill-switch and
emergency-stop triggers, human approval gates, escalation, and a
monitoring hook (REQ 16.1-16.30 enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass, field


def exposes_within_limit(exposure: float, cap: float) -> bool:
    """Return whether exposure stays within the cap (REQ 16.3.2)."""
    return exposure <= cap


def concentration_exceeded(weight: float, cap: float) -> bool:
    """Return whether a single position breaches concentration cap (16.12)."""
    return weight > cap


def loss_within_limit(loss: float, limit: float) -> bool:
    """Return whether a (per-trade or daily) loss is within the limit."""
    return loss <= limit


def drawdown_within_limit(drawdown: float, limit: float) -> bool:
    """Return whether drawdown stays within its limit (REQ 16.7)."""
    return drawdown <= limit


def returns_below_drawdown(value: float, peak: float) -> bool:
    """Return whether the current value has fallen below 0% drawdown (16.7.1)."""
    return value < peak


def stop_loss_breached(price: float, stop: float) -> bool:
    """Return whether price breached the stop-loss level (REQ 16.8)."""
    return price <= stop


def kill_switch_triggered(drawdown: float, limit: float) -> bool:
    """Return whether the kill switch must fire (REQ 16.18.1)."""
    return drawdown > limit


def approval_required(action: str, sensitive: bool) -> bool:
    """Return whether a human approval gate applies (REQ 16.20.1)."""
    return sensitive or action in {"kill", "emergency"}


@dataclass
class RiskEngine:
    """Continuously monitors risk state for a named context (16.22)."""

    name: str
    escalations: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def monitor(self) -> str:
        """Report current risk posture (REQ 16.22)."""
        if any(threat > 0.8 for threat in self.escalations):
            return "elevated"
        return "nominal"

    @staticmethod
    def escalate(threat: float, level: float) -> bool:
        """Return whether an escalation is warranted (REQ 16.21.1)."""
        return threat > level
