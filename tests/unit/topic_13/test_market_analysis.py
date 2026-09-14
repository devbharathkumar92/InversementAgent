"""Tests for Topic 13 — Market Analysis Engine.

Covers trend analysis (13.3), technical indicators (13.8), news
relevance/impact (13.10), sentiment (13.11), conflicting signal
detection/resolution (13.17), confidence assessment (13.18), and
market regime detection/transition (13.19).
"""

import pytest

from src.common.market.engine import (
    MarketAnalysisEngine,
    analyze_news_impact,
    confidence_assessed,
    conflict_flagged,
    detect_regime,
    momentum_is_up,
    news_relevant,
    resolve_conflict,
    sentiment_from,
    transition_to,
    trend_direction,
)


class TestTrendAnalysis:
    """REQ 13.3 — trend direction from a price series."""

    def test_uptrend(self):
        assert trend_direction([10, 11, 12, 13]) == "up"

    def test_downtrend(self):
        assert trend_direction([13, 11, 10, 9]) == "down"

    def test_sideways(self):
        assert trend_direction([10, 11, 10, 11]) == "sideways"

    def test_momentum_up(self):
        assert momentum_is_up(now=100, prior=95) is True


class TestTechnicalAnalysis:
    """REQ 13.8 — indicators computed from price inputs."""

    def test_above_sma(self):
        eng = MarketAnalysisEngine(name="m")
        assert eng.above_sma(price=105, sma=100) is True

    def test_below_sma(self):
        eng = MarketAnalysisEngine(name="m")
        assert eng.above_sma(price=95, sma=100) is False


class TestNewsImpact:
    """REQ 13.10/13.10.1/13.10.2 — relevance and impact."""

    def test_relevant_news(self):
        assert news_relevant(["earnings"], {"earnings": True}) is True

    def test_irrelevant_news(self):
        assert news_relevant(["weather"], {"earnings": True}) is False

    def test_high_impact(self):
        assert analyze_news_impact(negative=3, positive=0) == "negative"

    def test_neutral_impact(self):
        assert analyze_news_impact(negative=0, positive=0) == "neutral"


class TestSentiment:
    """REQ 13.11/13.11.1 — sentiment from score and confidence."""

    def test_positive_sentiment(self):
        assert sentiment_from(score=0.8, confidence=0.9) == "positive"

    def test_negative_sentiment(self):
        assert sentiment_from(score=-0.6, confidence=0.8) == "negative"

    def test_fairly_neutral(self):
        assert sentiment_from(score=0.05, confidence=0.5) == "neutral"


class TestConflictDetection:
    """REQ 13.17/13.17.1/13.17.2 — conflicting signals resolved."""

    def test_conflict_flagged(self):
        assert conflict_flagged(bullish=True, bearish=True) is True

    def test_no_conflict(self):
        assert conflict_flagged(bullish=True, bearish=False) is False

    def test_resolution_prefers_stronger(self):
        assert resolve_conflict(bull=0.6, bear=0.4) == "bull"


class TestConfidenceAssessment:
    """REQ 13.18.1/13.18.2 — confidence and threshold."""

    def test_confidence_score(self):
        assert confidence_assessed(agreement=9, total=10, threshold=0.7) == 0.9

    def test_below_threshold(self):
        assert confidence_assessed(agreement=5, total=10, threshold=0.7) == 0.5


class TestRegimeDetection:
    """REQ 13.19/13.19.1/13.19.2 — regime classification and transition."""

    def test_bull_regime(self):
        assert detect_regime(momentum=0.5, volatility=0.2) == "bull"

    def test_bear_regime(self):
        assert detect_regime(momentum=-0.5, volatility=0.2) == "bear"

    def test_high_volatility_chop(self):
        assert detect_regime(momentum=0.5, volatility=0.95) == "chop"

    def test_regime_transition(self):
        assert transition_to(current="bull", signal="bear") is True


pytestmark = pytest.mark.unit
