"""Tests for Topic 23 — Audit Trail and Observability.

Covers event logging (23.2), audit event structure (23.15), event
retention (23.20), and correlation with trace IDs (23.17/23.18),
giving the system an audit-trail backbone.
"""

import pytest

from src.common.audit.engine import (
    AuditEngine,
    AuditEvent,
    capture_event,
    correlation,
    event_required_or_optional,
    retention_allowed,
    secure_deletion,
    trace_eligible,
    trace_id_generated,
)


class TestAuditEvents:
    """REQ 23.2/23.15/23.15.2/23.16/23.20."""

    def test_capture_event_mandatory(self):
        assert capture_event(kind="decision", mandatory=True) is True

    def test_event_required_or_optional(self):
        assert event_required_or_optional(kind="security") == "required"

    def test_secure_deletion(self):
        assert secure_deletion(tampered=False) is True

    def test_retention_allowed(self):
        assert retention_allowed(elapsed_days=365, period_days=730) is True

    def test_retention_denied(self):
        assert retention_allowed(elapsed_days=800, period_days=730) is False


class TestTracing:
    """REQ 23.17/23.18/23.18.1/23.18.2."""

    def test_trace_id_generated(self):
        assert trace_id_generated(span="s1") is True

    def test_correlation(self):
        assert correlation(trace_a="t1", trace_b="t1") is True

    def test_correlation_mismatch(self):
        assert correlation(trace_a="t1", trace_b="t2") is False

    def test_trace_eligibility(self):
        assert trace_eligible(distributed=True, trace_id="abc") is True


class TestAuditEngine:
    """REQ 23.1 — observability lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            AuditEngine(name=" ")

    def test_event_record(self):
        e = AuditEvent(channel="logs")
        assert e.channel == "logs"

    def test_engine_active(self):
        assert AuditEngine(name="a").active is True


def test_capture_event_optional_collects():
    assert capture_event(kind="debug", mandatory=False) is True


pytestmark = pytest.mark.unit
