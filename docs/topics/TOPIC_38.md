# Topic 38 — PoV Release Criteria

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-38-pov-release`

## Decision

**Implementation required (core).** Topic 38 defines the gating
criteria a PoV must satisfy before release:

- **38.2 / 38.2.1 / 38.2.2**: functional minimums and functional
  blocking conditions.
- **38.3 / 38.4 / 38.5 / 38.6**: technical, data-quality, agent
  behaviour and decision-quality criteria.
- **38.7 / 38.7.1 / 38.7.2**: mandatory safety conditions and safety
  failure conditions.
- **38.8 / 38.9 / 38.9.1 / 38.9.2 / 38.10 / 38.11**: backtesting,
  paper-trading (minimums + failure), monitoring and P&L tracking
  criteria.
- **38.12 / 38.13 / 38.14 / 38.15 / 38.16 / 38.17**: dashboard,
  notification, error-recovery, security, reliability and
  performance criteria.
- **38.18 / 38.19 / 38.20 / 38.21 / 38.22 / 38.23 / 38.24**: test
  coverage, SRS compliance, traceability, auditability, human
  approval, evidence and failure criteria.
- **38.25 / 38.25.1 / 38.25.2**: release blocking conditions and stop
  actions.
- **38.26 / 38.26.1 / 38.26.2**: readiness checklist and readiness
  score.
- **38.27 / 38.28 / 38.29 / 38.29.1 / 38.29.2 / 38.30**: final
  validation, PoV approval, release decision (approval/rejection)
  and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 38.2.1/38.2.2 | Functional Minimums / Blockers | `engine.py` (`functional_required`) | `test_pov_release.py::TestCriteria` |
| 38.7.1/38.7.2 | Mandatory Safety / Failure | `engine.py` (`safety_met`) | `test_pov_release.py::TestCriteria` |
| 38.9.1/38.9.2 | Paper-Trading Minimums / Failure | `engine.py` (`paper_trading_ok`) | `test_pov_release.py::TestCriteria` |
| 38.10 | Monitoring Criteria | `engine.py` (`monitoring_ok`) | `test_pov_release.py::TestReadiness` |
| 38.18 | Test Coverage Criteria | `engine.py` (`coverage_met`) | `test_pov_release.py::TestCriteria` |
| 38.25.1 | Blocking Condition | `engine.py` (`blocking_free`) | `test_pov_release.py::TestReadiness` |
| 38.26.1/38.26.2 | Readiness Checklist / Score | `engine.py` (`readiness_gate`) | `test_pov_release.py::TestReadiness` |
| 38.27 | Final Validation | `engine.py` (`final_validation`) | `test_pov_release.py::TestDecision` |
| 38.22/38.28 | Human / PoV Approval | `engine.py` (`human_approved`) | `test_pov_release.py::TestDecision` |
| 38.29.1/38.29.2 | Release Approval / Rejection | `engine.py` (`release_approved`) | `test_pov_release.py::TestDecision` |
| 38.1 | PoV Release Objectives | `engine.py` (`PovReleaseEngine`) | `test_pov_release.py::TestEngine` |
| — | Full Topic 38 contract | `registry.py` (+ traceability test) | `test_pov_release_registry.py` |

## Registry addition

Topic 38 (absent before) added as the authoritative 42-item block.
Captures `Nested Children`: 38.2.1 Functional Minimums, 38.2.2
Functional Blocking Conditions; 38.7.1 Mandatory Safety Conditions,
38.7.2 Safety Failure Conditions; 38.9.1 Minimum Paper-Trading
Requirements, 38.9.2 Paper-Trading Failure Conditions; 38.25.1
Blocking Condition, 38.25.2 Release Stop Action; 38.26.1 Readiness
Checklist, 38.26.2 Readiness Score; 38.29.1 Release Approval,
38.29.2 Release Rejection. Note: 38.11 is **P&L Tracking Criteria**
(not Backtesting — heading corrected from the auto-scan).

## Validation

- `python -m pytest -m unit` → **755 passed** (19 from Topic 38)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (130 files)

## Notes / decisions

- Functional, safety and paper-trading criteria fail on any blocking/
  failure condition (38.2.2/38.7.2/38.9.2) — no override path.
- The readiness gate requires the checklist AND a readiness score of
  at least 0.8 (38.26).
- The final release decision is an AND over validation, score and
  zero blockers (38.29).