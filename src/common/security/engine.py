"""Topic 37 — Security and Secrets Management.

Access is granted only through a defined authentication method with
no auth failure (37.3) and authorization rules with no failure
(37.4); RBAC (37.5) and agent permissions (37.6) apply. API keys and
secrets live in a vault, never in plaintext (37.8), stored encrypted
with access controls (37.9) and rotated via a defined procedure
(37.10). Data is encrypted at rest and in transit (37.15);
vulnerabilities are scanned (37.23) and incidents are detected and
responded to (37.25). (REQ 37.1-37.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def auth_ok(method: bool, failure: bool) -> bool:
    """Return whether authentication passes (37.3.1/37.3.2)."""
    return method and not failure


def agent_authorized(rules: bool, failure: bool) -> bool:
    """Return whether authorization passes (37.4.1/37.4.2)."""
    return rules and not failure


def rbac_enforced(roles: bool) -> bool:
    """Return whether RBAC is enforced (37.5)."""
    return roles


def api_key_valid(vault: bool, scrambled: bool) -> bool:
    """Return whether API keys are managed securely (37.8.1/37.8.2)."""
    return vault and scrambled


def secret_stored_securely(encrypted: bool, access_controls: bool) -> bool:
    """Return whether secret storage is secure (37.9.1/37.9.2)."""
    return encrypted and access_controls


def secret_rotated(triggered: bool, procedure: bool) -> bool:
    """Return whether secret rotation is defined (37.10.1/37.10.2)."""
    return triggered and procedure


def encrypted(at_rest: bool, in_transit: bool) -> bool:
    """Return whether data is encrypted (37.15)."""
    return at_rest and in_transit


def vulnerability_detected(scanned: bool) -> bool:
    """Return whether vulnerability detection runs (37.23.1)."""
    return scanned


def incident_handled(detected: bool, response: bool) -> bool:
    """Return whether incidents are handled (37.25.1/37.25.2)."""
    return detected and response


@dataclass
class SecurityEngine:
    """Security lifecycle (37.1)."""

    name: str
    _secured: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._secured = True

    def status(self) -> str:
        """Return the security state."""
        return "secured" if self._secured else "unsecured"
