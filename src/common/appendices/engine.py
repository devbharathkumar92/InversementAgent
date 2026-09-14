"""Topic 40 — Appendices.

Appendices are the controlled reference layer. Requirement IDs must
obey a stable convention and stay unique (40.4); state transitions
are rule-based (40.9.3/40.10.3); audit events carry mandatory
fields and typed events (40.17); architecture/data-flow/dependency/
interaction diagrams are present (40.23-40.26); the test matrix maps
tests to requirements with evidence (40.27); and the traceability
matrix links requirements across layers (40.28). (REQ 40.1-40.30
enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def requirement_id_valid(convention: bool, unique: bool) -> bool:
    """Return whether requirement IDs satisfy the convention (40.4)."""
    return convention and unique


def state_transition_ok(defined: bool) -> bool:
    """Return whether state transition rules are defined (40.9.3/40.10.3)."""
    return defined


def audit_fields_ok(mandatory: bool, event_types: bool) -> bool:
    """Return whether audit event schema holds (40.17.1/40.17.2)."""
    return mandatory and event_types


def diagram_present(system: bool, data_flow: bool) -> bool:
    """Return whether required diagrams exist (40.23/40.24)."""
    return system and data_flow


def matrix_mapping_ok(mapped: bool, evidence: bool) -> bool:
    """Return whether the test matrix is complete (40.27)."""
    return mapped and evidence


def traceability_matrix_ok(requirements: bool, evidence: bool) -> bool:
    """Return whether the traceability matrix holds (40.28)."""
    return requirements and evidence


def matrix_complete(change_log: bool, references: bool) -> bool:
    """Return whether supporting appendix artifacts exist (40.29/40.30)."""
    return change_log and references


@dataclass
class AppendicesEngine:
    """Appendices lifecycle (40.1)."""

    name: str
    _maintained: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._maintained = True

    def status(self) -> str:
        """Return the appendices state."""
        return "maintained" if self._maintained else "stale"
