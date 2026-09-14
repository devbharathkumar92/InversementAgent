"""Tests for Topic 25 — Self-Evaluation.

Covers goal/SRS/scope compliance checks (25.2/25.3/25.4), evaluation
checks (25.7/25.9), stuck-state and deviation detection (25.20/25.21),
evidence capture (25.23), scoring and thresholds (25.24/25.25), and
failed-evaluation handling (25.26).
"""

import pytest

from src.common.evaluation.engine import (
    EvaluationEngine,
    deviation_severity,
    evidence_captured,
    failed_evaluation_recovery,
    goal_met,
    methodology_compliant,
    score_threshold_met,
    stuck_detected,
    violation_detected,
)


class TestCompliance:
    """REQ 25.2/25.2.2/25.3/25.3.2/25.4."""

    def test_goal_met(self):
        assert goal_met(result=True, expected=True) is True

    def test_goal_deviation(self):
        assert goal_met(result=False, expected=True) is False

    def test_violation_detected(self):
        assert violation_detected(delta=0.5, tolerance=0.2) is True

    def test_no_violation(self):
        assert violation_detected(delta=0.1, tolerance=0.2) is False

    def test_methodology_compliant(self):
        assert methodology_compliant(scope=True, requirements=True) is True


class TestDetection:
    """REQ 25.20/25.20.2/25.21.2/25.23."""

    def test_stuck_detected(self):
        assert stuck_detected(progress_made=False, since_turns=5) is True

    def test_stuck_cleared(self):
        assert stuck_detected(progress_made=True, since_turns=5) is False

    def test_deviation_severity(self):
        assert deviation_severity(delta=0.9) == "high"

    def test_evidence_captured(self):
        assert evidence_captured(run_id="r1", saved=True) is True


class TestScoring:
    """REQ 25.24.2/25.26/25.26.2."""

    def test_score_threshold_met(self):
        assert score_threshold_met(score=0.92, threshold=0.8) is True

    def test_score_reject(self):
        assert score_threshold_met(score=0.6, threshold=0.8) is False

    def test_failed_recovery(self):
        assert failed_evaluation_recovery(escalated=True) == "escalated"


class TestEngine:
    """REQ 25.1 — evaluation lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            EvaluationEngine(name=" ")

    def test_engine_armed(self):
        assert EvaluationEngine(name="e").status() == "evaluating"


pytestmark = pytest.mark.unit
