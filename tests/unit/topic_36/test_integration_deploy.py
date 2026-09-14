"""Tests for Topic 36 — Integration and Deployment.

Covers branch integration and merge validation (36.13/36.14),
deployment environments and promotion (36.16), deployment process
gates (36.21), rollback (36.24), disaster recovery (36.25) and
release management (36.26).
"""

import pytest

from src.common.integdeploy.engine import (
    IntegDeployEngine,
    branch_merge_allowed,
    deployment_accepted,
    deployment_validated,
    environment_defined,
    gate_passed,
    integration_complete,
    promotion_ok,
    recovery_ok,
    release_managed,
    rollback_possible,
)


class TestIntegration:
    """REQ 36.3/36.4/36.5/36.13.1/36.13.2/36.14.1."""

    def test_integration_complete(self):
        assert integration_complete(components=True, data=True, api=True) is True

    def test_integration_missing_api(self):
        assert integration_complete(components=True, data=True, api=False) is False

    def test_branch_merge_allowed(self):
        assert branch_merge_allowed(rules=True, preconditions=True) is True

    def test_merge_precondition_missing(self):
        assert branch_merge_allowed(rules=True, preconditions=False) is False


class TestDeployment:
    """REQ 36.16.1/36.16.2/36.21.1/36.21.2/36.22."""

    def test_environment_defined(self):
        assert environment_defined(name="staging", defined=True) is True

    def test_environment_undefined(self):
        assert environment_defined(name="prod", defined=False) is False

    def test_promotion_ok(self):
        assert promotion_ok(validated=True, gates=True) is True

    def test_gate_passed(self):
        assert gate_passed(check=True) is True

    def test_deployment_validated(self):
        assert deployment_validated(checks=True, monitored=True) is True

    def test_deployment_invalid(self):
        assert deployment_validated(checks=False, monitored=True) is False

    def test_deployment_accepted(self):
        assert deployment_accepted(criteria=True, satisfied=True) is True


class TestRecovery:
    """REQ 36.24.1/36.24.2/36.25.1/36.25.2/36.26."""

    def test_rollback_possible(self):
        assert rollback_possible(trigger=True, procedure=True) is True

    def test_rollback_procedure_missing(self):
        assert rollback_possible(trigger=True, procedure=False) is False

    def test_recovery_ok(self):
        assert recovery_ok(objective=True, procedure=True) is True

    def test_recovery_objective_missing(self):
        assert recovery_ok(objective=False, procedure=True) is False

    def test_release_managed(self):
        assert release_managed(plan=True, audit=True) is True


class TestEngine:
    """REQ 36.1 — integration/deployment lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            IntegDeployEngine(name=" ")

    def test_engine_status(self):
        assert IntegDeployEngine(name="i").status() == "planned"


pytestmark = pytest.mark.unit
