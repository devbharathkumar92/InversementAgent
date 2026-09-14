# Topic 23 — Audit Trail and Observability

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-23-audit`

## Decision

**Implementation required (core).** Topic 23 builds the audit-trail
backbone underpinning trust and cost/risk explainability:

- **23.2 / 23.3-23.14**: event logging across agent/sub-agent activity,
  decisions, data acquisition, errors, config, SRS changes, user
  interactions, approvals, deployments, performance and security.
- **23.15 / 23.15.1 / 23.15.2 / 23.16**: structured audit event with
  mandatory fields, event types and timestamping.
- **23.17 / 23.17.1 / 23.18 / 23.18.1 / 23.18.2**: event correlation
  rules and trace ID generation/propagation.
- **23.19 / 23.19.1 / 23.19.2 / 23.20 / 23.20.1 / 23.20.2**: log
  integrity protection, tamper detection, retention period and secure
  deletion.
- **23.21-23.24**: observability metrics, health monitoring, distributed
  tracing and alerting.
- **23.25 / 23.26**: audit search and reporting.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 23.2 | Event Logging | `engine.py` (`capture_event`, `event_required_or_optional`) | `test_observability.py::TestAuditEvents` |
| 23.15 | Audit Event Structure | `engine.py` (`AuditEvent`) | `test_observability.py::TestAuditEvents` |
| 23.16 | Event Timestamping | `engine.py` (`AuditEvent.identity`) | `test_observability.py::TestAuditEvents` |
| 23.20.2 | Secure Deletion | `engine.py` (`secure_deletion`) | `test_observability.py::TestAuditEvents` |
| 23.20.1 | Retention Period | `engine.py` (`retention_allowed`) | `test_observability.py::TestAuditEvents` |
| 23.18.1 | Trace ID Generation | `engine.py` (`trace_id_generated`) | `test_observability.py::TestTracing` |
| 23.17 | Event Correlation | `engine.py` (`correlation`) | `test_observability.py::TestTracing` |
| 23.18.2 | Trace Propagation | `engine.py` (`trace_eligible`) | `test_observability.py::TestTracing` |
| 23.1 | Observability Objectives | `engine.py` (`AuditEngine`) | `test_observability.py::TestAuditEngine` |
| — | Full Topic 23 contract | `registry.py` (+ traceability test) | `test_observability_registry.py` |

## Registry addition

Topic 23 (absent before) added as the authoritative 39-item block.
Captures `Nested Children`: 23.15.1 Mandatory Event Fields, 23.15.2
Event Types; 23.17.1 Correlation Rules; 23.18.1 Trace ID Generation,
23.18.2 Trace Propagation; 23.19.1 Integrity Protection, 23.19.2
Tamper Detection; 23.20.1 Retention Period, 23.20.2 Secure Deletion.

## Validation

- `python -m pytest -m unit` → **469 passed** (14 from Topic 23)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (100 files)

## Notes / decisions

- Only event classes derived as writing classes (security/approval/error)
  are treated as *required*; e.g. debug-only instrumentation stays
  *optional* (23.2).
- Correlation is modelled as trace-equality over a `trace_id` (23.17);
  trace propagation is gated on the distributed flag (23.18.2).
- Secure deletion refuses to purge any log flagged as tampered, which
  preserves evidence required by the audit trail (23.19.2/23.20.2).
- Transport/sinks (OpenTelemetry exporters, object-store retention
  jobs) are integration scope; the engine exposes the decision seams.