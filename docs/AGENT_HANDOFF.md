# Agent Handoff

This file tells the next autonomous agent exactly where the project stands and
what to do next.

---

## Current State (all topics implemented)

| Item | Value |
|---|---|
| Bootstrap | **COMPLETE** |
| Default branch | `main` |
| Topics implemented | **40 / 40 — all `COMPLETED`** |
| Latest `main` commit | `23a3dd5` (registry completeness fix) |
| Unit tests | **799 passed** (3 warnings) |
| Lint / types | `ruff check` + `ruff format` clean; `mypy` clean (136 files) |
| Requirement IDs registered | **1,758** across 40 topics, verified 1:1 against `srs/` |
| Evidence | `python scripts/gen_evidence.py` → `data/evidences/evidence.json` |

## Authoritative Documents

Read these in order of authority before changing anything:

1. `SRS.md` — SRS index/navigation (Topics 1–40)
2. `srs/topics/TOPIC_NN.md` — authoritative frozen requirements per topic
3. `MASTER.md` — implementation-governance operating rules
4. `prompts/PROMPT_00_PROJECT_BOOTSTRAP.md` and
   `PROMPT_00_PROJECT_BOOTSTRAP.md` (root, detailed) — bootstrap specs
5. `docs/ARCHITECTURE.md` — derived architecture
6. `docs/TECHNICAL_PLAN.md` — technical implementation roadmap (phases, DoD, gates)
7. `docs/DECISIONS.md` — decisions made so far
8. `PROJECT_STATUS.md` — per-topic status, branch, verification, commit

## What Has Been Completed

- [x] `SRS.md` (authoritative topic index) added
- [x] `srs/topics/TOPIC_01.md` … `TOPIC_40.md` (authoritative per-topic requirements) added
- [x] `MASTER.md` added (governance rules)
- [x] Project directory structure created (`src/`, `tests/`, `docs/`, `prompts/`, …)
- [x] Documentation suite created
- [x] Prompt infrastructure created (`prompts/TOPICS/TOPIC_01.md` … `TOPIC_40.md`)
- [x] Topic decomposition + dependency graph created
- [x] `PROJECT_STATUS.md` created and maintained
- [x] Testing infrastructure scaffolded (`pyproject.toml`, `tests/`)
- [x] CI workflow template added under `ci/workflows/`
  (activation steps in `ci/workflows/README.md`; needs a token with `workflow`
  scope or GitHub UI to activate)
- [x] `.env.example`, `.gitignore` created
- [x] **All 40 topics implemented test-driven**, each on its own
  `feature/topic-NN-*` branch, validated (ruff/mypy/full suite), then merged to
  `main`. Per-topic docs live under `docs/topics/TOPIC_NN.md`.
- [x] **Requirement registry completed** — a cross-check of every frozen SRS
  topic against `src/common/requirements/registry.py` surfaced 8 headings that
  earlier extraction had skipped (`7.11`, `7.27`, `8.6.2`, `19.15.1`,
  `20.9.1–20.9.3`, `26.25.2`). They are now registered and locked by
  `tests/unit/requirements/test_registry_gaps.py`
  (see `docs/topics/TOPIC_REGISTRY_COMPLETENESS.md`).
- [x] **Evidence generation** — `src/common/evidence/` + `scripts/gen_evidence.py`
  emit `data/evidences/evidence.json`, answering the MASTER.md §24 traceability
  questions (requirement IDs, source modules, tests, spec/doc, commit) for every
  topic. Covered by `tests/unit/evidence/test_evidence_generator.py`.

## What Has NOT Been Done (planned work)

Nothing outstanding against the frozen SRS. Optional / non-SRS follow-ups:

- **Activate CI** from `ci/workflows/` (needs a token with `workflow` scope, or
  the GitHub UI).
- **Close issue #1** manually — the repository PAT is fine-grained and scoped to
  Contents only (no Issues permission).

## Next Recommended Action

No topic remains. To extend the project, add a new SRS topic first, then
follow `docs/AUTONOMOUS_WORKFLOW.md`:

1. Create branch `feature/topic-NN-<name>`.
2. Write unit tests for the topic's requirement IDs.
3. Implement until the suite is green.
4. Validate with `ruff check`, `ruff format --check`, `mypy src`, and the full
   pytest suite; capture evidence.
5. Update `docs/topics/TOPIC_NN.md`, `PROJECT_STATUS.md`, and this handoff;
   commit, push, merge to `main`.

## Known Limitations

- The SRS topics are specified, tested, and validated, but much of the runtime
  behaviour is a **specification contract** rather than a live trading system.
- `SRS.md` is the topic index; the authoritative requirements are the per-topic
  files under `srs/topics/`.
- Technology baseline is frozen by Topic 7 (`docs/DECISIONS.md`, D-000x).
- No live execution path exists (by design); broker sandbox mode is enforced.

## Open Blockers

- Issue #1 ("add this file on this repo for reference this is Whole SRS document
  for this repo") is addressed by the commit on `main`, but could not be
  auto-closed via API: the repository PAT is fine-grained and scoped to Contents
  only (no Issues permission). Close it manually (or with an Issues-write token).

---

*Update this file after every topic (see `MASTER.md` §20).*