"""Tests for Topic 2.1/2.2/2.3/2.5 — Goal, Mission, Primary Objective, Scope."""

import pytest

from src.common.goal.goal import (
    CoreGoal,
    ScopeBounds,
    is_within_scope,
)


def make_goal(**overrides):
    data = {
        "goal_statement": "Research and evaluate short-term investment opportunities",
        "mission_statement": (
            "Acquire and validate data; discover, analyze, and evaluate opportunities"
        ),
        "primary_objective": (
            "Identify and evaluate short-term opportunities using validated evidence"
        ),
        "scope": ScopeBounds(geography="India", currency="INR", horizon_days=30),
    }
    data.update(overrides)
    return data


class TestGoalStatement:
    """REQ 2.1 — single authoritative purpose."""

    def test_goal_requires_statement(self):
        with pytest.raises(ValueError):
            CoreGoal(goal_statement="", mission_statement="x", primary_objective="y", scope=None)

    def test_goal_is_stored(self):
        goal = CoreGoal(**make_goal())
        assert goal.goal_statement.startswith("Research and evaluate")


class TestMissionStatement:
    """REQ 2.2 — operational mission connected to the purpose."""

    def test_mission_requires_statement(self):
        with pytest.raises(ValueError):
            CoreGoal(goal_statement="x", mission_statement="", primary_objective="y", scope=None)

    def test_mission_is_stored(self):
        goal = CoreGoal(**make_goal())
        assert "Acquire and validate data" in goal.mission_statement


class TestPrimaryObjective:
    """REQ 2.3/2.3.1 — measurable, highest-priority objective."""

    def test_primary_objective_stored(self):
        goal = CoreGoal(**make_goal())
        assert "opportunities" in goal.primary_objective

    def test_primary_objective_is_distinct_from_goal(self):
        goal = CoreGoal(**make_goal())
        assert goal.primary_objective != goal.goal_statement


class TestGoalScope:
    """REQ 2.5 — India/INR scope check."""

    def test_india_inr_in_scope(self):
        assert is_within_scope(ScopeBounds("India", "INR", 30), geography="India", currency="INR")

    def test_outside_geography_out_of_scope(self):
        assert not is_within_scope(ScopeBounds("India", "INR", 30), geography="US", currency="INR")

    def test_outside_currency_out_of_scope(self):
        assert not is_within_scope(
            ScopeBounds("India", "INR", 30), geography="India", currency="USD"
        )

    def test_unknown_geography_raises_error(self):
        with pytest.raises(ValueError):
            is_within_scope(ScopeBounds("India", "INR", 30), geography="", currency="INR")


pytestmark = pytest.mark.unit
