"""Topic 8 — Agent Determinism and Specification Completeness.

Implements deterministic, explainable controls so agents never invent
missing requirements, never rely on forbidden assumptions, resolve
ambiguity against an explicit reference, apply rules in declared
priority order, fall back to a safe behaviour on undefined states, and
self-verify before continuing (REQ 8.1/8.7/8.16-8.21/8.26).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Vague / non-deterministic phrases that should trigger clarification.
_DEFAULT_AMBIGUITY_TRIGGERS = (
    "approximately",
    "around",
    "about",
    "quickly",
    "soon",
    "as soon as possible",
    "some",
)


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


def detect_ambiguity(text: str) -> bool:
    """Return whether an instruction contains ambiguous phrasing (8.18.1)."""
    lowered = text.lower()
    return any(trigger in lowered for trigger in _DEFAULT_AMBIGUITY_TRIGGERS)


def determine_rule_priority(rules: list[dict[str, Any]]) -> str:
    """Return the rule id that takes priority.

    Higher ``priority`` number wins; ties break on lexicographically
    smallest rule id for deterministic ordering (REQ 8.7.2).
    """
    if not rules:
        raise ValueError("no rules supplied")
    ordered = sorted(
        rules,
        key=lambda r: (int(r["priority"]), tuple(-ord(c) for c in str(r["id"]))),
        reverse=True,
    )
    return str(ordered[0]["id"])


def safe_behaviour_for(state: str) -> str:
    """Return the safe behaviour for an undefined/unknown state (8.20.2)."""
    known = {"RUNNING": "continue-monitored", "INIT": "continue-monitored"}
    return known.get(state, "blocked")


@dataclass
class AmbiguityDetector:
    """Detector with configurable trigger phrases (REQ 8.18.1)."""

    triggers: list[str] = field(default_factory=lambda: list(_DEFAULT_AMBIGUITY_TRIGGERS))

    def detect(self, text: str) -> bool:
        lowered = text.lower()
        return any(t.lower() in lowered for t in self.triggers)

    def resolve(self, text: str, reference: str) -> str:
        """Resolve ambiguity against an explicit reference (8.18.2)."""
        if self.detect(text):
            return "use-reference" if reference.strip() else "escalate"
        return "as-specified"


@dataclass
class DeterminismEngine:
    """Central determinism control (REQ 8.1).

    Holds the forbidden-assumption list, the ordered decision rules, the
    escalation states, and whether agent self-verification is required
    (REQ 8.17.1/8.7/8.21.2/8.26).
    """

    name: str = ""
    forbidden_assumptions: list[str] = field(default_factory=list)
    rules: list[dict[str, Any]] = field(default_factory=list)
    escalation_states: set[str] = field(default_factory=set)
    _self_verification_required: bool = False

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")

    def assumption_forbidden(self, assumption: str) -> bool:
        """Return whether an assumption is on the forbidden list (8.17.1)."""
        return assumption in self.forbidden_assumptions

    def has_supporting_evidence(self, instruction: str) -> bool:
        """Return whether an instruction carries supporting evidence (8.17)."""
        return bool(instruction.strip()) and not detect_ambiguity(instruction)

    def is_escalation_state(self, state: str) -> bool:
        return state in self.escalation_states

    def self_verification_required(self) -> bool:
        return self._self_verification_required
