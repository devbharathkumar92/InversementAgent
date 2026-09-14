"""Tests for Topic 29 — Sub-Agent Architecture.

Covers agent roles (29.2-29.14), responsibilities and boundaries
(29.15/29.16), interfaces (29.19), communication (29.20), state
management (29.21), dependencies/priorities (29.22/29.23) and
isolation/recovery (29.24/29.25).
"""

import pytest

from src.common.subagents.engine import (
    SubAgentEngine,
    agent_inputs_ok,
    agent_outputs_ok,
    boundaries_respected,
    communication_reliable,
    dependencies_resolved,
    handoff_valid,
    interface_contract_met,
    master_authority,
    recovery_supported,
    responsibility_scope,
    state_transition_allowed,
)


class TestAgentRoles:
    """REQ 29.2/29.2.1/29.15.1."""

    def test_master_authority(self):
        assert master_authority(autonomous=True) is True

    def test_authority_restricted(self):
        assert master_authority(autonomous=False) is False

    def test_responsibility_scope(self):
        assert responsibility_scope(assigned=True) is True

    def test_scope_unassigned(self):
        assert responsibility_scope(assigned=False) is False


class TestInterfaces:
    """REQ 29.16/29.17/29.18/29.19.1/29.19.2."""

    def test_boundaries_respected(self):
        assert boundaries_respected(within=True, peer=True) is True

    def test_boundary_violation(self):
        assert boundaries_respected(within=True, peer=False) is False

    def test_agent_inputs_ok(self):
        assert agent_inputs_ok(complete=True, typed=True) is True

    def test_agent_outputs_ok(self):
        assert agent_outputs_ok(schema=True, traceable=True) is True

    def test_interface_contract_met(self):
        assert interface_contract_met(contract=True) is True

    def test_handoff_valid(self):
        assert handoff_valid(sender=True, receiver=True, message=True) is True

    def test_handoff_dropped(self):
        assert handoff_valid(sender=True, receiver=False, message=True) is False


class TestCoordination:
    """REQ 29.20/29.20.2/29.21/29.21.2/29.22/29.25."""

    def test_communication_reliable(self):
        assert communication_reliable(acks=True, retries=0) is True

    def test_communication_failure(self):
        assert communication_reliable(acks=False, retries=2) is False

    def test_state_transition_allowed(self):
        assert state_transition_allowed(current="idle", next_state="active") is True

    def test_state_jump_invalid(self):
        assert state_transition_allowed(current="active", next_state="idle") is False

    def test_dependencies_resolved(self):
        assert dependencies_resolved(acyclic=True) is True

    def test_dependency_cycle(self):
        assert dependencies_resolved(acyclic=False) is False

    def test_recovery_supported(self):
        assert recovery_supported(replay=True) is True


class TestEngine:
    """REQ 29.1 — sub-agent architecture lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            SubAgentEngine(name=" ")

    def test_engine_status(self):
        assert SubAgentEngine(name="a").status() == "ready"


pytestmark = pytest.mark.unit
