"""Topic 2.11 — goal alignment requirements.

Every material requirement, agent task, capability, and release criterion
must map directly to the approved goal, preventing disconnected work.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class GoalAlignmentError(ValueError):
    """Raised when an alignment record is incomplete."""


@dataclass
class RequirementAlignment:
    """Maps a single requirement to the approved goal with evidence."""

    requirement_id: str
    goal_statement: str
    evidence: str

    def __post_init__(self) -> None:
        if not self.requirement_id or not self.requirement_id.strip():
            raise GoalAlignmentError("requirement_id must be non-empty")
        if not self.goal_statement or not self.goal_statement.strip():
            raise GoalAlignmentError("goal_statement must be non-empty")
        if not self.evidence or not self.evidence.strip():
            raise GoalAlignmentError("evidence must be non-empty")

    def is_aligned(self) -> bool:
        return self.goal_statement.strip() != ""


@dataclass
class GoalAlignment:
    """Aggregates requirement-to-goal alignments."""

    _alignments: list[RequirementAlignment] = field(default_factory=list)

    def add(self, alignment: RequirementAlignment) -> None:
        self._alignments.append(alignment)

    def all_aligned(self) -> bool:
        return len(self._alignments) > 0 and all(a.is_aligned() for a in self._alignments)
