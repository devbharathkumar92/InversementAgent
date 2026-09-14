# Topic 2 — Core Goal and Mission

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-02-core-goal-mission`

## Decision

**Implementation required.** Topic 2 defines the goal/mission primitives
that all downstream topics align against. Several rules — goal
immutability, violation detection, conflict priority, alignment, deviation
detection — are deterministic, testable business logic and deserve
first-class code (they will be reused by enforcement agents at runtime).

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 2.1 | Goal Statement | `goal.py` (`CoreGoal`) | `test_goal_mission.py::TestGoalStatement` |
| 2.2 | Mission Statement | `goal.py` (`Mission`) | `test_goal_mission.py::TestMissionStatement` |
| 2.3 / 2.3.1 | Primary Objective | `goal.py` (`PrimaryObjective`) | `test_goal_mission.py::TestPrimaryObjective` |
| 2.5 | Goal Scope | `goal.py` (`ScopeBounds`, `is_within_scope`) | `test_goal_mission.py::TestGoalScope` |
| 2.7 / 2.7.1 / 2.7.2 | Non-Negotiable Conditions / Violations | `violations.py` (`GoalViolationDetector`) | `test_goal_integrity.py` |
| 2.8 / 2.8.1 / 2.8.2 | Immutability & Controlled Change | `immutability.py` | `test_goal_integrity.py` |
| 2.9 | Goal Evaluation Criteria | `evaluation.py` | `test_goal_alignment_conflict.py::TestGoalEvaluation` |
| 2.11 | Goal Alignment | `alignment.py` | `test_goal_alignment_conflict.py::TestGoalAlignment` |
| 2.12 / 2.12.1 / 2.12.2 | Conflict Detection / Priority | `conflicts.py` | `test_goal_alignment_conflict.py::TestConflictResolution` |
| 2.13 | Deviation Detection | `deviation.py` | `test_goal_alignment_conflict.py::TestDeviationDetection` |

## Validation

- `python -m pytest -m unit` → **92 passed** (26 from Topic 2)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (58 files)

## Notes / decisions

- REQ 2.12.2 priority model is an `IntEnum` (safety/non-negotiable highest).
- `GoalViolationDetector` is intentionally conservative: suspicious
  `scope_change`, `safety_bypass`, `evidence_bypass`, and unapproved
  `purpose_change` events produce a violation; `data_validated` events do
  not.
- Immutability is enforced by rejecting non-authorized actors
  (`ImmutableGoalError`); the only permitted path is the
  `ControlledGoalChange` workflow (impact assessment + governance approval).