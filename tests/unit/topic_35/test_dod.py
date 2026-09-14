"""Tests for Topic 35 — Definition of Done.

Covers requirement completion (35.2), code and test completion
(35.5/35.6), deployment readiness (35.24), human and release
approval (35.25/35.26) and final validation/approval (35.27).
"""

import pytest

from src.common.dod.engine import (
    DoDEngine,
    code_complete,
    deployment_ready,
    final_approved,
    final_validation,
    human_approved,
    release_approved,
    requirement_complete,
    suite_green,
    traceability_complete,
)


class TestCompletion:
    """REQ 35.2.1/35.2.2/35.5.1/35.6.1/35.6.2/35.18."""

    def test_requirement_complete(self):
        assert requirement_complete(status="done", evidence=True) is True

    def test_requirement_no_evidence(self):
        assert requirement_complete(status="done", evidence=False) is False

    def test_code_complete(self):
        assert code_complete(complete=True, reviewed=True) is True

    def test_code_not_reviewed(self):
        assert code_complete(complete=True, reviewed=False) is False

    def test_suite_green(self):
        assert suite_green(executed=True, passed=True) is True

    def test_tests_failed(self):
        assert suite_green(executed=True, passed=False) is False

    def test_traceability_complete(self):
        assert traceability_complete(linked=True) is True


class TestApproval:
    """REQ 35.24.1/35.24.2/35.25/35.26/35.27.1/35.27.2."""

    def test_deployment_ready(self):
        assert deployment_ready(checklist=True, blockers=0) is True

    def test_deployment_blocked(self):
        assert deployment_ready(checklist=True, blockers=1) is False

    def test_human_approved(self):
        assert human_approved(approved=True) is True

    def test_release_approved(self):
        assert release_approved(approved=True) is True

    def test_final_validated(self):
        assert final_validation(valid=True) is True

    def test_final_approved(self):
        assert final_approved(valid=True, approved=True) is True

    def test_final_denied(self):
        assert final_approved(valid=True, approved=False) is False


class TestEngine:
    """REQ 35.1 — definition of done lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            DoDEngine(name=" ")

    def test_engine_status(self):
        assert DoDEngine(name="d").status() == "defined"


pytestmark = pytest.mark.unit
