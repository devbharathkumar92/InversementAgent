# Topic 3 — Proof of Value Definition

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-03-pov-definition`

## Decision

**Implementation required.** Topic 3 defines the Proof-of-Value contract:
objectives, success thresholds, release-blocking conditions, acceptance,
failure classification, and completion criteria. These are deterministic
decision rules re-used by the PoV review/approval workflows, so they are
coded as a controlled `PoVDefinition` model.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 3.1 | PoV Definition | `definition.py` (`PoVDefinition`) | `test_pov_definition.py::TestPoVDefinition` |
| 3.3 / 3.3.1–3.3.3 | PoV Objectives | `definition.py` (functional/technical/outcome, `objective_traceability`) | `test_pov_definition.py::TestPoVDefinition` |
| 3.5.1 | Minimum Success Thresholds | `definition.py` (`meets_success_threshold`) | `test_pov_definition.py::TestMinimumSuccessThresholds` |
| 3.5.2 | Release Blocking Conditions | `definition.py` (`evaluate_release_gate`, `ReleaseGate`) | `test_pov_definition.py::TestReleaseBlockingConditions` |
| 3.17 / 3.17.1 / 3.17.2 | Acceptance Criteria | `definition.py` (`validate_completion`) | `test_pov_definition.py::TestAcceptanceCriteria` |
| 3.18 / 3.18.1 / 3.18.2 | Failure Criteria | `definition.py` (`failure_class`, `FailureClass`) | `test_pov_definition.py::TestFailureClassification` |
| 3.21 | Completion Criteria | `definition.py` (`completion_status`, `PoVStatus`) | `test_pov_definition.py::TestAcceptanceCriteria` |
| 1.0A (traceability) | Full contract per item | `registry.py` + `test_pov_registry.py` | `test_pov_registry.py` |

## Validation

- `python -m pytest -m unit` → **110 passed** (18 from Topic 3)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (60 files)

## Notes / decisions

- Failure classification (3.18) uses explicit critical keywords: safety,
  violation, bypass, evidence, critical → `CRITICAL`; everything else is
  `NON_CRITICAL`.
- Completion (3.21) requires **both** functional and safety acceptance;
  missing either gate fails the PoV.
- Release gate (3.5.2) only reacts to conditions that are explicitly
  declared as `release_blocking_conditions` in the controlled PoV
  definition — unknown conditions do not block (no silent assumptions).