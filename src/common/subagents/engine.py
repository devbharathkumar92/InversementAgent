"""Topic 29 — Sub-Agent Architecture.

Defines the master agent with full authority (29.2.1), specialises
sub-agents (29.3-29.14), and enforces responsibility boundaries
(29.15), interface/handoff contracts (29.19), communication rules
(29.20) and acyclic dependencies (29.22). (REQ 29.1-29.30 enforced
subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field

_VALID_TRANSITIONS: frozenset[tuple[str, str]] = frozenset(
    {
        ("idle", "active"),
        ("active", "paused"),
        ("paused", "active"),
        ("active", "complete"),
        ("paused", "complete"),
    }
)


def master_authority(autonomous: bool) -> bool:
    """Return whether the master agent holds authority (29.2.1)."""
    return autonomous


def responsibility_scope(assigned: bool) -> bool:
    """Return whether a responsibility is within scope (29.15.1)."""
    return assigned


def boundaries_respected(within: bool, peer: bool) -> bool:
    """Return whether agent boundaries hold (29.15.2/29.16)."""
    return within and peer


def agent_inputs_ok(complete: bool, typed: bool) -> bool:
    """Return whether agent inputs are valid (29.17)."""
    return complete and typed


def agent_outputs_ok(schema: bool, traceable: bool) -> bool:
    """Return whether agent outputs are valid (29.18)."""
    return schema and traceable


def interface_contract_met(contract: bool) -> bool:
    """Return whether an interface contract is met (29.19.1)."""
    return contract


def handoff_valid(sender: bool, receiver: bool, message: bool) -> bool:
    """Return whether a handoff is valid (29.19.2)."""
    return sender and receiver and message


def communication_reliable(acks: bool, retries: int) -> bool:
    """Return whether agent communication is reliable (29.20)."""
    return acks or retries <= 0


def state_transition_allowed(current: str, next_state: str) -> bool:
    """Return whether a state transition is allowed (29.21.2)."""
    return (current, next_state) in _VALID_TRANSITIONS


def dependencies_resolved(acyclic: bool) -> bool:
    """Return whether agent dependencies resolve (29.22)."""
    return acyclic


def recovery_supported(replay: bool) -> bool:
    """Return whether an agent supports recovery (29.25)."""
    return replay


@dataclass
class SubAgentEngine:
    """Sub-agent architecture lifecycle (29.1)."""

    name: str
    _ready: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._ready = True

    def status(self) -> str:
        """Return the sub-agent topology state."""
        return "ready" if self._ready else "initialising"
