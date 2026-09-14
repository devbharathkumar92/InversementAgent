"""Topic 30 — Sub-Agent Task Specification.

Specifies a task completely: objective and scope (30.3/30.4),
schema-validated inputs/outputs (30.5/30.6), implementation and
processing rules (30.12-30.16), error/blocked handling
(30.18/30.19), and acceptance/handoff gates (30.21/30.22/30.26).
(REQ 30.1-30.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def objective_defined(goal: bool, outcome: bool) -> bool:
    """Return whether task purpose is defined (30.3.1/30.3.2)."""
    return goal and outcome


def constraints_ok(in_scope: bool, excluded: bool) -> bool:
    """Return whether task scope/constraints are set (30.4/30.15)."""
    return in_scope and excluded


def prerequisites_met(ready: bool) -> bool:
    """Return whether task prerequisites are met (30.7)."""
    return ready


def input_valid(schema: bool, values: bool) -> bool:
    """Return whether inputs pass schema validation (30.5.2)."""
    return schema and values


def output_valid(schema: bool, values: bool) -> bool:
    """Return whether outputs pass schema validation (30.6.2)."""
    return schema and values


def implementation_specified(steps: bool, restrictions: bool) -> bool:
    """Return whether implementation is specified (30.12.1/30.12.2)."""
    return steps and restrictions


def no_prohibited_actions(allowed: bool, listed: bool) -> bool:
    """Return whether prohibited actions are bounded (30.16)."""
    return allowed and listed


def error_recoverable(recoverable: bool) -> bool:
    """Return whether an error is recoverable (30.18.1/30.18.2)."""
    return recoverable


def blocked_action_defined(conditions: bool, action: bool) -> bool:
    """Return whether blocked-state handling is defined (30.19)."""
    return conditions and action


def acceptance_met(functional: bool, technical: bool) -> bool:
    """Return whether acceptance criteria are met (30.21.1/30.21.2)."""
    return functional and technical


def requirements_met(defined: bool, executed: bool) -> bool:
    """Return whether test requirements are met (30.22)."""
    return defined and executed


def handoff_package_ok(outputs: bool, evidence: bool) -> bool:
    """Return whether a handoff package is complete (30.26.1)."""
    return outputs and evidence


@dataclass
class TaskSpecEngine:
    """Task specification lifecycle (30.1)."""

    name: str
    _specified: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._specified = True

    def status(self) -> str:
        """Return the task specification state."""
        return "specified" if self._specified else "unspecified"
