"""Tests for Topic 12 — Opportunity Discovery Engine.

Covers market scanning (12.3), detection signals (12.5), hard/soft
filters (12.6), price/volume/volatility detection (12.10-12.12),
qualification (12.14), ranking (12.15), deduplication (12.16),
evidence (12.17), confidence (12.18), expiry (12.19), and false-signal
detection (12.21).
"""

import pytest

from src.common.discovery.engine import (
    DiscoveryEngine,
    add_evidence,
    confidence_from,
    detect_momentum,
    detect_volatility_expansion,
    detect_volume_spike,
    expired_opportunity,
    false_signal_flagged,
    is_duplicate,
    passes_filters,
    rank_opportunities,
)


class TestMarketScanning:
    """REQ 12.3/12.4 — a bounded asset universe is scanned for signals."""

    def test_scan_yields_zero_opportunities(self):
        eng = DiscoveryEngine(name="d")
        assert eng.scan(universe=["A", "B"]) == []


class TestDetectionSignals:
    """REQ 12.5/12.10 — price momentum/volume/volatility signals."""

    def test_momentum_detected(self):
        assert detect_momentum(move_pct=5.0, threshold=3.0) is True

    def test_no_momentum(self):
        assert detect_momentum(move_pct=1.0, threshold=3.0) is False

    def test_volume_spike(self):
        assert detect_volume_spike(volume=1_000_000, avg=100_000) is True

    def test_volatility_expansion(self):
        assert detect_volatility_expansion(current=0.4, norm=0.2) is True


class TestFilters:
    """REQ 12.6/12.6.1 — hard filters block, soft filters rank."""

    def test_hard_filter_passes(self):
        assert passes_filters(metric=0.9, hard_min=0.5) is True

    def test_hard_filter_blocks(self):
        assert passes_filters(metric=0.3, hard_min=0.5) is False

    def test_soft_filter_holds_metric(self):
        assert passes_filters(metric=0.6, hard_min=0.5, soft_min=0.75) is False


class TestQualification:
    """REQ 12.14/12.14.1 — opportunities must be eligible to proceed."""

    def test_qualifies_when_liquid(self):
        eng = DiscoveryEngine(name="d")
        assert eng.qualifies({"liquid": True, "regime_ok": True}) is True

    def test_illiquid_disqualified(self):
        eng = DiscoveryEngine(name="d")
        assert eng.qualifies({"liquid": False, "regime_ok": True}) is False


class TestRanking:
    """REQ 12.15 — opportunities rank by discovery score descending."""

    def test_ranks_by_score(self):
        ranked = rank_opportunities([{"id": "a", "score": 60}, {"id": "b", "score": 80}])
        assert ranked[0]["id"] == "b"


class TestDeduplication:
    """REQ 12.16 — duplicate signals are collapsed."""

    def test_duplicate_identical_keys(self):
        assert is_duplicate({"asset": "A"}, {"asset": "A"}) is True

    def test_not_duplicate(self):
        assert is_duplicate({"asset": "A"}, {"asset": "B"}) is False


class TestEvidence:
    """REQ 12.17/12.17.1 — opportunities collect supporting evidence."""

    def test_evidence_appended(self):
        bag = add_evidence({"evidence": []}, "news-headline")
        assert bag["evidence"] == ["news-headline"]


class TestConfidence:
    """REQ 12.18.1/12.18.2 — confidence from weighted inputs + threshold."""

    def test_confidences(self):
        assert confidence_from(signal=0.9, data=0.9) == 0.9

    def test_below_threshold(self):
        assert confidence_from(signal=0.3, data=0.3) < 0.5


class TestExpiry:
    """REQ 12.19 — opportunities expire and are handled."""

    def test_active_when_recent(self):
        assert (
            expired_opportunity(
                created="2026-09-14T10:00:00Z", ttl_s=3600, now="2026-09-14T10:30:00Z"
            )
            is False
        )

    def test_expired_when_stale(self):
        assert (
            expired_opportunity(
                created="2026-09-14T10:00:00Z", ttl_s=600, now="2026-09-14T10:30:00Z"
            )
            is True
        )


class TestFalseSignalDetection:
    """REQ 12.21/12.21.1 — false signals are flagged."""

    def test_blip_with_low_volume_flagged(self):
        assert false_signal_flagged(volume_ratio=1.2, min_ratio=2.0) is True

    def test_signal_with_volume_not_flagged(self):
        assert false_signal_flagged(volume_ratio=4.0, min_ratio=2.0) is False


pytestmark = pytest.mark.unit
