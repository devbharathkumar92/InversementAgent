"""Tests for Topic 24 — Error Detection and Recovery.

Covers error classification (24.2), detection (24.14), automatic
recovery (24.16), retry policies (24.17), fallback mechanisms (24.18),
safe-state transitions (24.19), task restore (24.20/24.21/24.22) and
error evidence collection (24.25/24.26).
"""

import pytest

from src.common.recovery.engine import (
    RecoveryEngine,
    auto_recoverable,
    classify_error,
    evidence_collected,
    fallback_available,
    retry_condition_allowed,
    retry_exhausted,
    safe_transition,
    severity_action_mapped,
    task_restart_allowed,
    task_rollback_allowed,
)


class TestErrorClassification:
    """REQ 24.2/24.2.1/24.2.2/24.15.2."""

    def test_classify_error(self):
        assert classify_error(kind="network") == "transient"

    def test_classify_unknown_secure(self):
        assert classify_error(kind="alien") == "critical"

    def test_severity_action_mapped(self):
        assert severity_action_mapped(severity=2) == "retry"


class TestRecovery:
    """REQ 24.14/24.16/24.17/24.18/24.19/24.21."""

    def test_auto_recoverable(self):
        assert auto_recoverable(kind="network") is True

    def test_non_recoverable(self):
        assert auto_recoverable(kind="logic") is False

    def test_retry_condition_allowed(self):
        assert retry_condition_allowed(kind="api") is True

    def test_retry_exhausted(self):
        assert retry_exhausted(attempts=3, limit=3) is True

    def test_fallback_available(self):
        assert fallback_available(kind="api", alternate=True) is True

    def test_fallback_unavailable(self):
        assert fallback_available(kind="api", alternate=False) is False

    def test_safe_transition(self):
        assert safe_transition(safe=True) is True

    def test_task_rollback_allowed(self):
        assert task_rollback_allowed(persisted=True) is True

    def test_task_restart_allowed(self):
        assert task_restart_allowed(idempotent=True) is True


class TestEngine:
    """REQ 24.1 — recovery lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            RecoveryEngine(name=" ")

    def test_evidence_collected(self):
        assert evidence_collected(error_id="e1", saved=True) is True

    def test_engine_status(self):
        assert RecoveryEngine(name="r").status() == "armed"


pytestmark = pytest.mark.unit
