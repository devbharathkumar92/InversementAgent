"""Topic 13 — Market Analysis Engine.

Provides market context analysis primitives: trend direction, price
momentum, technical indicators, news relevance and impact, sentiment,
conflicting-signal detection and resolution, confidence assessment,
and market regime classification/transition (REQ 13.1-13.30 enforced
subset).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def trend_direction(prices: list[float]) -> str:
    """Classify a price series as up/down/sideways (REQ 13.3)."""
    if len(prices) < 2:
        return "sideways"
    start = prices[0]
    end = prices[-1]
    mid = prices[len(prices) // 2]
    if end > start and mid > start:
        return "up"
    if end < start and mid < start:
        return "down"
    return "sideways"


def momentum_is_up(now: float, prior: float) -> bool:
    """Return whether price is moving up vs the prior reference (13.4)."""
    return now > prior


def news_relevant(topics: list[str], tags: dict[str, bool]) -> bool:
    """Return whether news topics match relevance tags (REQ 13.10.1)."""
    return any(tags.get(topic, False) for topic in topics)


def analyze_news_impact(negative: int, positive: int) -> str:
    """Classify news impact as negative/positive/neutral (REQ 13.10.2)."""
    if negative > positive:
        return "negative"
    if positive > negative:
        return "positive"
    return "neutral"


def sentiment_from(score: float, confidence: float) -> str:
    """Classify sentiment from a signed score (REQ 13.11)."""
    if score > 0.2:
        return "positive"
    if score < -0.2:
        return "negative"
    return "neutral"


def conflict_flagged(bullish: bool, bearish: bool) -> bool:
    """Return whether bullish and bearish signals conflict (13.17.1)."""
    return bullish and bearish


def resolve_conflict(bull: float, bear: float) -> str:
    """Resolve a conflict by signal strength (REQ 13.17.2)."""
    if bull >= bear:
        return "bull"
    return "bear"


def confidence_assessed(agreement: int, total: int, threshold: float) -> float:
    """Return agreement-based confidence; caller compares to threshold."""
    if total <= 0:
        return 0.0
    return agreement / total


def detect_regime(momentum: float, volatility: float) -> str:
    """Classify the market regime from momentum and volatility (13.19.1)."""
    if volatility >= 0.5:
        return "chop"
    if momentum >= 0:
        return "bull"
    return "bear"


def transition_to(current: str, signal: str) -> bool:
    """Return whether a regime transition is warranted (REQ 13.19.2)."""
    return current != signal


@dataclass
class MarketAnalysisEngine:
    """Holds shared analysis state for a named market context (13.2)."""

    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def above_sma(self, price: float, sma: float) -> bool:
        """Return whether price is above its moving average (REQ 13.8)."""
        return price > sma

    def analyze(self, context: dict[str, Any]) -> dict[str, Any]:
        """Run a lightweight context analysis (REQ 13.2)."""
        return {"regime": detect_regime(context.get("momentum", 0), context.get("volatility", 0))}
