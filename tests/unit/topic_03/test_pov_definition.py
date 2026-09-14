"""Tests for Topic 3 — Proof of Value definition and decision rules.

Covers REQ 3.1, 3.3/3.3.1-3.3.3, 3.5/3.5.1/3.5.2, 3.17/3.17.1/3.17.2,
3.18/3.18.1/3.18.2, 3.21, 3.22.
"""

import pytest

from src.common.pov.definition import (
    FailureClass,
    PoVDefinition,
    PoVStatus,
    completion_status,
    evaluate_release_gate,
    failure_class,
    meets_success_threshold,
    validate_completion,
)


def make_pov(**overrides):
    data = {
        "name": "InversementAgent PoV",
        "objectives": {
            "functional": "Detect and evaluate short-term NSE opportunities",
            "technical": "Reliable data validation and evidence pipeline",
            "outcome": "Approved evaluation artifacts without unsupported labels",
        },
        "success_conditions": ["Validated evidence", "Risk-aware evaluation"],
        "minimum_success_thresholds": {"detection": 0.9, "data_quality": 0.95},
        "release_blocking_conditions": ["Unresolved critical failure", "Safety violation"],
        "acceptance_criteria": {"functional": "All core flows pass", "safety": "No safety bypass"},
    }
    data.update(overrides)
    return PoVDefinition(**data)


class TestPoVDefinition:
    """REQ 3.1 — PoV is a controlled definition with objectives/scope."""

    def test_pov_requires_name_and_objectives(self):
        pov = make_pov()
        assert pov.name == "InversementAgent PoV"
        assert set(pov.objectives) == {"functional", "technical", "outcome"}

    def test_pov_requires_all_objective_types(self):
        with pytest.raises(ValueError):
            make_pov(objectives={"functional": "only"})

    def test_pov_objective_categories_covered(self):
        pov = make_pov()
        assert {"3.3.1", "3.3.2", "3.3.3"} <= set(pov.objective_traceability())


class TestMinimumSuccessThresholds:
    """REQ 3.5.1 — explicit minimum success thresholds."""

    def test_meets_threshold_when_above(self):
        assert meets_success_threshold(0.92, 0.90)

    def test_fails_threshold_when_below(self):
        assert not meets_success_threshold(0.80, 0.90)

    def test_threshold_requires_numeric(self):
        with pytest.raises(ValueError):
            meets_success_threshold("high", 0.90)


class TestReleaseBlockingConditions:
    """REQ 3.5.2 — release-blocking conditions halt release."""

    def test_release_blocked_when_condition_present(self):
        pov = make_pov()
        gate = evaluate_release_gate(pov, active_blockers=["Unresolved critical failure"])
        assert gate.release_approved is False
        assert "Unresolved critical failure" in gate.blockers

    def test_release_blocked_on_safety_violation(self):
        gate = evaluate_release_gate(make_pov(), active_blockers=["Safety violation"])
        assert gate.release_approved is False

    def test_release_approved_when_no_blockers(self):
        gate = evaluate_release_gate(make_pov(), active_blockers=[])
        assert gate.release_approved is True


class TestFailureClassification:
    """REQ 3.18/3.18.1/3.18.2 — critical vs non-critical failure."""

    def test_safety_failure_is_critical(self):
        assert failure_class("safety violation") is FailureClass.CRITICAL

    def test_evidence_failure_is_critical(self):
        assert failure_class("missing evidence") is FailureClass.CRITICAL

    def test_data_quality_failure_is_non_critical(self):
        assert failure_class("data quality dip") is FailureClass.NON_CRITICAL

    def test_unknown_failure_is_non_critical(self):
        assert failure_class("minor ui glitch") is FailureClass.NON_CRITICAL


class TestAcceptanceCriteria:
    """REQ 3.17/3.17.1/3.17.2 — functional and safety acceptance."""

    def test_acceptance_met_when_all_passed(self):
        pov = make_pov()
        # both functional and safety accepted -> completed POV
        assert validate_completion(pov, functional_acceptance=True, safety_acceptance=True) is True

    def test_completion_fails_without_safety_acceptance(self):
        pov = make_pov()
        with pytest.raises(ValueError):
            validate_completion(pov, functional_acceptance=True, safety_acceptance=False)

    def test_completion_status_is_terminal(self):
        assert (
            completion_status(safety_acceptance=True, functional_acceptance=True)
            is PoVStatus.COMPLETED
        )


pytestmark = pytest.mark.unit
