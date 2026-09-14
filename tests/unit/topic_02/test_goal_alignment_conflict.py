"""Tests for Topic 2 — Evaluation, Alignment, Conflicts, Deviation.

Covers REQ 2.9, 2.11, 2.12/2.12.1/2.12.2, 2.13.
"""

import pytest

from src.common.goal.alignment import GoalAlignment, RequirementAlignment
from src.common.goal.conflicts import (
    Conflict,
    ConflictPriority,
    ConflictResolver,
    detect_conflict,
)
from src.common.goal.deviation import GoalDeviationDetector
from src.common.goal.evaluation import GoalEvaluation, evaluate_goal_compliance


class TestGoalEvaluation:
    """REQ 2.9 — objective compliance criteria."""

    def test_evaluation_requires_criteria(self):
        evaluation = GoalEvaluation(
            functional_alignment=True,
            scope_alignment=True,
            safety_alignment=True,
            evidence_quality=True,
            traceability=True,
        )
        assert evaluate_goal_compliance(evaluation) is True

    def test_evaluation_fails_when_safety_missing(self):
        evaluation = GoalEvaluation(
            functional_alignment=True,
            scope_alignment=True,
            safety_alignment=False,
            evidence_quality=True,
            traceability=True,
        )
        assert evaluate_goal_compliance(evaluation) is False


class TestGoalAlignment:
    """REQ 2.11 — every material requirement maps to the goal."""

    def test_alignment_maps_requirement_to_goal(self):
        alignment = RequirementAlignment(
            requirement_id="6.10",
            goal_statement="align to goal",
            evidence="traceability record",
        )
        assert alignment.is_aligned()

    def test_alignment_requires_goal_statement(self):
        with pytest.raises(ValueError):
            RequirementAlignment(requirement_id="6.10", goal_statement="", evidence="x")

    def test_goal_alignment_aggregates_requirements(self):
        ga = GoalAlignment()
        ga.add(RequirementAlignment("6.10", "supports goal", "evidence"))
        ga.add(RequirementAlignment("7.1", "supports goal", "evidence"))
        assert ga.all_aligned()


class TestConflictResolution:
    """REQ 2.12/2.12.1/2.12.2 — detect, classify, prioritize conflicts."""

    def test_detect_conflict_between_instructions(self):
        conflict = detect_conflict(
            instruction_a="increase returns",
            instruction_b="bypass safety",
            kind="safety_vs_objective",
        )
        assert conflict is not None

    def test_safety_priority_is_highest(self):
        assert ConflictPriority.SAFETY_NON_NEGOTIABLE > ConflictPriority.APPROVED_GOAL
        assert ConflictPriority.APPROVED_GOAL > ConflictPriority.APPROVED_SRS
        assert ConflictPriority.APPROVED_SRS > ConflictPriority.TASK_INSTRUCTIONS

    def test_resolver_follows_priority_model(self):
        resolver = ConflictResolver()
        conflict = Conflict(
            priority_a=ConflictPriority.OPTIMIZATION_OBJECTIVE,
            priority_b=ConflictPriority.SAFETY_NON_NEGOTIABLE,
        )
        winner = resolver.resolve(conflict)
        assert winner == ConflictPriority.SAFETY_NON_NEGOTIABLE


class TestDeviationDetection:
    """REQ 2.13 — detect drift from the approved goal."""

    def test_no_deviation_when_in_alignment(self):
        detector = GoalDeviationDetector()
        assert (
            detector.monitor(work_item="evaluate NSE opportunity", current_goal="evaluate") is None
        )

    def test_deviation_detected_when_out_of_alignment(self):
        detector = GoalDeviationDetector()
        deviation = detector.monitor(work_item="expand to US markets", current_goal="India focus")
        assert deviation is not None


pytestmark = pytest.mark.unit
