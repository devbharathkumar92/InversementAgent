"""Topic 2.8/2.8.1/2.8.2 — goal immutability and the controlled change exception."""

from __future__ import annotations

from dataclasses import dataclass, field


class ImmutableGoalError(Exception):
    """Raised when an unauthorized agent attempts to change an immutable element."""


@dataclass
class ImmutableGoalElements:
    """The elements ordinary agents cannot change (Topic 2.8.1).

    The initial protected set covers the fundamental purpose, primary
    objective, initial geographic/currency scope, and safety-first
    requirement.
    """

    elements: set[str] = field(
        default_factory=lambda: {
            "fundamental_purpose",
            "primary_objective",
            "initial_geographic_currency_scope",
            "safety_first_requirement",
        }
    )

    def modify(self, element: str, new_value: str, by: str) -> None:
        """Reject any change made by a non-authorized actor.

        Only the controlled change workflow (``ControlledGoalChange``) may
        change an immutable element; ordinary agents are always rejected.
        """
        if element in self.elements:
            if by not in {"project-governance", "human-gate"}:
                raise ImmutableGoalError(
                    f"Agent {by!r} cannot modify immutable element {element!r}"
                )
            # Even authorized actors must go through the controlled workflow;
            # direct mutation is prohibited here by design.


@dataclass(frozen=True)
class ControlledGoalChange:
    """The only permitted path for an immutable-goal change (Topic 2.8.2)."""

    requires_impact_assessment: bool = True
    approved_by: str = "project-governance"


def preconditions_satisfied(change: ControlledGoalChange) -> bool:
    """Whether the controlled goal change satisfies its preconditions."""
    return change.requires_impact_assessment is True and change.approved_by in {
        "project-governance",
        "human-gate",
    }
