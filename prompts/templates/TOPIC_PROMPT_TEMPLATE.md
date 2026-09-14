# TOPIC XX — <TOPIC NAME>

> Template. Each generated topic prompt (in `prompts/TOPICS/`) is an instance of
> this template. The authoritative requirements are in `SRS.md`; governance is in
> `MASTER.md`.

## Objective

<What this topic must achieve.>

## SRS Requirements Covered

<Requirement IDs from SRS.md, e.g. "6.1–6.30".>

## MASTER.md References

<Relevant MASTER.md sections, e.g. §3, §8, §16.>

## Preconditions

<What must already be complete before starting this topic.>

## Dependencies

| Dependency | Type | Status in PROJECT_STATUS.md |
|---|---|---|
| <Topic NN> | hard/soft/blocking | <COMPLETED / …> |

## Existing Components To Reuse

<Files/components already in the repo that this topic builds on.>

## Files To Create

<Exact paths.>

## Files To Modify

<Exact paths.>

## Implementation Requirements

<Numbered requirements — MUST trace to SRS.md.>

## Database Requirements

<N/A or concrete. If N/A write "Not Applicable — <reason>".>

## API Requirements

<N/A or concrete.>

## UI Requirements

<N/A or concrete.>

## Business Logic Requirements

<Deterministic rules, validation, state transitions.>

## Error Handling

<Failure modes, blocked states, unblocking conditions, escalation.>

## Security Requirements

<Auth, secrets, safety boundaries applicable to this topic.>

## Testing Requirements

<Behavioural tests mapping to requirements.>

## Unit Tests

<List.>

## Integration Tests

<List.>

## End-to-End Tests

<List or "Not Applicable — <reason>".>

## Validation Commands

```bash
# Only existing/supported commands; never claim a check ran if it did not.
```

## Acceptance Criteria

<Verifiable conditions of acceptance.>

## Self-Review Checklist

- [ ] Every SRS requirement implemented (no silent omissions)?
- [ ] Tests map to requirements and validate behaviour?
- [ ] No unrelated changes introduced?
- [ ] No secrets committed?
- [ ] Docs/status/handoff updated?

## Completion Criteria

<Exactly when this topic may be marked COMPLETED.>

## Git Branch

```text
feature/topic-XX-<short-name>
```

## Commit Requirements

```text
feat(topic-XX): <concise description>
```

## Final Report

Report back: branch, commit SHA, requirements implemented, tests run, validation
results, evidence, known limitations, blockers (if any), and the recommended next
topic.