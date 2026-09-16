# Data Acquisition Boundary (Topic 10)

> Derived from the authoritative SRS Topic 10 and `docs/ARCHITECTURE.md`
> §4. Describes the executable acquisition boundary and, deliberately,
> what it does **not** do.

---

## 1. Purpose

Topic 10 previously existed only as control-oriented helpers in
`src/common/acquisition/engine.py`, with `src/data_layer/acquire/`
containing nothing but an empty `__init__.py`. There was no way to
actually acquire, normalize, prove, or preserve a market-data record.

This layer adds the smallest executable boundary that closes that gap
while preserving the existing deterministic paper runtime.

```text
SOURCE -> ACQUISITION -> NORMALIZATION -> [Topic 11 VALIDATION] -> downstream
```

---

## 2. Entry point

```python
from src.data_layer.acquire import (
    AcquisitionRequest,
    AcquisitionService,
    DeterministicProvider,
    default_source_registry,
)

service = AcquisitionService(
    name="acquisition",
    registry=default_source_registry(),
    provider=DeterministicProvider(),
)
result = service.acquire(
    AcquisitionRequest(
        source_id="synthetic",
        asset="NSE:TESTCO",
        kind="market",
        timestamp="2026-09-14T09:30:00Z",
        as_of="2026-09-14T09:35:00Z",
        max_age_s=600.0,
    )
)
```

`result.record` is a `MarketDataRecord`; `result.evidence` is preserved
in `service.evidence_log()`.

---

## 3. Pipeline inside `acquire()`

| Step | Behaviour | Failure class |
|---|---|---|
| 1. Source vetting | Registered? supported kind? approved via `approve_source`? licensed? enabled? kind matches request? | `UNAPPROVED_SOURCE`, `MISSING_LICENSE`, `DISABLED_SOURCE` |
| 2. Rate budget | Deterministic call budget via the existing `rate_limit_exceeded` control | `RATE_LIMITED` |
| 3. Fetch | Across the `ProviderAdapter` boundary | `PROVIDER_ERROR`, `MALFORMED_RESPONSE` |
| 4. Admissibility | Provenance present? timestamp ISO-8601? fresh within `max_age_s`? | `MISSING_PROVENANCE`, `BAD_TIMESTAMP`, `STALE_DATA` |
| 5. Normalize | Typed `MarketDataRecord` + provenance + evidence | — |

Every outcome is classified and every outcome (success or not) is
recorded as evidence.

### Outcome semantics

* **REJECTED** — the source or the delivered *data* is not admissible.
  The system declines it and never substitutes another source.
* **FAILED** — the provider could not deliver a well-formed payload.

---

## 4. Time handling

Source time semantics are retained exactly as received in
`record.timestamp`; the explicit UTC representation is
`record.timestamp_utc`. Freshness is evaluated in UTC against the
request's `as_of` and `max_age_s`.

---

## 5. Determinism

Repeated acquisition of identical inputs produces identical normalized
data, provenance, acquisition id, status, and evidence. The acquisition
id is a SHA-256 digest of
`source_id | asset | timestamp | price | volume` — no clock, no
randomness, no UUID, no network ordering. This is asserted by tests.

---

## 6. Security

The boundary has no credentials, no API keys, and no secret fields. It
imports no network modules. Evidence carries only ids, timestamps, and
payload — never an `Authorization` header or token. Tests assert the
absence of secret-like keys and deny network access while acquiring.

---

## 7. Runtime integration

`runtime_market_fields(record)` maps an acquired record onto the runtime
input fields it genuinely owns:

```text
asset, price, volume, fetched_at
```

Analytics fields the runtime also needs (`prior_price`, `volatility`,
`projected_return`, `capital`, ...) are **not** invented by this layer.
They remain the caller's explicit responsibility, so acquired data is
never silently dressed up as analysis.

The default runtime path is unchanged: a `SyntheticInput` run still needs
no acquisition and still reports `source == "synthetic"`.

---

## 8. Production providers — BLOCKED, not invented

REQ 10.3.1/10.3.4 require an explicit approval and licensing decision
before a source may be used. **No such decision exists in this
repository.** Accordingly:

```python
from src.data_layer.acquire import production_provider_status

status = production_provider_status()
status.approved     # False
status.reason       # why approval is absent
status.candidates   # ("yfinance",)
```

`yfinance` is present as an optional dependency and is listed as a
*candidate only*. A dependency is not an authorization, and the code
never treats it as one. Enabling a real vendor requires a recorded
governance/licensing decision and a new `ProviderAdapter` implementation
— neither is added here.

---

## 9. Remaining gaps (not implemented, not claimed)

* **Live market data** — no live feed is wired. Only the deterministic
  synthetic provider exists.
* **Production vendor** — blocked pending an approval/licensing decision
  (see §8).
* **Retries** — REQ 10.18.1 is represented by classification and evidence,
  not by an automatic retry loop; retry policy is not defined yet.
* **Fallback source switching** — REQ 10.18.2 is deliberately absent:
  silent source substitution is prohibited.
* **Storage / historical backfill** — not on this path.
* **News / financial / economic / alternative providers** — source kinds
  are registered and vetted, but no provider implements them.

Nothing above is claimed as complete.

---

## 10. Tests

* `tests/unit/topic_10/test_acquisition_boundary.py` — 38 tests covering
  registration, rejection paths, deterministic acquisition, schema,
  timestamps, provenance/evidence, determinism, rate limits, failure
  classification, security, and Topic 11 integration.
* `tests/integration/test_acquisition_runtime_end_to_end.py` — acquired
  data -> Topic 11 shape -> runtime, plus proof the default synthetic
  runtime path is unchanged.
