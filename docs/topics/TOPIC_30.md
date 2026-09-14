# Topic 30 — Sub-Agent Task Specification

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-30-task-spec`

## Decision

**Implementation required (core).** Topic 30 makes every delegated
task fully specified and verifiable:

- **30.2 / 30.3 / 30.3.1 / 30.3.2 / 30.4**: task ID, purpose, objective,
  expected outcome and scope.
- **30.5 / 30.5.1 / 30.5.2 / 30.6 / 30.6.1 / 30.6.2 / 30.7 / 30.8**:
  schema-validated inputs/outputs, prerequisites and dependencies.
- **30.9 / 30.10 / 30.11**: required technology, tools and data sources.
- **30.12 / 30.12.1 / 30.12.2 / 30.13 / 30.14 / 30.15 / 30.16 / 30.17**:
  implementation steps/restrictions, processing and decision rules,
  constraints, prohibited actions and expected behaviour.
- **30.18 / 30.18.1 / 30.18.2 / 30.19 / 30.19.1 / 30.19.2 / 30.20**:
  error handling (recoverable vs non-recoverable), blocked-state
  handling and escalation conditions.
- **30.21 / 30.21.1 / 30.21.2 / 30.22 / 30.23 / 30.24 / 30.25**:
  acceptance criteria, test/evidence/documentation/integration
  requirements.
- **30.26 / 30.26.1 / 30.26.2 / 30.27 / 30.28 / 30.29 / 30.30**:
  handoff requirements, completion status, progress reporting,
  validation and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 30.3.1/30.3.2 | Task Objective / Expected Outcome | `engine.py` (`objective_defined`) | `test_task_spec.py::TestTaskDefinition` |
| 30.4/30.15 | Task Scope / Constraints | `engine.py` (`constraints_ok`) | `test_task_spec.py::TestTaskDefinition` |
| 30.7 | Task Prerequisites | `engine.py` (`prerequisites_met`) | `test_task_spec.py::TestTaskDefinition` |
| 30.5.2 | Input Validation | `engine.py` (`input_valid`) | `test_task_spec.py::TestIOValidation` |
| 30.6.2 | Output Validation | `engine.py` (`output_valid`) | `test_task_spec.py::TestIOValidation` |
| 30.12.1/30.12.2 | Implementation Spec/Restrictions | `engine.py` (`implementation_specified`) | `test_task_spec.py::TestExecutionConstraints` |
| 30.16 | Prohibited Actions | `engine.py` (`no_prohibited_actions`) | `test_task_spec.py::TestExecutionConstraints` |
| 30.18.1/30.18.2 | Recoverable/Non-Recoverable Error | `engine.py` (`error_recoverable`) | `test_task_spec.py::TestExecutionConstraints` |
| 30.19 | Blocked-State Handling | `engine.py` (`blocked_action_defined`) | `test_task_spec.py::TestExecutionConstraints` |
| 30.21.1/30.21.2 | Functional/Technical Acceptance | `engine.py` (`acceptance_met`) | `test_task_spec.py::TestAcceptance` |
| 30.22 | Test Requirements | `engine.py` (`requirements_met`) | `test_task_spec.py::TestAcceptance` |
| 30.26.1 | Handoff Package | `engine.py` (`handoff_package_ok`) | `test_task_spec.py::TestAcceptance` |
| 30.1 | Task Specification Objectives | `engine.py` (`TaskSpecEngine`) | `test_task_spec.py::TestEngine` |
| — | Full Topic 30 contract | `registry.py` (+ traceability test) | `test_task_spec_registry.py` |

## Registry addition

Topic 30 (absent before) added as the authoritative 46-item block.
Captures `Nested Children`: 30.3.1 Task Objective, 30.3.2 Expected
Outcome; 30.5.1 Input Schema, 30.5.2 Input Validation; 30.6.1 Output
Schema, 30.6.2 Output Validation; 30.12.1 Required Implementation
Steps, 30.12.2 Implementation Restrictions; 30.18.1 Recoverable Error,
30.18.2 Non-Recoverable Error; 30.19.1 Blocked Conditions, 30.19.2
Blocked-State Action; 30.21.1 Functional Acceptance, 30.21.2
Technical Acceptance; 30.26.1 Handoff Package, 30.26.2 Handoff
Validation.

## Validation

- `python -m pytest -m unit` → **605 passed** (26 from Topic 30)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (114 files)

## Notes / decisions

- A task must have both an objective and an expected outcome before it
  is delegable (30.3.1/30.3.2).
- Inputs and outputs are validated against schemas; mismatches block
  execution (30.5.2/30.6.2).
- Acceptance requires both functional and technical criteria; a
  handoff package is complete only with outputs plus evidence
  (30.21/30.26.1).