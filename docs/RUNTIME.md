# Runtime Orchestration

> Derived from the authoritative SRS topics 9/10–20/23/31 and
> `docs/ARCHITECTURE.md`. This document describes the **executable
> runtime path** that connects the existing deterministic engines.

---

## 1. Purpose

Before this feature the repository held the deterministic engine
implementations plus the FastAPI scaffold, but nothing instantiated the
engines into one executable workflow. This layer adds the smallest
production-quality runtime that wires them together and is proven by
tests.

The runtime is **synthetic/paper only**. It requires no live market
data, no broker credentials, no network access, and it cannot place a
real order.

---

## 2. Bounded runtime contract

Entry point: `src/task_runtime/orchestration/orchestrator.py`
(`RuntimeOrchestrator`).

```text
SyntheticInput (validated)
        │
        ▼
RuntimeOrchestrator.run()
        │
        ├── INPUT            synthetic provenance
        ├── VALIDATION       QualityEngine          (Topic 11)
        ├── DISCOVERY        DiscoveryEngine        (Topic 12)
        ├── MARKET_ANALYSIS  MarketAnalysisEngine   (Topic 13)
        ├── SCORING          ScoringEngine          (Topic 14)
        ├── STRATEGY         StrategyEngine         (Topic 15)
        ├── RISK             RiskEngine             (Topic 16)  [gate]
        ├── DECISION         DecisionEngine         (Topic 19)  [gate]
        ├── PAPER_TRADING    PaperEngine            (Topic 18)
        ├── PNL              MonitoringEngine       (Topic 20)
        └── AUDIT            AuditEngine            (Topic 23)
```

The stage order is frozen in `STAGE_ORDER` and asserted by tests.

### Gates

- **Validation** rejects stale/incomplete input (`REJECTED`).
- **Risk** rejection, kill-switch, or limit breach stops paper trading
  and everything after it (`REJECTED`).
- **Decision** no-action/rejection stops paper trading (`REJECTED`).
- **Upstream failure** produces a deterministic `FAILED` result and
  stops all downstream stages. No failure path can bypass safety.

### State machine

`src/task_runtime/state_machine/engine.py` implements the controlled
lifecycle:

```text
CREATED -> VALIDATING -> RUNNING -> COMPLETED
                     \-> REJECTED
                     \-> FAILED
```

Undefined transitions raise `InvalidTransitionError` and leave state
unchanged (fail-closed).

### Result

`ExecutionResult` (in `contracts.py`) is the bounded, deterministic
result: trace id, status, state, per-stage records and outputs, failure
detail, and `paper_only = True`. Trace ids are derived from the input
(`run-<asset>-<as_of>`) — never random.

---

## 3. API entry point

`POST /run/paper` (`src/api/v1/runtime.py`) accepts a validated
`SyntheticRunRequest` and returns the full `ExecutionResult`. Policy
overrides (`min_score`, `max_exposure_fraction`, `position_fraction`)
let a caller exercise the risk/decision gates.

---

## 4. Local execution

```bash
python -m uvicorn src.api.v1.main:app --host 0.0.0.0 --port 8000
curl -i http://127.0.0.1:8000/health
```

Deterministic synthetic request:

```bash
curl -s -X POST http://127.0.0.1:8000/run/paper \
  -H 'Content-Type: application/json' \
  -d '{
    "asset":"NSE:TESTCO","price":110.0,"prior_price":100.0,
    "volume":1000000.0,"avg_volume":100000.0,
    "volatility":0.4,"normal_volatility":0.2,"liquidity":0.9,
    "regime_ok":true,"projected_return":0.1,"risk":0.15,
    "reward":4.0,"risk_amount":1.5,"signal":"buy",
    "fetched_at":"2026-09-14T09:30:00Z","as_of":"2026-09-14T09:35:00Z",
    "capital":100000.0,"virtual_capital":100000.0
  }'
```

Or run the runtime directly:

```python
from src.task_runtime.orchestration import RuntimeOrchestrator, SyntheticInput

result = RuntimeOrchestrator(name="local").run(SyntheticInput(...))
print(result.status, result.pnl)
```

---

## 5. Celery / worker extension point

`docs/ARCHITECTURE.md` lists Celery + Redis as a **non-binding bootstrap
default** for background monitoring. This stage's goal is the first
local executable proof, so no broker/Redis infrastructure was added.

Extension point: a Celery task would call
`RuntimeOrchestrator(...).run(...)` unchanged; the orchestrator is
synchronous, deterministic, and free of infrastructure dependencies, so
it can be wrapped without modification. Deterministic tests remain
independent of Redis.

---

## 6. Remaining gaps (not implemented, not claimed)

- **Real-time market data** — the runtime consumes synthetic input only.
  NSE/BSE acquisition (Topic 10) is not wired to a live feed.
- **External news integration** — market analysis uses synthetic
  news-impact inputs.
- **Live broker execution** — no broker adapter, order management, or
  credentials are connected. Topic 19 gate is respected and live
  execution remains separately governed.
- **Backtesting replay (Topic 17)** — the backtest engine exists but is
  not on this runtime path.
- **Celery/Redis workers** — not introduced (see §5).
- **Production deployment** — out of scope; no autonomous deployment.

Nothing above is claimed as complete.