# Topic 31 — Dependency and Execution Plan

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-31-exec-plan`

## Decision

**Implementation required (core).** Topic 31 orders work by
dependency, not by convention:

- **31.2 / 31.3 / 31.3.1 / 31.3.2 / 31.4 / 31.5**: task dependency
  model, hard/soft dependencies, mandatory dependencies and
  prerequisites.
- **31.6 / 31.7 / 31.8**: dependency identification, validation and
  graph.
- **31.9 / 31.10 / 31.11 / 31.11.1 / 31.11.2**: execution order,
  sequential rules and parallel eligibility conditions/restrictions.
- **31.12 / 31.12.1 / 31.12.2 / 31.13 / 31.14**: blocking/unblocking
  conditions, failure handling and recovery.
- **31.15 / 31.16 / 31.17 / 31.18 / 31.19 / 31.20**: cross-agent,
  data, environment, integration, testing and deployment
  dependencies.
- **31.21 / 31.22 / 31.23**: dependency monitoring, change detection
  and re-evaluation.
- **31.24 / 31.24.1 / 31.24.2 / 31.25**: critical path identification
  and monitoring, progress tracking.
- **31.26 / 31.27 / 31.28 / 31.29 / 31.30**: audit trail, testing,
  acceptance criteria, review and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 31.3.1 | Mandatory Dependency | `engine.py` (`hard_dependency_met`) | `test_exec_plan.py::TestDependencyModel` |
| 31.4 | Soft Dependencies | `engine.py` (`soft_preferred`) | `test_exec_plan.py::TestDependencyModel` |
| 31.5 | Prerequisite Definition | `engine.py` (`prerequisites_defined`) | `test_exec_plan.py::TestDependencyModel` |
| 31.9 | Execution Order | `engine.py` (`execution_order_ok`) | `test_exec_plan.py::TestExecutionOrder` |
| 31.11.1/31.11.2 | Parallelization Conditions/Restrictions | `engine.py` (`parallel_eligible`) | `test_exec_plan.py::TestExecutionOrder` |
| 31.12.2 | Unblocking Condition | `engine.py` (`blocking_resolved`) | `test_exec_plan.py::TestExecutionOrder` |
| 31.6/31.7 | Dependency Identification/Validation | `engine.py` (`dependency_valid`) | `test_exec_plan.py::TestExecutionOrder` |
| 31.14 | Dependency Recovery | `engine.py` (`recovery_planned`) | `test_exec_plan.py::TestFailureAndProgress` |
| 31.24.1/31.24.2 | Critical Path Identification/Monitoring | `engine.py` (`critical_path_identified`) | `test_exec_plan.py::TestFailureAndProgress` |
| 31.25 | Execution Progress Tracking | `engine.py` (`progress_tracked`) | `test_exec_plan.py::TestFailureAndProgress` |
| 31.1 | Dependency Planning Objectives | `engine.py` (`ExecutionPlanEngine`) | `test_exec_plan.py::TestEngine` |
| — | Full Topic 31 contract | `registry.py` (+ traceability test) | `test_exec_plan_registry.py` |

## Registry addition

Topic 31 (absent before) added as the authoritative 38-item block.
Captures `Nested Children`: 31.3.1 Mandatory Dependency, 31.3.2
Dependency Failure Effect; 31.11.1 Parallelization Conditions, 31.11.2
Parallelization Restrictions; 31.12.1 Blocking Condition, 31.12.2
Unblocking Condition; 31.24.1 Critical Path Identification, 31.24.2
Critical Path Monitoring.

## Validation

- `python -m pytest -m unit` → **621 passed** (16 from Topic 31)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (116 files)

## Notes / decisions

- Mandatory dependencies gate their dependents; a block only clears
  when its explicit unblocking condition is satisfied (31.3.1/31.12.2).
- Parallel execution requires both independence and sufficient
  resources (31.11.1/31.11.2).
- Dependencies must form an acyclic graph; cycles are rejected at
  validation time (31.7).