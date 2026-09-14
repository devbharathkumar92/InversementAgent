"""Topic 29 — Sub-Agent Architecture.

Models the master/sub-agent topology, one-hop handoffs, and
failure isolation with replay recovery (REQ 29.1-29.30 subset).
"""

from .engine import (
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

__all__ = [
    "SubAgentEngine",
    "agent_inputs_ok",
    "agent_outputs_ok",
    "boundaries_respected",
    "communication_reliable",
    "dependencies_resolved",
    "handoff_valid",
    "interface_contract_met",
    "master_authority",
    "recovery_supported",
    "responsibility_scope",
    "state_transition_allowed",
]
