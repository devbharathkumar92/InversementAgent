"""Topic 2.9 — goal evaluation criteria (objective compliance judgment)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GoalEvaluation:
    """The objective compliance criteria (Topic 2.9)."""

    functional_alignment: bool
    scope_alignment: bool
    safety_alignment: bool
    evidence_quality: bool
    traceability: bool

    def is_compliant(self) -> bool:
        return all(
            (
                self.functional_alignment,
                self.scope_alignment,
                self.safety_alignment,
                self.evidence_quality,
                self.traceability,
            )
        )


def evaluate_goal_compliance(evaluation: GoalEvaluation) -> bool:
    """Return whether the work satisfies every goal evaluation criterion."""
    return evaluation.is_compliant()
