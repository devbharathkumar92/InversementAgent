# Topic 25 — Self-Evaluation

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-25-self-eval`

## Decision

**Implementation required (core).** Topic 25 lets the agent assess its
own output against goals and the SRS, and act when it is off-track:

- **25.2 / 25.2.1 / 25.2.2**: goal checklist and goal deviation test.
- **25.3 / 25.3.1 / 25.3.2**: SRS coverage and SRS violation detection.
- **25.4 / 25.5 / 25.6**: scope, requirement and technical compliance.
- **25.7-25.19**: data quality, agent behaviour, output quality,
  performance, accuracy, reliability, risk, security, dependency,
  integration, testing, documentation and progress evaluation.
- **25.20 / 25.20.1 / 25.20.2 / 25.21 / 25.21.1 / 25.21.2**: stuck-state
  and deviation detection with deviation severity.
- **25.22 / 25.23**: regression detection and evidence collection.
- **25.24 / 25.24.1 / 25.24.2 / 25.25**: evaluation scoring, score
  threshold and evaluation thresholds.
- **25.26 / 25.26.1 / 25.26.2**: failed-evaluation recovery and
  escalation.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 25.2.2 | Goal Deviation Test | `engine.py` (`goal_met`) | `test_self_eval.py::TestCompliance` |
| 25.3.2 | SRS Violation Detection | `engine.py` (`violation_detected`) | `test_self_eval.py::TestCompliance` |
| 25.4/25.5 | Scope / Requirement Compliance | `engine.py` (`methodology_compliant`) | `test_self_eval.py::TestCompliance` |
| 25.20.2 | Stuck-State Detection | `engine.py` (`stuck_detected`) | `test_self_eval.py::TestDetection` |
| 25.21.2 | Deviation Severity | `engine.py` (`deviation_severity`) | `test_self_eval.py::TestDetection` |
| 25.23 | Evidence Collection | `engine.py` (`evidence_captured`) | `test_self_eval.py::TestDetection` |
| 25.24.2 | Score Threshold | `engine.py` (`score_threshold_met`) | `test_self_eval.py::TestScoring` |
| 25.26.2 | Escalation Action | `engine.py` (`failed_evaluation_recovery`) | `test_self_eval.py::TestScoring` |
| 25.1 | Self-Evaluation Objectives | `engine.py` (`EvaluationEngine`) | `test_self_eval.py::TestEngine` |
| — | Full Topic 25 contract | `registry.py` (+ traceability test) | `test_self_eval_registry.py` |

## Registry addition

Topic 25 (absent before) added as the authoritative 43-item block.
Captures `Nested Children`: 25.2.1 Goal Checklist, 25.2.2 Goal
Deviation Test; 25.3.1 SRS Coverage, 25.3.2 SRS Violation Detection;
25.20.1 Stuck-State Definition, 25.20.2 Stuck-State Detection; 25.21.1
Deviation Detection, 25.21.2 Deviation Severity; 25.24.1 Evaluation
Score Calculation, 25.24.2 Score Threshold; 25.26.1 Recovery Action,
25.26.2 Escalation Action.

## Validation

- `python -m pytest -m unit` → **500 passed** (15 from Topic 25)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (104 files)

## Notes / decisions

- A run is `stuck` only after ≥3 turns with no progress, avoiding
  premature escalation on slow but healthy steps (25.20.2).
- SRS violations trigger when the deviation exceeds a configured
  tolerance; this feeds failed-evaluation handling (25.3.2/25.26).
- Deviation severity tiers (low/medium/high) map to continue →
  review → escalate for downstream consumers (25.21.2).
- Scoring is a threshold gate: a score below threshold routes the run
  to recovery/escalation, not silent continuation (25.24.2).