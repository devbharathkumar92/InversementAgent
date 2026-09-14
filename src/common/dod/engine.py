"""Topic 35 — Definition of Done.

A requirement is done only when its status is fulfilled and evidence
exists (35.2), code is complete and reviewed (35.5), tests have
executed and passed (35.6), and traceability is established (35.18).
Release additionally requires a clean deployment checklist without
blocking conditions (35.24), human approval (35.25), release
approval (35.26) and final validation with final approval (35.27).
(REQ 35.1-35.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def requirement_complete(status: str, evidence: bool) -> bool:
    """Return whether a requirement is complete (35.2.1/35.2.2)."""
    return status == "done" and evidence


def code_complete(complete: bool, reviewed: bool) -> bool:
    """Return whether code completion holds (35.5.1/35.5.2)."""
    return complete and reviewed


def suite_green(executed: bool, passed: bool) -> bool:
    """Return whether tests completed (35.6.1/35.6.2)."""
    return executed and passed


def traceability_complete(linked: bool) -> bool:
    """Return whether SRS traceability is complete (35.18)."""
    return linked


def deployment_ready(checklist: bool, blockers: int) -> bool:
    """Return whether deployment is ready (35.24.1/35.24.2)."""
    return checklist and blockers == 0


def human_approved(approved: bool) -> bool:
    """Return whether human approval was given (35.25)."""
    return approved


def release_approved(approved: bool) -> bool:
    """Return whether release approval was given (35.26)."""
    return approved


def final_validation(valid: bool) -> bool:
    """Return whether final validation passes (35.27.1)."""
    return valid


def final_approved(valid: bool, approved: bool) -> bool:
    """Return whether final approval was granted (35.27.2)."""
    return valid and approved


@dataclass
class DoDEngine:
    """Definition of done lifecycle (35.1)."""

    name: str
    _defined: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._defined = True

    def status(self) -> str:
        """Return the definition of done state."""
        return "defined" if self._defined else "undefined"
