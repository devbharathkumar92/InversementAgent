"""Topic 28 — Requirement Traceability.

Links requirements to goals, SRS, tasks, agents, code and tests;
detects missing/broken traces and measures coverage against
thresholds (REQ 28.1-28.25 subset).
"""

from .engine import (
    TraceabilityEngine,
    broken_trace_detected,
    code_coverage_sufficient,
    coverage_met,
    goals_mapped,
    id_format_valid,
    id_unique,
    missing_trace_detected,
    requirement_classified,
    result_mapped,
    trace_validated,
)

__all__ = [
    "TraceabilityEngine",
    "broken_trace_detected",
    "code_coverage_sufficient",
    "coverage_met",
    "goals_mapped",
    "id_format_valid",
    "id_unique",
    "missing_trace_detected",
    "requirement_classified",
    "result_mapped",
    "trace_validated",
]
