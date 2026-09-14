"""Topic 20 — Monitoring and P&L Management.

Real-time portfolio monitoring across capital, position, order,
strategy and risk, coupled with P&L accounting (real-time, fees, tax,
drawdown), alert thresholds, anomaly detection and dashboard hooks.
"""

from .engine import (
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

__all__ = [
    "MonitoringEngine",
    "anomaly_detected",
    "benchmark_comparison",
    "capital_level_ok",
    "drawdown",
    "monitoring_dashboard",
    "net_return",
    "order_monitored",
    "position_monitored",
    "real_time_pnl",
    "threshold_state",
]
