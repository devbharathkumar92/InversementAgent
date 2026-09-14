# Technical Plan — AI Investment Opportunity Agent

> Roadmap for implementing the system described by the authoritative SRS.
> This plan is **derived** from the frozen SRS hierarchy (`SRS.md` +
> `srs/topics/TOPIC_01..40.md`), `MASTER.md` governance, and the bootstrap
> details in `docs/AGENT_HANDOFF.md`. It does **not** override any requirement
> or freeze any design before its owning topic is implemented.

---

## 1. Baseline (already verified)

| Area | Status |
|---|---|
| Repository bootstrap | ✅ Committed on `main` (`a9e1a0a`) |
| SRS access model | ✅ `SRS.md` + `srs/topics/TOPIC_01..40.md` |
| Governance | ✅ `MASTER.md` present and unmodified |
| Prompt infrastructure | ✅ `prompts/` (PROMPT_00 + TOPIC_01..40 + templates) |
| Project structure | ✅ `src/` layered skeleton matching SRS Topic 6 layers |
| Docs | ✅ `docs/ARCHITECTURE.md`, `DEVELOPMENT.md`, `TESTING.md`, `DECISIONS.md`, `AGENT_HANDOFF.md`, `TOPIC_DEPENDENCY_GRAPH.md` |
| Validation | ✅ `ruff` clean, `mypy` clean (40 src files), `pytest` 1 passed |
| CI | 🕓 Workflow template in `ci/workflows/ci.yml.example` (activation pending) |

**Source-of-truth rule (MASTER.md §2/§3):** every implementation step must read
`SRS.md` + the assigned `srs/topics/TOPIC_XX.md` + `MASTER.md`. Topic prompts are
executable summaries, never a substitute for the SRS.

---

## 2. Guiding Constraints (from MASTER.md §4 / SRS Topic 6)

- India / INR Proof-of-Value scope.
- **Bounded multi-agent** system; analysis/decision authority strictly
  separated from live execution authority.
- **Validated data flow** at every boundary.
- **Simulation and paper trading before live execution.**
- Dashboard visibility and auditability are mandatory.
- Safety controls enforceable (limits, stop-loss, kill switch, human gates).
- Determinism, provenance, state lineage, fail-closed behavior where required.
- No fabricated data/evidence; no unsupported assumptions become facts.

---

## 3. Implementation Strategy

### 3.1 Topic-driven incremental build

Each of the 40 SRS topics is implemented as one isolated unit on its own
feature branch, in dependency order:

```text
feature/topic-01-document-control
feature/topic-02-core-goal-mission
...
feature/topic-40-appendices
```

Rules (MASTER.md §8–§10, §29):

- Always branch from an up-to-date `main`.
- Implement **only the current topic** plus the minimum dependency-supporting
  work required; document any such foundation change.
- Run all validation before commit; capture evidence; update
  `PROJECT_STATUS.md` and `docs/AGENT_HANDOFF.md`.
- Push and report the exact commit/tag/pipeline result.

### 3.2 Phase sequence (MASTER.md §3)

The SRS is organized into seven phases. Each phase ends at a defined baseline
gate where tests and evidence must be green before the next phase begins.

| Phase | Topics | Theme | Exit baseline gate |
|---|---|---|---|
| P1 | 1–5 | Foundation | Scope/goal/principles baseline documented and approved |
| P2 | 6–9 | Architecture & Technical Specification | Architecture baseline + technology baseline frozen |
| P3 | 10–15 | Data & Intelligence | Data pipeline + discovery/analysis/scoring/strategy validated |
| P4 | 16–20 | Trading/Investment Simulation & Safety | Risk-gated backtest/paper-trade loop validated |
| P5 | 21–26 | User Visibility & Reliability | Dashboard + monitoring + observability operational |
| P6 | 27–32 | Multi-Agent Development | Sub-agent architecture, task spec, execution/branching plans |
| P7 | 33–40 | QA & Release | SRS-validation, SoD, integration, security, release criteria |

---

## 4. Per-Topic Definition of Done (executable contract)

For **every** topic, the implementing agent must produce (see `MASTER.md`
§26 and the topic prompt template):

1. **SRS mapping** — list of exact requirement IDs covered.
2. **Code** — only the components owned by this topic (+ documented
   dependency-supporting changes).
3. **Tests** — unit (+ integration/e2e where applicable) matching the
   requirement's testable behavior; no "code exists" assertions.
4. **Validation** — `ruff check`, `ruff format --check`, `mypy`, `pytest`
   all green.
5. **Evidence** — JSON/log/coverage artifacts under `data/evidences/`
   referencing requirement IDs.
6. **Traceability** — update `docs/TOPIC_DEPENDENCY_GRAPH.md` (or tracking
   table) to mark coverage.
7. **Status & handoff** — update `PROJECT_STATUS.md` and `docs/AGENT_HANDOFF.md`.
8. **Commit** — single focused commit (or logically grouped commits) with a
   message referencing the topic and requirement IDs.
9. **Report** — exact commit hash, validation output, remaining risks.

---

## 5. Phase-Level Technical Work

> Per-phase deliverables are directional and will be finalized by the owning
> topic's implementation (especially Topic 7 technology decisions).

### P1 — Foundation (Topics 1–5)

- Set up document control: versioned requirement IDs, change-control
  discipline, `docs/DECISIONS.md` (already partially present).
- Define PoV success measures and the system scope/boundary (what is in/out
  of scope for the India/INR PoV).
- Codify principles and non-negotiable rules (safety, separation, audit).

**Technical outputs:** governance/config docs, requirement–ID registry,
validation harness skeleton. Little-to-no runtime code.

### P2 — Architecture & Technical Specification (Topics 6–9)

- Topic 6: formalize the layered architecture (`src/` mirrors it).
- Topic 7: **freeze the technology baseline** — language, backend, DB, data
  processing, LLM/agent framework, scraping, real-time data, backtesting,
  paper trading, dashboard, notifications, authn/z, CI/CD, containerization,
  observability, local dev environment. Record every selection in
  `docs/DECISIONS.md` (D-000x).
- Topic 8: define agent determinism and specification completeness rules
  (machine-readable contracts, message schemas, interface contracts).
- Topic 9: define the system execution lifecycle (states and transitions).

**Technical outputs:** architecture baseline doc, technology baseline,
interface/contract schemas (JSON), state machine spec, CI pipeline activated.

### P3 — Data & Intelligence (Topics 10–15)

- Topic 10: `src/data_layer/acquire/` — approved India data sources
  (NSE/BSE), adapters, rate limiting, auth, historical + real-time.
- Topic 11: `src/data_layer/validate/` — quality rules, provenance checks,
  schema validation, `data/raw` → `data/validated` flow.
- Topic 12–15: `src/intelligence_layer/{discovery,market_analysis,scoring,
  strategy}/` — opportunity discovery, market analysis, scoring, strategy
  engines. LLM-assisted where Topic 7 approves; deterministic controls
  where required.

**Technical outputs:** data pipeline, validated data store, intelligence
models, scoring/strategy services with API contracts.

### P4 — Trading/Investment Simulation & Safety (Topics 16–20)

- Topic 16: `src/risk_safety_layer/` — limits, stop-loss, drawdown,
  liquidity/volatility/concentration risk, kill switch, human approval gates.
- Topic 17: `src/simulation_layer/backtesting/` — reproducible backtesting
  over validated historical data.
- Topic 18: `src/simulation_layer/paper_trading/` — broker sandbox, order
  simulation, position tracking.
- Topic 19: `src/decision_layer/` — eligibility, thresholds, ranking,
  allocation decisions, strictly gated.
- Topic 20: `src/observability_layer/` — real-time monitoring, P&L.

**Technical outputs:** safety engine, backtest/paper engine, decision engine,
P&L monitoring services. **No live execution enabled.**

### P5 — User Visibility & Reliability (Topics 21–26)

- Dashboard layer (`src/observability_layer/dashboard` + FastAPI reads),
  notifications, audit trail, error detection/recovery, self-evaluation,
  self-improvement hooks (change management).

**Technical outputs:** dashboard UI/API, alerting, audit store, retry/backoff
and recovery state machines.

### P6 — Multi-Agent Development (Topics 27–32)

- Sub-agent architecture (`src/agent_layer/*`): Master, Data, Analysis,
  Strategy, Risk, Testing, Monitoring, Dashboard, Notification, Background
  Checker, SRS Writer.
- Task specification for each agent, dependency/execution plan, parallel
  development plan.
- `src/task_runtime/`: state machine, queue, config.

**Technical outputs:** agent framework and message contracts, task runtime,
parallel-delivery playbook.

### P7 — QA & Release (Topics 33–40)

- Testing strategy, SRS self-validation, Definition of Done, integration &
  deployment, security/secrets management, PoV release criteria, future
  expansion framework, appendices.

**Technical outputs:** full regression suite, security hardening, release
runbook, final gate (`MASTER.md` §27).

---

## 6. Technical Decisions to Make (recorded as they are made)

| # | Decision | Owner topic | Recorded in |
|---|---|---|---|
| TD-1 | Technology baseline (backend, DB, LLM, agent framework, dashboard) | 7 | `docs/DECISIONS.md` D-000x |
| TD-2 | Approved data sources & acquisition stack | 10 / 7.10 | `docs/DECISIONS.md` |
| TD-3 | Data validation rules & schema versioning | 11 | `docs/DECISIONS.md` |
| TD-4 | Scoring/strategy model choice (deterministic vs LLM-assisted) | 12–15 / 7.7 | `docs/DECISIONS.md` |
| TD-5 | Broker sandbox & paper-trading infra | 18 / 7.13 | `docs/DECISIONS.md` |
| TD-6 | Dashboard framework & auth model | 21 / 7.14, 7.16 | `docs/DECISIONS.md` |
| TD-7 | Observability / audit storage choices | 20, 23 / 7.24 | `docs/DECISIONS.md` |
| TD-8 | Agent inter-communication protocol | 27–32 / 6.17 | `docs/DECISIONS.md` |
| TD-9 | CI/CD activation & release pipeline | 7.19, 36 | CI workflow |

Provisional bootstrap defaults (Python, FastAPI, SQLAlchemy/PostgreSQL,
Celery/Redis, pandas, Docker, GitHub Actions) are **non-binding** until TD-1.

---

## 7. Validation Gates

Executable per commit (root `pyproject.toml`):

```bash
python -m ruff check src tests scripts            # all checks passed
python -m ruff format --check src tests scripts   # formatting clean
python -m mypy src                                # no issues
python -m pytest -m unit                          # unit tests pass
```

Integration/e2e gates run as the corresponding topics land (data sources,
brokers, dashboards). A secret-scan is included in the CI pipeline; the
workflow template and activation steps live in `ci/workflows/` (see
`ci/workflows/README.md`).

---

## 8. Environment & Data Management

- `.env.example` documents required env vars; real secrets are **never**
  committed (MASTER.md §15).
- `data/{raw,interim,processed,validated,evidences}/` are the staged data
  stores; `.gitkeep` only in bootstrap; access controls at Topic 37.
- Dependency management per MASTER.md §11 (pin, audit, avoid bloat).

## 9. Key Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Scope creep beyond PoV | Strict branch-per-topic + DoD gate (MASTER §9/§26) |
| Technology mis-selection | Provisional defaults; freeze only at Topic 7 |
| Data source reliability/availability | Authorized-source list (Topic 10), validation & retries (Topic 11) |
| Fabricated/unsupported data | Validated flow + evidence store + provenance (MASTER §24) |
| Unauthorized live execution | Simulation-gated architecture; no live path until separate governance |
| Requirements drift | Frozen SRS hierarchy + change control (Topic 27) |

## 10. Milestones

| Milestone | Entry criteria | Exit criteria |
|---|---|---|
| M1 Bootstrap | — | Baseline committed; validation green (done) |
| M2 Architecture baseline | Bootstrap green | Topic 6 & 7 frozen; technology baseline recorded |
| M3 Data & intelligence loop | Architecture frozen | Data pipeline + discovery→strategy validated |
| M4 Simulation & safety loop | P3 green | Backtest/paper + risk gates validated |
| M5 Visibility & reliability | P4 green | Dashboard, alerts, audit, recovery operational |
| M6 Multi-agent system | P5 green | Agent architecture + task runtime operational |
| M7 PoV release candidate | P6 green | Full regression + security + Release Criteria met |

---

*Authoritative inputs: `SRS.md`, `srs/topics/*`, `MASTER.md`, `docs/ARCHITECTURE.md`, `docs/TOPIC_DEPENDENCY_GRAPH.md`. Updates must go through the controlled change workflow (MASTER.md §21).*