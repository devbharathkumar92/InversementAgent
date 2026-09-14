"""Tests for Topic 28 — Requirement Traceability.

Covers requirement IDs (28.3), mappings to goals/SRS/tasks/agents/code
(28.6-28.9), trace validation (28.10.2/28.19.1/28.20.1), coverage
measurement (28.18) and governance (28.21/28.23).
"""

import pytest

from src.common.traceability.engine import (
    TraceabilityEngine,
    broken_trace_detected,
    code_coverage_sufficient,
    coverage_met,
    goals_mapped,
    id_format_valid,
    id_unique,
    missing_trace_detected,
    requirement_classified,
    result_mapped,
    trace_validated,
)


class TestRequirementIDs:
    """REQ 28.3/28.3.1/28.3.2."""

    def test_id_format_valid(self):
        assert id_format_valid("REQ-24.15") is True

    def test_id_format_invalid(self):
        assert id_format_valid("x") is False

    def test_id_unique(self):
        assert id_unique(conflicts=0) is True

    def test_id_duplicate(self):
        assert id_unique(conflicts=1) is False


class TestMapping:
    """REQ 28.6/28.10.2/28.11.2."""

    def test_goals_mapped(self):
        assert goals_mapped(goals=True, srs=True) is True

    def test_goal_gap(self):
        assert goals_mapped(goals=False, srs=True) is False

    def test_code_coverage_sufficient(self):
        assert code_coverage_sufficient(target=True, actual=True) is True

    def test_code_uncovered(self):
        assert code_coverage_sufficient(target=True, actual=False) is False

    def test_result_mapped(self):
        assert result_mapped(recorded=True, passed=True) is True


class TestTraceChecks:
    """REQ 28.19.1/28.20.1/28.21/28.18.2."""

    def test_missing_trace_detected(self):
        assert missing_trace_detected(verified=False) is True

    def test_no_missing_trace(self):
        assert missing_trace_detected(verified=True) is False

    def test_broken_trace_detected(self):
        assert broken_trace_detected(intact=False) is True

    def test_trace_validated(self):
        assert trace_validated(missing=0, broken=0) is True

    def test_coverage_met(self):
        assert coverage_met(coverage=0.95, threshold=0.9) is True

    def test_coverage_below_threshold(self):
        assert coverage_met(coverage=0.7, threshold=0.9) is False

    def test_requirement_classified(self):
        assert requirement_classified(kind="functional") is True


class TestEngine:
    """REQ 28.1 — traceability lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            TraceabilityEngine(name=" ")

    def test_engine_status(self):
        assert TraceabilityEngine(name="t").status() == "tracked"


pytestmark = pytest.mark.unit
