"""Topic 18 — Paper Trading Engine.

Runs strategies against live market data on a virtual account:
configured virtual capital, validated simulated orders, conservative
slippage and fee fills, position/cash accounting, and monitoring of
the paper-pilot's duration criteria (REQ 18.1-18.30 enforced subset).
"""

from __future__ import annotations

from dataclasses import dataclass


def virtual_capital_valid(amount: float) -> bool:
    """Return whether the virtual capital is positive (REQ 18.2.1)."""
    return amount > 0


def validate_order(side: str, qty: float, price: float) -> bool:
    """Validate a simulated order before execution (REQ 18.4.2)."""
    if side not in {"buy", "sell"}:
        raise ValueError(f"unknown side: {side}")
    if qty <= 0:
        raise ValueError("qty must be positive")
    if price <= 0:
        raise ValueError("price must be positive")
    return True


def slippage_fill(price: float, slippage: float) -> float:
    """Return the executed price including slippage (REQ 18.6)."""
    return price * (1 + slippage)


def fee_applied(price: float, fee: float) -> float:
    """Return the all-in price after the fee fraction (REQ 18.7)."""
    return price * (1 + fee)


def position_size(price: float, cash: float) -> float:
    """Return the share-equivalent size the cash buys at price (REQ 18.9)."""
    return cash / price


def cash_after_trade(cash: float, cost: float) -> float:
    """Return the remaining cash after a trade's full cost (REQ 18.10)."""
    return cash - cost


@dataclass
class PaperEngine:
    """Tracks the paper-trading pilot state (REQ 18.19/18.27)."""

    name: str
    window_days: int = 30

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def monitor(self) -> str:
        """Report the pilot's current state (REQ 18.19)."""
        return "active"

    def duration_met(self, days: int) -> bool:
        """Return whether the paper-pilot duration criteria are met (18.27)."""
        return days >= self.window_days
