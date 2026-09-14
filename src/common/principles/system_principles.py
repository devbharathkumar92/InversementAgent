"""Topic 5 — System Principles and Non-Negotiable Rules.

Principles are controlled and non-negotiable. The enforcement model
rejects actions that violate declared rules, requires human approval for
all high-impact actions (approval by default), and locks baselines
against uncontrolled modification (REQ 5.30/5.33).
"""

from __future__ import annotations

from dataclasses import dataclass, field

BASELINE_PREFIX = "baseline-"


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


@dataclass
class ApprovalGate:
    """Record of a human approval (REQ 5.8/5.27.3)."""

    action: str
    approved_by: str
    approved: bool = True

    def __post_init__(self) -> None:
        _require_non_empty(self.action, "action")
        _require_non_empty(self.approved_by, "approved_by")


@dataclass
class ChangeProposal:
    """A proposed change to a rule or baseline (REQ 5.27/5.27.1/5.27.3)."""

    rule_id: str
    change: str
    approved: bool = False
    evidence: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        _require_non_empty(self.rule_id, "rule_id")
        _require_non_empty(self.change, "change")

    def approve(self, approved_by: str) -> None:
        """Record governance approval of this change proposal."""
        _require_non_empty(approved_by, "approved_by")
        self.approved = True
        self.evidence.append(f"approved-by:{approved_by}")


@dataclass
class PrincipleRegistry:
    """Maps principle/rule names to SRS requirement IDs (5.x)."""

    @staticmethod
    def rule_id(rule_name: str) -> str:
        """Build a deterministic traceability ID for a rule."""
        return f"5.29.rule.{rule_name}"


@dataclass
class SystemPrinciples:
    """The controlled principle set of the system (REQ 5.1/5.2)."""

    name: str = ""
    non_negotiable_rules: list[str] = field(default_factory=list)
    approval_required_actions: list[str] = field(default_factory=list)
    non_approval_actions: list[str] = field(default_factory=list)
    prohibited_self_modifications: list[str] = field(default_factory=list)
    allowed_improvements: list[str] = field(default_factory=list)
    _baselines: set[str] = field(default_factory=set)

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")
        self._baselines = set()

    @staticmethod
    def rule_id(rule_name: str) -> str:
        return PrincipleRegistry.rule_id(rule_name)

    def requires_approval(self, action: str) -> bool:
        """Return whether an action needs human approval (5.8/5.8.1/5.8.2).

        Approval is required by default: only explicitly listed
        non-approval actions are exempt.
        """
        if action in self.non_approval_actions:
            return False
        if action in self.approval_required_actions:
            return True
        return True

    def has_evidence(self, claim: str) -> bool:
        """No-assumption principle: claims need explicit evidence (5.6).

        A claim is evidenced when it cites a concrete data source or an
        explicit ``as of`` timestamp rather than an unsupported prediction.
        """
        lowered = claim.lower()
        has_source = any(marker in lowered for marker in ("source:", "cited from"))
        has_as_of = "as of" in lowered
        predicts_future = any(marker in lowered for marker in ("will", "tomorrow", "predict"))
        return (has_source or has_as_of) and not predicts_future

    def self_modification_allowed(self, modification: str) -> bool:
        """Return whether a self-modification is permitted (5.26.x)."""
        if modification in self.prohibited_self_modifications:
            return False
        return modification in self.allowed_improvements

    def record_baseline(self, baseline_id: str) -> str:
        """Record a created baseline and lock it (5.33.1/5.33.2)."""
        _require_non_empty(baseline_id, "baseline_id")
        self._baselines.add(baseline_id)
        return baseline_id

    def baseline_locked(self, baseline_id: str) -> bool:
        """Return whether a baseline is currently locked."""
        return baseline_id in self._baselines or is_locked_baseline(baseline_id)


def is_locked_baseline(baseline_id: str) -> bool:
    """Return whether a baseline id matches the locked-naming convention."""
    return baseline_id.startswith(BASELINE_PREFIX)


def detect_rule_violations(principles: SystemPrinciples, actions: list[str]) -> list[str]:
    """Return the subset of actions that violate non-negotiable rules (5.29)."""
    return [a for a in actions if a in principles.non_negotiable_rules]


class RuleEnforcer:
    """Enforces non-negotiable rules at the action boundary (REQ 5.30)."""

    def __init__(self, principles: SystemPrinciples) -> None:
        self.principles = principles

    def enforce(self, action: str) -> None:
        """Raise if the action violates a non-negotiable rule."""
        if action in self.principles.non_negotiable_rules:
            raise ValueError(f"action violates non-negotiable rule: {action}")
        if self.principles.requires_approval(action):
            raise ValueError(f"action requires human approval: {action}")
