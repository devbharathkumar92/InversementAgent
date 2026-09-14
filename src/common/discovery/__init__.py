"""Topic 12 — Opportunity Discovery Engine.

Market scanning, detection signals, filtering, qualification, ranking,
deduplication, evidence collection, confidence, expiry, and false-signal
detection.
"""

from .engine import (
    DetectionSignal,
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

__all__ = [
    "DetectionSignal",
    "DiscoveryEngine",
    "add_evidence",
    "confidence_from",
    "detect_momentum",
    "detect_volatility_expansion",
    "detect_volume_spike",
    "expired_opportunity",
    "false_signal_flagged",
    "is_duplicate",
    "passes_filters",
    "rank_opportunities",
]
