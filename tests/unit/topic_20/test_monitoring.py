"""Tests for Topic 20 — Monitoring and P&L Management.

Covers real-time portfolio monitoring (20.2), capital/position/order/
market/strategy/risk monitoring (20.3-20.8), real-time P&L (20.9),
fees and tax impact (20.12/20.13), net return calculation (20.14),
drawdown monitoring (20.15), benchmark comparison (20.17), alert
thresholds (20.18), anomaly detection (20.19), and dashboard
integration (20.24).
"""

import pytest

from src.common.monitoring.engine import (
    MonitoringEngine,
    anomaly_detected,
    benchmark_comparison,
    capital_level_ok,
    drawdown,
    monitoring_dashboard,
    net_return,
    order_monitored,
    position_monitored,
    real_time_pnl,
    threshold_state,
)


class TestPortfolioMonitoring:
    """REQ 20.2/20.3/20.4/20.5 — portfolio, capital, position, order."""

    def test_position_monitored(self):
        assert position_monitored(qty=10, side="long") is True

    def test_order_monitored(self):
        assert order_monitored(order_id="o-1", status="filled") is True

    def test_capital_level_ok(self):
        assert capital_level_ok(capital=1000.0, floor=100.0) is True

    def test_capital_breached(self):
        assert capital_level_ok(capital=50.0, floor=100.0) is False


class TestPnl:
    """REQ 20.9/20.12/20.13/20.14/20.15."""

    def test_real_time_pnl(self):
        assert real_time_pnl(mark=110.0, entry=100.0, qty=10) == 100.0

    def test_net_return(self):
        assert net_return(gross=10.0, fees=1.0, tax=0.5) == 8.5

    def test_drawdown(self):
        assert drawdown(peak=100.0, value=80.0) == 0.2

    def test_no_drawdown_at_peak(self):
        assert drawdown(peak=100.0, value=100.0) == 0.0


class TestAlerts:
    """REQ 20.17/20.18/20.19/20.24."""

    def test_benchmark_outperformed(self):
        assert benchmark_comparison(strategy=0.10, benchmark=0.06) is True

    def test_threshold_normal(self):
        assert threshold_state(value=50.0, threshold=100.0) == "normal"

    def test_threshold_breached(self):
        assert threshold_state(value=110.0, threshold=100.0) == "breached"

    def test_anomaly_detected(self):
        assert anomaly_detected(deviation=4.5, band=2.0) is True

    def test_dashboard_connected(self):
        assert monitoring_dashboard(connected=True) is True


class TestEngine:
    """REQ 20.1 — monitoring lifecycle."""

    def test_engine_requires_name(self):
        with pytest.raises(ValueError):
            MonitoringEngine(name=" ")

    def test_engine_status(self):
        eng = MonitoringEngine(name="m")
        assert eng.status() == "monitoring"


pytestmark = pytest.mark.unit
