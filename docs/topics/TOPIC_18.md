# Topic 18 — Paper Trading Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-18-paper-trading`

## Decision

**Implementation required (core).** Topic 18 validates strategies in a
risk-free, virtual-capital pilot before any live transition:

- **18.2 / 18.2.1 / 18.2.2**: virtual capital configuration and reset
  rules.
- **18.3 / 18.4 / 18.4.1 / 18.4.2**: live-data integration, simulated
  order generation, and order validation.
- **18.5 / 18.5.1 / 18.5.2**: simulated execution model and failure
  handling.
- **18.6 / 18.7**: slippage and fee simulation.
- **18.9 / 18.10**: position and cash balance tracking.
- **18.11 / 18.11.1**: real-time P&L calculation.
- **18.15**: risk metrics.
- **18.17 / 18.18**: execution accuracy and signal-to-execution
  tracking.
- **18.19 / 18.20**: monitoring and alerts.
- **18.27**: paper trading duration criteria.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 18.2.1 | Initial Virtual Capital | `engine.py` (`virtual_capital_valid`) | `test_paper.py::TestVirtualAccount` |
| 18.4.2 | Order Validation | `engine.py` (`validate_order`) | `test_paper.py::TestOrders` |
| 18.6 | Slippage Simulation | `engine.py` (`slippage_fill`) | `test_paper.py::TestExecution` |
| 18.7 | Fee Simulation | `engine.py` (`fee_applied`) | `test_paper.py::TestExecution` |
| 18.9 | Position Tracking | `engine.py` (`position_size`) | `test_paper.py::TestExecution` |
| 18.10 | Cash Balance Tracking | `engine.py` (`cash_after_trade`) | `test_paper.py::TestExecution` |
| 18.19 | Paper Trading Monitoring | `engine.py` (`PaperEngine.monitor`) | `test_paper.py::TestPaperEngine` |
| 18.27 | Duration Criteria | `engine.py` (`PaperEngine.duration_met`) | `test_paper.py::TestPaperEngine` |
| — | Full Topic 18 contract | `registry.py` (+ traceability test) | `test_paper_registry.py` |

## Registry addition

Topic 18 (absent before) added as the authoritative 42-item block.
SRS uses `Field Specification` with `Nested Children`; captures include
18.4.1 Order Generation Conditions, 18.5.1 Execution Model,
18.11.1 P&L Calculation, 18.22.1/18.22.2 Reconciliation, and
18.28.1/18.28.2 Readiness/Approval.

## Validation

- `python -m pytest -m unit` → **388 passed** (13 from Topic 18)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (90 files)

## Notes / decisions

- `src/common/paper/` mirrors the earlier engine packages.
- Order validation is strict: unknown side, non-positive quantity or
  price raise `ValueError` (REQ 18.4.2), failing fast before fill.
- Slippage and fee are both applied additively to price
  (`price × (1 + slippage)` and `price × (1 + fee)`), the
  conservative convention used across topics.
- The engine tracks the pilot window (`duration_met`) so the
  paper-to-live transition gate (18.28) can be checked downstream.