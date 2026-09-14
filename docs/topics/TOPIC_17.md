# Topic 17 — Backtesting and Simulation

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-17-backtesting-simulation`

## Decision

**Implementation required (core).** Topic 17 validates strategies
before live/pilot use by replaying history under realistic costs:

- **17.2 / 17.2.1 / 17.2.2**: historical dataset selection/quality.
- **17.4 / 17.4.1 / 17.4.2**: market replay rules and strict time
  ordering.
- **17.5**: strategy simulation.
- **17.9 / 17.9.1**: transaction costs applied after gross returns.
- **17.12 / 17.12.1**: slippage model on entry prices.
- **17.15 / 17.16**: multiple market conditions (bull/bear/sideways).
- **17.17**: stress testing.
- **17.19 / 17.20 / 17.20.1**: out-of-sample and walk-forward testing.
- **17.21 / 17.21.1**: overfitting detection.
- **17.22 / 17.24**: performance metrics and benchmark comparison.
- **17.25**: simulation reproducibility (seeded engines).

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 17.4.2 | Time Ordering | `engine.py` (`replay_ordered`) | `test_backtest.py::TestDataset` |
| 17.9.1 | Transaction Costs | `engine.py` (`returns_after_cost`) | `test_backtest.py::TestCosts` |
| 17.12.1 | Slippage Model | `engine.py` (`apply_slippage`) | `test_backtest.py::TestCosts` |
| 17.16/17.17 | Bull/Bear/Sideways & Stress | `engine.py` (`stress_test`) | `test_backtest.py::TestConditions` |
| 17.20.1 | Walk-Forward Windows | `engine.py` (`validate_walkforward`) | `test_backtest.py::TestConditions` |
| 17.21.1 | Overfitting Indicators | `engine.py` (`detect_overfit`) | `test_backtest.py::TestOverfit` |
| 17.24 | Benchmark Comparison | `engine.py` (`benchmark_outperformed`) | `test_backtest.py::TestMetrics` |
| 17.5/17.25 | Simulation & Reproducibility | `engine.py` (`BacktestEngine`) | `test_backtest.py::TestEngine` |
| — | Full Topic 17 contract | `registry.py` (+ traceability test) | `test_backtest_registry.py` |

## Registry addition

Topic 17 (absent before) added as the authoritative 42-item block.
`Field Specification` heading format with `Nested Children`; the 17.5
`Strategy Simulation` item is a plain section with no children. All
nested items (17.4.1 Market Replay Rules, 17.9.1 Transaction Costs,
17.12.1 Slippage Model, 17.19.1 Training Period, 17.20.1 Walk-Forward
Windows, 17.21.1 Overfitting Indicators) captured exactly.

## Validation

- `python -m pytest -m unit` → **375 passed** (14 from Topic 17)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (88 files)

## Notes / decisions

- `stress_test` is a frozen dataclass exposing the canonical
  bull/bear/sideways regime set and a worst-case `run()`; it doubles
  as the multi-condition harness for REQ 17.16.
- Slippage is conservative: entry price is inflated by the slippage
  fraction (17.12.1), while exit-side deflation is integration scope.
- Overfitting is flagged when in-sample beats out-of-sample by ≥ 25
  points (17.21.1), a configurable gap.