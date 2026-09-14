"""Tests for Topic 40 — Appendices.

Covers conventions (40.4-40.8), state definitions (40.9/40.10),
classifications (40.11-40.16), schemas (40.17-40.21), references
(40.22), diagrams (40.23-40.26), matrices (40.27/40.28) and
change log (40.29).
"""

import pytest

from src.common.appendices.engine import (
    AppendicesEngine,
    audit_fields_ok,
    diagram_present,
    matrix_complete,
    matrix_mapping_ok,
    requirement_id_valid,
    state_transition_ok,
    traceability_matrix_ok,
)


class TestConventions:
    """REQ 40.4/40.9.3/40.10.3."""

    def test_requirement_id_valid(self):
        assert requirement_id_valid(convention=True, unique=True) is True

    def test_requirement_id_not_unique(self):
        assert requirement_id_valid(convention=True, unique=False) is False

    def test_state_transition_ok(self):
        assert state_transition_ok(defined=True) is True


class TestSchema:
    """REQ 40.17.1/40.17.2/40.18/40.21."""

    def test_audit_fields_ok(self):
        assert audit_fields_ok(mandatory=True, event_types=True) is True

    def test_audit_event_types_missing(self):
        assert audit_fields_ok(mandatory=True, event_types=False) is False


class TestDiagrams:
    """REQ 40.23/40.24/40.25/40.26."""

    def test_diagram_present(self):
        assert diagram_present(system=True, data_flow=True) is True

    def test_diagram_missing_dataflow(self):
        assert diagram_present(system=True, data_flow=False) is False


class TestMatrices:
    """REQ 40.27/40.28."""

    def test_matrix_mapping_ok(self):
        assert matrix_mapping_ok(mapped=True, evidence=True) is True

    def test_test_evidence_missing(self):
        assert matrix_mapping_ok(mapped=True, evidence=False) is False

    def test_traceability_matrix_ok(self):
        assert traceability_matrix_ok(requirements=True, evidence=True) is True

    def test_traceability_evidence_missing(self):
        assert traceability_matrix_ok(requirements=True, evidence=False) is False

    def test_matrix_complete(self):
        assert matrix_complete(change_log=True, references=True) is True


class TestEngine:
    """REQ 40.1 — appendices lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            AppendicesEngine(name=" ")

    def test_engine_status(self):
        assert AppendicesEngine(name="a").status() == "maintained"


pytestmark = pytest.mark.unit
