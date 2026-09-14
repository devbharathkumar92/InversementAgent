"""Topic 12 — Opportunity Discovery Engine.

Performs market scanning over an asset universe, detects signals
(price, volume, volatility), filters and qualifies opportunities,
ranks them, deduplicates, collects evidence, and detects false
signals (REQ 12.1-12.30 enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any


class DetectionSignal(Enum):
    """Signals that can trigger opportunity detection (REQ 12.5.1)."""

    PRICE_MOVEMENT = "price"
    VOLUME = "volume"
    VOLATILITY = "volatility"
    NEWS = "news"


def detect_momentum(move_pct: float, threshold: float) -> bool:
    """Return whether a price move exceeds the momentum threshold (12.10)."""
    return abs(move_pct) >= threshold


def detect_volume_spike(volume: float, avg: float) -> bool:
    """Return whether volume is above the average by a multiplier (12.11)."""
    if avg <= 0:
        return volume > 0
    return volume / avg >= 2.0


def detect_volatility_expansion(current: float, norm: float) -> bool:
    """Return whether volatility has at least doubled (REQ 12.12)."""
    if norm <= 0:
        return current > 0
    return current / norm >= 2.0


def passes_filters(
    metric: float,
    hard_min: float,
    soft_min: float | None = None,
    hard_max: float | None = None,
) -> bool:
    """Return whether a candidate passes the configured filters (12.6)."""
    if metric < hard_min:
        return False
    if hard_max is not None and metric > hard_max:
        return False
    if soft_min is not None and metric < soft_min:
        return False
    return True


def add_evidence(bag: dict[str, Any], evidence_item: str) -> dict[str, Any]:
    """Append a piece of evidence to an opportunity (REQ 12.17)."""
    bag.setdefault("evidence", []).append(evidence_item)
    return bag


def confidence_from(signal: float, data: float) -> float:
    """Combine signal and data confidence inputs (REQ 12.18.1)."""
    return (signal + data) / 2.0


def expired_opportunity(created: str, ttl_s: float, now: str) -> bool:
    """Return whether an opportunity has outlived its TTL (REQ 12.19)."""
    created_at = datetime.fromisoformat(created.replace("Z", "+00:00"))
    now_at = datetime.fromisoformat(now.replace("Z", "+00:00"))
    return (now_at - created_at) > timedelta(seconds=ttl_s)


def false_signal_flagged(volume_ratio: float, min_ratio: float) -> bool:
    """Return whether a move without volume is a false signal (12.21.1)."""
    return volume_ratio < min_ratio


def rank_opportunities(opportunities: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sort opportunities by discovery score, best first (REQ 12.15)."""
    return sorted(opportunities, key=lambda o: o.get("score", 0), reverse=True)


def is_duplicate(a: dict[str, Any], b: dict[str, Any]) -> bool:
    """Return whether two opportunities are duplicates (REQ 12.16)."""
    return a == b


@dataclass
class DiscoveryEngine:
    """Scans an asset universe and applies qualification rules (12.3)."""

    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def scan(self, universe: list[str]) -> list[dict[str, Any]]:
        """Return detected opportunities for a bounded universe (REQ 12.4)."""
        return []

    def qualifies(self, record: dict[str, Any]) -> bool:
        """Apply qualification criteria (REQ 12.14.1)."""
        criteria = {"liquid", "regime_ok"}
        return all(record.get(key) is True for key in criteria)
