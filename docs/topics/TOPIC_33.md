# Topic 33 — Testing Strategy

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-33-testing-strategy`

## Decision

**Implementation required (core).** Topic 33 defines the testing
strategy used across the system:

- **33.2 / 33.3**: testing principles and test environment.
- **33.4 / 33.4.1 / 33.4.2 / 33.5 / 33.6 / 33.6.1 / 33.6.2**:
  unit/component/integration testing with expected results and
  interface validation.
- **33.7 / 33.8 / 33.9 / 33.10**: system, E2E, API and data testing.
- **33.11 / 33.11.1 / 33.11.2 / 33.12 / 33.13 / 33.14**: agent,
  sub-agent, decision and risk testing.
- **33.15 / 33.16 / 33.17 / 33.18**: backtesting, paper trading,
  dashboard and notification validation.
- **33.19 / 33.20 / 33.21 / 33.22 / 33.23 / 33.24 / 33.25**: security,
  performance, reliability, failure recovery, regression, stress and
  edge-case testing.
- **33.26 / 33.26.1 / 33.26.2**: acceptance testing with criteria and
  results.
- **33.27 / 33.28 / 33.29 / 33.30**: automation, reporting, evidence/
  audit trail and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 33.4.1/33.4.2 | Test Case Definition / Expected Result | `engine.py` (`unit_case_defined`) | `test_testing_strategy.py::TestTestLevels` |
| 33.6.1/33.6.2 | Integration Cases / Interface Validation | `engine.py` (`integration_covered`) | `test_testing_strategy.py::TestTestLevels` |
| 33.7/33.8/33.9 | System/E2E/API | `engine.py` (`system_covered`) | `test_testing_strategy.py::TestTestLevels` |
| 33.11.1/33.11.2 | Agent Behaviour/Compliance | `engine.py` (`agent_compliance_tested`) | `test_testing_strategy.py::TestDomainSuites` |
| 33.13 | Decision Testing | `engine.py` (`decision_tested`) | `test_testing_strategy.py::TestDomainSuites` |
| 33.14 | Risk Testing | `engine.py` (`risk_tested`) | `test_testing_strategy.py::TestDomainSuites` |
| 33.19 | Security Testing | `engine.py` (`security_tested`) | `test_testing_strategy.py::TestQualityAttributes` |
| 33.21 | Reliability Testing | `engine.py` (`reliability_tested`) | `test_testing_strategy.py::TestQualityAttributes` |
| 33.22 | Failure Recovery Testing | `engine.py` (`failure_recovery_tested`) | `test_testing_strategy.py::TestQualityAttributes` |
| 33.23 | Regression Testing | `engine.py` (`regression_testing`) | `test_testing_strategy.py::TestQualityAttributes` |
| 33.26.1/33.26.2 | Acceptance Criteria / Result | `engine.py` (`acceptance_passed`) | `test_testing_strategy.py::TestAcceptanceAndAutomation` |
| 33.27 | Test Automation | `engine.py` (`automated`) | `test_testing_strategy.py::TestAcceptanceAndAutomation` |
| 33.29 | Test Evidence and Audit Trail | `engine.py` (`evidence_recorded`) | `test_testing_strategy.py::TestAcceptanceAndAutomation` |
| 33.1 | Testing Objectives | `engine.py` (`TestStrategyEngine`) | `test_testing_strategy.py::TestEngine` |
| — | Full Topic 33 contract | `registry.py` (+ traceability test) | `test_testing_strategy_registry.py` |

## Registry addition

Topic 33 (absent before) added as the authoritative 38-item block.
Captures `Nested Children`: 33.4.1 Test Case Definition, 33.4.2
Expected Result; 33.6.1 Integration Test Cases, 33.6.2 Interface
Validation; 33.11.1 Agent Behaviour Tests, 33.11.2 Agent Compliance
Tests; 33.26.1 Acceptance Test Criteria, 33.26.2 Acceptance Result.

## Validation

- `python -m pytest -m unit` → **661 passed** (20 from Topic 33)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (120 files)

## Notes / decisions

- Every unit case must declare its expected result before it counts
  (33.4.2).
- Integration testing is gated on interface validation (33.6.2);
  acceptance requires both defined criteria and a pass result
  (33.26).
- The strategy is automated and repeatable with auditable evidence to
  satisfy requirement traceability (33.27/33.29).