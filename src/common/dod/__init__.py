"""Topic 35 — Definition of Done.

Gates completion on requirement status+evidence, code review,
passing tests, deployment readiness and final human/release
approval (REQ 35.1-35.30 subset).
"""

from .engine import (
    DoDEngine,
    code_complete,
    deployment_ready,
    final_approved,
    final_validation,
    human_approved,
    release_approved,
    requirement_complete,
    suite_green,
    traceability_complete,
)

__all__ = [
    "DoDEngine",
    "code_complete",
    "deployment_ready",
    "final_approved",
    "final_validation",
    "human_approved",
    "release_approved",
    "requirement_complete",
    "suite_green",
    "traceability_complete",
]
