# Topic 39 — Future Expansion Framework

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-39-future-expansion`

## Decision

**Implementation required (core).** Topic 39 defines a governed,
gated path for expanding the product over time:

- **39.2 / 39.3 / 39.3.1 / 39.3.2**: expansion principles, scope
  expansion rules, trigger and preconditions.
- **39.4 / 39.4.1 / 39.4.2 / 39.5 / 39.5.1 / 39.5.2 / 39.6 / 39.7 /
  39.7.1 / 39.7.2**: market, geographic, currency and asset-class
  expansion (evaluation + approval).
- **39.8 / 39.9 / 39.10 / 39.11**: data-source, strategy, agent and
  sub-agent expansion.
- **39.12 / 39.13 / 39.14 / 39.15 / 39.15.1 / 39.15.2 / 39.16 /
  39.17 / 39.18 / 39.19**: infrastructure, technology, performance,
  capital (conditions + limits), risk, security, dashboard and
  monitoring scaling.
- **39.20 / 39.21 / 39.22**: multi-market, multi-currency and
  multi-strategy support.
- **39.23 / 39.24 / 39.25 / 39.25.1 / 39.25.2**: expansion
  validation, testing, readiness checklist and blocking conditions.
- **39.26 / 39.26.1 / 39.26.2 / 39.27 / 39.28**: expansion approval
  (authority + decision), rollback and audit trail.
- **39.29 / 39.30**: expansion roadmap and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 39.3.1/39.3.2 | Expansion Trigger / Preconditions | `engine.py` (`expansion_allowed`) | `test_expansion.py::TestExpansionValues` |
| 39.4.1/39.4.2 | New Market Evaluation / Approval | `engine.py` (`market_ok`) | `test_expansion.py::TestExpansionValues` |
| 39.5.1/39.5.2 | Geographic Readiness / Approval | `engine.py` (`geographic_ok`) | `test_expansion.py::TestExpansionValues` |
| 39.7.1/39.7.2 | Asset-Class Evaluation / Approval | `engine.py` (`asset_class_ok`) | `test_expansion.py::TestExpansionValues` |
| 39.15.1/39.15.2 | Capital Conditions / Limits | `engine.py` (`capital_scaling_ok`) | `test_expansion.py::TestScaling` |
| 39.25.1/39.25.2 | Readiness Checklist / Blockers | `engine.py` (`expansion_ready`) | `test_expansion.py::TestReleaseGate` |
| 39.26.1/39.26.2 | Approval Authority / Decision | `engine.py` (`expansion_approved`) | `test_expansion.py::TestReleaseGate` |
| 39.27 | Expansion Rollback | `engine.py` (`rollback_available`) | `test_expansion.py::TestReleaseGate` |
| 39.1 | Expansion Objectives | `engine.py` (`ExpansionEngine`) | `test_expansion.py::TestEngine` |
| — | Full Topic 39 contract | `registry.py` (+ traceability test) | `test_expansion_registry.py` |

## Registry addition

Topic 39 (absent before) added as the authoritative 44-item block.
Captures `Nested Children`: 39.3.1 Expansion Trigger, 39.3.2
Expansion Preconditions; 39.4.1 New Market Evaluation, 39.4.2 Market
Approval; 39.5.1 Geographic Readiness, 39.5.2 Geographic Approval;
39.7.1 Asset-Class Evaluation, 39.7.2 Asset-Class Approval; 39.15.1
Capital Scaling Conditions, 39.15.2 Capital Scaling Limits; 39.25.1
Readiness Checklist, 39.25.2 Blocking Conditions; 39.26.1 Approval
Authority, 39.26.2 Approval Decision.

## Validation

- `python -m pytest -m unit` → **772 passed** (17 from Topic 39)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (132 files)

## Notes / decisions

- Expansion requires an explicit trigger AND preconditions; no
  expansion starts by default (39.3).
- Market/geographic/asset-class expansion each need evaluation AND
  approval — a missing approval blocks the expansion
  (39.4.2/39.5.2/39.7.2).
- Capital scaling must satisfy conditions AND stay within limits
  (39.15).
- Expansion release requires readiness, authority + decision
  approval and a defined rollback (39.25-39.27).