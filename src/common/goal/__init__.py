"""Topic 2 — Core Goal and Mission.

Implements the goal/mission statements, primary objective, scope bounds,
non-negotiable conditions, immutability, alignment, conflict resolution,
deviation detection, evaluation, and success metrics.
"""

from .alignment import GoalAlignment, RequirementAlignment
from .conflicts import Conflict, ConflictPriority, ConflictResolver, detect_conflict
from .deviation import GoalDeviation, GoalDeviationDetector
from .evaluation import GoalEvaluation, evaluate_goal_compliance
from .goal import CoreGoal, Mission, PrimaryObjective, ScopeBounds, is_within_scope
from .immutability import (
    ControlledGoalChange,
    ImmutableGoalElements,
    ImmutableGoalError,
    preconditions_satisfied,
)
from .violations import GoalViolation, GoalViolationDetector

__all__ = [
    "CoreGoal",
    "Mission",
    "PrimaryObjective",
    "ScopeBounds",
    "is_within_scope",
    "GoalAlignment",
    "RequirementAlignment",
    "Conflict",
    "ConflictPriority",
    "ConflictResolver",
    "detect_conflict",
    "GoalDeviation",
    "GoalDeviationDetector",
    "GoalEvaluation",
    "evaluate_goal_compliance",
    "ControlledGoalChange",
    "ImmutableGoalElements",
    "ImmutableGoalError",
    "preconditions_satisfied",
    "GoalViolation",
    "GoalViolationDetector",
]
