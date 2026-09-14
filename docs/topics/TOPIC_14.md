# Topic 14 — Opportunity Scoring Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-14-opportunity-scoring`

## Decision

**Implementation required (core).** Topic 14 is the scoring layer that
produces a comparable, weighted composite score per opportunity:

- **14.2 / 14.2.2**: a scoring framework with a weighted composite
  formula.
- **14.3-14.15**: component scores (return potential, risk, risk-reward,
  probability, liquidity, volatility, time-to-opportunity, data
  confidence, market condition, news impact, cost/fee, tax impact,
  capital requirement).
- **14.16 / 14.16.1 / 14.16.2**: composite score from component scores
  and weights.
- **14.17 / 14.17.1 / 14.17.2**: weight definition and validation
  (non-negative, sum to 1, canonical names).
- **14.18 / 14.18.1**: minimum-score thresholds.
- **14.19**: opportunity ranking.
- **14.21 / 14.21.1**: score recalculation triggers.
- **14.22 / 14.22.1 / 14.22.2**: score decay and expiry.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 14.3-14.9 | Component Scores | `engine.py` (`return_potential_score`, `risk_score`, `risk_reward_score`) | `test_scoring.py::TestComponentScores` |
| 14.16/14.16.1/14.16.2 | Composite Score | `engine.py` (`composite_score`) | `test_scoring.py::TestCompositeScore` |
| 14.17.1/14.17.2 | Weight Validation | `engine.py` (`weights_valid`) | `test_scoring.py::TestWeightValidation` |
| 14.18/14.18.1 | Minimum Score Threshold | `engine.py` (`acceptable`) | `test_scoring.py::TestThresholds` |
| 14.19 | Opportunity Ranking | `engine.py` (`ScoringEngine.rank`) | `test_scoring.py::TestRanking` |
| 14.21 | Score Recalculation | `engine.py` (`recalculate`) | `test_scoring.py::TestRecalculationAndDecay` |
| 14.22/14.22.1/14.22.2 | Score Decay and Expiry | `engine.py` (`decayed_score`) | `test_scoring.py::TestRecalculationAndDecay` |
| — | Full Topic 14 contract | `registry.py` (+ traceability test) | `test_scoring_registry.py` |

## Registry addition

Topic 14 (absent before) added as the authoritative 41-item block,
exactly matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **325 passed** (17 from Topic 14)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (82 files)

## Notes / decisions

- Component scores are normalized to a 0-100 scale; only canonical
  component names are accepted in weight sets.
- The composite uses `sum(component * weight)` and raises `ValueError`
  on invalid weights to fail explicitly rather than silently mismatching.
- `risk_score` inverts the risk metric (lower risk → higher score) so
  all components are aligned as higher-is-better.
- Score decay is proportional; a decayed score at or below the expiry
  floor is zeroed out (REQ 14.22.2).