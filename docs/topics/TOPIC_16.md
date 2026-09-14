# Topic 16 — Risk and Safety Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-16-risk-safety`

## Decision

**Implementation required (core).** Topic 16 is the risk envelope that
keeps the agent within capital-protection boundaries:

- **16.3 / 16.3.1 / 16.3.2**: maximum capital exposure and its
  calculation/enforcement.
- **16.4**: maximum position exposure.
- **16.5 / 16.6**: per-trade, aggregate and daily loss limits.
- **16.7 / 16.7.1 / 16.7.2**: drawdown limits, calculation and action.
- **16.8**: stop-loss enforcement.
- **16.12**: concentration risk controls.
- **16.13**: counterparty risk controls (escalation).
- **16.18 / 16.18.1**: kill-switch triggers.
- **16.19 / 16.19.1 / 16.19.2**: emergency-stop conditions/state.
- **16.20 / 16.20.1**: human approval gates.
- **16.21 / 16.21.1**: risk escalation thresholds.
- **16.22**: continuous risk monitoring.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 16.3.2/16.4 | Exposure Limits | `engine.py` (`exposes_within_limit`) | `test_risk.py::TestExposure` |
| 16.12 | Concentration Controls | `engine.py` (`concentration_exceeded`) | `test_risk.py::TestExposure` |
| 16.5/16.6 | Loss Limits | `engine.py` (`loss_within_limit`) | `test_risk.py::TestLossAndDrawdown` |
| 16.7/16.7.1 | Drawdown Limits | `engine.py` (`drawdown_within_limit`, `returns_below_drawdown`) | `test_risk.py::TestLossAndDrawdown` |
| 16.8 | Stop-Loss Enforcement | `engine.py` (`stop_loss_breached`) | `test_risk.py::TestStopLoss` |
| 16.18.1 | Kill-Switch Triggers | `engine.py` (`kill_switch_triggered`) | `test_risk.py::TestKillSwitch` |
| 16.20.1 | Human Approval Gates | `engine.py` (`approval_required`) | `test_risk.py::TestApprovalGates` |
| 16.22 | Risk Monitoring | `engine.py` (`RiskEngine.monitor`) | `test_risk.py::TestRiskEngine` |
| 16.21.1 | Escalation Threshold | `engine.py` (`RiskEngine.escalate`) | `test_risk.py::TestRiskEngine` |
| — | Full Topic 16 contract | `registry.py` (+ traceability test) | `test_risk_registry.py` |

## Registry addition

Topic 16 (absent before) added as the authoritative 45-item block. The
SRS topic file uses a different heading format (`Field Specification` /
`Nested Children` instead of `---`); every heading including the
nested children (16.7.1 Drawdown Calculation, 16.18.2/16.18.3,
16.19.2, 16.20.2, 16.21.1/16.21.2) was captured exactly, verified
against the SRS.

## Validation

- `python -m pytest -m unit` → **361 passed** (18 from Topic 16)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (86 files)

## Notes / decisions

- `risk` package is named per the repo convention (`src/common/risk/`).
- All checks are boundary-inclusive (`exposure <= cap` passes) so an
  exactly-at-limit state is not spuriously flagged.
- `approval_required` covers sensitive actions plus `kill`/`emergency`
  regardless of the sensitivity flag, matching REQ 16.20.1.
- Kill switch and escalation thresholds are strict (`>`), i.e. the
  switch fires only when the limit is genuinely crossed.