"""Topic 4 — System Scope and Boundaries.

Defines the controlled system scope: included capabilities, explicit
exclusions, market/geographic/currency bounds, agent authority limits,
scope-expansion approval, exception escalation, and boundary enforcement.
"""

from .system_scope import (
    ExpansionApproval,
    ScopeBoundary,
    ScopeEnforcer,
    ScopeException,
    SystemScope,
    is_in_scope,
)

__all__ = [
    "SystemScope",
    "ScopeBoundary",
    "ScopeEnforcer",
    "ScopeException",
    "ExpansionApproval",
    "is_in_scope",
]
