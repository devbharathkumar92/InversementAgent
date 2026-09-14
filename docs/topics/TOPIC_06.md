# Topic 6 — High-Level System Architecture

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-06-architecture`

## Decision

**Implementation required (subset).** Topic 6 is largely advisory
architecture documentation, but it carries concrete, enforceable
contracts:

- **6.4 / 6.12**: strict separation of analysis/decision authority from
  live execution authority; execution layers do not participate in
  simulation mode.
- **6.22 / 6.22.1 / 6.22.2**: a defined, guarded system state machine
  (System States / State Transitions).
- **6.12**: execution-mode gating — simulation / paper-trading first;
  live only after governance authorization.
- **6.23 / 6.24**: failure isolation (blocked state) and recovery.

The many descriptive items (6.1–6.3, 6.6–6.11, 6.13–6.21, 6.25–6.30)
are architecture guidance captured in the registry for traceability; no
runtime logic was invented for them.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 6.1 / 6.4 | Architecture Objectives / Core Components | `system.py` (`SystemArchitecture`, `ArchitectureLayer`) | `test_architecture.py::TestArchitectureLayers` |
| 6.5 | Agent Layer Architecture | `system.py` (`is_execution_layer`) | `test_architecture.py::TestExecutionSeparation` |
| 6.12 | Execution Layer | `system.py` (`ExecutionMode`, `authorize_live`) | `test_architecture.py::TestExecutionSeparation`, `TestPoVGating` |
| 6.19 | Data Flow Architecture | `system.py` (layer `component_id`) | `test_architecture.py::TestArchitectureLayers` |
| 6.22 / 6.22.1 / 6.22.2 | State Management / System States / Transitions | `system.py` (`SystemState`, `transition_state`) | `test_architecture.py::TestStateMachine` |
| 6.23 / 6.23.1 | Failure Isolation | `system.py` (`enter_blocked`) | `test_architecture.py::TestFailureArchitecture` |
| 6.24 | Recovery Architecture | `system.py` (`recover`) | `test_architecture.py::TestFailureArchitecture` |
| — | Full Topic 6 contract | `registry.py` (+ traceability test) | `test_architecture_registry.py` |

## Registry addition

Topic 6 was **absent** from the requirement registry. Added the complete
authoritative block (44 items) from the SRS topic file so the Topic 6
traceability test passes and future topics can reference `REQ_REGISTRY["6"]`.

## Validation

- `python -m pytest -m unit` → **171 passed** (20 from Topic 6)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (66 files)

## Notes / decisions

- Live execution (6.12) requires both an explicit mode switch and a
  recorded governance authorization; by default the system runs in
  `SIMULATION`, and `PAPER` is the maximum allowed pre-approval mode.
- The state machine (6.22) is guarded: only declared transitions are
  allowed; `TERMINAL` is absorbing.
- Execution-layer participation is denied in simulation/paper mode
  (separation of authority, 6.12).