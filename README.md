# AI Investment Opportunity Agent

An India/INR-scoped Proof of Value for a **bounded multi-agent system** that
finds, validates, analyses, scores, and (through clearly separated paper-trading
and simulation gates) acts on investment opportunities — with strict separation
between **analysis/decision** and **live execution**, enforce-able safety
controls, full auditability, and a user-visible dashboard.

This repository currently contains the **project bootstrap**: the authoritative
requirements, governance rules, architecture skeleton, autonomous development
prompt infrastructure, and tracking documents. Application features are
implemented incrementally as **Topics 1–40**.

---

## Quick Navigation

| Document | Purpose |
|---|---|
| [`SRS.md`](./SRS.md) | SRS index/navigation — how to read the authoritative requirements |
| [`srs/topics/`](./srs/topics/) | Authoritative per-topic requirements (`TOPIC_01.md` … `TOPIC_40.md`) — source of truth |
| [`MASTER.md`](./MASTER.md) | Implementation-governance operating rules for autonomous agents |
| [`PROJECT_STATUS.md`](./PROJECT_STATUS.md) | Per-topic implementation status |
| [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | Derived system architecture |
| [`docs/AUTONOMOUS_WORKFLOW.md`](./docs/AUTONOMOUS_WORKFLOW.md) | How every topic is implemented |
| [`docs/AGENT_HANDOFF.md`](./docs/AGENT_HANDOFF.md) | Where the next agent resumes |
| [`docs/TECHNICAL_PLAN.md`](./docs/TECHNICAL_PLAN.md) | Technical implementation roadmap (phases, DoD, gates) |
| [`docs/TOPIC_DEPENDENCY_GRAPH.md`](./docs/TOPIC_DEPENDENCY_GRAPH.md) | Topic order and dependencies |
| [`prompts/`](./prompts/) | Autonomous development prompts (PROMPT_00 variants + TOPIC_01..40) |

---

## Source-of-Truth Hierarchy

1. Approved SRS baseline and its controlled versions
2. Approved governance/change-control decisions
3. `MASTER.md`
4. Topic-specific implementation prompts
5. Agent assumptions

Neither `SRS.md` nor `MASTER.md` may be silently altered by an implementation
agent. Any material change requires the controlled change workflow defined in
`MASTER.md` (`§21`) and Topic 27 (SRS Governance).

---

## Project Scope (PoV Summary)

- **Geography / currency:** India, INR
- **Market data:** NSE/BSE and other authorized data sources
- **System type:** bounded multi-agent system (Master, Data, Analysis, Strategy,
  Risk, Testing, Monitoring, Dashboard, Notification agents, …)
- **Modes:** data acquisition → validation → discovery → analysis → scoring →
  strategy → risk → backtesting/paper trading → decision → (separately governed)
  execution
- **Non-goals (prohibited during PoV unless explicitly approved):**
  - unauthorized live financial execution
  - representing simulated results as real results
  - fabricating market data or performance evidence

---

## Repository Layout

```text
.
├── SRS.md                          # SRS index/navigation
├── srs/topics/                     # Authoritative per-topic requirements (01–40)
├── MASTER.md                       # Governance rules for autonomous development
├── PROJECT_STATUS.md               # Per-topic status
├── PROMPT_00_PROJECT_BOOTSTRAP.md  # The bootstrap prompt specification
├── pyproject.toml                  # Python project/build/test config
├── .env.example                    # Environment template (never real secrets)
├── docs/                           # Architecture, decisions, handoff, dependency graph
├── src/                            # Layered application skeleton (see ARCHITECTURE.md)
├── tests/                          # unit / integration / e2e
├── prompts/                        # Autonomous development prompt infrastructure
├── scripts/                        # Dev/ops helper scripts
├── config/                         # Versioned configuration
├── ci/                             # CI helpers
├── infra/                          # Docker / Kubernetes
└── data/                           # Raw/processed/validated/evidence (gitignored)
```

---

## Getting Started (Development)

> App features are implemented per-topic; this section describes the tooling
> foundation created during bootstrap.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

cp .env.example .env          # then fill in non-secret local defaults

pytest                        # run the test suite
ruff check src tests          # lint
ruff format --check src tests # format check
```

See [`docs/DEVELOPMENT.md`](./docs/DEVELOPMENT.md) and
[`docs/TESTING.md`](./docs/TESTING.md).

---

## Autonomous Development Model

The SRS is decomposed into **40 implementation topics** across 7 phases.
Each topic is implemented on its own feature branch
(`feature/topic-XX-<short-name>`) by an autonomous agent following the
workflow in [`docs/AUTONOMOUS_WORKFLOW.md`](./docs/AUTONOMOUS_WORKFLOW.md).

```text
Phase 1 (1–5):  Foundation
Phase 2 (6–9):  Architecture & Technical Specification
Phase 3 (10–15): Data & Intelligence
Phase 4 (16–20): Trading / Investment Simulation & Safety
Phase 5 (21–26): User Visibility & Reliability
Phase 6 (27–32): Multi-Agent Development
Phase 7 (33–40): QA & Release
```

See [`docs/TOPIC_DEPENDENCY_GRAPH.md`](./docs/TOPIC_DEPENDENCY_GRAPH.md) and
`prompts/TOPICS/TOPIC_01.md` … `TOPIC_40.md`.

---

## Security

- Never commit tokens, API keys, passwords, private keys, or real `.env` files.
- Use environment variables / a secret manager.
- `.env.example` documents the required variables.
- Live trading is **never** enabled without a separately governed authorization.
- See `MASTER.md` §15 (Security and Secrets) and §16 (Financial Safety).

---

## Status

- **Bootstrap:** COMPLETE (initial commit on the default branch).
- **Topics:** all 40 `COMPLETED` (see [`PROJECT_STATUS.md`](./PROJECT_STATUS.md)).
- **Next task:** none — the frozen SRS topic set is fully implemented and
  validated (799 unit tests; ruff/mypy clean). Registry verified 1:1 against
  the frozen hierarchy (1,758 requirement IDs); regenerate traceability
  evidence with `python scripts/gen_evidence.py`.