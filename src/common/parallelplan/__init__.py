"""Topic 32 — Parallel Development Plan.

Schedules independent work in parallel while enforcing shared
contracts, workspace isolation and safe merge gates
(REQ 32.1-32.30 subset).
"""

from .engine import (
    ParallelPlanEngine,
    branch_naming_convention,
    conflict_detected,
    contract_valid,
    eligible_for_parallel,
    final_readiness_gate,
    interface_compatibility,
    isolation_respected,
    merge_preconditions_met,
    parallel_acceptance,
    resource_contention_handled,
    shared_resources_identified,
    workspaces_isolated,
)

__all__ = [
    "ParallelPlanEngine",
    "branch_naming_convention",
    "conflict_detected",
    "contract_valid",
    "eligible_for_parallel",
    "final_readiness_gate",
    "interface_compatibility",
    "isolation_respected",
    "merge_preconditions_met",
    "parallel_acceptance",
    "resource_contention_handled",
    "shared_resources_identified",
    "workspaces_isolated",
]
