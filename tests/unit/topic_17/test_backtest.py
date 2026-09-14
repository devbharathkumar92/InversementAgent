"""Tests for Topic 17 — Backtesting and Simulation.

Covers dataset selection (17.2), market replay/time ordering (17.4),
strategy simulation (17.5), transaction costs/slippage (17.9/17.12),
bull/bear/sideways testing (17.16), stress testing (17.17), walk-
forward windows (17.20.1), overfitting detection (17.21), performance
metrics (17.22), benchmark comparison (17.24), and reproducibility
(17.25).
"""

import pytest

from src.common.backtest.engine import (
    BacktestEngine,
    apply_slippage,
    benchmark_outperformed,
    detect_overfit,
    replay_ordered,
    returns_after_cost,
    stress_test,
    validate_walkforward,
)


class TestDataset:
    """REQ 17.2.1/17.4.2 — dataset selection and time-ordered replay."""

    def test_replay_ordered(self):
        assert replay_ordered([1, 2, 3]) is True

    def test_replay_unordered(self):
        assert replay_ordered([3, 1, 2]) is False


class TestCosts:
    """REQ 17.9/17.9.1/17.12.1 — transaction costs and slippage."""

    def test_returns_after_cost(self):
        assert returns_after_cost(gross=10.0, cost=0.5) == 9.5

    def test_slippage_applied(self):
        assert apply_slippage(price=100.0, slippage=0.01) == 101.0


class TestConditions:
    """REQ 17.16/17.17/17.20.1 — multi-condition and stress testing."""

    def test_bull_bear_sideways_covered(self):
        assert {"bull", "bear", "sideways"}.issubset(stress_test.regimes)

    def test_walkforward_valid(self):
        assert validate_walkforward(start=0, end=100, window=50) is True

    def test_walkforward_invalid_window(self):
        assert validate_walkforward(start=0, end=100, window=200) is False


class TestOverfit:
    """REQ 17.21.1 — overfitting detection."""

    def test_train_test_divergence_flags_overfit(self):
        assert detect_overfit(train=0.95, test=0.55) is True

    def test_no_overfit(self):
        assert detect_overfit(train=0.60, test=0.58) is False


class TestMetrics:
    """REQ 17.22/17.24 — performance metrics and benchmark comparison."""

    def test_benchmark_outperformed(self):
        assert benchmark_outperformed(strategy=0.12, benchmark=0.07) is True

    def test_benchmark_not_outperformed(self):
        assert benchmark_outperformed(strategy=0.04, benchmark=0.07) is False


class TestEngine:
    """REQ 17.5/17.25 — simulation engine lifecycle."""

    def test_engine_requires_name(self):
        with pytest.raises(ValueError):
            BacktestEngine(name=" ")

    def test_engine_reproducible_seed(self):
        first = BacktestEngine(name="b", seed=7)
        second = BacktestEngine(name="b", seed=7)
        assert first.seed == second.seed


pytestmark = pytest.mark.unit
