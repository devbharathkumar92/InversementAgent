# Topic 12 — Opportunity Discovery Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-12-opportunity-discovery`

## Decision

**Implementation required (core).** Topic 12 is the discovery layer that
turns validated market data into scored opportunities:

- **12.3 / 12.4**: a bounded asset universe is scanned.
- **12.5 / 12.5.1**: detection signals are enumerated (price, volume,
  volatility, news).
- **12.10 / 12.11 / 12.12**: price-movement, volume-based, and
  volatility-based detection.
- **12.6 / 12.6.1 / 12.6.2**: hard and soft filters.
- **12.14 / 12.14.1**: qualification criteria with liquidity / regime
  checks.
- **12.15**: opportunity ranking.
- **12.16**: deduplication.
- **12.17 / 12.17.1**: evidence collection.
- **12.18 / 12.18.1**: confidence score from combined inputs; thresholds.
- **12.19 / 12.19.1**: expiry with TTL.
- **12.21 / 12.21.1**: false-signal detection (e.g., price move without
  supporting volume).

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 12.3/12.4 | Market Scanning + Asset Universe | `engine.py` (`DiscoveryEngine.scan`) | `test_discovery.py::TestMarketScanning` |
| 12.5.1/12.10 | Price-Movement Detection | `engine.py` (`detect_momentum`) | `test_discovery.py::TestDetectionSignals` |
| 12.11 | Volume-Based Detection | `engine.py` (`detect_volume_spike`) | `test_discovery.py::TestDetectionSignals` |
| 12.12 | Volatility-Based Detection | `engine.py` (`detect_volatility_expansion`) | `test_discovery.py::TestDetectionSignals` |
| 12.6/12.6.1/12.6.2 | Hard/Soft Filters | `engine.py` (`passes_filters`) | `test_discovery.py::TestFilters` |
| 12.14/12.14.1 | Qualification | `engine.py` (`DiscoveryEngine.qualifies`) | `test_discovery.py::TestQualification` |
| 12.15 | Opportunity Ranking | `engine.py` (`rank_opportunities`) | `test_discovery.py::TestRanking` |
| 12.16 | Deduplication | `engine.py` (`is_duplicate`) | `test_discovery.py::TestDeduplication` |
| 12.17 | Evidence Collection | `engine.py` (`add_evidence`) | `test_discovery.py::TestEvidence` |
| 12.18.1/12.18.2 | Confidence Score | `engine.py` (`confidence_from`) | `test_discovery.py::TestConfidence` |
| 12.19 | Opportunity Expiry | `engine.py` (`expired_opportunity`) | `test_discovery.py::TestExpiry` |
| 12.21.1 | False-Signal Detection | `engine.py` (`false_signal_flagged`) | `test_discovery.py::TestFalseSignalDetection` |
| — | Full Topic 12 contract | `registry.py` (+ traceability test) | `test_discovery_registry.py` |

## Registry addition

Topic 12 (absent before) added as the authoritative 44-item block,
exactly matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **285 passed** (21 from Topic 12)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (78 files)

## Notes / decisions

- Volume and volatility detection require a 2.0× expansion (per REQ
  12.11/12.12); a zero/empty baseline is treated as "no signal" except
  when any positive value is itself notable.
- The `DiscoveryEngine.scan` model currently returns an empty signal set
  by default; concrete detection wiring (calls into `detect_momentum`
  et al. per asset) is exercised via the individual detectors and the
  full pipeline is assembled in the integration pass.
- False-signal logic flags a move as false when its volume confirmation
  is weak — a price blip without volume is demoted rather than passed on
  to qualification.