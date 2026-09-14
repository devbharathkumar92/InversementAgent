"""Topic 9 — System Execution Lifecycle.

Lifecycle stage tracking, environment validation, task assignment and
prioritization, sequential/parallel execution gating, blocked-state
management, and completion verification.
"""

from .engine import (
    LifecycleEngine,
    LifecyclePhase,
    LifecycleStage,
    check_dependencies,
    compute_progress,
    validate_prerequisites,
)

__all__ = [
    "LifecycleEngine",
    "LifecyclePhase",
    "LifecycleStage",
    "check_dependencies",
    "compute_progress",
    "validate_prerequisites",
]
