"""Tests for Topic 38 — PoV Release Criteria.

Covers functional release criteria (38.2), safety conditions
(38.7), paper-trading requirements (38.9), monitoring/test
criteria (38.10/38.18), blocking conditions (38.25), readiness
assessment (38.26) and the final PoV release decision (38.29).
"""

import pytest

from src.common.povrelease.engine import (
    PovReleaseEngine,
    blocking_free,
    coverage_met,
    final_validation,
    functional_required,
    human_approved,
    monitoring_ok,
    paper_trading_ok,
    readiness_gate,
    release_approved,
    safety_met,
)


class TestCriteria:
    """REQ 38.2.1/38.2.2/38.7.1/38.7.2/38.9.1/38.9.2."""

    def test_functional_required(self):
        assert functional_required(minimums=True, blockers=False) is True

    def test_functional_blocked(self):
        assert functional_required(minimums=True, blockers=True) is False

    def test_safety_met(self):
        assert safety_met(conditions=True, failures=False) is True

    def test_safety_violation(self):
        assert safety_met(conditions=True, failures=True) is False

    def test_paper_trading_ok(self):
        assert paper_trading_ok(requirements=True, failures=False) is True

    def test_paper_trading_failure(self):
        assert paper_trading_ok(requirements=True, failures=True) is False

    def test_coverage_met(self):
        assert coverage_met(coverage=True) is True


class TestReadiness:
    """REQ 38.10/38.25.1/38.25.2/38.26.1/38.26.2."""

    def test_monitoring_ok(self):
        assert monitoring_ok(enabled=True) is True

    def test_blocking_free(self):
        assert blocking_free(blockers=0) is True

    def test_blocker_present(self):
        assert blocking_free(blockers=1) is False

    def test_readiness_gate_passed(self):
        assert readiness_gate(checklist=True, score=0.95) is True

    def test_readiness_gate_low_score(self):
        assert readiness_gate(checklist=True, score=0.75) is False


class TestDecision:
    """REQ 38.27/38.28/38.29.1/38.29.2."""

    def test_final_validated(self):
        assert final_validation(valid=True) is True

    def test_human_approved(self):
        assert human_approved(approved=True) is True

    def test_release_approved(self):
        assert release_approved(validated=True, score=0.95, blockers=0) is True

    def test_release_rejected(self):
        assert release_approved(validated=True, score=0.95, blockers=1) is False


class TestEngine:
    """REQ 38.1 — PoV release lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            PovReleaseEngine(name=" ")

    def test_engine_status(self):
        assert PovReleaseEngine(name="p").status() == "assessed"


pytestmark = pytest.mark.unit
