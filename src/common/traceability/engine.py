"""Topic 28 — Requirement Traceability.

Tracks each requirement from identification (28.2) through goal/SRS/
task/agent/code/test mapping (28.6-28.11), measuring coverage and
surfacing missing or broken traces (28.18-28.20). (REQ 28.1-28.25
enforced subset.)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

_REQ_ID_RE = re.compile(r"^REQ-\d+(?:\.\d+)*$")


def id_format_valid(req_id: str) -> bool:
    """Return whether an ID matches the requirement ID format (28.3.1)."""
    return _REQ_ID_RE.match(req_id) is not None


def id_unique(conflicts: int) -> bool:
    """Return whether requirement IDs resolve without conflicts (28.3.2)."""
    return conflicts == 0


def requirement_classified(kind: str) -> bool:
    """Return whether a requirement is classified (28.4)."""
    return bool(kind)


def goals_mapped(goals: bool, srs: bool) -> bool:
    """Return whether a requirement maps to goals/SRS (28.6/28.7)."""
    return goals and srs


def code_coverage_sufficient(target: bool, actual: bool) -> bool:
    """Return whether code coverage is achieved (28.10.2)."""
    return target and actual


def result_mapped(recorded: bool, passed: bool) -> bool:
    """Return whether a test result is mapped (28.11.2)."""
    return recorded and passed


def missing_trace_detected(verified: bool) -> bool:
    """Return whether a missing trace was found (28.19.1)."""
    return not verified


def broken_trace_detected(intact: bool) -> bool:
    """Return whether a broken trace was found (28.20.1)."""
    return not intact


def trace_validated(missing: int, broken: int) -> bool:
    """Return whether all traces validate (28.21)."""
    return missing == 0 and broken == 0


def coverage_met(coverage: float, threshold: float) -> bool:
    """Return whether coverage passes the threshold (28.18.2)."""
    return coverage >= threshold


@dataclass
class TraceabilityEngine:
    """Traceability lifecycle (28.1)."""

    name: str
    _tracked: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._tracked = True

    def status(self) -> str:
        """Return the traceability engine state."""
        return "tracked" if self._tracked else "untracked"
