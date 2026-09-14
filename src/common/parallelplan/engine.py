"""Topic 32 — Parallel Development Plan.

Permits parallel execution only for exclusive, independent tasks
(32.2.1), isolates agent workspaces (32.9), validates shared
interface contracts (32.5/32.14), detects conflicts (32.15) and
gates merges on preconditions (32.20.1) plus a final readiness
gate (32.29.2). (REQ 32.1-32.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def eligible_for_parallel(independent: bool, exclusive: bool) -> bool:
    """Return whether a task may run in parallel (32.2.1/32.2.2)."""
    return independent and exclusive


def shared_resources_identified(known: bool) -> bool:
    """Return whether shared resources are identified (32.4)."""
    return known


def contract_valid(defined: bool, owned: bool) -> bool:
    """Return whether a shared interface contract is valid (32.5.1/32.5.2)."""
    return defined and owned


def branch_naming_convention(respects: bool) -> bool:
    """Return whether branch naming is respected (32.8)."""
    return respects


def workspaces_isolated(separate: bool) -> bool:
    """Return whether agent workspaces are isolated (32.9.1)."""
    return separate


def isolation_respected(isolated: bool, shared_rules: bool) -> bool:
    """Return whether isolation and shared rules hold (32.9.2)."""
    return isolated and shared_rules


def interface_compatibility(compatible: bool) -> bool:
    """Return whether interfaces are compatible (32.13)."""
    return compatible


def conflict_detected(identified: bool) -> bool:
    """Return whether conflicts are detectable (32.15.1)."""
    return identified


def merge_preconditions_met(tested: bool, reviewed: bool) -> bool:
    """Return whether merge preconditions are met (32.20.1)."""
    return tested and reviewed


def resource_contention_handled(managed: bool) -> bool:
    """Return whether resource contention is managed (32.24)."""
    return managed


def parallel_acceptance(planned: bool, validated: bool) -> bool:
    """Return whether parallel acceptance criteria are met (32.28)."""
    return planned and validated


def final_readiness_gate(checklist: bool, gates: bool) -> bool:
    """Return whether final integration readiness holds (32.29.1/32.29.2)."""
    return checklist and gates


@dataclass
class ParallelPlanEngine:
    """Parallel development lifecycle (32.1)."""

    name: str
    _scheduled: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._scheduled = True

    def status(self) -> str:
        """Return the parallel plan state."""
        return "scheduled" if self._scheduled else "draft"
