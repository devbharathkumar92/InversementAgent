"""Tests for Topic 1.5/1.5.1/1.5.2/1.5.3 — Change Control workflow."""

import pytest

from src.common.document_control.change_control import (
    APPROVAL_AUTHORITIES,
    ChangeImpactAssessment,
    ChangeRequest,
    InvalidTransitionError,
    UnauthorizedApprovalError,
    approve_change,
    assess_impact,
    reject_change,
)


class TestChangeRequest:
    """REQ 1.5.1 — structured, uniquely identifiable change request."""

    def test_create_change_request(self):
        req = ChangeRequest("CR-001", "Fix document typo")
        assert req.change_id == "CR-001"
        assert req.summary == "Fix document typo"
        assert req.state == "SUBMITTED"
        assert req.impact is None
        assert req.approval_state is None

    def test_change_requires_non_empty_fields(self):
        with pytest.raises(ValueError):
            ChangeRequest("", "summary")
        with pytest.raises(ValueError):
            ChangeRequest("CR-002", "")


class TestImpactAssessment:
    """REQ 1.5.2 — recorded impact assessment before approval."""

    def test_assess_impact_records_affected_artifacts(self):
        req = ChangeRequest("CR-003", "Amend scope")
        assess_impact(req, affected=["SRS.md", "docs/ARCHITECTURE.md"], risks=["scope"])
        assert req.impact is not None
        assert isinstance(req.impact, ChangeImpactAssessment)
        assert "SRS.md" in req.impact.affected_artifacts
        assert "scope" in req.impact.risks

    def test_assess_impact_requires_request_submitted(self):
        req = ChangeRequest("CR-004", "x", state="APPROVED")
        with pytest.raises(InvalidTransitionError):
            assess_impact(req, affected=[], risks=[])


class TestChangeApproval:
    """REQ 1.5.3/1.6 — approval requires authority and prior assessment."""

    def test_approval_after_assessment_by_authority(self):
        req = ChangeRequest("CR-005", "Change baseline")
        assess_impact(req, affected=["SRS.md"], risks=[])
        approve_change(req, by="project-governance")
        assert req.approval_state == "APPROVED"

    def test_approval_rejected_without_impact_assessment(self):
        req = ChangeRequest("CR-006", "Change baseline")
        with pytest.raises(InvalidTransitionError, match="impact assessment"):
            approve_change(req, by="project-governance")

    def test_approval_rejects_unauthorized_actor(self):
        req = ChangeRequest("CR-007", "Change baseline")
        assess_impact(req, affected=["SRS.md"], risks=[])
        with pytest.raises(UnauthorizedApprovalError):
            approve_change(req, by="srs-writer")

    def test_rejection_records_approval_state_rejected(self):
        req = ChangeRequest("CR-008", "x")
        assess_impact(req, affected=[], risks=[])
        reject_change(req, by="project-governance")
        assert req.approval_state == "REJECTED"


class TestApprovalAuthorities:
    """REQ 1.6.1 — designated approval authority set is non-empty."""

    def test_approved_authorities_defined(self):
        assert "project-governance" in APPROVAL_AUTHORITIES
        assert "srs-writer" not in APPROVAL_AUTHORITIES


pytestmark = pytest.mark.unit
