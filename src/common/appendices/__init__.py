"""Topic 40 — Appendices.

Maintains conventions, state definitions, classifications,
schemas, references, diagrams and matrices (glossary, traceability,
test matrix, change log) that make the SRS self-contained and
auditable (REQ 40.1-40.30 subset).
"""

from .engine import (
    AppendicesEngine,
    audit_fields_ok,
    diagram_present,
    matrix_complete,
    matrix_mapping_ok,
    requirement_id_valid,
    state_transition_ok,
    traceability_matrix_ok,
)

__all__ = [
    "AppendicesEngine",
    "audit_fields_ok",
    "diagram_present",
    "matrix_complete",
    "requirement_id_valid",
    "state_transition_ok",
    "matrix_mapping_ok",
    "traceability_matrix_ok",
]
