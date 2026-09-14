"""Topic 20 — Monitoring and P&L Management.

Tracks portfolio state (positions, orders, capital) and computes
real-time P&L, net of fees and tax, with drawdown, benchmarks, alert
thresholds and anomaly detection (REQ 20.1-20.30 enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass, field


def position_monitored(qty: float, side: str) -> bool:
    """Return whether a position is being monitored (REQ 20.4)."""
    return qty >= 0 and side in {"long", "short", "flat"}


def order_monitored(order_id: str, status: str) -> bool:
    """Return whether an order is being tracked (REQ 20.5)."""
    return bool(order_id) and status in {"new", "filled", "partial", "cancelled"}


def capital_level_ok(capital: float, floor: float) -> bool:
    """Return whether capital is above the monitoring floor (REQ 20.3)."""
    return capital >= floor


def real_time_pnl(mark: float, entry: float, qty: float) -> float:
    """Compute the mark-to-market P&L for a position (REQ 20.9)."""
    return (mark - entry) * qty


def net_return(gross: float, fees: float, tax: float) -> float:
    """Compute net return after fees and tax (REQ 20.14.3)."""
    return gross - fees - tax


def drawdown(peak: float, value: float) -> float:
    """Return the fractional drawdown from peak (REQ 20.15)."""
    if peak == 0:
        return 0.0
    return max(0.0, (peak - value) / peak)


def benchmark_comparison(strategy: float, benchmark: float) -> bool:
    """Return whether the strategy outperformed the benchmark (REQ 20.17)."""
    return strategy > benchmark


def threshold_state(value: float, threshold: float) -> str:
    """Return the alert state for a monitored metric (REQ 20.18.2)."""
    return "breached" if value > threshold else "normal"


def anomaly_detected(deviation: float, band: float) -> bool:
    """Return whether deviation exceeds the anomaly band (REQ 20.19)."""
    return deviation > band


def monitoring_dashboard(connected: bool) -> bool:
    """Return whether the monitoring dashboard is connected (REQ 20.24)."""
    return connected


@dataclass
class MonitoringEngine:
    """Monitoring lifecycle (REQ 20.1)."""

    name: str
    _active: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._active = True

    def status(self) -> str:
        """Return the current monitoring engine state (REQ 20.1)."""
        return "monitoring" if self._active else "stopped"
