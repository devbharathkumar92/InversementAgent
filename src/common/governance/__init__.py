"""Topic 27 — SRS Version Control and Governance.

Enforces SRS versioning, baselining, change control and release
validation, with integrity and consistency protection
(REQ 27.1-27.30 subset).
"""

from .engine import (
    GovernanceEngine,
    approval_allowed,
    change_justified,
    change_requires_approval,
    documented_after_change,
    emergency_approval,
    impact_risk_assessed,
    release_validated,
    srs_authority,
    srs_consistent,
    srs_integrity_ok,
    version_format_valid,
    version_increment_valid,
)

__all__ = [
    "GovernanceEngine",
    "approval_allowed",
    "change_justified",
    "change_requires_approval",
    "documented_after_change",
    "emergency_approval",
    "impact_risk_assessed",
    "release_validated",
    "srs_authority",
    "srs_consistent",
    "srs_integrity_ok",
    "version_format_valid",
    "version_increment_valid",
]
