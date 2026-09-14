# Topic 1 — Document Control and Versioning

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-01-document-control`

## Decision

**Implementation required.** Topic 1 defines the controlled-document
lifecycle that every other SRS topic depends on (identity, metadata,
versioning, change control, baseline locking, audit). It is foundational,
reusable logic with clear, testable business rules.

## Approach (TDD)

1. Read authoritative requirements: `srs/topics/TOPIC_01.md`.
2. Registered the numbered requirement IDs (1.0–1.12 + sub-items) in
   `src/common/requirements/registry.py` as the traceability backbone.
3. Wrote unit tests covering each requirement's testable behaviors
   **first** (`tests/unit/topic_01/`), confirming they fail (red).
4. Implemented `src/common/document_control/` until all tests passed (green).

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 1.1 | Document Identity | `document.py` (SRSDocument, composite `(document_id, version)` uniqueness) | `test_document_identity.py` |
| 1.2 | Document Metadata | `document.py` (mandatory metadata, schema validation) | `test_document_identity.py::TestDocumentMetadata` |
| 1.3 / 1.3.1 | Versioning Structure / Numbering | `versioning.py` (`Version`, parse validation) | `test_versioning.py::TestVersionFormat` |
| 1.3.2 | Version Increment Rules | `versioning.py` (`next_version`, change-class → increment) | `test_versioning.py::TestVersionIncrementRules` |
| 1.4 | Version Status | `versioning.py` (status transitions), `REQ_AUTHORIZED_STATUSES` | `test_versioning.py::TestVersionStatus` |
| 1.5 / 1.5.1 / 1.5.2 / 1.5.3 | Change Control workflow | `change_control.py` (ChangeRequest, assess_impact, approve/reject) | `test_change_control.py` |
| 1.6 / 1.6.1 / 1.6.2 | Approval & Governance | `change_control.py` (APPROVAL_AUTHORITIES, approval_state) | `test_change_control.py` |
| 1.8 | Document Integrity | `integrity.py` (SHA-256 content hash) | `test_baseline_and_audit.py::TestIntegrity` |
| 1.10 | Document Review Cycle | `review.py` (ReviewCycle, ReviewOutcome) | `test_baseline_and_audit.py::TestReviewCycle` |
| 1.11 / 1.11.1 / 1.11.2 / 1.11.3 | Baseline Locking | `baseline.py` (create/lock/controlled replacement) | `test_baseline_and_audit.py::TestBaseline` |
| 1.12 | Auditability | `audit.py` (AuditEvent/AuditLog) | `test_baseline_and_audit.py::TestAudit` |
| — (traceability) | Requirements registry | `src/common/requirements/registry.py` | `test_requirements_registry.py` |

## Validation

- `python -m pytest -m unit` → **66 passed** (65 Topic 1 + 1 health)
- `python -m ruff check src tests` → All checks passed
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (50 files)

## Notes / decisions

- REQ 1.1's "Document ID shall remain stable across ordinary version
  changes" is modeled as a **composite identity `(document_id, version)`**:
  the same `document_id` across versions is allowed (stability); the same
  `(document_id, version)` twice is rejected (uniqueness).
- Version increments (REQ 1.3.2) only occur after approval; this is
  enforced by the `approved=` guard in `next_version`.
- Baseline direct modification is rejected (`BaselineLockError`); changes
  are possible only through `create_controlled_replacement`, which retains
  the predecessor baseline (REQ 1.11.3).