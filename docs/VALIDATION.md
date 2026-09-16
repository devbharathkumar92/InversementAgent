# Validation & Quality Boundary (Topic 11)

> Derived from the authoritative SRS Topic 11 and `docs/ARCHITECTURE.md`.
> Describes the executable validation boundary, its threshold policy, and
> what it deliberately does **not** do.

---

## 1. Purpose

Topic 11 previously existed only as primitives in
`src/common/quality/engine.py`, with `src/data_layer/validate/` containing
nothing but an empty `__init__.py`. There was no way to execute a full
validation, reach a disposition, or preserve evidence.

This layer adds the smallest executable boundary that consumes Topic 10
acquisition output and prevents invalid or uncertain data from silently
reaching downstream intelligence.

```text
Topic 10 ACQUIRED
        |
        v
   VALIDATION  -->  ACCEPTED     (downstream usable)
             \-->  REJECTED     (invalid/inadmissible)
             \-->  QUARANTINED  (uncertain / unverifiable)
                        |
                        v
                RECOVERY -> REVALIDATION -> accepted | still blocked
```

---

## 2. Threshold policy (the important part)

`srs/topics/TOPIC_11.md` (4800 lines) requires thresholds to exist as
version-controlled controls (11.2.2 missing-field thresholds, 11.20.2
confidence thresholds, 11.21 quality thresholds) but **never states a
numeric value**. A regex for `\d+ %`, `percent`, or `seconds` over the whole
file returns an empty set.

Therefore:

* every threshold is caller-supplied configuration in `QualityRules`;
* a *required* check whose threshold was not configured fails closed:
  `THRESHOLD_UNCONFIGURED` -> `QUARANTINED`;
* no magic value is ever invented.

`QualityRules.version` is mandatory and is traced through the result,
evidence, report, and audit entry (11.30).

---

## 3. Entry point

```python
from src.data_layer.validate import (
    CheckName, QualityRules, ValidationService, request_from_acquisition,
)

rules = QualityRules(
    version="t11-rules-v1",
    schema_version="t11-schema-v1",
    required_fields=("asset", "price", "volume", "timestamp_utc"),
    max_age_s=600.0,
    required_checks=frozenset({CheckName.FRESHNESS}),
)
service = ValidationService(name="validation", rules=rules)
result = service.validate(
    request_from_acquisition(acquired, rules=rules, as_of="2026-09-14T09:35:00Z")
)
```

`request_from_acquisition()` raises `ValueError` if the acquisition carries
no record — nothing is fabricated.

---

## 4. Checks

| Check | Requirement | Threshold source |
|---|---|---|
| `COMPLETENESS` | 11.2/11.2.1 | `required_fields`, `max_missing` |
| `MISSING_THRESHOLD` | 11.2.2 | `max_missing` |
| `INTEGRITY` | 11.6 | — (present fields must not be `None`) |
| `PROVENANCE` | 11.21.1 | — (source and acquisition id must match) |
| `INVALID_TYPE` | 11.9 | — (numeric fields; invalid characters) |
| `TIMESTAMP` | 11.13 | — |
| `CONSISTENCY` | 11.4 | — (identity + source/UTC instant agreement) |
| `FRESHNESS` | 11.5 | `max_age_s` + caller `as_of` |
| `DUPLICATES` | 11.7 | — (acquisition-id identity) |
| `ACCURACY` | 11.3 | `accuracy_tolerance` + caller `reference` |
| `ANOMALY` | 11.10 | `anomaly_tolerance` (severity via existing `severity_grade`) |
| `OUTLIER` | 11.11 | `outlier_tolerance` + caller `baseline` |
| `CROSS_SOURCE` | 11.12/11.19 | `accuracy_tolerance` + caller `peers` |
| `CONFIDENCE` | 11.20 | `min_confidence` |

`CORE_CHECKS` always run. Other checks run when configured **and** listed in
`required_checks`.

`CROSS_SOURCE` reports conflicts and **never** resolves them: no
authoritative source-precedence rule exists in the repository, so silently
preferring one source is prohibited (11.12.2).

---

## 5. Dispositions

* **ACCEPTED** — every required check passed; `downstream_usable is True`.
* **REJECTED** — definitively invalid/inadmissible: bad type, missing
  provenance, provenance mismatch, version mismatch, bad timestamp, too many
  missing fields, integrity failure, stale, duplicate, inconsistent.
* **QUARANTINED** — correctness uncertain or unverifiable: unconfigured
  threshold, confidence below threshold, conflict, accuracy out of
  tolerance, anomaly, outlier, unsupported domain.

A detected conflict is reported ahead of `UNVERIFIABLE`, since positive
evidence of a problem outranks "could not check".

Rejected and quarantined records are stored in the quarantine with reason,
provenance, and rule version, and are never reported as downstream-usable.

**Recovery (11.22.3/11.24) does not imply acceptance:** `recover()` releases
a record only when revalidating it actually passes.

---

## 6. Determinism

The validation id is a SHA-256 digest of
`source_id | asset | acquisition_id | timestamp_utc | rules_version`, and the
trace id derives from it. No `random`, `uuid`, `datetime.now()`, or
`time.time()` appears anywhere in the layer (AST-verified). Freshness uses
only the caller-supplied `as_of`.

---

## 7. Security

No credentials, no API keys, no secret fields. No network modules are
imported. Evidence, report, and audit entries are asserted to contain no
secret-like keys, and acquisition succeeds while socket creation is denied.

---

## 8. Domain applicability — blocked, not faked

`domain_applicability("market")` is applicable. `news` and `financial`
return `applicable=False` with a reason: **no approved schema or contract
for those domains exists in the repository.** Validating a `news` record
therefore yields `UNSUPPORTED_DOMAIN` -> `QUARANTINED` rather than
fabricated domain rules.

---

## 9. Boundary with Topic 10

```text
Topic 10: source acquisition + acquisition normalization
Topic 11: quality validation + quality state
```

Validation consumes acquired data. It does not acquire, does not call
providers, and does not duplicate acquisition normalization. The input
record is never mutated (asserted by test), so source truth is preserved.

Integration is a caller-driven seam: `RuntimeOrchestrator` does not depend
on the validation layer, so the existing dependency direction is not
inverted.

---

## 10. Remaining blockers (not implemented, not claimed)

* **All numeric thresholds (11.2.2/11.20.2/11.21)** — BLOCKED BY GOVERNANCE.
  The SRS requires the controls but states no values. Configuration is
  required; see §2.
* **News / financial validation (11.15/11.16)** — BLOCKED. No approved
  schema or contract exists.
* **Cross-source conflict resolution (11.12.2)** — BLOCKED. No authoritative
  precedence rule exists, so conflicts are surfaced, not resolved.
* **Persistent quarantine (11.23)** — DEFERRED. Quarantine is in-memory;
  no storage requirement or infrastructure is authorized for this path.
* **Transformation (11.18)** — NOT APPLICABLE YET. Belongs to downstream
  topics.
* **External monitoring platform (11.26)** — NOT INTRODUCED. Counters are
  deterministic and in-process.

Nothing above is claimed as complete.

---

## 11. Tests

* `tests/unit/topic_11/test_validation_boundary.py` — 74 tests.
* `tests/integration/test_validation_runtime_end_to_end.py` — 6 tests.