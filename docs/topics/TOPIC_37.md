# Topic 37 — Security and Secrets Management

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-37-security`

## Decision

**Implementation required (core).** Topic 37 defines the security and
secrets-management foundation:

- **37.2 / 37.3 / 37.3.1 / 37.3.2 / 37.4 / 37.4.1 / 37.4.2**: security
  principles, authentication (method + failure) and authorization
  (rules + failure).
- **37.5 / 37.6 / 37.6.1 / 37.6.2 / 37.7**: RBAC, agent permissions
  and restricted agent actions; sub-agent permissions.
- **37.8 / 37.8.1 / 37.8.2 / 37.9 / 37.9.1 / 37.9.2 / 37.10 /
  37.10.1 / 37.10.2**: API key management, secret creation/access,
  secret storage with access controls, and rotation trigger/
  procedure.
- **37.11 / 37.12 / 37.13 / 37.14**: credential, database, API and
  network security.
- **37.15 / 37.16 / 37.17 / 37.18 / 37.19 / 37.20**: data encryption,
  privacy, secure logging, audit security, dashboard security and
  notification security.
- **37.21 / 37.22**: repository and dependency security.
- **37.23 / 37.23.1 / 37.23.2 / 37.24**: vulnerability detection and
  severity; security monitoring.
- **37.25 / 37.25.1 / 37.25.2 / 37.26 / 37.27**: incident detection/
  response, security recovery and security testing.
- **37.28 / 37.29 / 37.30**: security compliance, acceptance criteria
  and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 37.3.1/37.3.2 | Authentication Method/Failure | `engine.py` (`auth_ok`) | `test_security.py::TestAuth` |
| 37.4.1/37.4.2 | Authorization Rules/Failure | `engine.py` (`agent_authorized`) | `test_security.py::TestAuth` |
| 37.5 | Role-Based Access Control | `engine.py` (`rbac_enforced`) | `test_security.py::TestAuth` |
| 37.8.1/37.8.2 | Secret Creation / Access | `engine.py` (`api_key_valid`) | `test_security.py::TestSecrets` |
| 37.9.1/37.9.2 | Secret Storage / Access Controls | `engine.py` (`secret_stored_securely`) | `test_security.py::TestSecrets` |
| 37.10.1/37.10.2 | Rotation Trigger / Procedure | `engine.py` (`secret_rotated`) | `test_security.py::TestSecrets` |
| 37.15 | Data Encryption | `engine.py` (`encrypted`) | `test_security.py::TestProtections` |
| 37.23.1 | Vulnerability Detection | `engine.py` (`vulnerability_detected`) | `test_security.py::TestProtections` |
| 37.25.1/37.25.2 | Incident Detection / Response | `engine.py` (`incident_handled`) | `test_security.py::TestProtections` |
| 37.1 | Security Objectives | `engine.py` (`SecurityEngine`) | `test_security.py::TestEngine` |
| — | Full Topic 37 contract | `registry.py` (+ traceability test) | `test_security_registry.py` |

## Registry addition

Topic 37 (absent before) added as the authoritative 46-item block.
Captures `Nested Children`: 37.3.1 Authentication Method, 37.3.2
Authentication Failure; 37.4.1 Authorization Rules, 37.4.2
Authorization Failure; 37.6.1 Agent Permissions, 37.6.2 Restricted
Agent Actions; 37.8.1 Secret Creation, 37.8.2 Secret Access; 37.9.1
Secret Storage Requirements, 37.9.2 Secret Access Controls; 37.10.1
Rotation Trigger, 37.10.2 Rotation Procedure; 37.23.1 Vulnerability
Detection, 37.23.2 Vulnerability Severity; 37.25.1 Incident
Detection, 37.25.2 Incident Response.

## Validation

- `python -m pytest -m unit` → **736 passed** (19 from Topic 37)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (128 files)

## Notes / decisions

- Authentication/authorization fail closed: any failure blocks access
  (37.3.2/37.4.2).
- API keys must never appear in plaintext; they live in a vault and
  are stored scrambled (37.8).
- Secret storage requires encryption AND access controls; rotation
  requires both a trigger and a procedure (37.9/37.10).
- Data must be encrypted at rest and in transit (37.15).