"""Tests for Topic 1.7/1.8/1.10/1.11/1.12 — History, Integrity, Review, Baseline, Audit."""

import pytest

from src.common.document_control.audit import AuditEvent, AuditLog
from src.common.document_control.baseline import (
    Baseline,
    BaselineLockError,
    InvalidBaselineError,
)
from src.common.document_control.integrity import content_hash
from src.common.document_control.review import ReviewCycle, ReviewOutcome


class TestIntegrity:
    """REQ 1.8 — detect unauthorized modification via content hash."""

    def test_hash_stable_for_same_content(self):
        assert content_hash(b"same content") == content_hash(b"same content")

    def test_hash_differs_for_different_content(self):
        assert content_hash(b"abc") != content_hash(b"abd")

    def test_hash_is_hex_string(self):
        value = content_hash(b"abc")
        assert isinstance(value, str)
        assert len(value) == 64  # sha256


class TestAudit:
    """REQ 1.12 — structured, machine-readable audit events."""

    def test_audit_event_records_fields(self):
        event = AuditEvent(
            action="DOCUMENT_CREATED",
            actor="srs-governance",
            object_id="SRST1BL001",
            result="ok",
        )
        assert event.action == "DOCUMENT_CREATED"
        assert event.actor == "srs-governance"
        assert event.object_id == "SRST1BL001"
        assert event.result == "ok"
        assert event.timestamp is not None

    def test_audit_log_orders_events_and_is_queryable(self):
        log = AuditLog()
        log.record(action="CREATE", actor="a", object_id="obj-1")
        log.record(action="UPDATE", actor="a", object_id="obj-1")
        assert len(list(log.events())) == 2
        assert log.events()[0].action == "CREATE"

    def test_audit_log_requires_action(self):
        log = AuditLog()
        with pytest.raises(ValueError):
            log.record(action="", actor="a", object_id="obj-1")


class TestBaseline:
    """REQ 1.11/1.11.1/1.11.2/1.11.3 — baseline creation, lock, modification."""

    def test_create_baseline_from_approved_version(self):
        bl = Baseline.create(
            version="1.0.0",
            integrity_hash=content_hash(b"content"),
            approved_by="project-governance",
        )
        assert bl.version == "1.0.0"
        assert bl.locked is True

    def test_cannot_create_baseline_without_approval_hash(self):
        with pytest.raises(InvalidBaselineError):
            Baseline.create(version="1.0.0", integrity_hash="", approved_by="srs-writer")

    def test_locked_baseline_rejects_direct_write(self):
        bl = Baseline.create("1.0.0", content_hash(b"c"), "project-governance")
        with pytest.raises(BaselineLockError):
            bl.modify(b"new content")

    def test_baseline_modification_via_controlled_workflow_preserves_old(self):
        bl = Baseline.create("1.0.0", content_hash(b"old"), "project-governance")
        new_bl = bl.create_controlled_replacement(
            new_content=b"new",
            approved_by="project-governance",
        )
        assert new_bl.version == "1.1.0"
        assert bl.version == "1.0.0"  # old baseline preserved


class TestReviewCycle:
    """REQ 1.10 — scheduled + event-triggered review."""

    def test_review_triggered_by_event(self):
        rc = ReviewCycle(
            cadence_days=90,
            event_conditions={"major_change": True, "validation_failure": True},
        )
        assert rc.should_trigger(event={"validation_failure": True})
        assert not rc.should_trigger(event={})

    def test_review_outcome_recorded(self):
        rc = ReviewCycle(cadence_days=90, event_conditions={})
        outcome = rc.record_outcome("change_required")
        assert outcome == ReviewOutcome.CHANGE_REQUIRED


pytestmark = pytest.mark.unit
