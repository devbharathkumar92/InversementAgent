"""Topic 5 — System Principles and Non-Negotiable Rules.

Implements the controlled principle set: non-negotiable rules, human
approval gates, the no-assumption principle, self-improvement
restrictions, rule-violation detection/enforcement, baseline locking,
and change governance.
"""

from .system_principles import (
    ApprovalGate,
    ChangeProposal,
    PrincipleRegistry,
    RuleEnforcer,
    SystemPrinciples,
    detect_rule_violations,
    is_locked_baseline,
)

__all__ = [
    "SystemPrinciples",
    "ApprovalGate",
    "ChangeProposal",
    "PrincipleRegistry",
    "RuleEnforcer",
    "detect_rule_violations",
    "is_locked_baseline",
]
