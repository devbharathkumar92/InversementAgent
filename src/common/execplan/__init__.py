"""Topic 31 — Dependency and Execution Plan.

Orders execution by a validated dependency graph, allowing parallel
execution only where safe, and tracks progress/critical path
(REQ 31.1-31.30 subset).
"""

from .engine import (
    ExecutionPlanEngine,
    blocking_resolved,
    critical_path_identified,
    dependency_valid,
    execution_order_ok,
    hard_dependency_met,
    parallel_eligible,
    prerequisites_defined,
    progress_tracked,
    recovery_planned,
    soft_preferred,
)

__all__ = [
    "ExecutionPlanEngine",
    "blocking_resolved",
    "critical_path_identified",
    "dependency_valid",
    "execution_order_ok",
    "hard_dependency_met",
    "parallel_eligible",
    "prerequisites_defined",
    "progress_tracked",
    "recovery_planned",
    "soft_preferred",
]
