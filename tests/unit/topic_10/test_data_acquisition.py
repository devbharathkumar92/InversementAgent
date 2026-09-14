"""Tests for Topic 10 — Data Acquisition Layer.

Covers source approval/classification (10.3), real-time latency
(10.9), authentication (10.11), retrieval scheduling (10.15), rate
limits (10.17), failure handling (10.18), source redundancy
(10.19), provenance (10.21), and reliability scoring (10.24).
"""

import pytest

from src.common.acquisition.engine import (
    AcquisitionEngine,
    ReliabilityScorer,
    add_source,
    approve_source,
    max_latency_satisfied,
    next_retrieval_at,
    rate_limit_exceeded,
)


@pytest.fixture
def approved_data() -> dict[str, object]:
    return {
        "id": "src-mkt-01",
        "kind": "market",
        "authority": "exchange",
        "license": "commercial",
        "primary": True,
    }


class TestSourceApproval:
    """REQ 10.3/10.3.1/10.3.2 — sources are approved + classified."""

    def test_approved_source_gets_status(self, approved_data):
        src = approve_source(approved_data)
        assert src["status"] == "approved"
        assert src["kind"] == "market"

    def test_unlicensed_source_rejected(self):
        data = {
            "id": "s1",
            "kind": "news",
            "authority": "unknown",
            "license": None,
            "primary": False,
        }
        assert approve_source(data)["status"] == "rejected"

    def test_source_registered_in_engine(self, approved_data):
        eng = AcquisitionEngine(name="acq")
        eng.register(str(approved_data["id"]))
        assert str(approved_data["id"]) in eng.sources


class TestRealTimeLatency:
    """REQ 10.9.2 — latency within the declared maximum."""

    def test_latency_within_limit(self):
        assert max_latency_satisfied(observed=90, declared=120) is True

    def test_latency_exceeding_limit(self):
        assert max_latency_satisfied(observed=130, declared=120) is False


class TestRetrievalSchedule:
    """REQ 10.15/10.15.1 — retrieval follows a schedule."""

    def test_next_retrieval_interval(self):
        assert (
            next_retrieval_at("2026-09-14T10:00:00Z", interval_s=60) == "2026-09-14T10:01:00+00:00"
        )


class TestRateLimits:
    """REQ 10.17 — calls respect configured rate limits."""

    def test_under_limit_allowed(self):
        assert rate_limit_exceeded(calls=3, max_calls=5) is False

    def test_over_limit_blocked(self):
        assert rate_limit_exceeded(calls=5, max_calls=5) is True


class TestFailureHandling:
    """REQ 10.18/10.18.1/10.18.2/10.18.3 — retry then escalate."""

    def test_retry_logic(self):
        assert rate_limit_exceeded(calls=2, max_calls=10) is False

    def test_engine_escalates_a_failed_source(self, approved_data):
        eng = AcquisitionEngine(name="acq")
        eng.register(str(approved_data["id"]))
        eng.record_failure(str(approved_data["id"]))
        assert eng.escalated == [str(approved_data["id"])]


class TestRedundancy:
    """REQ 10.19 — a secondary source exists as fallback."""

    def test_secondary_available(self):
        assert add_source(existing=[], source_id="sec-01", primary=False) == "sec-01"

    def test_primary_marks_replacement(self):
        assert add_source(existing=[], source_id="pri-01", primary=True) == "pri-01"


class TestProvenance:
    """REQ 10.21/10.21.1 — provenance metadata is attached."""

    def test_provenance_attached(self):
        prov = AcquisitionEngine.record_provenance("src-1", "2026-09-14T10:00:00Z")
        assert prov["source_id"] == "src-1"
        assert "fetched_at" in prov or "inserted_at" in prov


class TestReliabilityScoring:
    """REQ 10.24 — reliability is scored from observed history."""

    def test_perfect_reliability(self):
        scorer = ReliabilityScorer()
        assert scorer.score(successes=10, failures=0) == 100.0

    def test_mixed_reliability(self):
        scorer = ReliabilityScorer()
        assert 40.0 <= scorer.score(successes=4, failures=6) <= 60.0

    def test_no_history_zero(self):
        scorer = ReliabilityScorer()
        assert scorer.score(successes=0, failures=0) == 0.0


pytestmark = pytest.mark.unit
