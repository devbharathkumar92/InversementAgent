# Topic 28 — Requirement Traceability

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-28-traceability`

## Decision

**Implementation required (core).** Topic 28 ties every requirement to
everything that realises or verifies it:

- **28.2 / 28.3 / 28.3.1 / 28.3.2 / 28.4 / 28.5**: requirement
  identification, ID format/uniqueness, classification and source.
- **28.6 / 28.7 / 28.8 / 28.9**: requirement-to-goal, -SRS, -task and
  -agent mapping.
- **28.10 / 28.10.1 / 28.10.2 / 28.11 / 28.11.1 / 28.11.2**: mapping to
  code (with coverage status) and tests (with result mapping).
- **28.12 / 28.13 / 28.14 / 28.15 / 28.16 / 28.17**: output, dependency,
  change, decision, evidence and version traceability.
- **28.18 / 28.18.1 / 28.18.2 / 28.19 / 28.19.1 / 28.20 / 28.20.1**:
  coverage calculation/threshold and missing/broken trace detection.
- **28.21 / 28.22 / 28.23 / 28.24 / 28.25**: validation, reporting,
  audit, testing and acceptance criteria.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 28.3.1 | ID Format | `engine.py` (`id_format_valid`) | `test_traceability.py::TestRequirementIDs` |
| 28.3.2 | ID Uniqueness | `engine.py` (`id_unique`) | `test_traceability.py::TestRequirementIDs` |
| 28.6/28.7 | Requirement-to-Goal/SRS Mapping | `engine.py` (`goals_mapped`) | `test_traceability.py::TestMapping` |
| 28.10.2 | Code Coverage Status | `engine.py` (`code_coverage_sufficient`) | `test_traceability.py::TestMapping` |
| 28.11.2 | Test Result Mapping | `engine.py` (`result_mapped`) | `test_traceability.py::TestMapping` |
| 28.19.1 | Missing Trace Detection | `engine.py` (`missing_trace_detected`) | `test_traceability.py::TestTraceChecks` |
| 28.20.1 | Broken Trace Detection | `engine.py` (`broken_trace_detected`) | `test_traceability.py::TestTraceChecks` |
| 28.21 | Traceability Validation | `engine.py` (`trace_validated`) | `test_traceability.py::TestTraceChecks` |
| 28.18.2 | Coverage Threshold | `engine.py` (`coverage_met`) | `test_traceability.py::TestTraceChecks` |
| 28.4 | Requirement Classification | `engine.py` (`requirement_classified`) | `test_traceability.py::TestTraceChecks` |
| 28.1 | Traceability Objectives | `engine.py` (`TraceabilityEngine`) | `test_traceability.py::TestEngine` |
| — | Full Topic 28 contract | `registry.py` (+ traceability test) | `test_traceability_registry.py` |

## Registry addition

Topic 28 (absent before) added as the authoritative 35-item block.
Captures `Nested Children`: 28.3.1 ID Format, 28.3.2 ID Uniqueness;
28.10.1 Requirement-to-Code Mapping, 28.10.2 Code Coverage Status;
28.11.1 Requirement-to-Test Mapping, 28.11.2 Test Result Mapping;
28.18.1 Coverage Calculation, 28.18.2 Coverage Threshold; 28.19.1
Missing Trace Detection; 28.20.1 Broken Trace Detection.

## Validation

- `python -m pytest -m unit` → **558 passed** (19 from Topic 28)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (110 files)

## Notes / decisions

- Requirement IDs must match `REQ-N.N(.N...)` and be conflict-free
  (28.3.1/28.3.2).
- A requirement is only trace-complete when mapped to goals + SRS, and
  only validated when there are zero missing and zero broken traces
  (28.6/28.21).
- Coverage must meet the configured threshold; anything below is
  reported as a gap for the audit trail (28.18.2).