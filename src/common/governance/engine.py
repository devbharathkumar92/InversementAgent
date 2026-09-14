"""Topic 27 — SRS Version Control and Governance.

Governs the SRS as a baselined, versioned document: changes require
justification, impact/risk analysis and approval (27.8-27.13); the
document is validated for integrity and consistency (27.17/27.19);
and releases are prepared and validated (27.28). (REQ 27.1-27.30
enforced subset.)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def version_format_valid(version: str) -> bool:
    """Return whether the version follows major.minor.patch (27.5.1)."""
    return _VERSION_RE.match(version) is not None


def version_increment_valid(old: str, new: str) -> bool:
    """Return whether a version increment is valid (27.5.2)."""
    if not version_format_valid(old) or not version_format_valid(new):
        return False
    return tuple(int(p) for p in new.split(".")) > tuple(int(p) for p in old.split("."))


def documented_after_change(logged: bool) -> bool:
    """Return whether the change was logged (27.15)."""
    return logged


def change_justified(reason: bool, impact: bool) -> bool:
    """Return whether a change is justified (27.9.2)."""
    return reason and impact


def impact_risk_assessed(areas: bool, risk: bool) -> bool:
    """Return whether impact analysis is complete (27.10)."""
    return areas and risk


def approval_allowed(authority: bool, state: str) -> bool:
    """Return whether an approval is permitted (27.11.1/27.11.2)."""
    return authority and state in {"draft", "reviewed"}


def change_requires_approval(major: bool) -> bool:
    """Return whether a change needs formal approval (27.11)."""
    return major


def emergency_approval(criteria: bool, authority: bool) -> bool:
    """Return whether an emergency change may proceed (27.13.2)."""
    return criteria and authority


def srs_authority(owner: str) -> str:
    """Return the SRS governing authority (27.3)."""
    return owner if owner else "unassigned"


def srs_integrity_ok(checksum_match: bool) -> bool:
    """Return whether document integrity holds (27.17)."""
    return checksum_match


def srs_consistent(cross_refs: bool, headings: bool) -> bool:
    """Return whether the SRS passes consistency checks (27.19)."""
    return cross_refs and headings


def release_validated(prepared: bool, tested: bool) -> bool:
    """Return whether a release is ready (27.28.2)."""
    return prepared and tested


@dataclass
class GovernanceEngine:
    """SRS governance lifecycle (27.1)."""

    name: str
    _governed: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._governed = True

    def status(self) -> str:
        """Return the governance engine state."""
        return "governed" if self._governed else "unmanaged"
