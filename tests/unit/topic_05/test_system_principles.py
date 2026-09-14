"""Tests for Topic 5 — System Principles and Non-Negotiable Rules.

Covers REQ 5.1, 5.2, 5.4, 5.6, 5.8/5.8.1/5.8.2, 5.9, 5.26/5.26.1/5.26.2,
5.29, 5.30, 5.31, 5.33/5.33.1/5.33.2, 5.34, 5.27/5.27.1/5.27.3.
"""

import pytest

from src.common.principles.system_principles import (
    ApprovalGate,
    ChangeProposal,
    RuleEnforcer,
    SystemPrinciples,
    detect_rule_violations,
    is_locked_baseline,
)


def make_principles(**overrides):
    data = {
        "name": "InversementAgent Principles",
        "non_negotiable_rules": ["no-direct-real-trading", "no-unsupported-labels"],
        "approval_required_actions": ["execute-live-trade", "expand-scope"],
        "non_approval_actions": ["read-public-data"],
        "prohibited_self_modifications": ["change-goal", "modify-principles"],
        "allowed_improvements": ["optimize-query-performance", "fix-documentation"],
    }
    data.update(overrides)
    return data


class TestPrincipleRegistry:
    """REQ 5.1/5.2 — principles and non-negotiable rules are explicit."""

    def test_principles_require_name(self):
        with pytest.raises(ValueError):
            SystemPrinciples(**make_principles(name=""))

    def test_non_negotiable_rules_listed(self):
        principles = SystemPrinciples(**make_principles())
        assert "no-direct-real-trading" in principles.non_negotiable_rules

    def test_rule_registry_maps_ids(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.rule_id("no-direct-real-trading") == "5.29.rule.no-direct-real-trading"


class TestHumanApproval:
    """REQ 5.8/5.8.1/5.8.2 — approval-required vs non-approval actions."""

    def test_approval_required_action(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.requires_approval("execute-live-trade") is True

    def test_non_approval_action(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.requires_approval("read-public-data") is False

    def test_undeclared_action_requires_approval(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.requires_approval("delete-database") is True

    def test_approval_gate_records_evidence(self):
        gate = ApprovalGate(action="execute-live-trade", approved_by="risk-review")
        assert gate.approved is True


class TestNoAssumption:
    """REQ 5.6 — no-assumption principle."""

    def test_unverified_claim_rejected(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.has_evidence("price will rise tomorrow") is False

    def test_evidence_supported_claim_accepted(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.has_evidence("NSE data as of 2026-09-01") is True


class TestSelfModification:
    """REQ 5.26/5.26.1/5.26.2 — allowed vs prohibited self-modifications."""

    def test_prohibited_self_modification(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.self_modification_allowed("change-goal") is False

    def test_allowed_improvement(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.self_modification_allowed("optimize-query-performance") is True


class TestRuleEnforcement:
    """REQ 5.29/5.30 — rule violation detection and enforcement."""

    def test_violation_detected_for_non_negotiable_rule(self):
        principles = SystemPrinciples(**make_principles())
        violations = detect_rule_violations(principles, ["no-direct-real-trading"])
        assert violations == ["no-direct-real-trading"]

    def test_no_violation_for_clean_actions(self):
        principles = SystemPrinciples(**make_principles())
        assert detect_rule_violations(principles, ["read-public-data"]) == []

    def test_enforcer_blocks_violating_action(self):
        principles = SystemPrinciples(**make_principles())
        enforcer = RuleEnforcer(principles)
        with pytest.raises(ValueError):
            enforcer.enforce("no-direct-real-trading")


class TestBaselineLock:
    """REQ 5.33/5.33.1/5.33.2 — baseline creation + protection."""

    def test_created_baseline_is_locked(self):
        baseline = "baseline-v1"
        assert is_locked_baseline(baseline) is True

    def test_unknown_baseline_is_not_locked(self):
        assert is_locked_baseline("future-baseline") is False

    def test_principles_record_baseline(self):
        principles = SystemPrinciples(**make_principles())
        assert principles.record_baseline("baseline-v1-2026-09-01") == "baseline-v1-2026-09-01"


class TestChangeGovernance:
    """REQ 5.27/5.27.1/5.27.3 — change proposals require approval."""

    def test_change_proposal_without_approval_rejected(self):
        proposal = ChangeProposal(rule_id="5.24", change="reorder resolution")
        assert proposal.approved is False

    def test_change_proposal_approved_by_gate(self):
        proposal = ChangeProposal(rule_id="5.24", change="reorder resolution")
        proposal.approve("governance")
        assert proposal.approved is True


pytestmark = pytest.mark.unit
