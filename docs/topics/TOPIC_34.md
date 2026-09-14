# Topic 34 — SRS Self-Validation

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-34-self-validation`

## Decision

**Implementation required (core).** Topic 34 defines systematic
self-validation that every SRS revision must pass before approval:

- **34.2 / 34.3 / 34.3.1 / 34.3.2 / 34.4 / 34.4.1 / 34.4.2**:
  structural validation, completeness with threshold, and
  internal/cross-section consistency.
- **34.5 / 34.6 / 34.7 / 34.8 / 34.9 / 34.10**: goal alignment,
  scope, dependency, feasibility, technology and agent specification
  validation.
- **34.11 / 34.12 / 34.13 / 34.14 / 34.15 / 34.16 / 34.17**:
  input/output, interface, acceptance-criteria, test-coverage,
  parallelization and integration validation.
- **34.18 / 34.19**: security and risk requirement validation.
- **34.20 / 34.20.1 / 34.20.2 / 34.21 / 34.21.1 / 34.21.2**:
  ambiguity and contradiction detection/classification/resolution.
- **34.22 / 34.23 / 34.24 / 34.25 / 34.26**: missing, duplicate,
  undefined-dependency and blocked-requirement detection; traceability
  validation.
- **34.27 / 34.27.1 / 34.27.2**: SRS quality score with minimum
  threshold.
- **34.28 / 34.29 / 34.30**: self-validation report, approval
  criteria and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 34.3.1/34.3.2 | Completeness / Threshold | `engine.py` (`completeness_ok`) | `test_self_validation.py::TestValidationChecks` |
| 34.4.1/34.4.2 | Internal / Cross-Section Consistency | `engine.py` (`consistency_ok`) | `test_self_validation.py::TestValidationChecks` |
| 34.20.1 | Ambiguity Detection | `engine.py` (`ambiguity_free`) | `test_self_validation.py::TestValidationChecks` |
| 34.21.1 | Contradiction Detection | `engine.py` (`contradiction_free`) | `test_self_validation.py::TestValidationChecks` |
| 34.23 | Duplicate Detection | `engine.py` (`duplicates_absent`) | `test_self_validation.py::TestDetection` |
| 34.25 | Blocked Requirement Detection | `engine.py` (`blocked_detected`) | `test_self_validation.py::TestDetection` |
| 34.26 | Traceability Validation | `engine.py` (`traceability_validated`) | `test_self_validation.py::TestDetection` |
| 34.27.2 | Quality Score / Threshold | `engine.py` (`quality_score_pass`) | `test_self_validation.py::TestQualityAndApproval` |
| 34.28/34.29 | Report / Approval Criteria | `engine.py` (`approval_recommended`) | `test_self_validation.py::TestQualityAndApproval` |
| 34.1 | Self-Validation Objectives | `engine.py` (`SelfValidationEngine`) | `test_self_validation.py::TestEngine` |
| — | Full Topic 34 contract | `registry.py` (+ traceability test) | `test_self_validation_registry.py` |

## Registry addition

Topic 34 (absent before) added as the authoritative 40-item block.
Captures `Nested Children`: 34.3.1 Missing Requirement Detection,
34.3.2 Completeness Threshold; 34.4.1 Internal Consistency, 34.4.2
Cross-Section Consistency; 34.20.1 Ambiguity Detection, 34.20.2
Ambiguity Classification; 34.21.1 Contradiction Detection, 34.21.2
Contradiction Resolution; 34.27.1 Quality Score Components, 34.27.2
Minimum Quality Threshold.

## Validation

- `python -m pytest -m unit` → **681 passed** (20 from Topic 34)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (122 files)

## Notes / decisions

- Completeness is strict: missing-requirement detection must return
  zero (34.3.1) regardless of the configured threshold (34.3.2).
- Any ambiguity, contradiction or duplicate blocks self-validation;
  approval additionally requires a quality score ≥ 0.90 and a report
  (34.27.2/34.29).
- Traceability must hold in both directions (34.26), matching the
  Topic 28 forward/backward contract.