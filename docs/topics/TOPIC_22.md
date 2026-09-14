# Topic 22 — Human Interaction and Notifications

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-22-interactions`

## Decision

**Implementation required (core).** Topic 22 adds the human touchpoints
required for supervised autonomy:

- **22.2 / 22.3 / 22.3.1 / 22.3.2 / 22.3.3**: human-in-the-loop and
  approval requirements (trigger, content, outcome).
- **22.4 / 22.4.1 / 22.4.2**: clarification requests.
- **22.5 / 22.5.1 / 22.5.2**: escalation requests and destinations.
- **22.6-22.15**: risk, error, system failure, blocked task, performance,
  P&L and security alerts across push/email/dashboard channels.
- **22.16 / 22.16.1 / 22.16.2**: priority levels and assignment.
- **22.17-22.22**: routing, deduplication, acknowledgement, retry,
  response timeout and escalation chain.
- **22.23 / 22.23.1 / 22.23.2**: non-blocking workflow interaction.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 22.3.1 | Approval Trigger | `engine.py` (`approval_required`) | `test_interactions.py::TestHumanInTheLoop` |
| 22.4.2 | Clarification Content | `engine.py` (`clarification_content`) | `test_interactions.py::TestHumanInTheLoop` |
| 22.5.1 | Escalation Trigger | `engine.py` (`escalation_triggered`) | `test_interactions.py::TestHumanInTheLoop` |
| 22.5.2 | Escalation Destination | `engine.py` (`escalation_destination`) | `test_interactions.py::TestHumanInTheLoop` |
| 22.23.1 | Non-Blocking Conditions | `engine.py` (`non_blocking`) | `test_interactions.py::TestHumanInTheLoop` |
| 22.16.2 | Priority Assignment | `engine.py` (`notification_priority_assigned`) | `test_interactions.py::TestNotifications` |
| 22.17 | Notification Routing | `engine.py` (`route_notification`) | `test_interactions.py::TestNotifications` |
| 22.6 | Risk Alerts | `engine.py` (`alert_triggered`) | `test_interactions.py::TestNotifications` |
| 22.18 | Notification Deduplication | `engine.py` (`Notification.dedupe_key`) | `test_interactions.py::TestNotifications` |
| 22.20 | Notification Retry | `engine.py` (`retry_pending`) | `test_interactions.py::TestNotifications` |
| 22.1/22.2 | Interaction Lifecycle | `engine.py` (`InteractionEngine`) | `test_interactions.py::TestEngine` |
| — | Full Topic 22 contract | `registry.py` (+ traceability test) | `test_interactions_registry.py` |

## Registry addition

Topic 22 (absent before) added as the authoritative 41-item block.
Captures `Nested Children`: 22.3.1 Approval Trigger, 22.3.2 Approval
Content, 22.3.3 Approval Outcome; 22.4.1 Clarification Trigger, 22.4.2
Clarification Content; 22.5.1 Escalation Trigger, 22.5.2 Escalation
Destination; 22.16.1 Priority Levels, 22.16.2 Priority Assignment;
22.23.1 Non-Blocking Conditions, 22.23.2 Blocking Conditions.

## Validation

- `python -m pytest -m unit` → **455 passed** (15 from Topic 22)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (98 files)

## Notes / decisions

- Approval triggers on high-value/high-risk actions: `kill`-class
  actions or notional ≥ 1000 (22.3.1).
- Escalation routes by level: level 1 → first line, level 2 → ops,
  higher → management (22.5.2).
- Deduplication keys on `(channel, event)` so the same event is not
  re-delivered per channel (22.18).
- Retry is allowed until `attempts == max_attempts`, after which the
  notification is considered failed (22.20).
- Channel routing and delivery are seams; transport adapters (email
  provider, push gateway) are integration scope.