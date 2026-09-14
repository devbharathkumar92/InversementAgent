# Topic 24 — Error Detection and Recovery

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-24-recovery`

## Decision

**Implementation required (core).** Topic 24 makes failures
observable and survivable without human babysitting:

- **24.2 / 24.2.1 / 24.2.2**: error classification by category and
  severity.
- **24.3-24.13**: input, data, API, network, tool, agent, sub-agent,
  logic, integration, security and runtime error coverage.
- **24.14**: error detection.
- **24.15 / 24.15.1 / 24.15.2**: severity levels and severity-to-action
  mapping.
- **24.16 / 24.16.1 / 24.16.2**: automatic recovery; recoverable vs
  non-recoverable errors.
- **24.17 / 24.17.1 / 24.17.2**: retry policies, conditions and limits.
- **24.18 / 24.18.1 / 24.18.2**: fallback selection and fallback failure.
- **24.19 / 24.19.1 / 24.19.2**: safe-state definition and transition.
- **24.20 / 24.21 / 24.22**: task restart, task rollback, state recovery.
- **24.25 / 24.25.1 / 24.26**: root-cause evidence collection.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 24.2/24.2.2 | Error Classification | `engine.py` (`classify_error`) | `test_recovery.py::TestErrorClassification` |
| 24.15.2 | Severity-to-Action Mapping | `engine.py` (`severity_action_mapped`) | `test_recovery.py::TestErrorClassification` |
| 24.16.1 | Recoverable Errors | `engine.py` (`auto_recoverable`) | `test_recovery.py::TestRecovery` |
| 24.17.1 | Retry Conditions | `engine.py` (`retry_condition_allowed`) | `test_recovery.py::TestRecovery` |
| 24.17.2 | Retry Limits | `engine.py` (`retry_exhausted`) | `test_recovery.py::TestRecovery` |
| 24.18.1 | Fallback Selection | `engine.py` (`fallback_available`) | `test_recovery.py::TestRecovery` |
| 24.19.1 | Safe-State Definition | `engine.py` (`safe_transition`) | `test_recovery.py::TestRecovery` |
| 24.21 | Task Rollback | `engine.py` (`task_rollback_allowed`) | `test_recovery.py::TestRecovery` |
| 24.20 | Task Restart | `engine.py` (`task_restart_allowed`) | `test_recovery.py::TestRecovery` |
| 24.1 | Error Management | `engine.py` (`RecoveryEngine`) | `test_recovery.py::TestEngine` |
| 24.25.1 | Evidence Collection | `engine.py` (`evidence_collected`) | `test_recovery.py::TestEngine` |
| — | Full Topic 24 contract | `registry.py` (+ traceability test) | `test_recovery_registry.py` |

## Registry addition

Topic 24 (absent before) added as the authoritative 44-item block.
Captures `Nested Children`: 24.2.1 Error Categories, 24.2.2 Severity
Classification; 24.15.1 Severity Levels, 24.15.2 Severity-to-Action
Mapping; 24.16.1 Recoverable Errors, 24.16.2 Non-Recoverable Errors;
24.17.1 Retry Conditions, 24.17.2 Retry Limits; 24.18.1 Fallback
Selection, 24.18.2 Fallback Failure; 24.19.1 Safe-State Definition,
24.19.2 Safe-State Transition; 24.25.1 Evidence Collection, 24.25.2
Root-Cause Classification.

## Validation

- `python -m pytest -m unit` → **485 passed** (16 from Topic 24)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (102 files)

## Notes / decisions

- Classification is conservative: anything unknown is treated as
  `critical` so it never bypasses human eyes (24.2.2).
- Only transient/retryable classes (network, API, timeout, rate,
  integration) are auto-recovered; logic errors are fatal (24.16.2).
- Severity-to-action mapping: 1 continue → 2 retry → 3 fallback →
  4 halt, so high severity forces safe-state transition (24.15.2).
- Task restore requires persistence (rollback) or idempotency
  (restart), preventing dangerous in-place retries (24.20/24.21).