# Topic 9 — System Execution Lifecycle

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-09-lifecycle`

## Decision

**Implementation required (core).** Topic 9 is the execution lifecycle
for the whole system. The implemented subset carries real runtime
control:

- **9.2 / 9.2.1**: system initialization and startup sequence with
  tracked lifecycle stages (`INIT → STARTUP → RUNNING → …`).
- **9.3**: environment validation gates startup.
- **9.4 / 9.5 / 9.6**: SRS, goal, and configuration verification flags.
- **9.7**: dependency verification before execution.
- **9.11 / 9.12**: task assignment and priority ordering.
- **9.13**: prerequisite validation.
- **9.14 / 9.15**: sequential vs parallel execution rules.
- **9.22 / 9.22.1**: blocked-state management and detection.
- **9.27**: completion verification.

Deployment-readiness checks (9.28), runtime monitoring (9.29), audit
trail (9.31), re-evaluation (9.33), and change control (9.34) are
modelled but deferred to the governance/human-in-the-loop pass.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 9.2/9.2.1/9.3 | System Initialization + Env Validation | `engine.py` (`LifecycleEngine`, `validate_environment`) | `test_lifecycle.py::TestInitialization` |
| 9.4/9.6 | SRS Loading and Verification | `engine.py` (`load_srs`, `srs_verified`) | `test_lifecycle.py::TestSRSAndConfig` |
| 9.7 | Dependency Verification | `engine.py` (`check_dependencies`) | `test_lifecycle.py::TestDependencyVerification` |
| 9.11/9.12 | Task Assignment and Prioritization | `engine.py` (`assign_task`, `next_task_id`) | `test_lifecycle.py::TestTaskAssignment` |
| 9.13 | Prerequisite Validation | `engine.py` (`validate_prerequisites`) | `test_lifecycle.py::TestPrerequisites` |
| 9.14/9.15 | Sequential / Parallel Execution | `engine.py` (`execute_sequence`, `can_parallelize`) | `test_lifecycle.py::TestParallelAndSequential` |
| 9.22/9.22.1 | Blocked-State Management | `engine.py` (`enter_blocked`, `complete_task`) | `test_lifecycle.py::TestBlockedAndCompletion` |
| 9.17/9.17.2 | Progress Calculation | `engine.py` (`compute_progress`) | `test_lifecycle.py::TestProgress` |
| 9.14.2/9.27 | Task Completion / Completion Verification | `engine.py` (`complete_task`, `completion_verified`) | `test_lifecycle.py::TestBlockedAndCompletion` |
| — | Full Topic 9 contract | `registry.py` (+ traceability test) | `test_lifecycle_registry.py` |

## Registry addition

Topic 9 (absent before) added as the authoritative 46-item block,
exactly matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **223 passed** (20 from Topic 9)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (72 files)

## Notes / decisions

- Task live `execution` assignment is refused: agents can only take
  tasks in simulation (aligned with Topic 6 live-execution gating).
- `compute_progress` treats an empty task set as 100% complete — an
  all-done signal with nothing left to do.
- Parallelization currently allows running tasks together by default;
  data-dependency restrictions (9.15.2) will be enforced once the
  Data Acquisition layer (Topic 10) defines shared dependencies.