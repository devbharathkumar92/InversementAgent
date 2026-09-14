"""Topic 17 — Backtesting and Simulation.

Time-ordered market replay, strategy simulation, transaction costs and
slippage, multi-condition and stress testing, walk-forward validation,
overfitting detection, performance metrics, benchmark comparison, and
reproducible engines.
"""

from .engine import (
    BacktestEngine,
    apply_slippage,
    benchmark_outperformed,
    detect_overfit,
    replay_ordered,
    returns_after_cost,
    stress_test,
    validate_walkforward,
)

__all__ = [
    "BacktestEngine",
    "apply_slippage",
    "benchmark_outperformed",
    "detect_overfit",
    "replay_ordered",
    "returns_after_cost",
    "stress_test",
    "validate_walkforward",
]
