# Topic 35 — Definition of Done

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-35-dod`

## Decision

**Implementation required (core).** Topic 35 defines the release gate
that every requirement and the product as a whole must clear:

- **35.2 / 35.2.1 / 35.2.2**: requirement completion via status + evidence.
- **35.3 / 35.4**: functional and technical completion.
- **35.5 / 35.5.1 / 35.5.2 / 35.6 / 35.6.1 / 35.6.2**: code completion
  (with review) and test completion (execution + pass criteria).
- **35.7 / 35.8 / 35.9 / 35.10 / 35.11**: documentation, security,
  performance and reliability completion; risk validation.
- **35.12 / 35.13 / 35.14 / 35.15 / 35.16 / 35.17 / 35.18**:
  integration, dashboard, monitoring, audit-trail, error-recovery
  and agent-validation completion; SRS traceability.
- **35.19 / 35.20 / 35.21 / 35.22 / 35.23**: acceptance criteria,
  evidence, code-review, automated-test and integration-test
  completion.
- **35.24 / 35.24.1 / 35.24.2**: deployment readiness (checklist,
  blocking conditions).
- **35.25 / 35.26 / 35.27 / 35.27.1 / 35.27.2**: human approval,
  release approval, final validation and final approval.
- **35.28 / 35.29 / 35.30**: completion status, audit and change
  control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 35.2.1/35.2.2 | Requirement Status / Evidence | `engine.py` (`requirement_complete`) | `test_dod.py::TestCompletion` |
| 35.5.1/35.5.2 | Code Completeness / Review | `engine.py` (`code_complete`) | `test_dod.py::TestCompletion` |
| 35.6.1/35.6.2 | Test Execution / Pass Criteria | `engine.py` (`suite_green`) | `test_dod.py::TestCompletion` |
| 35.18 | SRS Traceability Completion | `engine.py` (`traceability_complete`) | `test_dod.py::TestCompletion` |
| 35.24.1/35.24.2 | Deployment Checklist / Blocking | `engine.py` (`deployment_ready`) | `test_dod.py::TestApproval` |
| 35.25 | Human Approval | `engine.py` (`human_approved`) | `test_dod.py::TestApproval` |
| 35.26 | Release Approval | `engine.py` (`release_approved`) | `test_dod.py::TestApproval` |
| 35.27.1 | Final Validation | `engine.py` (`final_validation`) | `test_dod.py::TestApproval` |
| 35.27.2 | Final Approval | `engine.py` (`final_approved`) | `test_dod.py::TestApproval` |
| 35.1 | Definition of Done Objectives | `engine.py` (`DoDEngine`) | `test_dod.py::TestEngine` |
| — | Full Topic 35 contract | `registry.py` (+ traceability test) | `test_dod_registry.py` |

## Registry addition

Topic 35 (absent before) added as the authoritative 40-item block.
Captures `Nested Children`: 35.2.1 Requirement Status, 35.2.2
Requirement Evidence; 35.5.1 Code Completeness, 35.5.2 Code Review;
35.6.1 Test Execution, 35.6.2 Test Pass Criteria; 35.24.1 Deployment
Checklist, 35.24.2 Deployment Blocking Conditions; 35.27.1 Final
Validation, 35.27.2 Final Approval.

## Validation

- `python -m pytest -m unit` → **698 passed** (17 from Topic 35)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (124 files)

## Notes / decisions

- Requirement completion requires both an explicit status AND
  evidence (35.2); status alone is insufficient.
- Deployment is gated on checklist completion and zero blocking
  conditions (35.24).
- Release requires human, release and final approval after final
  validation (35.25/35.26/35.27) — no automated-only path.
- The helper was named `suite_green` (not `tests_*`) to avoid pytest
  collecting it as a test function.