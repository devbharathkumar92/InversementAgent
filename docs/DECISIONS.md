# Decisions Record

Controlled decision/change log. Each material decision is recorded with a
stable ID, date, authority, and rationale. Decisions here never override an
explicit SRS requirement unless the change itself was authorized through the
controlled change workflow (see `MASTER.md` §21 and Topic 27).

---

## D-0001 — Bootstrap technology defaults are provisional

- **Date:** 2026-09-14
- **Authority:** Bootstrap prompt (`PROMPT_00`) + architecture constraints
- **Status:** PROVISIONAL — superseded by Topic 7 decisions
- **Decision:** The bootstrap skeleton adopts Python 3.11, FastAPI, SQLAlchemy 2
  + PostgreSQL, Celery + Redis, pandas/numpy, pytest, ruff, mypy, Docker,
  GitHub Actions as **default tooling** only.
- **Rationale:** These defaults satisfy the SRS Topic 7 constraints (deterministic
  controls, secure data/API integration, reproducible backtesting/paper trading,
  observable services, controlled costs, maintainable deployment).
- **Link:** `docs/ARCHITECTURE.md` §5. The authoritative technology-selection
  decisions are made under **Topic 7** and will be recorded here as D-000x.

---

## D-0002 — Repository SRS model: SRS.md index + srs/topics/ authoritative files

- **Date:** 2026-09-14
- **Authority:** SRS package (`AI_Investment_Agent_SRS_Repo_Files.zip`) + MASTER.md §3
- **Status:** ACTIVE
- **Decision:** The repository SRS model is:
  - `SRS.md` — index/navigation describing the SRS access model.
  - `srs/topics/TOPIC_01.md` … `TOPIC_40.md` — the complete authoritative
    per-topic requirements (source PDF pages retained per file).
  - `MASTER.md` — governance rules (identical to the SRS package copy).
  - `prompts/PROMPT_00_PROJECT_BOOTSTRAP.md` — official bootstrap prompt.
- **Link:** `SRS.md` "Repository layout" section; `MASTER.md` §3.

---

## D-0003 — Application features deferred to topics; skeleton is structural only

- **Date:** 2026-09-14
- **Authority:** PROMPT_00 §20 (bootstrap rule)
- **Status:** ACTIVE
- **Decision:** Bootstrap creates only structural/config/test-infrastructure
  placeholders. No business logic is implemented during bootstrap.
- **Link:** `docs/ARCHITECTURE.md`; `PROJECT_STATUS.md`.