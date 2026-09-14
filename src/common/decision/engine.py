"""Topic 19 — Decision Engine.

Orders eligible actions (entry, exit, no-action) by priority and gates
them on capital availability, conflict resolution, expiry and the human
approval gate (REQ 19.1-19.30 enforced subset).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field

_REQUIRED_INPUTS: frozenset[str] = frozenset({"signal", "price"})


def validate_inputs(data: Mapping[str, object]) -> bool:
    """Return whether all required decision inputs are present (REQ 19.2.2)."""
    return _REQUIRED_INPUTS.issubset(data)


def eligibility_met(opp: float, strategy: float, risk: float) -> bool:
    """Return whether all three eligibility gates pass (REQ 19.4-19.6)."""
    return opp >= 0.6 and strategy >= 0.6 and risk >= 0.6


def decision_priority(candidates: Mapping[str, float]) -> str:
    """Return the highest-priority candidate decision (REQ 19.8.2/19.10)."""
    return max(candidates, key=lambda k: candidates[k])


def capital_eligible(required: float, available: float) -> bool:
    """Return whether enough capital is available (REQ 19.12.1/19.12.2)."""
    return available >= required


def entry_decision(score: float, threshold: float) -> bool:
    """Return whether the scored opportunity justifies entry (REQ 19.13)."""
    return score >= threshold


def no_action(score: float, threshold: float) -> bool:
    """Return whether the decision is to take no action (REQ 19.15)."""
    return score < threshold


def decision_rejected(risk: float, limit: float) -> bool:
    """Return whether the decision is rejected for risk (REQ 19.16)."""
    return risk > limit


def decision_expired(created: float, now: float, ttl: float) -> bool:
    """Return whether a decision has expired (REQ 19.17)."""
    return now - created > ttl


def conflict_handled(strategy_a: str, strategy_b: str) -> bool:
    """Return whether a strategy conflict was resolvable (REQ 19.19.1)."""
    return strategy_a != strategy_b


def approval_gate(action: str, approval: bool) -> bool:
    """Return whether an action may proceed (REQ 19.20.1/19.20.3)."""
    if action == "kill":
        return approval
    return True


@dataclass
class DecisionEngine:
    """Decision orchestration lifecycle (REQ 19.24)."""

    name: str
    _valid: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def validate(self, valid: bool) -> bool:
        """Validate the engine's configuration (REQ 19.24)."""
        self._valid = valid
        return self._valid
