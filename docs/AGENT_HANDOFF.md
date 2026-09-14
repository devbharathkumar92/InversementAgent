# Agent Handoff

This file tells the next autonomous agent exactly where the project stands and
what to do next.

---

## Current State (bootstrap complete)

| Item | Value |
|---|---|
| Bootstrap | **COMPLETE** |
| Default branch | `main` |
| Topics implemented | None yet |
| Next topic | `TOPIC_01` — Document Control and Versioning |

## Authoritative Documents

Read these in order of authority before implementing any topic:

1. `SRS.md` — SRS index/navigation (Topics 1–40)
2. `srs/topics/TOPIC_NN.md` — authoritative requirements for the assigned topic
3. `MASTER.md` — implementation-governance operating rules
4. `prompts/PROMPT_00_PROJECT_BOOTSTRAP.md` and
   `PROMPT_00_PROJECT_BOOTSTRAP.md` (root, detailed) — bootstrap specs
5. `docs/ARCHITECTURE.md` — derived architecture
6. `docs/TECHNICAL_PLAN.md` — technical implementation roadmap (phases, DoD, gates)
7. `docs/DECISIONS.md` — decisions made so far

## What Has Been Completed

- [x] `SRS.md` (authoritative topic index) added
- [x] `srs/topics/TOPIC_01.md` … `TOPIC_40.md` (authoritative per-topic requirements) added
- [x] `MASTER.md` added (governance rules)
- [x] Project directory structure created (`src/`, `tests/`, `docs/`, `prompts/`, …)
- [x] Documentation suite created
- [x] Prompt infrastructure created (`prompts/TOPICS/TOPIC_01.md` … `TOPIC_40.md`)
- [x] Topic decomposition + dependency graph created
- [x] `PROJECT_STATUS.md` created
- [x] Testing infrastructure scaffolded (`pyproject.toml`, `tests/`)
- [x] CI workflow template added under `ci/workflows/`
  (activation steps in `ci/workflows/README.md`; needs a token with `workflow`
  scope or GitHub UI to activate)
- [x] `.env.example`, `.gitignore` created

## What Has NOT Been Done (planned work)

- **Topic 1** — Document Control and Versioning (first implementation topic)
- The authoritative tech-selection decisions under **Topic 7**
- All application code (data acquisition through execution)

## Next Recommended Topic

**`TOPIC_01` — Document Control and Versioning** (Phase 1 · Foundation)

1. Create branch `feature/topic-01-document-control`.
2. Follow `docs/AUTONOMOUS_WORKFLOW.md`.
3. Read `prompts/TOPICS/TOPIC_01.md`.
4. Implement, test, validate, capture evidence, update status + handoff, commit,
   push.

## Known Limitations

- The project is a **skeleton**: no application features implemented yet.
- `SRS.md` is the topic index; the authoritative requirements are the per-topic
  files under `srs/topics/`.
- Technology choices are provisional until Topic 7.
- No live execution path exists (by design); broker sandbox mode is enforced.

## Open Blockers

- Issue #1 ("add this file on this repo for reference this is Whole SRS document
  for this repo") is addressed by the commit on `main`, but could not be
  auto-closed via API: the repository PAT is fine-grained and scoped to Contents
  only (no Issues permission). Close it manually (or with an Issues-write token).

---

*Update this file after every topic (see `MASTER.md` §20).*