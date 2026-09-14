"""Tests for Topic 2.7/2.7.1/2.7.2/2.8/2.8.1/2.8.2 — Non-Negotiable Conditions and Immutability."""

import pytest

from src.common.goal.immutability import (
    ControlledGoalChange,
    ImmutableGoalElements,
    ImmutableGoalError,
    preconditions_satisfied,
)
from src.common.goal.violations import GoalViolation, GoalViolationDetector


def test_immutable_elements_are_defined():
    elements = ImmutableGoalElements()
    assert "fundamental_purpose" in elements.elements
    assert "initial_geographic_currency_scope" in elements.elements
    assert "safety_first_requirement" in elements.elements


def test_no_unauthorized_change_to_immutable_element():
    elements = ImmutableGoalElements()
    try:
        elements.modify("fundamental_purpose", "new purpose", by="optimizer-agent")
    except ImmutableGoalError:
        pass
    else:
        raise AssertionError("optimizer-agent must not change an immutable element")


def test_controlled_change_allowed_with_authority():
    controlled = ControlledGoalChange(
        requires_impact_assessment=True, approved_by="project-governance"
    )
    assert preconditions_satisfied(controlled)


def test_violation_detector_flags_scope_expansion():
    detector = GoalViolationDetector()
    violation = detector.detect(
        event={"type": "scope_change", "geography": "US", "currency": "INR"},
        current={"geography": "India", "currency": "INR"},
    )
    assert violation is GoalViolation.GEOGRAPHIC_SCOPE_EXPANSION


def test_safety_bypass_is_a_violation():
    detector = GoalViolationDetector()
    violation = detector.detect(event={"type": "safety_bypass"}, current={})
    assert violation is GoalViolation.SAFETY_BYPASS


def test_no_violation_for_normal_event():
    detector = GoalViolationDetector()
    violation = detector.detect(event={"type": "data_validated"}, current={})
    assert violation is None


pytestmark = pytest.mark.unit
