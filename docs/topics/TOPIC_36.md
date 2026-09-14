# Topic 36 — Integration and Deployment

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-36-integration-deployment`

## Decision

**Implementation required (core).** Topic 36 defines how components
are integrated and how the product is promoted through environments
to production:

- **36.2 / 36.3 / 36.4 / 36.5 / 36.6 / 36.7 / 36.8 / 36.9 / 36.10 /
  36.11 / 36.12**: integration architecture for components, agents,
  data, APIs, database, dashboard, notifications, risk engine,
  monitoring and configuration.
- **36.13 / 36.13.1 / 36.13.2 / 36.14 / 36.14.1 / 36.14.2 /
  36.15**: branch integration rules, merge preconditions, merge
  validation/failure and integration testing.
- **36.16 / 36.16.1 / 36.16.2 / 36.17 / 36.18 / 36.19 / 36.20**:
  deployment environments (dev, testing, staging, production) with
  promotion rules.
- **36.21 / 36.21.1 / 36.21.2 / 36.22 / 36.23**: deployment process,
  steps, gates, validation and monitoring.
- **36.24 / 36.24.1 / 36.24.2 / 36.25 / 36.25.1 / 36.25.2**:
  rollback strategy and disaster recovery.
- **36.26 / 36.27 / 36.28 / 36.29 / 36.30**: release management,
  audit trail, deployment security, acceptance criteria and change
  control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 36.3/36.5/36.6 | Component/Data/API Integration | `engine.py` (`integration_complete`) | `test_integration_deploy.py::TestIntegration` |
| 36.13.1/36.13.2 | Branch Rules / Merge Preconditions | `engine.py` (`branch_merge_allowed`) | `test_integration_deploy.py::TestIntegration` |
| 36.16.1 | Environment Definitions | `engine.py` (`environment_defined`) | `test_integration_deploy.py::TestDeployment` |
| 36.16.2/36.21.2 | Promotion Rules / Gates | `engine.py` (`promotion_ok`, `gate_passed`) | `test_integration_deploy.py::TestDeployment` |
| 36.22/36.23 | Deployment Validation / Monitoring | `engine.py` (`deployment_validated`) | `test_integration_deploy.py::TestDeployment` |
| 36.29 | Deployment Acceptance Criteria | `engine.py` (`deployment_accepted`) | `test_integration_deploy.py::TestDeployment` |
| 36.24.1/36.24.2 | Rollback Trigger / Procedure | `engine.py` (`rollback_possible`) | `test_integration_deploy.py::TestRecovery` |
| 36.25.1/36.25.2 | Recovery Objective / Procedure | `engine.py` (`recovery_ok`) | `test_integration_deploy.py::TestRecovery` |
| 36.26/36.27 | Release Management / Audit | `engine.py` (`release_managed`) | `test_integration_deploy.py::TestRecovery` |
| 36.1 | Integration Objectives | `engine.py` (`IntegDeployEngine`) | `test_integration_deploy.py::TestEngine` |
| — | Full Topic 36 contract | `registry.py` (+ traceability test) | `test_integration_deploy_registry.py` |

## Registry addition

Topic 36 (absent before) added as the authoritative 42-item block.
Captures `Nested Children`: 36.13.1 Branch Integration Rules,
36.13.2 Merge Preconditions; 36.14.1 Merge Validation, 36.14.2 Merge
Failure; 36.16.1 Environment Definitions, 36.16.2 Environment
Promotion Rules; 36.21.1 Deployment Steps, 36.21.2 Deployment Gates;
36.24.1 Rollback Trigger, 36.24.2 Rollback Procedure; 36.25.1
Recovery Objective, 36.25.2 Recovery Procedure.

## Validation

- `python -m pytest -m unit` → **717 passed** (19 from Topic 36)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (126 files)

## Notes / decisions

- Integration completeness spans components, data and APIs; an
  unvalidated API blocks integration (36.6).
- Branch merges require both integration rules and preconditions
  (36.13), matching Topics 31/32 merge-gate contracts.
- Environment promotion is gated; a deployment is accepted only when
  acceptance criteria are met (36.29).
- Rollback and disaster-recovery paths are mandatory before release
  (36.24/36.25).