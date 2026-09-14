"""Tests for Topic 11 — Data Validation and Quality Layer.

Covers completeness (11.2), accuracy (11.3), integrity (11.6),
duplicate/missing/invalid detection (11.7-11.9), anomaly severity
(11.10.2), timestamp validation (11.13), confidence scoring (11.20),
and invalid-data handling — reject/quarantine/recover (11.22-11.24).
"""

import pytest

from src.common.quality.engine import (
    QualityEngine,
    confidence_score,
    detect_duplicates,
    is_complete,
    is_fresh,
    is_valid_timestamp,
    quarantine_record,
    reject_record,
    severity_grade,
)


class TestCompleteness:
    """REQ 11.2/11.2.1/11.2.2 — completeness vs missing-field thresholds."""

    def test_complete_record(self):
        assert is_complete({"a": 1, "b": 2}, required=("a", "b")) is True

    def test_missing_field_incomplete(self):
        assert is_complete({"a": 1}, required=("a", "b")) is False

    def test_accepts_none_value_as_present(self):
        assert is_complete({"a": None, "b": 1}, required=("a", "b")) is True


class TestAccuracy:
    """REQ 11.3 — accuracy rules enforced and cross-source conflicts flagged."""

    def test_within_tolerance_accurate(self):
        q = QualityEngine(name="q")
        assert q.within_tolerance(10.0, reference=10.2, tol=0.5) is True

    def test_out_of_tolerance(self):
        q = QualityEngine(name="q")
        assert q.within_tolerance(10.0, reference=11.0, tol=0.5) is False


class TestIntegrityAndDetection:
    """REQ 11.6/11.7/11.8/11.9 — integrity, duplicate, missing, invalid."""

    def test_duplicate_rows(self):
        rows = [{"id": 1}, {"id": 1}, {"id": 2}]
        assert detect_duplicates(rows, key="id") == 1

    def test_integrity_violated(self):
        q = QualityEngine(name="q")
        assert (
            q.integrity_ok({"name": "x", "value": None, "id": 1}, required=("name", "value"))
            is False
        )

    def test_missing_fields_zeroed(self):
        q = QualityEngine(name="q")
        assert q.missing_count({"a": 1, "b": None, "c": 3}) == 1


class TestFreshness:
    """REQ 11.5 — freshness validated against a max age."""

    def test_fresh_record(self):
        assert is_fresh("2026-09-14T10:00:00Z", max_age_s=100, now="2026-09-14T10:01:00Z") is True

    def test_stale_record(self):
        assert is_fresh("2026-09-14T10:00:00Z", max_age_s=30, now="2026-09-14T10:01:00Z") is False


class TestTimestampValidation:
    """REQ 11.13 — timestamps validated for format/sanity."""

    def test_valid_timestamp(self):
        assert is_valid_timestamp("2026-09-14T10:00:00Z") is True

    def test_invalid_timestamp(self):
        assert is_valid_timestamp("not-a-time") is False


class TestAnomalySeverity:
    """REQ 11.10.2 — anomalies carry a severity grade."""

    def test_severity_grading(self):
        assert severity_grade(tol=0.5, deviation=0.2) == "moderate"

    def test_large_deviation_high(self):
        assert severity_grade(tol=0.5, deviation=2.0) == "high"

    def test_mild_deviation_low(self):
        assert severity_grade(tol=0.5, deviation=0.05) == "low"


class TestConfidenceScoring:
    """REQ 11.20/11.20.1 — confidence from pass rate; 11.20.2 thresholds."""

    def test_full_confidence(self):
        assert confidence_score(passed=10, total=10) == 100.0

    def test_partial_confidence(self):
        assert confidence_score(passed=7, total=10) == 70.0

    def test_zero_total_is_zero(self):
        assert confidence_score(passed=0, total=0) == 0.0

    def test_threshold_attained(self):
        assert confidence_score(passed=9, total=10) >= 85.0


class TestInvalidDataHandling:
    """REQ 11.22/11.22.1/11.22.2/11.23/11.24 — reject/quarantine/recover."""

    def test_reject_is_disposition(self):
        assert reject_record("r1", reason="bad-type") == "rejected"

    def test_quarantine_isolates(self):
        assert quarantine_record("r2", reason="suspicious") == "quarantined"

    def test_engine_recovers_quarantined(self):
        q = QualityEngine(name="q")
        q.quarantined["r3"] = {"reason": "anomaly"}
        assert q.recover("r3") is True
        assert q.quarantined == {}

    def test_missing_recovery_record(self):
        q = QualityEngine(name="q")
        assert q.recover("nope") is False


pytestmark = pytest.mark.unit
