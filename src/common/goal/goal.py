"""Topic 2.1/2.2/2.3/2.5 — goal, mission, primary objective, scope bounds."""

from __future__ import annotations

from dataclasses import dataclass


class invalid_scope_error(ValueError):
    """Raised when scope parameters are invalid (e.g. blank geography)."""


@dataclass(frozen=True)
class ScopeBounds:
    """The approved geographic/currency/horizon scope (Topic 2.5)."""

    geography: str
    currency: str
    horizon_days: int

    def __post_init__(self) -> None:
        if not self.geography or not self.geography.strip():
            raise invalid_scope_error("geography must be non-empty")
        if not self.currency or not self.currency.strip():
            raise invalid_scope_error("currency must be non-empty")
        if self.horizon_days <= 0:
            raise invalid_scope_error("horizon_days must be positive")


def is_within_scope(
    bounds: ScopeBounds,
    geography: str,
    currency: str,
) -> bool:
    """Return whether an opportunity lies within the approved India/INR scope."""
    if not geography or not geography.strip():
        raise invalid_scope_error("geography must be non-empty")
    if not currency or not currency.strip():
        raise invalid_scope_error("currency must be non-empty")
    return (
        geography.strip() == bounds.geography.strip()
        and currency.strip() == bounds.currency.strip()
    )


@dataclass(frozen=True)
class PrimaryObjective:
    """The measurable, highest-priority objective (Topic 2.3)."""

    statement: str

    def __post_init__(self) -> None:
        if not self.statement or not self.statement.strip():
            raise ValueError("Primary objective statement must be non-empty")


@dataclass(frozen=True)
class Mission:
    """The operational mission translating the goal (Topic 2.2)."""

    statement: str

    def __post_init__(self) -> None:
        if not self.statement or not self.statement.strip():
            raise ValueError("Mission statement must be non-empty")


@dataclass(frozen=True)
class CoreGoal:
    """The single authoritative goal with its mission, objective, and scope."""

    goal_statement: str
    mission_statement: str
    primary_objective: str
    scope: ScopeBounds | None

    def __post_init__(self) -> None:
        if not self.goal_statement or not self.goal_statement.strip():
            raise ValueError("Goal statement must be non-empty")
        if not self.mission_statement or not self.mission_statement.strip():
            raise ValueError("Mission statement must be non-empty")
        if not self.primary_objective or not self.primary_objective.strip():
            raise ValueError("Primary objective must be non-empty")
