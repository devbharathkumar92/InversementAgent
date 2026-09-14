"""Topic 7 — Technology Stack and Technical Feasibility.

Technology responsibilities are partitioned: deterministic (non-LLM)
duties are versioned controls that must never be delegated to an LLM,
technologies are selected only under explicit governed criteria, branch
naming is restricted, and dependencies are pinned for reproducible
builds (REQ 7.7.2/7.1.1/7.1.2/7.18.2/7.26.1).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

_UNSUPPORTED_TECH = {"hardware-trading-engine"}


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


def validate_pinned_dependency(spec: str) -> bool:
    """Return whether a dependency is fully pinned with ``==``/``=``.

    A single ``=`` is accepted as a pinned exact-match declaration, and
    a bare name without any version is NOT pinned.
    """
    pattern = (
        r"[A-Za-z0-9_.\-\[\]]+==[0-9][A-Za-z0-9_.\-+]*|[A-Za-z0-9_.\-\[\]]+=[0-9][A-Za-z0-9_.\-+]*"
    )
    return re.fullmatch(pattern, spec) is not None


def validate_dependency_pinning(specs: list[str]) -> bool:
    """Return whether every dependency in the set is pinned (7.26.1)."""
    return all(validate_pinned_dependency(s) for s in specs)


@dataclass
class TechSelection:
    """The controlled technology-selection contract (REQ 7.1/7.7.2)."""

    name: str = ""
    deterministic_responsibilities: list[str] = field(default_factory=list)
    llm_responsibilities: list[str] = field(default_factory=list)
    selected_technologies: list[str] = field(default_factory=list)
    branch_prefixes: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")

    def is_deterministic(self, responsibility: str) -> bool:
        """Return whether a responsibility must be deterministic (7.7.2)."""
        return responsibility in self.deterministic_responsibilities

    def owner_of(self, responsibility: str) -> str:
        """Return the owning side of a responsibility (7.7.1/7.7.2)."""
        if responsibility in self.deterministic_responsibilities:
            return "deterministic"
        if responsibility in self.llm_responsibilities:
            return "llm"
        return "unassigned"

    def is_selected(self, spec: str) -> bool:
        """Return whether a technology is selected with a pinned version."""
        return spec in self.selected_technologies

    def reject_if_unsupported(self, technology: str) -> bool:
        """Return whether a technology should be rejected (7.1.2)."""
        return technology in _UNSUPPORTED_TECH or technology not in self.selected_technologies


@dataclass
class BranchStrategy:
    """Governed repository branch strategy (REQ 7.18.2)."""

    branch_prefixes: list[str] = field(default_factory=list)
    protected_branches: list[str] = field(default_factory=lambda: ["main", "master"])

    @classmethod
    def from_deps(cls, branch_prefixes: list[str], **_kwargs: object) -> BranchStrategy:
        """Build a strategy from a shared technology dict."""
        return cls(branch_prefixes=list(branch_prefixes))

    def is_conformant(self, branch: str) -> bool:
        """Return whether a branch name follows an allowed prefix."""
        return any(branch.startswith(prefix) for prefix in self.branch_prefixes)

    def is_protected(self, branch: str) -> bool:
        """Return whether a branch is protected from direct pushes."""
        return branch in self.protected_branches
