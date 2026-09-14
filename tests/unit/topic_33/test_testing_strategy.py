"""Tests for Topic 33 — Testing Strategy.

Covers the layered test pyramid (33.4 unit, 33.6 integration, 33.7
system, 33.8 E2E), domain-specific suites (33.9-33.12), quality
attributes (33.19-33.24), acceptance testing (33.26), automation
(33.27) and evidence/audit (33.29).
"""

import pytest

from src.common.testing.engine import (
    TestStrategyEngine,
    acceptance_passed,
    agent_compliance_tested,
    automated,
    decision_tested,
    evidence_recorded,
    failure_recovery_tested,
    integration_covered,
    regression_testing,
    reliability_tested,
    risk_tested,
    security_tested,
    system_covered,
    unit_case_defined,
)


class TestTestLevels:
    """REQ 33.4/33.4.1/33.6.1/33.6.2/33.7/33.8."""

    def test_unit_case_defined(self):
        assert unit_case_defined(case=True, expected=True) is True

    def test_unit_case_missing_expected(self):
        assert unit_case_defined(case=True, expected=False) is False

    def test_integration_covered(self):
        assert integration_covered(cases=True, interfaces=True) is True

    def test_integration_gap(self):
        assert integration_covered(cases=True, interfaces=False) is False

    def test_system_covered(self):
        assert system_covered(e2e=True, api=True) is True

    def test_system_e2e_missing(self):
        assert system_covered(e2e=False, api=True) is False


class TestDomainSuites:
    """REQ 33.10/33.11.1/33.11.2/33.13/33.14."""

    def test_risk_tested(self):
        assert risk_tested(scenarios=True) is True

    def test_agent_compliance(self):
        assert agent_compliance_tested(behaviour=True, compliance=True) is True

    def test_decision_tested(self):
        assert decision_tested(rules=True) is True


class TestQualityAttributes:
    """REQ 33.19/33.20/33.21/33.22/33.23."""

    def test_security_tested(self):
        assert security_tested(auth=True, injected=True) is True

    def test_regression_present(self):
        assert regression_testing(previous=True) is True

    def test_reliability_tested(self):
        assert reliability_tested(failover=True) is True

    def test_failure_recovery_tested(self):
        assert failure_recovery_tested(restart=True) is True


class TestAcceptanceAndAutomation:
    """REQ 33.26.1/33.26.2/33.27/33.29."""

    def test_acceptance_passed(self):
        assert acceptance_passed(criteria=True, passed=True) is True

    def test_acceptance_rejected(self):
        assert acceptance_passed(criteria=True, passed=False) is False

    def test_automated(self):
        assert automated(ci=True, repeatable=True) is True

    def test_evidence_recorded(self):
        assert evidence_recorded(stored=True, auditable=True) is True


class TestEngine:
    """REQ 33.1 — testing lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            TestStrategyEngine(name=" ")

    def test_engine_status(self):
        assert TestStrategyEngine(name="t").status() == "defined"


pytestmark = pytest.mark.unit
