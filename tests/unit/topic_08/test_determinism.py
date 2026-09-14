"""Tests for Topic 8 — Agent Determinism and Specification Completeness.

Covers determinism objectives (8.1), forbidden assumptions (8.17),
ambiguity detection/resolution (8.18), rule priority (8.7.2),
undefined-state safe behaviour (8.20), escalation state (8.21), and
agent self-verification (8.26).
"""

import pytest

from src.common.determinism.engine import (
    AmbiguityDetector,
    DeterminismEngine,
    detect_ambiguity,
    determine_rule_priority,
    safe_behaviour_for,
)


def make_engine(**overrides):
    data = {
        "name": "DeterminismEngine",
        "forbidden_assumptions": [
            "assume_market_liquidity",
            "assume_tax_regime",
        ],
        "rules": [
            {"id": "r-001", "priority": 1, "text": "validate then decide"},
            {"id": "r-002", "priority": 2, "text": "no live without author"},
        ],
    }
    data.update(overrides)
    return DeterminismEngine(**data)


class TestDeterminismObjectives:
    """REQ 8.1 — the determinism objective is a locked service."""

    def test_objective_set(self):
        eng = make_engine()
        assert eng.name == "DeterminismEngine"

    def test_goals_registered(self):
        eng = make_engine()
        assert "assume_market_liquidity" in eng.forbidden_assumptions


class TestRulePriority:
    """REQ 8.7.2 — rules are applied in declared priority order."""

    def test_higher_number_applied_first(self):
        rules = [
            {"id": "a", "priority": 1},
            {"id": "b", "priority": 9},
        ]
        assert determine_rule_priority(rules) == "b"

    def test_tie_breaks_by_id(self):
        rules = [
            {"id": "x", "priority": 5},
            {"id": "a", "priority": 5},
        ]
        assert determine_rule_priority(rules) == "a"


class TestForbiddenAssumptions:
    """REQ 8.16/8.17 — agents must not rely on forbidden assumptions."""

    def test_assumption_is_forbidden(self):
        eng = make_engine()
        assert eng.assumption_forbidden("assume_market_liquidity") is True

    def test_supported_assumption_allowed(self):
        eng = make_engine()
        assert eng.assumption_forbidden("explicitly-verified-order-size") is False

    def test_blank_instruction_has_no_evidence(self):
        eng = make_engine()
        assert eng.has_supporting_evidence("") is False


class TestAmbiguityDetection:
    """REQ 8.18/8.18.1/8.18.2 — ambiguity detected and resolved."""

    def test_detects_ambiguous_point(self):
        assert detect_ambiguity("commit in around 5 minutes") is True

    def test_accepts_explicit_point(self):
        assert detect_ambiguity("commit at 2026-09-14T12:00:00Z") is False

    def test_detector_uncertain_trigger(self):
        det = AmbiguityDetector(triggers=["approximately", "around"])
        assert det.detect("approximately 10 lots") is True

    def test_resolves_by_reference_instruction(self):
        det = AmbiguityDetector(triggers=["quickly"])
        assert det.resolve("reduce quickly", reference="speed is fixed at 60s") == "use-reference"


class TestUndefinedStateSafeBehaviour:
    """REQ 8.20/8.20.1/8.20.2 — unknown state → safe default."""

    def test_unknown_state_maps_to_blocked(self):
        assert safe_behaviour_for("no-such-defined-state") == "blocked"

    def test_defined_state_uses_rule(self):
        assert safe_behaviour_for("RUNNING") == "continue-monitored"


class TestEscalationState:
    """REQ 8.21.2 — an escalation state is explicitly flagged."""

    def test_escalation_accepted(self):
        eng = DeterminismEngine(
            name="e",
            forbidden_assumptions=[],
            rules=[],
            escalation_states={"ESCALATE-GOVERNANCE"},
        )
        assert "ESCALATE-GOVERNANCE" in eng.escalation_states


class TestAgentSelfVerification:
    """REQ 8.26 — agents self-verify before continuing."""

    def test_engine_verifies_agent_is_self_checking(self):
        eng = make_engine()
        # by default no self-verification configured
        assert eng.self_verification_required() is False

    def test_self_verification_can_be_required(self):
        eng = make_engine(_self_verification_required=True)
        assert eng.self_verification_required() is True


pytestmark = pytest.mark.unit
