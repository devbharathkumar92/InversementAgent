"""Tests for Topic 26 — Self-Improvement and Change Management.

Covers improvement scoping and opportunity detection (26.2/26.3),
root-cause analysis (26.5), proposals with expected benefit (26.6),
impact/risk/regression analysis (26.8/26.9/26.10), human approval
(26.14), version creation (26.19) and SRS/proposal integrity controls
(26.25-26.27).
"""

import pytest

from src.common.improvement.engine import (
    ImprovementEngine,
    approval_required,
    benefit_possible,
    change_expected_value_positive,
    change_validated,
    impact_assessed,
    proposal_action,
    risk_accepted,
    root_cause_evidence_sufficient,
    srs_baseline_protected,
    version_created,
)


class TestOpportunity:
    """REQ 26.2/26.3.2/26.5.1/26.6.2."""

    def test_benefit_possible(self):
        assert benefit_possible(improvement=True, scope=True) is True

    def test_no_opportunity_out_of_scope(self):
        assert benefit_possible(improvement=True, scope=False) is False

    def test_root_cause_evidence_sufficient(self):
        assert root_cause_evidence_sufficient(confidence=0.9) is True

    def test_root_cause_low_confidence(self):
        assert root_cause_evidence_sufficient(confidence=0.3) is False


class TestChangeAnalysis:
    """REQ 26.8/26.9/26.10/26.11/26.14.1."""

    def test_impact_assessed(self):
        assert impact_assessed(functional=True, risk=True) is True

    def test_missing_impact(self):
        assert impact_assessed(functional=False, risk=True) is False

    def test_risk_accepted(self):
        assert risk_accepted(acceptable=True, regression_free=True) is True

    def test_regression_blocks(self):
        assert risk_accepted(acceptable=True, regression_free=False) is False

    def test_change_validated(self):
        assert change_validated(approved=True, tested=True) is True

    def test_change_not_tested(self):
        assert change_validated(approved=True, tested=False) is False

    def test_approval_required(self):
        assert approval_required(srs_change=True) is True

    def test_proposal_action(self):
        assert proposal_action(approved=True, tested=True) == "deploy"


class TestIntegrity:
    """REQ 26.19/26.26.1/26.27.1."""

    def test_version_created(self):
        assert version_created(bumped=True, tagged=True) is True

    def test_srs_baseline_protected(self):
        assert srs_baseline_protected(protected=True) is True

    def test_baseline_violation(self):
        assert srs_baseline_protected(protected=False) is False


class TestEngine:
    """REQ 26.1 — improvement lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            ImprovementEngine(name=" ")

    def test_engine_status(self):
        assert ImprovementEngine(name="i").status() == "active"

    def test_expected_value_positive(self):
        assert change_expected_value_positive(benefit=1.2, cost=1.0) is True


pytestmark = pytest.mark.unit
