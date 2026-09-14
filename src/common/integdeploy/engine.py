"""Topic 36 — Integration and Deployment.

Integration is complete only when components, agents, data and APIs
are wired (36.3-36.6). Branches merge only under integration rules
and merge preconditions (36.13). Environments are clearly defined
(36.16.1) and promoted through gates (36.16.2/36.21); deployments
must validate and be accepted (36.22/36.29) with rollback and
recovery paths (36.24/36.25) under release management (36.26).
(REQ 36.1-36.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def integration_complete(components: bool, data: bool, api: bool) -> bool:
    """Return whether integration coverage holds (36.3/36.5/36.6)."""
    return components and data and api


def branch_merge_allowed(rules: bool, preconditions: bool) -> bool:
    """Return whether a branch may merge (36.13.1/36.13.2)."""
    return rules and preconditions


def environment_defined(name: str, defined: bool) -> bool:
    """Return whether a deployment environment is defined (36.16.1)."""
    return bool(name.strip()) and defined


def promotion_ok(validated: bool, gates: bool) -> bool:
    """Return whether environment promotion may proceed (36.16.2/36.21.2)."""
    return validated and gates


def gate_passed(check: bool) -> bool:
    """Return whether a deployment gate passed (36.21.2)."""
    return check


def deployment_validated(checks: bool, monitored: bool) -> bool:
    """Return whether deployment validation holds (36.22/36.23)."""
    return checks and monitored


def deployment_accepted(criteria: bool, satisfied: bool) -> bool:
    """Return whether deployment acceptance is met (36.29)."""
    return criteria and satisfied


def rollback_possible(trigger: bool, procedure: bool) -> bool:
    """Return whether rollback is possible (36.24.1/36.24.2)."""
    return trigger and procedure


def recovery_ok(objective: bool, procedure: bool) -> bool:
    """Return whether disaster recovery is ready (36.25.1/36.25.2)."""
    return objective and procedure


def release_managed(plan: bool, audit: bool) -> bool:
    """Return whether release management holds (36.26/36.27)."""
    return plan and audit


@dataclass
class IntegDeployEngine:
    """Integration and deployment lifecycle (36.1)."""

    name: str
    _planned: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._planned = True

    def status(self) -> str:
        """Return the integration/deployment state."""
        return "planned" if self._planned else "unplanned"
