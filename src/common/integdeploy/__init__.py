"""Topic 36 — Integration and Deployment.

Coordinates component/agent/data/API integration, branch merge
validation, environment promotion with gates, and deployment with
rollback and disaster recovery (REQ 36.1-36.30 subset).
"""

from .engine import (
    IntegDeployEngine,
    branch_merge_allowed,
    deployment_accepted,
    deployment_validated,
    environment_defined,
    gate_passed,
    integration_complete,
    promotion_ok,
    recovery_ok,
    release_managed,
    rollback_possible,
)

__all__ = [
    "IntegDeployEngine",
    "branch_merge_allowed",
    "deployment_accepted",
    "deployment_validated",
    "environment_defined",
    "gate_passed",
    "integration_complete",
    "promotion_ok",
    "recovery_ok",
    "release_managed",
    "rollback_possible",
]
