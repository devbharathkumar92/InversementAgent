"""Topic 19 — Decision Engine.

Aggregates opportunity, strategy and risk eligibility into an ordered,
prioritized action: entry, exit, or no-action, gated by capital
availability, conflict resolution, expiry and human approval.
"""

from .engine import (
    DecisionEngine,
    approval_gate,
    capital_eligible,
    conflict_handled,
    decision_expired,
    decision_priority,
    decision_rejected,
    eligibility_met,
    entry_decision,
    no_action,
    validate_inputs,
)

__all__ = [
    "DecisionEngine",
    "approval_gate",
    "capital_eligible",
    "conflict_handled",
    "decision_expired",
    "decision_priority",
    "decision_rejected",
    "eligibility_met",
    "entry_decision",
    "no_action",
    "validate_inputs",
]
