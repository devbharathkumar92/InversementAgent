"""Topic 2.12/2.12.1/2.12.2 — conflict detection and the fixed priority model.

Priority (highest to lowest) is fixed by the SRS:

    safety/non-negotiable rules -> approved core goal -> approved SRS
    requirements -> validated dependencies -> task instructions
    -> optimization/return objectives
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class ConflictPriority(IntEnum):
    """Precedence for resolving conflicts (Topic 2.12.2)."""

    SAFETY_NON_NEGOTIABLE = 5
    APPROVED_GOAL = 4
    APPROVED_SRS = 3
    VALIDATED_DEPENDENCY = 2
    TASK_INSTRUCTIONS = 1
    OPTIMIZATION_OBJECTIVE = 0


@dataclass(frozen=True)
class Conflict:
    """A detected conflict between two priorities."""

    priority_a: ConflictPriority
    priority_b: ConflictPriority
    kind: str = "generic"


class ConflictResolver:
    """Resolves conflicts by choosing the higher-priority side."""

    def resolve(self, conflict: Conflict) -> ConflictPriority:
        if conflict.priority_a == conflict.priority_b:
            raise ValueError("Cannot resolve a conflict where both sides have equal priority")
        return (
            conflict.priority_a
            if conflict.priority_a > conflict.priority_b
            else conflict.priority_b
        )


def detect_conflict(
    instruction_a: str,
    instruction_b: str,
    kind: str = "generic",
) -> Conflict | None:
    """Detect whether two instructions conflict (Topic 2.12.1).

    A conflict is detected when safety or goal protections are pitted
    against a lower-level objective. This is intentionally a conservative
    detector: suspicious keyword combinations produce a conflict.
    """
    lower_a = instruction_a.lower()
    lower_b = instruction_b.lower()
    protection_words = {"safety", "bypass", "violate", "unauthorized"}
    objective_words = {"returns", "profit", "speed", "optimize", "maximize"}

    if (
        any(w in lower_a for w in protection_words) and any(w in lower_b for w in objective_words)
    ) or (
        any(w in lower_b for w in protection_words) and any(w in lower_a for w in objective_words)
    ):
        return Conflict(
            ConflictPriority.SAFETY_NON_NEGOTIABLE, ConflictPriority.OPTIMIZATION_OBJECTIVE, kind
        )
    return None
