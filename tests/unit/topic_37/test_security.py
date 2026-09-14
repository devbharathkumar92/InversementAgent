"""Tests for Topic 37 — Security and Secrets Management.

Covers authentication/authorization (37.3/37.4), RBAC and agent
permissions (37.5/37.6), API key and secret management
(37.8/37.9/37.10), encryption/privacy (37.15/37.16), secure logging
(37.17), vulnerability detection (37.23) and incident handling
(37.25).
"""

import pytest

from src.common.security.engine import (
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


class TestAuth:
    """REQ 37.3.1/37.3.2/37.4.1/37.4.2."""

    def test_auth_ok(self):
        assert auth_ok(method=True, failure=False) is True

    def test_auth_method_missing(self):
        assert auth_ok(method=False, failure=False) is False

    def test_agent_authorized(self):
        assert agent_authorized(rules=True, failure=False) is True

    def test_agent_denied(self):
        assert agent_authorized(rules=True, failure=True) is False

    def test_rbac_enforced(self):
        assert rbac_enforced(roles=True) is True


class TestSecrets:
    """REQ 37.8.1/37.8.2/37.9.1/37.9.2/37.10.1/37.10.2."""

    def test_api_key_valid(self):
        assert api_key_valid(vault=True, scrambled=True) is True

    def test_api_key_plaintext(self):
        assert api_key_valid(vault=True, scrambled=False) is False

    def test_secret_stored_securely(self):
        assert secret_stored_securely(encrypted=True, access_controls=True) is True

    def test_secret_access_controls_missing(self):
        assert secret_stored_securely(encrypted=True, access_controls=False) is False

    def test_secret_rotated(self):
        assert secret_rotated(triggered=True, procedure=True) is True

    def test_secret_rotation_missing(self):
        assert secret_rotated(triggered=True, procedure=False) is False


class TestProtections:
    """REQ 37.15/37.16/37.17/37.23/37.25."""

    def test_encrypted(self):
        assert encrypted(at_rest=True, in_transit=True) is True

    def test_encryption_incomplete(self):
        assert encrypted(at_rest=True, in_transit=False) is False

    def test_vulnerability_detected(self):
        assert vulnerability_detected(scanned=True) is True

    def test_incident_handled(self):
        assert incident_handled(detected=True, response=True) is True

    def test_incident_response_missing(self):
        assert incident_handled(detected=True, response=False) is False


class TestEngine:
    """REQ 37.1 — security lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            SecurityEngine(name=" ")

    def test_engine_status(self):
        assert SecurityEngine(name="s").status() == "secured"


pytestmark = pytest.mark.unit
