"""Tests for Topic 30 — Sub-Agent Task Specification.

Covers task IDs/purpose/scope (30.2-30.4), input/output schemas and
validation (30.5/30.6), error and blocked-state handling
(30.18/30.19), acceptance criteria and test/evidence requirements
(30.21/30.22/30.23), handoff requirements (30.26) and completion
validation (30.29).
"""

import pytest

from src.common.taskspec.engine import (
    TaskSpecEngine,
    acceptance_met,
    blocked_action_defined,
    constraints_ok,
    error_recoverable,
    handoff_package_ok,
    implementation_specified,
    input_valid,
    no_prohibited_actions,
    objective_defined,
    output_valid,
    prerequisites_met,
    requirements_met,
)


class TestTaskDefinition:
    """REQ 30.2/30.3.1/30.3.2/30.4/30.7."""

    def test_objective_defined(self):
        assert objective_defined(goal=True, outcome=True) is True

    def test_objective_missing(self):
        assert objective_defined(goal=True, outcome=False) is False

    def test_scope_constrained(self):
        assert constraints_ok(in_scope=True, excluded=True) is True

    def test_scope_unbounded(self):
        assert constraints_ok(in_scope=True, excluded=False) is False

    def test_prerequisites_met(self):
        assert prerequisites_met(ready=True) is True

    def test_prerequisites_missing(self):
        assert prerequisites_met(ready=False) is False


class TestIOValidation:
    """REQ 30.5.1/30.5.2/30.6.1/30.6.2."""

    def test_input_valid(self):
        assert input_valid(schema=True, values=True) is True

    def test_input_schema_mismatch(self):
        assert input_valid(schema=False, values=True) is False

    def test_output_valid(self):
        assert output_valid(schema=True, values=True) is True

    def test_output_invalid(self):
        assert output_valid(schema=True, values=False) is False


class TestExecutionConstraints:
    """REQ 30.12.1/30.13/30.16/30.18/30.18.1/30.19.1/30.19.2."""

    def test_implementation_specified(self):
        assert implementation_specified(steps=True, restrictions=True) is True

    def test_implementation_vague(self):
        assert implementation_specified(steps=False, restrictions=True) is False

    def test_prohibited_actions_excluded(self):
        assert no_prohibited_actions(allowed=True, listed=True) is True

    def test_error_recoverable(self):
        assert error_recoverable(recoverable=True) is True

    def test_error_non_recoverable(self):
        assert error_recoverable(recoverable=False) is False

    def test_blocked_action_defined(self):
        assert blocked_action_defined(conditions=True, action=True) is True

    def test_blocked_no_action(self):
        assert blocked_action_defined(conditions=True, action=False) is False


class TestAcceptance:
    """REQ 30.21/30.21.1/30.21.2/30.22/30.26.1."""

    def test_acceptance_met(self):
        assert acceptance_met(functional=True, technical=True) is True

    def test_functional_failure(self):
        assert acceptance_met(functional=False, technical=True) is False

    def test_requirements_met(self):
        assert requirements_met(defined=True, executed=True) is True

    def test_test_coverage_gap(self):
        assert requirements_met(defined=True, executed=False) is False

    def test_handoff_package_ok(self):
        assert handoff_package_ok(outputs=True, evidence=True) is True

    def test_handoff_incomplete(self):
        assert handoff_package_ok(outputs=True, evidence=False) is False


class TestEngine:
    """REQ 30.1 — task specification lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            TaskSpecEngine(name=" ")

    def test_engine_status(self):
        assert TaskSpecEngine(name="t").status() == "specified"


pytestmark = pytest.mark.unit
