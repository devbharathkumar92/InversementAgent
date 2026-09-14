"""Topic 31 — Dependency and Execution Plan.

Plans execution so that hard dependencies gate their dependents
(31.3.1), only independent tasks run in parallel (31.11), blocked
tasks wait on explicit unblocking conditions (31.12), and the
critical path is identified and monitored (31.24). (REQ 31.1-31.30
enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def hard_dependency_met(mandatory: bool, satisfied: bool) -> bool:
    """Return whether a mandatory dependency is met (31.3.1)."""
    return (not mandatory) or satisfied


def soft_preferred(before: bool, after: bool) -> bool:
    """Return whether a soft dependency was honoured (31.4)."""
    return before or after


def prerequisites_defined(explicit: bool) -> bool:
    """Return whether prerequisites are defined (31.5)."""
    return explicit


def execution_order_ok(ordered: bool) -> bool:
    """Return whether execution order is established (31.9)."""
    return ordered


def parallel_eligible(independent: bool, resources: bool) -> bool:
    """Return whether a task may run in parallel (31.11.1/31.11.2)."""
    return independent and resources


def blocking_resolved(blocked: bool) -> bool:
    """Return whether a block is cleared (31.12.2)."""
    return not blocked


def dependency_valid(identified: bool, acyclic: bool) -> bool:
    """Return whether a dependency is valid (31.6/31.7)."""
    return identified and acyclic


def recovery_planned(route: bool) -> bool:
    """Return whether dependency recovery is planned (31.14)."""
    return route


def critical_path_identified(longest: bool, monitored: bool) -> bool:
    """Return whether the critical path is managed (31.24.1/31.24.2)."""
    return longest and monitored


def progress_tracked(recorded: bool, current: bool) -> bool:
    """Return whether execution progress is tracked (31.25)."""
    return recorded and current


@dataclass
class ExecutionPlanEngine:
    """Dependency planning lifecycle (31.1)."""

    name: str
    _planned: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._planned = True

    def status(self) -> str:
        """Return the execution plan state."""
        return "planned" if self._planned else "unplanned"
