# Autonomous Development Workflow

This is the canonical workflow that every **topic agent** must follow to
implement one SRS topic. It is defined by `MASTER.md` and this document
together.

---

## 0. Authority

For every topic, the agent must read (in order of authority):

```text
SRS.md
MASTER.md
current topic prompt (prompts/TOPICS/TOPIC_NN.md)
PROJECT_STATUS.md
docs/AGENT_HANDOFF.md
docs/DECISIONS.md
docs/ARCHITECTURE.md
```

Never implement based only on the topic prompt if `SRS.md` or `MASTER.md`
contains additional constraints.

---

## The Lifecycle

```text
READ
 ↓
UNDERSTAND
 ↓
AUDIT CURRENT REPOSITORY
 ↓
CHECK DEPENDENCIES
 ↓
PLAN
 ↓
CREATE FEATURE BRANCH          feature/topic-NN-<short-name>
 ↓
IMPLEMENT ONLY CURRENT TOPIC
 ↓
WRITE / UPDATE TESTS
 ↓
RUN VALIDATION
 ↓
SELF-REVIEW
 ↓
FIX FAILURES
 ↓
RUN REGRESSION TESTS
 ↓
CAPTURE EVIDENCE
 ↓
UPDATE TRACEABILITY / STATUS    PROJECT_STATUS.md, docs/DECISIONS.md,
                                docs/AGENT_HANDOFF.md
 ↓
COMMIT
 ↓
PUSH
 ↓
HAND OFF TO NEXT TOPIC         docs/AGENT_HANDOFF.md
```

---

## Phase Details

### 1. READ
- Read the authoritative documents and topic prompt completely.
- Determine prerequisite topics and inspect their outputs.

### 2. UNDERSTAND
- Identify the requirements assigned to this topic.
- Identify what already exists (from earlier topics / bootstrap skeleton).
- Identify required config, schemas, API, UI, and evidence.

### 3. AUDIT CURRENT REPOSITORY
- `git status`, inspect `src/` for related components, run existing tests.
- Do not blindly overwrite existing work.

### 4. CHECK DEPENDENCIES
- Identify hard / soft / blocking dependencies and downstream consumers.
- A blocked topic must record the blocker (see `MASTER.md` §11) — never silently
  bypass it.

### 5. PLAN
- Produce an implementation plan: files created/modified, interfaces, data
  model changes, tests, validation commands.
- Avoid unrelated changes.

### 6. CREATE FEATURE BRANCH
```bash
git checkout main
git pull
git checkout -b feature/topic-NN-<short-name>
```
One branch per topic. Do not implement multiple unrelated topics in one branch.

### 7. IMPLEMENT ONLY THE CURRENT TOPIC
- Implement exactly the requirements of this topic, plus only the minimum
  supporting changes required by dependencies (document such changes).
- Do not implement future topics prematurely.
- Do not fabricate external integrations or fake data/evidence.
- Do not weaken safety controls.

### 8. WRITE / UPDATE TESTS
- Map tests to requirements (`MASTER.md` §13).
- Test behaviour, not file existence.

### 9. RUN VALIDATION
- Run the topic's documented validation commands (lint, mypy, unit,
  integration, etc.).
- Use only commands that exist. Never claim a check passed if it was not run.

### 10. SELF-REVIEW
- Compare implementation against SRS, MASTER, topic prompt, acceptance criteria.
- Check edge cases, error paths, security, secrets, documentation, config.

### 11. FIX FAILURES
- Root-cause → fix → rerun. Repeat until green or genuinely blocked.
- Never hide failures or mark a failed task complete.

### 12. RUN REGRESSION
- Run the full existing suite to confirm nothing else broke.

### 13. CAPTURE EVIDENCE
- Record: requirement IDs implemented, files, tests, validation commands and
  results, config/version used, agent/actor, timestamp, commit.

### 14. UPDATE TRACEABILITY / STATUS
- Update `PROJECT_STATUS.md` for this topic.
- Update `docs/DECISIONS.md` for any decisions or deviations.
- Update `docs/TOPIC_DEPENDENCY_GRAPH.md` if dependency edges changed.
- Update `docs/AGENT_HANDOFF.md`.

### 15. COMMIT
```bash
git status
git diff
git diff --check
git add <files>
git commit -m "feat(topic-NN): <short description>"
```
Verify: no secrets, no unrelated files, no generated junk, no accidental
requirement changes.

### 16. PUSH
```bash
git push -u origin feature/topic-NN-<short-name>
```
No force-push. If a PR is desired after governance approval, open one against
`main`; never merge to `main` directly without governance.

### 17. HAND OFF
- Fill `docs/AGENT_HANDOFF.md` with completed topic, branch, commit, tests run,
  validation results, evidence, known limitations, unresolved blockers, and the
  next recommended topic, so the next agent can resume without reconstructing
  history.

---

## Branch Naming

```text
feature/topic-01-document-control
feature/topic-02-core-goal-mission
...
feature/topic-40-glossary
```

---

## Definition of Done

A topic is done only when:

- [ ] All requirements implemented (no silent omissions)
- [ ] Tests written and passing (mapped to requirements)
- [ ] Validation commands pass (or exact reason recorded)
- [ ] Regression suite passes
- [ ] Evidence captured
- [ ] `PROJECT_STATUS.md`, `docs/DECISIONS.md`, `docs/AGENT_HANDOFF.md` updated
- [ ] Git diff reviewed (no secrets, no junk)
- [ ] Committed with a meaningful message
- [ ] Pushed to its feature branch
- [ ] Not merged to `main` without governance approval