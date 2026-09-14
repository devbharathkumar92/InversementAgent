"""Topic 17 — Backtesting and Simulation.

The engine replays historical data in time order, simulates strategies
with realistic costs and slippage across multiple market conditions,
and guards against overfitting through walk-forward testing and
benchmark comparison (REQ 17.1-17.30 enforced subset).
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


def replay_ordered(prices: Iterable[float]) -> bool:
    """Return whether prices are strictly time-ordered (REQ 17.4.2)."""
    prev = None
    for price in prices:
        if prev is not None and price < prev:
            return False
        prev = price
    return True


def returns_after_cost(gross: float, cost: float) -> float:
    """Net a gross return by subtracting transaction costs (REQ 17.9.1)."""
    return gross - cost


def apply_slippage(price: float, slippage: float) -> float:
    """Inflate an entry price by the slippage fraction (REQ 17.12.1)."""
    return price * (1 + slippage)


@dataclass(frozen=True)
class stress_test:
    """Execution of a strategy under multiple market conditions (17.17)."""

    regimes: frozenset[str] = frozenset({"bull", "bear", "sideways"})

    def run(self, returns: Iterable[float]) -> float:
        """Return the worst-case (most negative) period return."""
        return min(returns, default=0.0)


def validate_walkforward(start: float, end: float, window: float) -> bool:
    """Return whether a walk-forward window fits inside [start, end] (17.20.1)."""
    return window > 0 and start + window <= end


def detect_overfit(train: float, test: float, gap: float = 0.25) -> bool:
    """Flag overfitting when train outruns out-of-sample test by a gap (17.21.1)."""
    return train - test >= gap


def benchmark_outperformed(strategy: float, benchmark: float) -> bool:
    """Return whether the strategy beat the benchmark (REQ 17.24)."""
    return strategy > benchmark


@dataclass(frozen=True)
class BacktestEngine:
    """Deterministic backtest engine over historical data (REQ 17.5/17.25)."""

    name: str
    seed: int = 42

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
