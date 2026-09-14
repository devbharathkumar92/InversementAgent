"""Tests for Topic 4 — System Scope and Boundaries.

Covers REQ 4.1, 4.2/4.2.1/4.2.2, 4.3/4.3.1, 4.7/4.7.1-4.7.3,
4.10/4.10.1/4.10.2, 4.15.2, 4.19, 4.20, 4.21/4.21.2, 4.25/4.25.2.
"""

import pytest

from src.common.scope.system_scope import (
    ExpansionApproval,
    ScopeEnforcer,
    ScopeException,
    SystemScope,
    is_in_scope,
)


def make_scope(**overrides):
    data = {
        "name": "InversementAgent System Scope",
        "included_capabilities": ["market_data_ingestion", "opportunity_analysis", "evaluation"],
        "out_of_scope": ["direct_trading", "real_money_orders", "financial_advice"],
        "geographic_scope": ["India"],
        "market_scope": ["NSE equities"],
        "currency_scope": ["INR"],
        "allowed_authority": ["simulation_trades", "read_public_data"],
        "prohibited_authority": ["place_live_orders", "transfer_funds"],
        "capability_limits": {"auto_execution": False, "max_live_orders_per_day": 0},
    }
    data.update(overrides)
    return data


class TestSystemScopeDefinition:
    """REQ 4.1/4.2/4.3 — scope is a controlled definition of included
    capabilities and explicit exclusions."""

    def test_scope_requires_name(self):
        with pytest.raises(ValueError):
            SystemScope(**make_scope(name=""))

    def test_in_scope_classification(self):
        scope = SystemScope(**make_scope())
        assert is_in_scope(scope, "market_data_ingestion") is True

    def test_out_of_scope_classification(self):
        scope = SystemScope(**make_scope())
        assert is_in_scope(scope, "direct_trading") is False

    def test_capability_not_declared_is_out_of_scope(self):
        scope = SystemScope(**make_scope())
        assert is_in_scope(scope, "arbitrage") is False


class TestScopeBoundaries:
    """REQ 4.7/4.7.1-4.7.3 — geographic, market, currency bounds."""

    def test_geographic_boundary_enforced(self):
        scope = SystemScope(**make_scope())
        assert scope.allows_market("India", "NSE equities", "INR") is True

    def test_outside_geography_rejected(self):
        scope = SystemScope(**make_scope())
        assert scope.allows_market("USA", "NSE equities", "INR") is False

    def test_wrong_market_rejected(self):
        scope = SystemScope(**make_scope())
        assert scope.allows_market("India", "NYSE", "INR") is False

    def test_wrong_currency_rejected(self):
        scope = SystemScope(**make_scope())
        assert scope.allows_market("India", "NSE equities", "USD") is False


class TestAgentAuthority:
    """REQ 4.10/4.10.1/4.10.2 — allowed vs prohibited agent authority."""

    def test_allowed_authority(self):
        scope = SystemScope(**make_scope())
        assert scope.authority_allowed("simulation_trades") is True

    def test_prohibited_authority(self):
        scope = SystemScope(**make_scope())
        assert scope.authority_allowed("place_live_orders") is False

    def test_undeclared_authority_rejected(self):
        scope = SystemScope(**make_scope())
        assert scope.authority_allowed("delete_records") is False

    def test_live_action_restriction(self):
        """REQ 4.15.2 — live-action restrictions."""
        scope = SystemScope(**make_scope())
        assert scope.authority_allowed("place_live_orders") is False


class TestCapabilityLimits:
    """REQ 4.2.2 — capability limits."""

    def test_capability_limit_zero_blocks_action(self):
        scope = SystemScope(**make_scope())
        with pytest.raises(ValueError):
            scope.check_capability_limit("max_live_orders_per_day", used=1)


class TestScopeEnforcement:
    """REQ 4.19/4.20 — violation detection and boundary enforcement."""

    def test_violation_detected_for_out_of_scope_action(self):
        scope = SystemScope(**make_scope())
        enforcer = ScopeEnforcer(scope)
        assert enforcer.detect_violations(["place_live_orders"]) == ["place_live_orders"]

    def test_no_violation_for_in_scope_action(self):
        scope = SystemScope(**make_scope())
        enforcer = ScopeEnforcer(scope)
        assert enforcer.detect_violations(["market_data_ingestion"]) == []

    def test_enforcer_blocks_prohibited_authority(self):
        scope = SystemScope(**make_scope())
        enforcer = ScopeEnforcer(scope)
        with pytest.raises(ValueError):
            enforcer.enforce_action("place_live_orders")


class TestScopeExpansion:
    """REQ 4.21/4.21.2 — expansion requires governance approval."""

    def test_expansion_rejected_without_approval(self):
        scope = SystemScope(**make_scope())
        assert scope.expansion_allowed("direct_trading") is False

    def test_expansion_allowed_with_approval(self):
        scope = SystemScope(**make_scope())
        approval = ExpansionApproval(scope_item="direct_trading", approved_by="governance")
        assert scope.approve_expansion(approval) is True
        assert scope.expansion_allowed("direct_trading") is True


class TestExceptionsAndEscalation:
    """REQ 4.25/4.25.1/4.25.2 — exceptions detected, escalate to humans."""

    def test_exception_detection(self):
        exception = ScopeException(scope_item="auto_execution", reason="manual review")
        assert exception.escalation_required() is True

    def test_exception_has_traceability(self):
        exception = ScopeException(scope_item="x", reason="y")
        assert exception.scope_item == "x"
        assert exception.reason == "y"


pytestmark = pytest.mark.unit
