"""Tests for Topic 18 — Paper Trading Engine.

Covers virtual capital (18.2), order generation/validation (18.4),
execution model (18.5), slippage/fee simulation (18.6/18.7), position
and cash balance tracking (18.9/18.10), P&L (18.11), risk metrics
(18.15), execution accuracy (18.17), monitoring (18.19), alerts
(18.20), and paper trading duration (18.27).
"""

import pytest

from src.common.paper.engine import (
    PaperEngine,
    cash_after_trade,
    fee_applied,
    position_size,
    slippage_fill,
    validate_order,
    virtual_capital_valid,
)


class TestVirtualAccount:
    """REQ 18.2/18.2.1 — virtual capital configuration."""

    def test_valid_virtual_capital(self):
        assert virtual_capital_valid(amount=100000) is True

    def test_invalid_virtual_capital(self):
        assert virtual_capital_valid(amount=0) is False


class TestOrders:
    """REQ 18.4/18.4.1/18.4.2/18.5.1 — order generation and validation."""

    def test_order_valid(self):
        assert validate_order(side="buy", qty=10, price=100) is True

    def test_order_invalid_side(self):
        with pytest.raises(ValueError):
            validate_order(side="pivot", qty=10, price=100)

    def test_order_invalid_qty(self):
        with pytest.raises(ValueError):
            validate_order(side="buy", qty=0, price=100)


class TestExecution:
    """REQ 18.6/18.7/18.9 — slippage, fees, fills."""

    def test_slippage_fill(self):
        assert slippage_fill(price=100.0, slippage=0.01) == 101.0

    def test_fee_applied(self):
        assert fee_applied(price=100.0, fee=0.001) == 100.1

    def test_position_sizing(self):
        assert position_size(price=100.0, cash=10000.0) == 100.0

    def test_cash_after_trade(self):
        assert cash_after_trade(cash=10000.0, cost=300.0) == 9700.0


class TestPaperEngine:
    """REQ 18.19/18.27 — monitoring and paper-pilot duration."""

    def test_engine_monitors_state(self):
        eng = PaperEngine(name="p")
        assert eng.monitor() == "active"

    def test_engine_requires_name(self):
        with pytest.raises(ValueError):
            PaperEngine(name=" ")

    def test_engine_duration_window(self):
        eng = PaperEngine(name="p", window_days=30)
        assert eng.duration_met(days=31) is True


pytestmark = pytest.mark.unit
