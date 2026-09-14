# TOPIC 15 — Strategy Engine

> Phase 3 — Data & Intelligence
> Generated from the SRS. Authoritative requirements: `SRS.md` and `srs/topics/`.
> Governance: `MASTER.md`. Follow `docs/AUTONOMOUS_WORKFLOW.md` and
> `prompts/PROMPT_00_PROJECT_BOOTSTRAP.md`.

## Objective

Implement **Topic 15 — Strategy Engine** in full, consistent with the authoritative
requirements in `srs/topics/TOPIC_15.md` and the governance rules in
`MASTER.md`, without silently altering any frozen requirement or implementing
future topics.

## SRS Requirements Covered

`srs/topics/TOPIC_15.md` (Topic 15 — Strategy Engine)

## MASTER.md References

- §2 Source-of-Truth Hierarchy
- §3 Frozen SRS Hierarchy
- §5 Mandatory Specification Contract
- §8 Branching Strategy
- §9 Scope Discipline
- §11 Dependency Management
- §13 Testing Policy
- §14 Validation Policy
- §15 Security and Secrets
- §16 Financial Safety
- §19 Project Status
- §20 Agent Handoff
- §23 Git Commit Rules
- §24 Evidence and Traceability

## Preconditions

- Dependencies recorded `COMPLETED` in `PROJECT_STATUS.md`.
- No open governance conflicts affecting this topic (escalate via `docs/DECISIONS.md`).

## Dependencies

| TOPIC_13 — Market Analysis Engine | hard | see PROJECT_STATUS.md |
| TOPIC_14 — Opportunity Scoring Engine | hard | see PROJECT_STATUS.md |

## Existing Components To Reuse

- Bootstrap skeleton under `src/` relevant to this topic.
- `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/TESTING.md`.

## Files To Create

Define exact paths during planning; place code in the layer(s) this topic owns.

## Files To Modify

- `PROJECT_STATUS.md`
- `docs/AGENT_HANDOFF.md`
- `docs/DECISIONS.md` (only if material decisions are made)

## Implementation Requirements

Implement **only** Topic 15 as specified in `srs/topics/TOPIC_15.md`. Do
not implement future topics. Document any minimum supporting change required by
a dependency in `docs/DECISIONS.md`.

## Database Requirements

Defined by the topic requirements and dependency contracts. If none applies,
write: `Not Applicable — <reason>`.

## API Requirements

Defined by the topic requirements and external-system contracts. If none
applies, write: `Not Applicable — <reason>`.

## UI Requirements

Defined by the topic requirements. If none applies, write:
`Not Applicable — <reason>`.

## Business Logic Requirements

- Implement deterministic rules exactly as specified.
- Validate inputs before use; preserve identifiers, timestamps, provenance,
  authority, and state lineage.
- Reject ambiguity rather than inventing intent; fail closed when correctness
  is uncertain.

## Error Handling

Classify errors, preserve evidence, retry only when explicitly recoverable,
and escalate material failures. Record blocked-state and unblocking conditions
per the SRS contract.

## Security Requirements

- No secrets committed (`MASTER.md` §15).
- Respect the SRS safety boundary (`MASTER.md` §16): no simulated results
  presented as real, no unauthorized live action, no fabricated data/evidence.

## Testing Requirements

Map behavioural tests to the requirements of this topic (`MASTER.md` §13,
`docs/TESTING.md`): positive, negative, boundary, invalid/stale input,
authz/authn, safety, error handling, recovery, concurrency/idempotency,
integration, regression.

## Unit Tests

List the concrete unit tests required for this topic's components.

## Integration Tests

List the integration tests required at this topic's boundaries.

## End-to-End Tests

List the end-to-end tests or write `Not Applicable — <reason>`.

## Validation Commands

```bash
# Examples (only run commands supported by the project):
# pytest
# ruff check src tests
# mypy src
```

Run all applicable commands and record the exact results.

## Acceptance Criteria

- All Topic 15 requirements implemented, validated, traceable, tested, and
  within scope.
- No unresolved blocking defects, no silent requirement changes.
- Evidence and traceability recorded.

## Self-Review Checklist

- [ ] Every Topic 15 requirement implemented (no silent omissions).
- [ ] Tests validate behaviour and map to requirements.
- [ ] No unrelated/future-topic changes introduced.
- [ ] No secrets or generated junk staged.
- [ ] `PROJECT_STATUS.md`, `docs/AGENT_HANDOFF.md`, `docs/DECISIONS.md` updated.
- [ ] Validation actually executed (never claimed without running).

## Completion Criteria

Mark this topic `COMPLETED` only after every acceptance criterion, test, and
validation gate passes and evidence is recorded (`MASTER.md` §19).

## Git Branch

```text
feature/topic-15-strategy-engine
```

Create it from the current default branch after pulling. Never force-push.

## Commit Requirements

```text
feat(topic-15): <concise description>
```

## Final Report

Report: branch, commit SHA, requirements implemented, tests executed,
validation results, evidence, known limitations, unresolved blockers, and the
next recommended topic.
