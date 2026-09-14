# Topic 26 — Self-Improvement and Change Management

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-26-improvement`

## Decision

**Implementation required (core).** Topic 26 controls how the agent
changes its own behaviour/code without drifting from the SRS:

- **26.2 / 26.3 / 26.3.1 / 26.3.2**: improvement scope, opportunity
  detection, triggers and candidates.
- **26.4 / 26.5 / 26.5.1 / 26.5.2**: issue identification and
  evidence-backed root-cause analysis with confidence.
- **26.6 / 26.6.1 / 26.6.2 / 26.7 / 26.8 / 26.8.1 / 26.8.2**: proposal
  definition, expected benefit, evidence and impact analysis
  (functional + risk).
- **26.9 / 26.10 / 26.11 / 26.12**: risk and regression analysis,
  proposed code and configuration changes.
- **26.13 / 26.13.1 / 26.13.2 / 26.14 / 26.14.1 / 26.14.2**: proposed
  SRS changes with impact analysis and human approval.
- **26.15 / 26.16 / 26.17 / 26.18 / 26.18.1 / 26.18.2**: change/
  automated/integration validation and rollback (trigger + procedure).
- **26.19 / 26.20 / 26.21 / 26.22**: version creation, documentation,
  deployment and post-deployment validation.
- **26.23 / 26.24**: performance measurement and failure handling.
- **26.25 / 26.25.1 / 26.26 / 26.26.1 / 26.27 / 26.27.1**: unauthorized
  change prevention, immutable goal and SRS baseline protection.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 26.3.2 | Improvement Candidate | `engine.py` (`benefit_possible`) | `test_improvement.py::TestOpportunity` |
| 26.5.2 | Root-Cause Confidence | `engine.py` (`root_cause_evidence_sufficient`) | `test_improvement.py::TestOpportunity` |
| 26.8 | Impact Analysis | `engine.py` (`impact_assessed`) | `test_improvement.py::TestChangeAnalysis` |
| 26.9/26.10 | Risk / Regression Analysis | `engine.py` (`risk_accepted`) | `test_improvement.py::TestChangeAnalysis` |
| 26.15/26.16 | Change Validation | `engine.py` (`change_validated`) | `test_improvement.py::TestChangeAnalysis` |
| 26.14.1 | Approval Trigger | `engine.py` (`approval_required`) | `test_improvement.py::TestChangeAnalysis` |
| 26.14.2 | Approval Decision | `engine.py` (`proposal_action`) | `test_improvement.py::TestChangeAnalysis` |
| 26.19 | Version Creation | `engine.py` (`version_created`) | `test_improvement.py::TestIntegrity` |
| 26.27.1 | SRS Baseline Protection | `engine.py` (`srs_baseline_protected`) | `test_improvement.py::TestIntegrity` |
| 26.6.2 | Expected Benefit | `engine.py` (`change_expected_value_positive`) | `test_improvement.py::TestEngine` |
| 26.1 | Self-Improvement Objectives | `engine.py` (`ImprovementEngine`) | `test_improvement.py::TestEngine` |
| — | Full Topic 26 contract | `registry.py` (+ traceability test) | `test_improvement_registry.py` |

## Registry addition

Topic 26 (absent before) added as the authoritative 47-item block.
Captures `Nested Children`: 26.3.1 Improvement Trigger, 26.3.2
Improvement Candidate; 26.5.1 Root-Cause Evidence, 26.5.2 Root-Cause
Confidence; 26.6.1 Proposal Definition, 26.6.2 Expected Benefit;
26.8.1 Functional Impact, 26.8.2 Risk Impact; 26.13.1 SRS Change
Proposal, 26.13.2 SRS Impact Analysis; 26.14.1 Approval Trigger,
26.14.2 Approval Decision; 26.18.1 Rollback Trigger, 26.18.2 Rollback
Procedure; 26.25.1 Unauthorized Change Detection; 26.26.1 Immutable
Goal Protection; 26.27.1 SRS Baseline Protection.

## Validation

- `python -m pytest -m unit` → **519 passed** (19 from Topic 26)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (106 files)

## Notes / decisions

- Root-cause analysis requires confidence ≥ 0.8 before it can justify
  a change (26.5.2), preventing guess-driven rewrites.
- SRS-changing proposals always require human approval (26.14.1);
  the SRS baseline is never mutated out-of-band (26.27.1).
- A change deploys only when both approved and tested; the rollback
  mechanism remains available should post-deployment validation fail
  (26.14.2/26.18/26.22).