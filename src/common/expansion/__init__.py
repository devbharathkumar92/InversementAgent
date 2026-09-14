"""Topic 39 — Future Expansion Framework.

Governs scope/market/geographic/asset-class expansion under
preconditions and approval, capital scaling limits, expansion
readiness, approval decision and rollback (REQ 39.1-39.30 subset).
"""

from .engine import (
    ExpansionEngine,
    asset_class_ok,
    capital_scaling_ok,
    expansion_allowed,
    expansion_approved,
    expansion_ready,
    geographic_ok,
    market_ok,
    rollback_available,
)

__all__ = [
    "ExpansionEngine",
    "asset_class_ok",
    "capital_scaling_ok",
    "expansion_allowed",
    "expansion_approved",
    "expansion_ready",
    "geographic_ok",
    "market_ok",
    "rollback_available",
]
