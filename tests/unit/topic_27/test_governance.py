"""Tests for Topic 27 — SRS Version Control and Governance.

Covers version numbering (27.5), baselining and locking
(27.6/27.7), change requests and proposals (27.8/27.9), impact
analysis and approval (27.10/27.11), document integrity and
validation (27.17/27.19/27.20), and the approval workflow and release
management (27.26/27.28).
"""

import pytest

from src.common.governance.engine import (
    GovernanceEngine,
    approval_allowed,
    change_justified,
    change_requires_approval,
    documented_after_change,
    emergency_approval,
    impact_risk_assessed,
    release_validated,
    srs_authority,
    srs_consistent,
    srs_integrity_ok,
    version_format_valid,
    version_increment_valid,
)


class TestVersioning:
    """REQ 27.5/27.5.1/27.5.2/27.16."""

    def test_version_format_valid(self):
        assert version_format_valid("1.2.3") is True

    def test_version_format_invalid(self):
        assert version_format_valid("v1") is False

    def test_version_increment_valid(self):
        assert version_increment_valid(old="1.2.3", new="1.2.4") is True

    def test_version_downgrade_invalid(self):
        assert version_increment_valid(old="1.2.4", new="1.2.3") is False

    def test_version_logged(self):
        assert documented_after_change(logged=True) is True


class TestChangeControl:
    """REQ 27.8/27.9.2/27.10/27.11/27.13.2."""

    def test_change_justified(self):
        assert change_justified(reason=True, impact=True) is True

    def test_unjustified_change(self):
        assert change_justified(reason=False, impact=True) is False

    def test_impact_risk_assessed(self):
        assert impact_risk_assessed(areas=True, risk=True) is True

    def test_approval_allowed(self):
        assert approval_allowed(authority=True, state="draft") is True

    def test_change_requires_approval(self):
        assert change_requires_approval(major=True) is True

    def test_emergency_approval(self):
        assert emergency_approval(criteria=True, authority=True) is True


class TestDocumentGovernance:
    """REQ 27.3/27.17/27.19/27.20/27.28.2."""

    def test_srs_authority(self):
        assert srs_authority(owner="SRS-owner") == "SRS-owner"

    def test_srs_integrity_ok(self):
        assert srs_integrity_ok(checksum_match=True) is True

    def test_tampered_document(self):
        assert srs_integrity_ok(checksum_match=False) is False

    def test_srs_consistent(self):
        assert srs_consistent(cross_refs=True, headings=True) is True

    def test_inconsistency_detected(self):
        assert srs_consistent(cross_refs=False, headings=True) is False

    def test_release_validated(self):
        assert release_validated(prepared=True, tested=True) is True


class TestEngine:
    """REQ 27.1 — governance lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            GovernanceEngine(name=" ")

    def test_engine_status(self):
        assert GovernanceEngine(name="g").status() == "governed"


pytestmark = pytest.mark.unit
