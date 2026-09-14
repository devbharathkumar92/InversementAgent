# Testing Guide

Testing is requirement-mapped: every topic defines the tests that prove its
requirements. This bootstrap establishes the testing **infrastructure** and
conventions; the suite grows topic by topic.

---

## 1. Test Hierarchy

```text
tests/
├── unit/          # Isolated units; no external services
├── integration/   # Local services (Postgres/Redis/test doubles for brokers)
├── e2e/           # Whole workflows through the public interfaces
└── fixtures/      # Shared fixtures, sample data, factories
```

Pytest markers: `unit`, `integration`, `e2e` (configured in `pyproject.toml`).

---

## 2. Running the Suite

```bash
pytest                        # everything
pytest -m unit                # fast unit tests only
pytest -m integration         # integration tests
pytest -m e2e                 # end-to-end tests
pytest --cov=src --cov-report=term-missing   # coverage
```

## 3. What Tests Must Cover (per topic)

Depending on the requirement, tests must cover (see `MASTER.md` §13):

- positive (happy path)
- negative (rejected inputs)
- boundary values
- invalid/stale/contradictory input
- authentication and authorization
- safety controls (e.g., risk limits, gates, kill switch)
- error handling and recovery
- concurrency / conflict / idempotency
- integration boundaries
- regression

A test must **validate behaviour** — not merely that a file, function, class,
or endpoint exists.

---

## 4. Determinism and Flakiness

- Tests must not depend on live market data or live LLM calls.
- External integrations are expressed with test doubles that implement the same
  interface contract.
- Time-dependent behaviour uses injected clocks.
- Randomness uses seeded generators.

---

## 5. Test Data

- Sample/raw fixtures live in `tests/fixtures/`.
- Large market datasets are **not** committed; they are generated or cached in
  git-ignored `data/` directories (or fetched by integration tests using
  recorded snapshots).

---

## 6. Validation Layers

See `MASTER.md` §14. Typical order:

```text
lint → mypy → unit → integration → e2e → security → traceability → acceptance
```

Each topic prompt lists the commands that must pass before completion.

---

## 7. HTML Coverage Reports

```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

`htmlcov/` is git-ignored.