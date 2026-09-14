"""Topic 15 — Strategy Engine.

Strategy definition, entry/exit conditions, position sizing, capital
allocation, stop-loss and profit-taking rules, risk/liquidity/market
requirements, strategy selection, conflict resolution, failure
detection, and re-evaluation.
"""

from .engine import (
    Strategy,
    StrategyEngine,
    allocate_capital,
    conflict_priority,
    entry_met,
    exit_met,
    fails_requirements,
    position_size,
    stop_loss_hit,
    strategy_conflict,
)

__all__ = [
    "Strategy",
    "StrategyEngine",
    "allocate_capital",
    "conflict_priority",
    "entry_met",
    "exit_met",
    "fails_requirements",
    "position_size",
    "stop_loss_hit",
    "strategy_conflict",
]
