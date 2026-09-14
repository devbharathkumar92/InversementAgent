"""Tests for Topic 34 — SRS Self-Validation.

Covers structural validation (34.2), completeness (34.3),
consistency (34.4), ambiguity/contradiction detection
(34.20/34.21), duplicate/blocked detection (34.23/34.25),
traceability validation (34.26), the quality score (34.27) and
approval criteria (34.29).
"""

import pytest

from src.common.selfvalidate.engine import (
    SelfValidationEngine,
    ambiguity_free,
    approval_recommended,
    blocked_detected,
    completeness_ok,
    consistency_ok,
    contradiction_free,
    duplicates_absent,
    quality_score_pass,
    traceability_validated,
)


class TestValidationChecks:
    """REQ 34.3.1/34.3.2/34.4.1/34.4.2/34.20/34.21."""

    def test_completeness_ok(self):
        assert completeness_ok(missing=0, threshold=0.95) is True

    def test_completeness_below_threshold(self):
        assert completeness_ok(missing=3, threshold=0.95) is False

    def test_consistency_ok(self):
        assert consistency_ok(internal=True, cross_section=True) is True

    def test_consistency_violation(self):
        assert consistency_ok(internal=False, cross_section=True) is False

    def test_ambiguity_free(self):
        assert ambiguity_free(ambiguous=0) is True

    def test_ambiguous_section(self):
        assert ambiguity_free(ambiguous=2) is False

    def test_contradiction_free(self):
        assert contradiction_free(contradictions=0) is True

    def test_contradiction_present(self):
        assert contradiction_free(contradictions=1) is False


class TestDetection:
    """REQ 34.22/34.23/34.24/34.25/34.26."""

    def test_duplicates_absent(self):
        assert duplicates_absent(duplicates=0) is True

    def test_duplicates_found(self):
        assert duplicates_absent(duplicates=1) is False

    def test_blocked_detected(self):
        assert blocked_detected(blocked=1) is True

    def test_traceability_validated(self):
        assert traceability_validated(forward=True, backward=True) is True

    def test_traceability_gap(self):
        assert traceability_validated(forward=True, backward=False) is False


class TestQualityAndApproval:
    """REQ 34.27/34.27.1/34.27.2/34.29."""

    def test_quality_score_pass(self):
        assert quality_score_pass(score=0.93, minimum=0.90) is True

    def test_quality_score_below(self):
        assert quality_score_pass(score=0.80, minimum=0.90) is False

    def test_approval_recommended(self):
        assert approval_recommended(score=0.93, report=True) is True

    def test_approval_denied(self):
        assert approval_recommended(score=0.80, report=True) is False


class TestEngine:
    """REQ 34.1 — self-validation lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            SelfValidationEngine(name=" ")

    def test_engine_status(self):
        assert SelfValidationEngine(name="v").status() == "validated"


pytestmark = pytest.mark.unit
