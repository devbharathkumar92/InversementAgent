"""Topic 14 — Opportunity Scoring Engine.

Scores opportunities on a 0-100 scale across components (return, risk,
risk-reward, probability, etc.), combines them into a weighted
composite, validates its weights, enforces minimum thresholds, ranks
opportunities, and applies time-based score decay (REQ 14.1-14.30
enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# Canonical component names accepted in weight sets (REQ 14.16.1).
SCORE_COMPONENTS = frozenset(
    {
        "return",
        "risk",
        "risk_reward",
        "prob",
        "liquidity",
        "volatility",
        "time",
        "data_confidence",
        "market",
        "news",
        "cost",
        "tax",
        "capital",
    }
)


def weights_valid(weights: dict[str, float]) -> bool:
    """Validate a weight set: known, non-negative, sums to one (14.17.2)."""
    total = 0.0
    for name, weight in weights.items():
        if name not in SCORE_COMPONENTS or weight < 0:
            return False
        total += weight
    return abs(total - 1.0) < 1e-6


def composite_score(components: dict[str, float], weights: dict[str, float]) -> float:
    """Compute the weighted composite score (REQ 14.16.2)."""
    if not weights_valid(weights):
        raise ValueError("weights must be known, non-negative and sum to 1")
    return round(
        sum(components.get(name, 0.0) * weight for name, weight in weights.items()),
        6,
    )


def decayed_score(base: float, decay: float, expiry: float = 0.0) -> float:
    """Apply a proportional decay, zeroing below the expiry floor (14.22)."""
    score = base * (1.0 - decay)
    if expiry > 0 and score <= expiry:
        return 0.0
    return score


@dataclass
class ScoringEngine:
    """Presents the scoring framework for opportunities (REQ 14.2)."""

    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def return_potential_score(self, projected_return: float) -> float:
        """Map projected return to a 0-100 score (REQ 14.3)."""
        return max(0.0, min(100.0, projected_return * 250.0))

    def risk_score(self, risk: float) -> float:
        """Map risk metric (0-1) to a 0-100 score; lower is better (14.4)."""
        return max(0.0, min(100.0, (1.0 - risk) * 100.0))

    def risk_reward_score(self, reward: float, risk: float) -> float:
        """Score risk-reward ratio (REQ 14.5)."""
        if risk <= 0:
            return 100.0
        ratio = reward / risk
        return max(0.0, min(100.0, ratio * 25.0))

    def acceptable(self, score: float, minimum: float) -> bool:
        """Return whether a score clears the minimum (REQ 14.18.1)."""
        return score >= minimum

    def recalculate(self, base: float, new_input: float) -> float:
        """Recalculate a score from fresh inputs (REQ 14.21)."""
        return new_input

    @staticmethod
    def rank(opportunities: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Rank scored opportunities best-to-worst (REQ 14.19)."""
        return sorted(opportunities, key=lambda o: o.get("score", 0), reverse=True)
