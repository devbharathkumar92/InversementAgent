# Topic 19 — Decision Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-19-decision-engine`

## Decision

**Implementation required (core).** Topic 19 turns evaluated
opportunities into a single prioritized, gated action:

- **19.2 / 19.2.1 / 19.2.2**: decision inputs and validation.
- **19.3 / 19.3.2**: preconditions incl. failed-precondition handling.
- **19.4 / 19.5 / 19.6**: opportunity, strategy and risk eligibility.
- **19.8 / 19.8.1 / 19.8.2**: decision rules, rule order and priority.
- **19.9 / 19.10 / 19.11**: thresholds, ranking, prioritization.
- **19.12 / 19.12.1 / 19.12.2**: capital allocation decision and limits.
- **19.13 / 19.14 / 19.15**: entry, exit, no-action decisions.
- **19.16 / 19.17**: rejection rules and expiry.
- **19.19 / 19.19.1 / 19.19.2**: conflict detection and resolution.
- **19.20 / 19.20.1 / 19.20.3**: human approval gate.
- **19.24**: decision validation.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 19.2.2 | Input Validation | `engine.py` (`validate_inputs`) | `test_decision.py::TestInputsPreconditions` |
| 19.3.2 | Failed Preconditions | `engine.py` (`eligibility_met`) | `test_decision.py::TestInputsPreconditions` |
| 19.4/19.5/19.6 | Eligibility gates | `engine.py` (`eligibility_met`) | `test_decision.py::TestDecisionRules` |
| 19.8.2/19.10 | Rule Priority / Ranking | `engine.py` (`decision_priority`) | `test_decision.py::TestDecisionRules` |
| 19.12.1/19.12.2 | Allocation Eligibility/Limits | `engine.py` (`capital_eligible`) | `test_decision.py::TestDecisionRules` |
| 19.13 | Entry Decision | `engine.py` (`entry_decision`) | `test_decision.py::TestOutcomes` |
| 19.15 | No-Action Decision | `engine.py` (`no_action`) | `test_decision.py::TestOutcomes` |
| 19.16 | Decision Rejection | `engine.py` (`decision_rejected`) | `test_decision.py::TestOutcomes` |
| 19.17 | Decision Expiry | `engine.py` (`decision_expired`) | `test_decision.py::TestOutcomes` |
| 19.19.1 | Conflict Detection | `engine.py` (`conflict_handled`) | `test_decision.py::TestOutcomes` |
| 19.20.1/19.20.3 | Approval Gate | `engine.py` (`approval_gate`) | `test_decision.py::TestOutcomes` |
| 19.24 | Decision Validation | `engine.py` (`DecisionEngine.validate`) | `test_decision.py::TestEngine` |
| — | Full Topic 19 contract | `registry.py` (+ traceability test) | `test_decision_registry.py` |

## Registry addition

Topic 19 (absent before) added as the authoritative 43-item block.
Includes every nested child (19.3.1 Preconditions, 19.8.1 Decision Rule
Order, 19.12.1 Allocation Eligibility, 19.19.1 Conflict Detection,
19.20.1-3 Approval Trigger/Timeout/Rejection). 19.27 is present in the
SRS as "Decision Performance Metrics".

## Validation

- `python -m pytest -m unit` → **409 passed** (21 from Topic 19)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (92 files)

## Notes / decisions

- Eligibility gate threshold is a decision-rule constant (≥ 0.6 per
  gate) representing the combined opportunity/strategy/risk filter
  (REQ 19.4-19.6).
- The approval gate is bypass-able: only `kill`-class actions require
  explicit human approval (REQ 19.20.1), while approval rejection
  blocks the action (19.20.3).
- `decision_priority` resolves the highest-ranked candidate, the
  tie-break for conflicting strategies (REQ 19.19).
- Conflict detection returns whether the two strategies are distinct
  and hence resolvable; true resolution is integration scope with the
  top-ranked strategy selected.