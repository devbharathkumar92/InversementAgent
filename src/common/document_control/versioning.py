"""Topic 1.3/1.3.1/1.3.2/1.4 — versioning structure and status lifecycle.

The version format is `major.minor.patch` (machine-sortable, human-readable,
never relying on filenames alone). Version increments are driven by an
approved change class. Document status follows a pre-defined transition graph.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import total_ordering

_VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

# Authorized statuses (aligned with REQ_AUTHORIZED_STATUSES).
_DOC_STATUSES = frozenset(
    {"DRAFT", "IN_REVIEW", "APPROVED", "BASELINED", "SUPERSEDED", "REJECTED", "ARCHIVED"}
)

# Allowed transitions: current -> {targets}.
_STATUS_TRANSITIONS: dict[str, frozenset[str]] = {
    "DRAFT": frozenset({"IN_REVIEW", "REJECTED"}),
    "IN_REVIEW": frozenset({"APPROVED", "REJECTED"}),
    "APPROVED": frozenset({"BASELINED", "SUPERSEDED"}),
    "BASELINED": frozenset({"SUPERSEDED", "ARCHIVED"}),
    "SUPERSEDED": frozenset({"ARCHIVED"}),
    "REJECTED": frozenset({"DRAFT", "ARCHIVED"}),
    "ARCHIVED": frozenset(),
}


@total_ordering
@dataclass(frozen=True)
class Version:
    """A `major.minor.patch` version identifier.

    Implements ordering so versions can be compared and sorted.
    """

    major: int
    minor: int = 0
    patch: int = 0

    def __init__(self, raw: str) -> None:
        parts = _parse(raw)
        object.__setattr__(self, "major", parts[0])
        object.__setattr__(self, "minor", parts[1])
        object.__setattr__(self, "patch", parts[2])

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def _cmpkey(self) -> tuple[int, int, int]:
        return (self.major, self.minor, self.patch)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return self._cmpkey() == other._cmpkey()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return self._cmpkey() < other._cmpkey()

    def bump(self, change_class: str) -> Version:
        """Return the next version per the approved change class.

        ``major`` -> ``x+1.0.0``; ``minor`` -> ``x.y+1.0``; ``patch`` -> ``x.y.z+1``.
        """
        if change_class == "major":
            return Version(f"{self.major + 1}.0.0")
        if change_class == "minor":
            return Version(f"{self.major}.{self.minor + 1}.0")
        if change_class == "patch":
            return Version(f"{self.major}.{self.minor}.{self.patch + 1}")
        raise ValueError(f"Unknown change class: {change_class}")


def _parse(raw: str) -> tuple[int, int, int]:
    if not isinstance(raw, str):
        raise ValueError("Version must be a string")
    m = _VERSION_RE.match(raw.strip())
    if not m:
        raise ValueError(f"Malformed version: {raw!r}; expected major.minor.patch")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def parse_version(raw: str) -> tuple[int, int, int]:
    """Validate and return the numeric components of a version string."""
    return _parse(raw)


def next_version(current: str | Version, change_class: str, approved: bool = True) -> str:
    """Return the next version string for an *approved* change.

    Args:
        current: Current version string or ``Version``.
        change_class: ``major``, ``minor``, or ``patch``.
        approved: Must be ``True``; increments never occur before approval.

    Raises:
        ValueError: if not approved, the change class is unknown, or the
            current version is malformed.
    """
    if not approved:
        raise ValueError("Version increment requires an approved change")
    if isinstance(current, Version):
        current_version = current
    else:
        current_version = Version(current)
    return str(current_version.bump(change_class))


def initial_status() -> str:
    """The lifecycle status of a newly created controlled document."""
    return "DRAFT"


def can_transition_status(current: str, target: str) -> bool:
    """Return whether ``target`` is a legal successor of ``current``."""
    if current not in _DOC_STATUSES:
        raise ValueError(f"Unknown status: {current}")
    if target not in _DOC_STATUSES:
        raise ValueError(f"Unknown status: {target}")
    return target in _STATUS_TRANSITIONS[current]
