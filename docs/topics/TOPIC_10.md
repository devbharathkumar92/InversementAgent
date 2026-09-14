# Topic 10 — Data Acquisition Layer

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-10-data-acquisition`

## Decision

**Implementation required (core).** Topic 10 is the data acquisition
layer with strongly enforceable controls:

- **10.3 / 10.3.1 / 10.3.2**: source approval criteria and
  classification — a source must declare a supported class, an
  authority, and a license.
- **10.4–10.8**: supported source classes (market / news / financial /
  economic / alternative).
- **10.9.2**: real-time maximum acceptable latency.
- **10.11 / 10.12**: source authentication and API integration
  modelled as registered connectors.
- **10.15 / 10.15.1**: retrieval scheduling.
- **10.17**: data rate limits.
- **10.18 / 10.18.1 / 10.18.2 / 10.18.3**: failure handling — retry,
  fallback, escalation.
- **10.19 / 10.19.1 / 10.19.2**: primary/secondary source redundancy.
- **10.21 / 10.21.1**: provenance metadata and source traceability.
- **10.24**: data source reliability scoring.

Cost control (10.27), change detection (10.28), monitoring (10.29) and
baseline/change control (10.30) are recognized; runtime wiring to the
external provider layer is deferred to the integration pass.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 10.3/10.3.1/10.3.2 | Source Approval + Classification | `engine.py` (`approve_source`, `SUPPORTED_KINDS`) | `test_data_acquisition.py::TestSourceApproval` |
| 10.9.2 | Maximum Acceptable Latency | `engine.py` (`max_latency_satisfied`) | `test_data_acquisition.py::TestRealTimeLatency` |
| 10.15.1 | Retrieval Schedule | `engine.py` (`next_retrieval_at`) | `test_data_acquisition.py::TestRetrievalSchedule` |
| 10.17 | Data Rate Limits | `engine.py` (`rate_limit_exceeded`) | `test_data_acquisition.py::TestRateLimits` |
| 10.18.1/10.18.3 | Retry + Failure Escalation | `engine.py` (`AcquisitionEngine.record_failure`) | `test_data_acquisition.py::TestFailureHandling` |
| 10.19/10.21.2 | Source Redundancy | `engine.py` (`add_source`) | `test_data_acquisition.py::TestRedundancy` |
| 10.21/10.21.1 | Provenance Metadata | `engine.py` (`record_provenance`) | `test_data_acquisition.py::TestProvenance` |
| 10.24 | Reliability Scoring | `engine.py` (`ReliabilityScorer`) | `test_data_acquisition.py::TestReliabilityScoring` |
| — | Full Topic 10 contract | `registry.py` (+ traceability test) | `test_acquisition_registry.py` |

## Registry addition

Topic 10 (absent before) added as the authoritative 46-item block,
exactly matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **240 passed** (17 from Topic 10)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (74 files)

## Notes / decisions

- Actual network connectors are intentionally not implemented inside the
  `common` layer; the layer defines the *contracts* (approval, latency,
  rate, provenance, reliability) that any concrete provider must satisfy.
- Reliability scoring is success-ratio based; a source with no history
  scores 0 and must build evidence before being trusted (aligned with
  Topic 10.3.3 authority requirements).