"""Topic 8 — Agent Determinism and Specification Completeness.

Deterministic services for agents: forbidden-assumption enforcement,
ambiguity detection/resolution, rule priority, undefined-state safe
behaviour, escalation state, and self-verification (REQ 8.1/8.7.2/
8.16-8.21/8.26).
"""

from .engine import (
    AmbiguityDetector,
    DeterminismEngine,
    detect_ambiguity,
    determine_rule_priority,
    safe_behaviour_for,
)

__all__ = [
    "AmbiguityDetector",
    "DeterminismEngine",
    "detect_ambiguity",
    "determine_rule_priority",
    "safe_behaviour_for",
]
