"""Topic 18 — Paper Trading Engine.

Virtual capital configuration, simulated order generation/validation,
slippage and fee simulation, position and cash tracking, monitoring,
and paper-pilot duration criteria.
"""

from .engine import (
    PaperEngine,
    cash_after_trade,
    fee_applied,
    position_size,
    slippage_fill,
    validate_order,
    virtual_capital_valid,
)

__all__ = [
    "PaperEngine",
    "cash_after_trade",
    "fee_applied",
    "position_size",
    "slippage_fill",
    "validate_order",
    "virtual_capital_valid",
]
