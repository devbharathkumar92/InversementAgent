# Topic 11 — Data Validation and Quality Layer

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-11-data-quality`

## Decision

**Implementation required (core).** Topic 11 is the data quality gate
between acquisition and analysis:

- **11.2**: completeness against required fields.
- **11.3**: accuracy — values must sit within declared tolerance of a
  reference.
- **11.5**: freshness validation with max-age windows.
- **11.6**: integrity — required fields must be present and non-null.
- **11.7 / 11.8 / 11.9**: duplicate, missing, and invalid data
  detection.
- **11.10.2**: anomaly severity grading.
- **11.13**: timestamp validation.
- **11.20 / 11.20.1**: confidence scoring; **11.20.2** thresholds.
- **11.22 / 11.22.1 / 11.22.2 / 11.23 / 11.24**: reject/quarantine/
  recover handling.

Reporting (11.25), monitoring (11.26), audit trail (11.27), testing
(11.28) and acceptance criteria (11.29) are recognized and deferred to
the quality-ops/QA pass.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 11.2/11.2.1 | Data Completeness | `engine.py` (`is_complete`) | `test_data_quality.py::TestCompleteness` |
| 11.3/11.3.1 | Data Accuracy | `engine.py` (`within_tolerance`) | `test_data_quality.py::TestAccuracy` |
| 11.6/11.7/11.8 | Integrity + Duplicate/Missing Detection | `engine.py` (`integrity_ok`, `detect_duplicates`, `missing_count`) | `test_data_quality.py::TestIntegrityAndDetection` |
| 11.5 | Freshness Validation | `engine.py` (`is_fresh`) | `test_data_quality.py::TestFreshness` |
| 11.13 | Timestamp Validation | `engine.py` (`is_valid_timestamp`) | `test_data_quality.py::TestTimestampValidation` |
| 11.10.2 | Anomaly Severity | `engine.py` (`severity_grade`) | `test_data_quality.py::TestAnomalySeverity` |
| 11.20/11.20.1/11.20.2 | Confidence Scoring + Thresholds | `engine.py` (`confidence_score`) | `test_data_quality.py::TestConfidenceScoring` |
| 11.22.1/11.22.2/11.23/11.24 | Reject/Quarantine/Recover | `engine.py` (`reject_record`, `quarantine_record`, `recover`) | `test_data_quality.py::TestInvalidDataHandling` |
| — | Full Topic 11 contract | `registry.py` (+ traceability test) | `test_quality_registry.py` |

## Registry addition

Topic 11 (absent before) added as the authoritative 43-item block,
exactly matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **264 passed** (24 from Topic 11)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (76 files)

## Notes / decisions

- Anomaly severity is graded relatively: deviation within 10% of
  tolerance → `low`, within tolerance → `moderate`, beyond → `high`.
- `is_complete` treats an explicitly present `None` as a *present*
  field, while `integrity_ok` (REQ 11.6) treats `None` as a violation —
  the strictest layer wins.
- A record with zero validation results scores 0 confidence (no
  evidence) rather than passing vacuously.