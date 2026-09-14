"""Requirements registry (traceability backbone).

Maps the authoritative SRS numbered requirement identifiers to their
titles. Requirement IDs and titles are extracted from the frozen
`SRS.md` + `srs/topics/` and must not be altered without going through
the controlled change workflow.
"""

from .registry import REQ_AUTHORIZED_STATUSES, REQ_REGISTRY, get_requirement_title

__all__ = ["REQ_REGISTRY", "REQ_AUTHORIZED_STATUSES", "get_requirement_title"]
