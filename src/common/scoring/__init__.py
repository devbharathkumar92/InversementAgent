"""Topic 14 — Opportunity Scoring Engine.

Component scores, weighted composite scoring, weight validation, score
thresholds, ranking, recalculation, and score decay.
"""

from .engine import (
    ScoringEngine,
    composite_score,
    decayed_score,
    weights_valid,
)

__all__ = [
    "ScoringEngine",
    "composite_score",
    "decayed_score",
    "weights_valid",
]
