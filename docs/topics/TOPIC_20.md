# Topic 20 — Monitoring and P&L Management

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-20-monitoring`

## Decision

**Implementation required (core).** Topic 20 gives the operator a
real-time view of the portfolio and its P&L:

- **20.2 / 20.3 / 20.4 / 20.5**: real-time portfolio, capital,
  position and order monitoring.
- **20.9**: real-time P&L.
- **20.12 / 20.13**: fees and charges, tax impact.
- **20.14 / 20.14.1 / 20.14.2 / 20.14.3**: gross return, costs and
  charges, net return calculation.
- **20.15**: drawdown monitoring.
- **20.17**: benchmark comparison.
- **20.18 / 20.18.1 / 20.18.2**: alert threshold definition and
  trigger.
- **20.19**: anomaly detection.
- **20.24**: monitoring dashboard integration.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 20.4 | Position Monitoring | `engine.py` (`position_monitored`) | `test_monitoring.py::TestPortfolioMonitoring` |
| 20.5 | Order Monitoring | `engine.py` (`order_monitored`) | `test_monitoring.py::TestPortfolioMonitoring` |
| 20.3 | Capital Monitoring | `engine.py` (`capital_level_ok`) | `test_monitoring.py::TestPortfolioMonitoring` |
| 20.9 | Real-Time P&L | `engine.py` (`real_time_pnl`) | `test_monitoring.py::TestPnl` |
| 20.14.3 | Net Return Calculation | `engine.py` (`net_return`) | `test_monitoring.py::TestPnl` |
| 20.15 | Drawdown Monitoring | `engine.py` (`drawdown`) | `test_monitoring.py::TestPnl` |
| 20.17 | Benchmark Comparison | `engine.py` (`benchmark_comparison`) | `test_monitoring.py::TestAlerts` |
| 20.18.2 | Alert Trigger | `engine.py` (`threshold_state`) | `test_monitoring.py::TestAlerts` |
| 20.19 | Anomaly Detection | `engine.py` (`anomaly_detected`) | `test_monitoring.py::TestAlerts` |
| 20.24 | Dashboard Integration | `engine.py` (`monitoring_dashboard`) | `test_monitoring.py::TestAlerts` |
| 20.1 | Monitoring Objectives | `engine.py` (`MonitoringEngine`) | `test_monitoring.py::TestEngine` |
| — | Full Topic 20 contract | `registry.py` (+ traceability test) | `test_monitoring_registry.py` |

## Registry addition

Topic 20 (absent before) added as the authoritative 37-item block.
Captures the `Nested Children`: 20.14.1 Gross Return, 20.14.2 Costs
and Charges, 20.14.3 Net Return; 20.18.1 Alert Threshold Definition;
20.22.1 Position Reconciliation; 20.22.2 Cash and P&L.

## Validation

- `python -m pytest -m unit` → **425 passed** (16 from Topic 20)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (94 files)

## Notes / decisions

- P&L is mark-to-market `(mark − entry) × qty` (20.9); net return is
  gross minus fees and tax (20.14.3).
- Drawdown is floor-clamped at 0 so a rising peak reports no drawdown.
- `threshold_state` compares against a single alert threshold,
  discriminating breach vs normal (20.18.2); multi-tier thresholds are
  dashboard configuration.
- Anomaly detection flags any deviation beyond the configured band
  (20.19); the monitoring engine is a lifecycle object whose status
  can be surfaced on the dashboard (20.24).