"""Topic 13 — Market Analysis Engine.

Trend analysis, technical indicators, news relevance/impact,
sentiment, conflicting-signal detection, confidence assessment, and
market regime detection.
"""

from .engine import (
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

__all__ = [
    "MarketAnalysisEngine",
    "analyze_news_impact",
    "confidence_assessed",
    "conflict_flagged",
    "detect_regime",
    "momentum_is_up",
    "news_relevant",
    "resolve_conflict",
    "sentiment_from",
    "transition_to",
    "trend_direction",
]
