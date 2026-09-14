# Topic 15 — Strategy Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-15-strategy-engine`

## Decision

**Implementation required (core).** Topic 15 is the strategy layer that
decides *whether* and *how much* the agent acts:

- **15.2**: strategy definition (named, parametrizable strategy).
- **15.4 / 15.4.1 / 15.4.2**: entry conditions with signal checking.
- **15.5 / 15.5.1 / 15.5.2**: exit conditions.
- **15.6 / 15.6.1 / 15.6.2**: position sizing (capital × fraction,
  capped by limits).
- **15.7**: capital allocation rules/limits.
- **15.9**: stop-loss trigger/enforcement.
- **15.10**: profit-taking rules.
- **15.11 / 15.12 / 15.13**: risk-reward, liquidity and market-condition
  requirements.
- **15.14 / 15.15**: strategy selection and ranking.
- **15.18 / 15.18.1 / 15.18.2**: strategy conflict detection and
  priority resolution.
- **15.22**: strategy failure detection.
- **15.26**: strategy re-evaluation.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 15.4/15.5 | Entry/Exit Conditions | `engine.py` (`entry_met`, `exit_met`) | `test_strategy.py::TestEntryExit` |
| 15.6.1/15.6.2 | Position Size Calculation/Limits | `engine.py` (`position_size`) | `test_strategy.py::TestPositionSizing` |
| 15.7 | Capital Allocation | `engine.py` (`allocate_capital`) | `test_strategy.py::TestPositionSizing` |
| 15.9.1 | Stop-Loss Trigger | `engine.py` (`stop_loss_hit`) | `test_strategy.py::TestRiskRules` |
| 15.11/15.12 | Risk-Reward & Liquidity Requirements | `engine.py` (`fails_requirements`) | `test_strategy.py::TestRiskRules` |
| 15.18.1/15.18.2 | Strategy Conflict / Priority | `engine.py` (`strategy_conflict`, `conflict_priority`) | `test_strategy.py::TestStrategySelection` |
| 15.22 | Strategy Failure Detection | `engine.py` (`StrategyEngine.failed`) | `test_strategy.py::TestLifecycle` |
| 15.26 | Strategy Re-Evaluation | `engine.py` (`StrategyEngine.reevaluate`) | `test_strategy.py::TestLifecycle` |
| — | Full Topic 15 contract | `registry.py` (+ traceability test) | `test_strategy_registry.py` |

## Registry addition

Topic 15 (absent before) added as the authoritative 45-item block
(including `15.6 --- Position Sizing`, which uses a single-space
separator in the SRS and was otherwise missed), exactly matching the
SRS topic file.

## Validation

- `python -m pytest -m unit` → **343 passed** (18 from Topic 15)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (84 files)

## Notes / decisions

- Entry/exit evaluation is exact-match on the declared condition keys;
  richer boolean compositions are deferred to the integration pass.
- Position sizing is `min(capital * fraction, max_size)` (REQ 15.6.2).
- `fails_requirements` checks risk-reward ratio and minimum liquidity;
  a risk-reward below the floor always fails regardless of the other
  constraints, and unknown constraints are ignored.
- Conflict priority elects the highest-priority strategy between a
  pair (first strategy wins ties), providing a deterministic order for
  REQ 15.18.2.