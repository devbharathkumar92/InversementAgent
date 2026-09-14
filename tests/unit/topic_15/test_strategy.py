"""Tests for Topic 15 — Strategy Engine.

Covers strategy definition (15.2), entry conditions (15.4), exit
conditions (15.5), position sizing (15.6), capital allocation (15.7),
stop-loss (15.9), profit-taking (15.10), risk-reward/liquidity/market
requirements (15.11-15.13), strategy selection (15.14), conflict
resolution (15.18), failure detection (15.22), and re-evaluation
(15.26).
"""

import pytest

from src.common.strategy.engine import (
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


class TestEntryExit:
    """REQ 15.4/15.5 — entry and exit conditions."""

    def test_entry_met(self):
        assert entry_met({"signal": "buy", "price": 100}, entry={"signal": "buy"}) is True

    def test_entry_not_met(self):
        assert entry_met({"signal": "sell", "price": 100}, entry={"signal": "buy"}) is False

    def test_exit_met(self):
        assert exit_met({"stop": True}, exit_conditions={"stop": True}) is True

    def test_exit_not_met(self):
        assert exit_met({"stop": False}, exit_conditions={"stop": True}) is False


class TestPositionSizing:
    """REQ 15.6.1/15.6.2 — size bounded by capital and limits."""

    def test_position_size_bounded(self):
        assert position_size(capital=100000, fraction=0.1, max_size=8000) == 8000

    def test_position_size_uncapped(self):
        assert position_size(capital=100000, fraction=0.1, max_size=50000) == 10000

    def test_allocation_limits(self):
        assert allocate_capital({}) == 0.0


class TestRiskRules:
    """REQ 15.9/15.10/15.11-15.13 — enforced risk constraints."""

    def test_stop_loss_hit(self):
        assert stop_loss_hit(price=95, stop=100) is True

    def test_stop_loss_not_hit(self):
        assert stop_loss_hit(price=105, stop=100) is False

    def test_fails_risk_reward(self):
        assert fails_requirements(reward=2.0, risk=5.0, risk_reward_min=3.0) is True

    def test_meets_liquidity(self):
        assert fails_requirements(liquidity=1e6, min_liquidity=1e3) is False


class TestStrategySelection:
    """REQ 15.14/15.18/15.18.2 — selection, conflict, priority."""

    def test_strategy_conflict_detected(self):
        assert strategy_conflict(strategy_a="momentum", strategy_b="mean_reversion") is True

    def test_priority_wins(self):
        assert conflict_priority("momentum", {"momentum": 3, "mean_reversion": 2}) == "momentum"

    def test_strategy_engine_requires_name(self):
        with pytest.raises(ValueError):
            StrategyEngine(name="   ")

    def test_strategy_needs_name(self):
        with pytest.raises(ValueError):
            Strategy(name="")


class TestLifecycle:
    """REQ 15.22/15.26 — failure detection and strategy re-evaluation."""

    def test_failure_detected(self):
        eng = StrategyEngine(name="s")
        assert eng.failed(returns=-0.5) is True

    def test_reevaluate_flips_active(self):
        eng = StrategyEngine(name="s")
        assert eng.reevaluate(active=True, score=20, threshold=50) is False


pytestmark = pytest.mark.unit
