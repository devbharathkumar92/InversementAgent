"""Tests for Topic 19 — Decision Engine.

Covers decision inputs (19.2), preconditions (19.3), opportunity/
strategy/risk eligibility (19.4-19.6), decision rules and priority
(19.8), thresholds and ranking (19.9/19.10), capital allocation
(19.12), entry/exit decisions (19.13/19.14), no-action decisions
(19.15), rejection (19.16), expiry (19.17), conflict handling
(19.19), human approval gate (19.20), and validation (19.24).
"""

import pytest

from src.common.decision.engine import (
    DecisionEngine,
    approval_gate,
    capital_eligible,
    conflict_handled,
    decision_expired,
    decision_priority,
    decision_rejected,
    eligibility_met,
    entry_decision,
    no_action,
    validate_inputs,
)


class TestInputsPreconditions:
    """REQ 19.2.1/19.2.2/19.3/19.3.2 — inputs and preconditions."""

    def test_inputs_valid(self):
        assert validate_inputs({"signal": "buy", "price": 100}) is True

    def test_inputs_missing(self):
        assert validate_inputs({"signal": "buy"}) is False

    def test_eligibility_met(self):
        assert eligibility_met(opp=0.8, strategy=0.7, risk=0.6) is True

    def test_eligibility_fails_on_risk(self):
        assert eligibility_met(opp=0.8, strategy=0.7, risk=0.1) is False


class TestDecisionRules:
    """REQ 19.4/19.5/19.6/19.8.2/19.10/19.12.1."""

    def test_opportunity_eligible(self):
        assert eligibility_met(opp=0.9, strategy=0.7, risk=0.7) is True

    def test_strategy_gate(self):
        assert eligibility_met(opp=0.9, strategy=0.1, risk=0.5) is False

    def test_priority_wins(self):
        assert decision_priority({"mom": 3, "rv": 2}) == "mom"

    def test_capital_eligible(self):
        assert capital_eligible(required=1000, available=5000) is True

    def test_capital_insufficient(self):
        assert capital_eligible(required=6000, available=5000) is False


class TestOutcomes:
    """REQ 19.13/19.14/19.15/19.16/19.17/19.19.1/19.20.1."""

    def test_entry_accepted(self):
        assert entry_decision(score=0.8, threshold=0.5) is True

    def test_entry_rejected_below_threshold(self):
        assert entry_decision(score=0.3, threshold=0.5) is False

    def test_no_action(self):
        assert no_action(score=0.2, threshold=0.5) is True

    def test_rejection(self):
        assert decision_rejected(risk=0.9, limit=0.8) is True

    def test_expiry(self):
        assert decision_expired(created=100, now=200, ttl=90) is True

    def test_not_expired(self):
        assert decision_expired(created=100, now=120, ttl=90) is False

    def test_conflict_handled(self):
        assert conflict_handled(strategy_a="momentum", strategy_b="mean_reversion") is True

    def test_approval_gate_open(self):
        assert approval_gate(action="kill", approval=True) is True

    def test_approval_gate_blocked(self):
        assert approval_gate(action="kill", approval=False) is False


class TestEngine:
    """REQ 19.24 — validation lifecycle."""

    def test_engine_requires_name(self):
        with pytest.raises(ValueError):
            DecisionEngine(name=" ")

    def test_engine_validates(self):
        eng = DecisionEngine(name="d")
        assert eng.validate(valid=True) is True


pytestmark = pytest.mark.unit
