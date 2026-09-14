"""Topic 4 — System Scope and Boundaries.

The system scope is a controlled definition of what the system may and
may not do. Boundary violations, unauthorized agent authority, capability
limits, and unapproved scope expansions are rejected (REQ 4.19/4.20).
"""

from __future__ import annotations

from dataclasses import dataclass, field


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


@dataclass
class ScopeBoundary:
    """A single named boundary declaring included values for a dimension."""

    dimension: str
    allowed_values: set[str]


@dataclass
class ExpansionApproval:
    """Evidence that a governance-approved scope expansion exists."""

    scope_item: str
    approved_by: str
    notes: str = ""

    def __post_init__(self) -> None:
        _require_non_empty(self.scope_item, "scope_item")
        _require_non_empty(self.approved_by, "approved_by")


@dataclass
class ScopeException:
    """A detected scope exception that must escalate to a human."""

    scope_item: str
    reason: str

    def __post_init__(self) -> None:
        _require_non_empty(self.scope_item, "scope_item")
        _require_non_empty(self.reason, "reason")

    def escalation_required(self) -> bool:
        """Exceptions always escalate to a human for resolution (4.25.2)."""
        return True


@dataclass
class SystemScope:
    """The controlled system-scope definition (REQ 4.1)."""

    name: str = ""
    included_capabilities: list[str] = field(default_factory=list)
    out_of_scope: list[str] = field(default_factory=list)
    geographic_scope: list[str] = field(default_factory=list)
    market_scope: list[str] = field(default_factory=list)
    currency_scope: list[str] = field(default_factory=list)
    allowed_authority: list[str] = field(default_factory=list)
    prohibited_authority: list[str] = field(default_factory=list)
    capability_limits: dict[str, int] = field(default_factory=dict)
    _expansions: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")
        self._expansions = {}

    def allows_market(self, geography: str, market: str, currency: str) -> bool:
        """Return whether the g/m/c triple is inside the declared bounds (4.7)."""
        return (
            geography in self.geographic_scope
            and market in self.market_scope
            and currency in self.currency_scope
        )

    def authority_allowed(self, authority: str) -> bool:
        """Return whether an agent authority is explicitly allowed (4.10)."""
        if authority in self.prohibited_authority:
            return False
        return authority in self.allowed_authority

    def check_capability_limit(self, limit_name: str, used: int) -> None:
        """Raise if a numeric capability limit is exceeded (4.2.2)."""
        limit = self.capability_limits.get(limit_name)
        if limit is not None and limit <= used:
            raise ValueError(f"capability limit exceeded: {limit_name}")

    def expansion_allowed(self, scope_item: str) -> bool:
        """Return whether a scope item has an approved expansion (4.21)."""
        return scope_item in self._expansions

    def approve_expansion(self, approval: ExpansionApproval) -> bool:
        """Record a governed scope expansion; item becomes in-scope (4.21.2)."""
        self._expansions[approval.scope_item] = approval.approved_by
        return True

    def describe(self) -> ScopeBoundary:
        """Expose the full boundary set for validation/reporting."""
        return ScopeBoundary(
            dimension="scope",
            allowed_values=set(self.included_capabilities) | set(self._expansions),
        )


def is_in_scope(scope: SystemScope, capability: str) -> bool:
    """Return whether a capability is currently within scope (4.2/4.3)."""
    if capability in scope.out_of_scope:
        return False
    if capability in scope.included_capabilities:
        return True
    return scope.expansion_allowed(capability)


class ScopeEnforcer:
    """Detects and blocks scope violations (REQ 4.19/4.20)."""

    def __init__(self, scope: SystemScope) -> None:
        self.scope = scope

    def detect_violations(self, actions: list[str]) -> list[str]:
        """Return the subset of actions that violate scope boundaries."""
        return [a for a in actions if not is_in_scope(self.scope, a)]

    def enforce_action(self, action: str) -> None:
        """Raise unless the action is in-scope and the authority is allowed."""
        if not is_in_scope(self.scope, action):
            raise ValueError(f"action out of scope: {action}")
        if not self.scope.authority_allowed(action):
            raise ValueError(f"authority not permitted: {action}")
