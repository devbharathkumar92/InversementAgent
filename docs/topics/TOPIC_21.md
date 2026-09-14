# Topic 21 — Dashboard and User Visibility

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-21-dashboard`

## Decision

**Implementation required (core).** Topic 21 surfaces the agent's
live state and pipeline outputs on a unified operator dashboard:

- **21.3 / 21.3.1 / 21.3.2**: agent status view with current activity.
- **21.5 / 21.6 / 21.6.1 / 21.6.2**: current task and progress
  percentage.
- **21.7 / 21.8**: task queue and dependency status.
- **21.9 / 21.9.1 / 21.9.2**: blocked task view with required action.
- **21.10-21.19**: error, data source, market analysis, opportunity,
  strategy, risk, portfolio, P&L, decision views and activity log.
- **21.21 / 21.21.1 / 21.21.2**: human approval requests and state.
- **21.22 / 21.23 / 21.24**: notification center, system health and
  performance view.
- **21.26**: search and filtering.
- **21.27 / 21.27.1 / 21.27.2**: user interaction incl. restricted
  actions.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 21.3.1 | Agent State | `engine.py` (`agent_status`) | `test_dashboard.py::TestAgentViews` |
| 21.3.2 | Agent Current Activity | `engine.py` (`agent_current_activity`) | `test_dashboard.py::TestAgentViews` |
| 21.6.1 | Progress Calculation | `engine.py` (`progress_percentage`) | `test_dashboard.py::TestAgentViews` |
| 21.9 | Blocked Task View | `engine.py` (`blocked_task`) | `test_dashboard.py::TestAgentViews` |
| 21.21.2 | Approval State | `engine.py` (`ApprovalState`) | `test_dashboard.py::TestViewsAndControls` |
| 21.23 | System Health View | `engine.py` (`system_health`) | `test_dashboard.py::TestViewsAndControls` |
| 21.26 | Search and Filtering | `engine.py` (`search_and_filter`) | `test_dashboard.py::TestViewsAndControls` |
| 21.27.2 | Restricted Actions | `engine.py` (`restricted_action`) | `test_dashboard.py::TestViewsAndControls` |
| 21.2/21.24 | Dashboard Lifecycle/Performance | `engine.py` (`Dashboard`) | `test_dashboard.py::TestDashboard` |
| — | Full Topic 21 contract | `registry.py` (+ traceability test) | `test_dashboard_registry.py` |

## Registry addition

Topic 21 (absent before) added as the authoritative 42-item block.
Captures `Nested Children`: 21.3.1 Agent State, 21.3.2 Agent Current
Activity; 21.4.1 Sub-Agent State, 21.4.2 Sub-Agent Progress; 21.6.1
Progress Calculation, 21.6.2 Progress Update; 21.9.1 Blocker Details,
21.9.2 Required Action; 21.21.1 Approval Request Details, 21.21.2
Approval State; 21.27.1 Allowed User Actions, 21.27.2 Restricted
Actions.

## Validation

- `python -m pytest -m unit` → **440 passed** (15 from Topic 21)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (96 files)

## Notes / decisions

- `restricted_action` implements the restricted-side of 21.27.2: a
  truthy result means the action is restricted and must be blocked.
- Progress is clamped to [0, 100] as a displayable percentage.
- The status views 21.10-21.21 are conceptually lightweight accessor
  views; approval state is a first-class enum so dashboard filters can
  group by PENDING/GRANTED/REJECTED.
- The dashboard lifecycle (`Dashboard`) carries a `ready` status and a
  render hook for the web layer.