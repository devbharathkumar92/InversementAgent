"""Topic 7 — Technology Stack and Technical Feasibility.

Declares the governed technology contract: deterministic (non-LLM)
responsibilities, technology selection/rejection rules, branch strategy,
and strict dependency pinning for reproducible builds.
"""

from .selection import (
    BranchStrategy,
    TechSelection,
    validate_dependency_pinning,
    validate_pinned_dependency,
)

__all__ = [
    "TechSelection",
    "BranchStrategy",
    "validate_dependency_pinning",
    "validate_pinned_dependency",
]
