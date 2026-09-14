# System Architecture

> Derived from the authoritative `SRS.md` (Topics 6–9 are the Architecture &
> Technical Specification phase). This document reflects the **bootstrap-time
> architecture skeleton**, not a frozen final design. The authoritative
> architecture requirements are in `SRS.md` Topic 6, and the technology-selection
> decisions are made under Topic 7 (recorded in `docs/DECISIONS.md`).

---

## 1. Architecture Principles

Derived from SRS Topic 6 (High-Level System Architecture) and `MASTER.md`:

1. **Bounded multi-agent architecture** — specialized agents with separated
   responsibilities; analysis/decision authority strictly separated from any
   live execution authority.
2. **Data-flow validation** — every data boundary validates inputs, provenance,
   and quality before downstream use.
3. **Simulation before live execution** — backtesting and paper trading gates
   precede any (separately governed) live action.
4. **Safety controls are enforceable** — risk, limits, kill switches, and human
   approval gates are first-class components, not advisory.
5. **Dashboard visibility** — humans can observe system state, agents, tasks,
   decisions, and P&L (paper/simulated).
6. **Auditability** — every material event is traceable to requirement ID,
   version, actor/component, timestamp, evidence, and change linkage.
7. **Determinism where required** — explicit rules, versioned config, preserved
   identifiers/provenance/state lineage; fail closed on uncertainty.

---

## 2. Logical Layers

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                         HUMAN LAYER (dashboard, approvals)              │
│   src/observability_layer/dashboard · src/api            (21, 22)       │
├─────────────────────────────────────────────────────────────────────────┤
│                         AGENT LAYER                                      │
│   src/agent_layer/*  (Master, Data, Analysis, Strategy, Risk,           │
│                        Testing, Monitoring, Dashboard, Notification,    │
│                        Background Checker, SRS Writer)   (27–32)        │
├─────────────────────────────────────────────────────────────────────────┤
│                         TASK RUNTIME                                     │
│   src/task_runtime/*  (state machine, queue, config)       (31)         │
├─────────────────────────────────────────────────────────────────────────┤
│ INTELLIGENCE  │  DECISION        │  RISK / SAFETY                        │
│ discovery     │  src/decision_   │  src/risk_safety_layer                │
│ analysis      │  layer           │  (limits, stop-loss, kill switch,     │
│ scoring       │  (eligibility,   │   human approval gates)               │
│ strategy      │   ranking,       │                       (16, 19)        │
│ (12–15)       │   allocation)    │                                       │
├─────────────────────────────────────────────────────────────────────────┤
│ SIMULATION    │  EXECUTION        │  OBSERVABILITY                       │
│ backtesting   │  broker_adapters  │  logging · metrics · notifications   │
│ paper trading │  order_mgmt       │  (23, 24)                            │
│ (17, 18)      │  (governed, never│                                       │
│               │   auto-live)     │                                       │
├─────────────────────────────────────────────────────────────────────────┤
│ DATA LAYER: acquire → validate → storage → schemas   (10, 11)            │
│ SECURITY LAYER: auth · secret_management · audit      (37)               │
│ API LAYER: src/api/v1  (exposed via FastAPI)                             │
└─────────────────────────────────────────────────────────────────────────┘
```

Numbers in parentheses reference the SRS topics that own each component.

---

## 3. Core System Components (SRS Topic 6)

The architecture defines these component families (mirrored in `src/`):

- **Agent Layer** — Master Agent, Background Checker, SRS Writer, Data Agent,
  Analysis Agent, Strategy Agent, Risk Agent, Testing Agent, Monitoring Agent,
  Dashboard Agent, Notification Agent.
- **Background Monitoring Layer** — scheduled monitors (data freshness,
  validation health, safety limits, task states).
- **SRS Management Layer** — requirements registry, baseline control, change
  records, traceability.
- **Data Layer** — acquisition, validation/quality, storage, schemas.
- **Intelligence & Analysis Layer** — opportunity discovery, market analysis,
  scoring, strategy.
- **Decision Layer** — eligibility, thresholds, ranking, prioritization,
  capital-allocation decisions.
- **Risk & Safety Layer** — exposure/loss/drawdown limits, stop-loss,
  liquidity/volatility/concentration risk, kill switch, human approval gates.
- **Execution Layer** — broker adapters, order management; strictly gated and
  **never** auto-granted live authority.
- **Monitoring & P&L Layer** — real-time portfolio, position, order, market,
  strategy, risk monitoring; realized/unrealized P&L.
- **Dashboard Layer** — status views, agent/task status, progress, blocked
  tasks, errors, data source status, market analysis view.
- **Notification Layer** — alerts, approvals, escalations.
- **External Systems & API Layer** — NSE/BSE data, news, broker sandbox,
  LLM providers.
- **Inter-Agent Communication** — protocol, message contracts, interface
  contracts, I/O contracts.
- **Data/Control Flow** — data ownership, event/message routing, state
  management, state transitions.

---

## 4. Data Flow (primary)

```text
Market/News Data (NSE/BSE, authorized sources)
        │  (Topic 10 Data Acquisition)
        ▼
Acquisition layer ──► Validation & Quality (Topic 11)
        │                      │
        ▼                      ▼
   raw store             validated store
        │                      │
        └──────────────────────► Discovery (Topic 12)
                                   │
                                   ▼
                               Market Analysis (Topic 13)
                                   │
                                   ▼
                               Scoring (Topic 14)
                                   │
                                   ▼
                          Strategy Engine (Topic 15)
                                   │
                                   ▼
                             Risk / Safety (Topic 16)
                                   │
                                   ▼
              Backtesting (17) / Paper Trading (18)
                                   │
                                   ▼
                        Decision Engine (Topic 19)
                                   │
                                   ▼
                         Monitoring & P&L (20)
                         Dashboard (21) · Notifications (22)
                                   │
                                   ▼
              EXECUTION (separately governed, gated)
```

---

## 5. Technology Skeleton (bootstrap defaults)

> Exact selections are decided under **Topic 7** and recorded in
> `docs/DECISIONS.md`. There are **no binding technology decisions yet**;
> the defaults below are chosen because they satisfy the SRS constraints
> (deterministic controls, secure integration, reproducible backtesting,
> observable services, maintainable deployment).

| Concern | Bootstrap default | Rationale (constraints-compliant) |
|---|---|---|
| Language | Python ≥ 3.11 | Rich data/ML/trading ecosystem, deterministic controls |
| Backend API | FastAPI + Uvicorn | Async, typed, OpenAPI-native, testable |
| ORM / storage | SQLAlchemy 2 + PostgreSQL | Transactions, ACID, versioned schemas |
| Task queue | Celery + Redis | Background monitoring, scheduled jobs |
| Analysis/data | pandas / numpy | Reproducible backtesting & data processing |
| LLM | Provider-agnostic (OpenAI-compatible) | Agent layer; chosen under Topic 7 |
| Secrets | env vars / secret manager | Never in repo (`.env.example` only) |
| Container | Docker (+ Kubernetes optional) | Reproducible environments |
| CI | GitHub Actions | Traceable, repeatable validation |
| Testing | pytest (+ coverage) | Requirement-mapped testing |

---

## 6. Security and Safety Architecture

- **Separation of duties:** analysis/decision agents cannot submit live orders;
  execution is gated by risk + human approval and remains governed separately.
- **Kill switch / emergency stop:** fail-closed path defined in Topic 16.
- **Secret management:** no secrets in source; provided at runtime.
- **Audit:** structured audit trail for every material event (who/what/when/
  evidence/change linkage).

---

## 7. Deployment View (bootstrap)

- Local: `uvicorn src.api.v1.main:app`
- Workers: Celery workers for background/monitoring tasks
- Infra: `infra/docker` (compose) and `infra/kubernetes` (charts skeleton)

Full PoV release criteria are defined under Topic 38.