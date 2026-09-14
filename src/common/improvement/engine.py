"""Topic 26 — Self-Improvement and Change Management.

Improves the agent only through evidence-backed, risk-assessed,
human-approved changes (26.3/26.5/26.6/26.8/26.13/26.14), deployed
as versions (26.19) without mutating the SRS baseline (26.27).
(REQ 26.1-26.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field

_MIN_ROOT_CAUSE_CONFIDENCE = 0.8


def benefit_possible(improvement: bool, scope: bool) -> bool:
    """Return whether an improvement is worth pursuing (26.3.2)."""
    return improvement and scope


def root_cause_evidence_sufficient(confidence: float) -> bool:
    """Return whether root-cause evidence is sufficient (26.5.2)."""
    return confidence >= _MIN_ROOT_CAUSE_CONFIDENCE


def impact_assessed(functional: bool, risk: bool) -> bool:
    """Return whether impact analysis was completed (26.8)."""
    return functional and risk


def risk_accepted(acceptable: bool, regression_free: bool) -> bool:
    """Return whether change risk is accepted (26.9/26.10)."""
    return acceptable and regression_free


def change_validated(approved: bool, tested: bool) -> bool:
    """Return whether a change passed validation (26.15/26.16)."""
    return approved and tested


def approval_required(srs_change: bool) -> bool:
    """Return whether human approval is required (26.14.1)."""
    return srs_change


def proposal_action(approved: bool, tested: bool) -> str:
    """Return the disposition for a proposal (26.14.2)."""
    if approved and tested:
        return "deploy"
    return "reject"


def change_expected_value_positive(benefit: float, cost: float) -> bool:
    """Return whether expected benefit outweighs cost (26.6.2)."""
    return benefit > cost


def version_created(bumped: bool, tagged: bool) -> bool:
    """Return whether a change version was created (26.19)."""
    return bumped and tagged


def srs_baseline_protected(protected: bool) -> bool:
    """Return whether the SRS baseline is protected (26.27.1)."""
    return protected


@dataclass
class ImprovementEngine:
    """Self-improvement lifecycle (26.1)."""

    name: str
    _active: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._active = True

    def status(self) -> str:
        """Return the improvement engine state."""
        return "active" if self._active else "idle"
