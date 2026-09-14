"""Topic 37 — Security and Secrets Management.

Enforces authentication/authorization, RBAC, agent permissions,
secure secret lifecycle (creation, storage, rotation) and
encryption plus vulnerability and incident handling
(REQ 37.1-37.30 subset).
"""

from .engine import (
    SecurityEngine,
    agent_authorized,
    api_key_valid,
    auth_ok,
    encrypted,
    incident_handled,
    rbac_enforced,
    secret_rotated,
    secret_stored_securely,
    vulnerability_detected,
)

__all__ = [
    "SecurityEngine",
    "agent_authorized",
    "api_key_valid",
    "auth_ok",
    "encrypted",
    "incident_handled",
    "rbac_enforced",
    "secret_rotated",
    "secret_stored_securely",
    "vulnerability_detected",
]
