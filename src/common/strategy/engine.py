"""Topic 15 — Strategy Engine.

Enforces a strategy's entry/exit conditions, computes bounded position
sizes, enforces risk/liquidity/market requirements, selects strategies
and resolves conflicts by priority, and detects failure to trigger
re-evaluation (REQ 15.1-15.30 enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


def entry_met(market: dict[str, Any], entry: dict[str, Any]) -> bool:
    """Return whether the market snapshot satisfies the entry (15.4)."""
    return all(market.get(k) == v for k, v in entry.items())


def exit_met(market: dict[str, Any], exit_conditions: dict[str, Any]) -> bool:
    """Return whether the market snapshot satisfies exit conditions (15.5)."""
    return all(market.get(k) == v for k, v in exit_conditions.items())


def position_size(capital: float, fraction: float, max_size: float) -> float:
    """Size a position from capital*fraction, capped by max_size (15.6.2)."""
    return min(capital * fraction, max_size)


def allocate_capital(_constraints: dict[str, Any]) -> float:
    """Allocate capital per rules; currently returns a neutral 0.0."""
    return 0.0


def stop_loss_hit(price: float, stop: float) -> bool:
    """Return whether price has breached the stop-loss level (15.9.1)."""
    return price <= stop


def fails_requirements(
    reward: float | None = None,
    risk: float | None = None,
    risk_reward_min: float | None = None,
    liquidity: float | None = None,
    min_liquidity: float | None = None,
) -> bool:
    """Check risk-reward and liquidity constraints against a strategy (15.11/15.12)."""
    if risk_reward_min is not None and reward is not None and risk is not None:
        if risk <= 0 or reward / risk < risk_reward_min:
            return True
    if min_liquidity is not None and liquidity is not None and liquidity < min_liquidity:
        return True
    return False


def strategy_conflict(strategy_a: str, strategy_b: str) -> bool:
    """Return whether two strategies signal in opposite directions (15.18.1)."""
    return strategy_a != strategy_b


def conflict_priority(strategy: str, priorities: dict[str, int]) -> str:
    """Resolve a conflict by electing the highest-priority strategy (15.18.2)."""
    return max(priorities, key=lambda s: (priorities[s], s == strategy))


@dataclass
class Strategy:
    """A definable, named strategy (REQ 15.2)."""

    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")


@dataclass
class StrategyEngine:
    """Evaluates and manages the lifecycle of strategies."""

    name: str
    history: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def failed(self, returns: float) -> bool:
        """Flag a strategy as failed when returns are strongly negative (15.22)."""
        return returns <= -0.5

    def reevaluate(self, active: bool, score: float, threshold: float) -> bool:
        """Re-evaluate a strategy; deactivate when score drops below (15.26)."""
        return active and score >= threshold
