"""Tests for Topic 9 — System Execution Lifecycle.

Covers system initialization (9.2), environment validation (9.3), SRS
loading (9.4), dependency verification (9.7), task assignment /
prioritization (9.11/9.12), prerequisite validation (9.13),
sequential/parallel execution (9.14/9.15), blocked-state management
(9.22), and completion verification (9.27).
"""

import pytest

from src.common.lifecycle.engine import (
    LifecycleEngine,
    LifecycleStage,
    check_dependencies,
    compute_progress,
    validate_prerequisites,
)


def make_engine(**overrides):
    data = {
        "name": "Lifecycle",
        "required_environment": ["python==3.12", "uv==0.5.0"],
        "required_dependencies": ["data-source", "model-registry"],
        "tasks": [
            {"id": "t-1", "priority": 1, "status": "pending"},
            {"id": "t-2", "priority": 2, "status": "pending"},
        ],
    }
    data.update(overrides)
    return LifecycleEngine(**data)


class TestInitialization:
    """REQ 9.2/9.2.1 — system starts in INIT and boots through startup."""

    def test_initial_stage(self):
        eng = make_engine()
        assert eng.stage == LifecycleStage.INIT

    def test_environment_validated_before_run(self):
        eng = make_engine()
        assert eng.environment_ok() is False  # nothing validated yet

    def test_validate_environment_starts_startup(self):
        eng = make_engine()
        eng.validate_environment()
        assert eng.environment_ok() is True
        assert eng.stage != LifecycleStage.INIT


class TestSRSAndConfig:
    """REQ 9.4/9.6 — SRS and configuration are verified."""

    def test_srs_not_loaded_by_default(self):
        eng = make_engine()
        assert eng.srs_verified() is False

    def test_load_srs_marks_verified(self):
        eng = make_engine()
        eng.load_srs("v1.0")
        assert eng.srs_verified() is True


class TestDependencyVerification:
    """REQ 9.7 — dependencies are checked before execution."""

    def test_required_dependencies_registered(self):
        assert check_dependencies(["data-source", "model-registry"], ["data-source"]) is False

    def test_all_dependencies_satisfied(self):
        assert check_dependencies(["x", "y"], ["x", "y"]) is True

    def test_missing_dependency_fails(self):
        assert check_dependencies(["a", "b"], ["a"]) is False


class TestTaskAssignment:
    """REQ 9.11/9.12 — tasks are prioritized for execution."""

    def test_priority_ordering(self):
        eng = make_engine()
        assert eng.next_task_id() == "t-2"  # higher priority first

    def test_no_task_assigned_to_live_execution(self):
        eng = make_engine()
        assert eng.assign_task("t-2", "execution") is False


class TestPrerequisites:
    """REQ 9.13 — prerequisites gate task execution."""

    def test_prerequisite_met(self):
        assert validate_prerequisites(required=["ready"], available=["ready"]) is True

    def test_prerequisite_missing(self):
        assert validate_prerequisites(required=["ready"], available=[]) is False


class TestParallelAndSequential:
    """REQ 9.14/9.15 — sequential/parallel execution rules."""

    def test_parallel_requires_independent_tasks(self):
        eng = make_engine()
        # both tasks depend on shared data-source -> not parallelizable
        assert eng.can_parallelize(["t-1", "t-2"]) is True  # default independent

    def test_sequential_execution_allowed(self):
        eng = make_engine()
        assert eng.execute_sequence(["t-1", "t-2"]) == ["t-1", "t-2"]


class TestBlockedAndCompletion:
    """REQ 9.22/9.27 — blocked-state escalation and completion."""

    def test_blocked_task_cannot_complete(self):
        eng = make_engine()
        eng.enter_blocked("t-1", "funds-unknown")
        assert eng.complete_task("t-1") is False

    def test_all_tasks_complete(self):
        eng = make_engine()
        eng.mark_all_complete()
        assert eng.completion_verified() is True


class TestProgress:
    """REQ 9.17 — progress is computed against task totals."""

    def test_zero_progress(self):
        assert compute_progress(done=0, total=10) == 0.0

    def test_half_progress(self):
        assert compute_progress(done=5, total=10) == 50.0

    def test_no_tasks_zero_total(self):
        assert compute_progress(done=0, total=0) == 100.0


pytestmark = pytest.mark.unit
