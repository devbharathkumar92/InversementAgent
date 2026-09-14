"""Tests for Topic 39 — Future Expansion Framework.

Covers expansion rules (39.3), market/geographic/asset-class
expansion (39.4/39.5/39.7), capital scaling (39.15), expansion
readiness (39.25), approval (39.26) and rollback (39.27).
"""

import pytest

from src.common.expansion.engine import (
    ExpansionEngine,
    asset_class_ok,
    capital_scaling_ok,
    expansion_allowed,
    expansion_approved,
    expansion_ready,
    geographic_ok,
    market_ok,
    rollback_available,
)


class TestExpansionValues:
    """REQ 39.3.1/39.3.2/39.4.1/39.4.2."""

    def test_expansion_allowed(self):
        assert expansion_allowed(trigger=True, preconditions=True) is True

    def test_expansion_no_trigger(self):
        assert expansion_allowed(trigger=False, preconditions=True) is False

    def test_market_ok(self):
        assert market_ok(evaluated=True, approved=True) is True

    def test_market_unapproved(self):
        assert market_ok(evaluated=True, approved=False) is False

    def test_geographic_ok(self):
        assert geographic_ok(ready=True, approved=True) is True

    def test_geographic_not_ready(self):
        assert geographic_ok(ready=False, approved=True) is False

    def test_asset_class_ok(self):
        assert asset_class_ok(evaluated=True, approved=True) is True


class TestScaling:
    """REQ 39.15.1/39.15.2."""

    def test_capital_scaling_ok(self):
        assert capital_scaling_ok(conditions=True, within_limits=True) is True

    def test_capital_over_limit(self):
        assert capital_scaling_ok(conditions=True, within_limits=False) is False


class TestReleaseGate:
    """REQ 39.25.1/39.25.2/39.26.1/39.26.2/39.27."""

    def test_expansion_ready(self):
        assert expansion_ready(checklist=True, blockers=0) is True

    def test_expansion_blocked(self):
        assert expansion_ready(checklist=True, blockers=1) is False

    def test_expansion_approved(self):
        assert expansion_approved(authority=True, decision=True) is True

    def test_expansion_declined(self):
        assert expansion_approved(authority=True, decision=False) is False

    def test_rollback_available(self):
        assert rollback_available(defined=True) is True


class TestEngine:
    """REQ 39.1 — expansion lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            ExpansionEngine(name=" ")

    def test_engine_status(self):
        assert ExpansionEngine(name="e").status() == "scoped"


pytestmark = pytest.mark.unit
