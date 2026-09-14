"""Tests for Topic 31 — Dependency and Execution Plan.

Covers the dependency model (31.3/31.4), dependency validation
(31.7), execution order (31.9/31.10), parallel eligibility
(31.11), blocking dependencies (31.12), failure handling/recovery
(31.13/31.14), critical path (31.24) and progress tracking (31.25).
"""

import pytest

from src.common.execplan.engine import (
    ExecutionPlanEngine,
    blocking_resolved,
    critical_path_identified,
    dependency_valid,
    execution_order_ok,
    hard_dependency_met,
    parallel_eligible,
    prerequisites_defined,
    progress_tracked,
    recovery_planned,
    soft_preferred,
)


class TestDependencyModel:
    """REQ 31.3/31.3.1/31.4/31.5."""

    def test_hard_dependency_met(self):
        assert hard_dependency_met(mandatory=True, satisfied=True) is True

    def test_hard_dependency_violated(self):
        assert hard_dependency_met(mandatory=True, satisfied=False) is False

    def test_soft_preferred(self):
        assert soft_preferred(before=False, after=True) is True

    def test_prerequisites_defined(self):
        assert prerequisites_defined(explicit=True) is True


class TestExecutionOrder:
    """REQ 31.9/31.10/31.11.1/31.11.2/31.12."""

    def test_execution_order_ok(self):
        assert execution_order_ok(ordered=True) is True

    def test_parallel_eligible(self):
        assert parallel_eligible(independent=True, resources=True) is True

    def test_parallel_not_eligible(self):
        assert parallel_eligible(independent=False, resources=True) is False

    def test_blocking_resolved(self):
        assert blocking_resolved(blocked=False) is True

    def test_dependency_valid(self):
        assert dependency_valid(identified=True, acyclic=True) is True

    def test_dependency_cycle_invalid(self):
        assert dependency_valid(identified=True, acyclic=False) is False


class TestFailureAndProgress:
    """REQ 31.13/31.14/31.24.1/31.25."""

    def test_recovery_planned(self):
        assert recovery_planned(route=True) is True

    def test_critical_path_identified(self):
        assert critical_path_identified(longest=True, monitored=True) is True

    def test_progress_tracked(self):
        assert progress_tracked(recorded=True, current=True) is True


class TestEngine:
    """REQ 31.1 — dependency planning lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            ExecutionPlanEngine(name=" ")

    def test_engine_status(self):
        assert ExecutionPlanEngine(name="p").status() == "planned"


pytestmark = pytest.mark.unit
