"""Topic 1.5/1.5.1/1.5.2/1.5.3/1.6/1.6.1/1.6.2 — change control and approval.

The change lifecycle follows the mandated pipeline:

    submit -> assess impact -> approve/reject -> (implement/version/baseline)

Increments only occur after an approved change. Assessment and approval
are separate steps and approval is limited to designated authorities.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

# Designated approval authorities (REQ 1.6.1). "srs-writer" and other
# implementation agents are intentionally excluded from approval power.
APPROVAL_AUTHORITIES: frozenset[str] = frozenset({"project-governance", "human-gate"})


class ChangeWorkflowError(Exception):
    """Base error for the change-control workflow."""


class InvalidTransitionError(ChangeWorkflowError):
    """Raised when the request is not in the expected state for an action."""


class UnauthorizedApprovalError(ChangeWorkflowError):
    """Raised when a non-authority attempts to approve or reject a change."""


@dataclass
class ChangeImpactAssessment:
    """Recorded impact of a proposed change (REQ 1.5.2)."""

    affected_artifacts: Sequence[str]
    risks: Sequence[str] = ()
    disposition: str = "PENDING"


@dataclass
class ChangeRequest:
    """A controlled change proposal (REQ 1.5.1).

    States: ``SUBMITTED`` -> ``ASSESSED`` -> ``APPROVED``/``REJECTED``.
    """

    change_id: str
    summary: str
    impact_class: str = "minor"
    state: str = "SUBMITTED"
    approval_state: str | None = None
    impact: ChangeImpactAssessment | None = None

    def __post_init__(self) -> None:
        if not self.change_id or not self.change_id.strip():
            raise ValueError("Change request requires a non-empty change ID")
        if not self.summary or not self.summary.strip():
            raise ValueError("Change request requires a non-empty summary")
        if self.impact_class not in {"major", "minor", "patch"}:
            raise ValueError(f"Unknown impact class: {self.impact_class}")


def assess_impact(
    request: ChangeRequest,
    affected: Sequence[str],
    risks: Sequence[str] = (),
    disposition: str = "PENDING",
) -> ChangeImpactAssessment:
    """Record a change impact assessment.

    Raises:
        InvalidTransitionError: if the request is not in ``SUBMITTED`` state.
    """
    if request.state != "SUBMITTED":
        raise InvalidTransitionError(
            f"Cannot assess impact in state {request.state!r}; must be SUBMITTED"
        )
    assessment = ChangeImpactAssessment(
        affected_artifacts=list(affected),
        risks=list(risks),
        disposition=disposition,
    )
    request.impact = assessment
    request.state = "ASSESSED"
    return assessment


def _require_authority(actor: str, action: str) -> None:
    if actor not in APPROVAL_AUTHORITIES:
        raise UnauthorizedApprovalError(
            f"Actor {actor!r} is not an approved authority for {action}"
        )


def approve_change(request: ChangeRequest, by: str) -> None:
    """Approve an assessed change request.

    Raises:
        InvalidTransitionError: if the request has not been impact-assessed.
        UnauthorizedApprovalError: if ``by`` is not a designated authority.
    """
    _require_authority(by, "approval")
    if request.impact is None or request.state != "ASSESSED":
        raise InvalidTransitionError("Change must complete an impact assessment before approval")
    request.approval_state = "APPROVED"
    request.state = "APPROVED"


def reject_change(request: ChangeRequest, by: str) -> None:
    """Reject an assessed change request."""
    _require_authority(by, "rejection")
    if request.impact is None or request.state != "ASSESSED":
        raise InvalidTransitionError("Change must complete an impact assessment before rejection")
    request.approval_state = "REJECTED"
    request.state = "REJECTED"
