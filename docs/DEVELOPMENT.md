# Development Guide

This guide explains how to set up the local environment for developing the
AI Investment Opportunity Agent. During bootstrap, application features are not
yet implemented — this documents the **tooling foundation**.

---

## 1. Prerequisites

- Python ≥ 3.11
- Git
- (Recommended) PostgreSQL and Redis for local integration tests

---

## 2. Local Setup

```bash
git clone https://github.com/devbharathkumar92/InversementAgent.git
cd InversementAgent

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -e ".[dev]"

cp .env.example .env             # fill in local non-secret defaults
```

> `.env` is git-ignored. Never commit it.

---

## 3. Project Structure (Development View)

```text
src/
├── agent_layer/         # Autonomous agents (Topic 27–32)
├── data_layer/          # acquisition, validation, storage, schemas (10–11)
├── intelligence_layer/  # discovery, market analysis, scoring, strategy (12–15)
├── decision_layer/      # decision engine (19)
├── risk_safety_layer/   # risk & safety controls (16)
├── simulation_layer/    # backtesting (17), paper trading (18)
├── execution_layer/     # broker adapters, order management (gated)
├── observability_layer/ # logging, metrics, dashboard, notifications (20–24)
├── security_layer/      # auth, secret management, audit (37)
├── task_runtime/        # state machine, orchestration, queue, config (9/31)
├── api/v1/              # REST API (FastAPI)
├── worker/celery_app/   # Celery tasks (background monitoring)
└── common/              # shared helpers, contracts, exceptions
```

---

## 4. Running Checks

```bash
# Tests
pytest

# With coverage
pytest --cov=src --cov-report=term-missing

# Lint
ruff check src tests

# Format
ruff format --check src tests

# Type checking
mypy src
```

> Only run commands that exist in this project. If a check cannot run yet (some
> topics not implemented), record the exact reason — never claim it passed.

---

## 5. Environment Variables

See [`.env.example`](../.env.example). Key variables:

| Variable | Purpose |
|---|---|
| `APP_ENV` | Runtime environment |
| `POSTGRES_*` | Database connection |
| `REDIS_URL` | Redis connection |
| `SECRET_KEY` / `JWT_SECRET` | Signing keys (runtime-injected) |
| `LLM_*` | LLM provider settings |
| `BROKER_SANDBOX_MODE` | Must stay `true` during PoV |
| `PAPER_TRADING_ENABLED` | Paper-trading gate |

---

## 6. Git Branch Model

See [`docs/AUTONOMOUS_WORKFLOW.md`](./AUTONOMOUS_WORKFLOW.md) for the full
workflow. In short:

- Default/integration branch: `main`
- Each topic gets its own branch: `feature/topic-XX-<short-name>`
- No force-push; no rewriting protected history

---

## 7. Local Services (optional, for later integration topics)

```bash
# Run PostgreSQL + Redis via docker-compose
docker compose -f infra/docker/docker-compose.yml up -d
```

---

## 8. Conventions

- Python style: PEP 8 with `ruff`; lines ≤ 100 chars.
- Type hints required (mypy strict).
- Tests validate behaviour, not mere file/function existence.
- Never commit secrets; inspect `git diff` before committing.
- Documentation changes must stay consistent with `SRS.md`.