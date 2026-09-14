# Topic 27 — SRS Version Control and Governance

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-27-governance`

## Decision

**Implementation required (core).** Topic 27 treats the SRS as a
controlled, versioned document:

- **27.2 / 27.3 / 27.4**: ownership, authority and structure.
- **27.5 / 27.5.1 / 27.5.2**: version numbering, format and increment
  rules.
- **27.6 / 27.7**: baseline definition and locking.
- **27.8 / 27.8.1 / 27.9 / 27.9.1 / 27.9.2**: change requests,
  proposals and justification.
- **27.10 / 27.10.1 / 27.10.2 / 27.11 / 27.11.1 / 27.11.2 / 27.12**:
  change impact analysis, risk assessment, approval authority/state
  and rejection.
- **27.13 / 27.13.1 / 27.13.2**: emergency change criteria and
  approval.
- **27.14 / 27.15 / 27.16 / 27.17 / 27.18**: version history, change
  log, requirement traceability, document integrity, conflict
  resolution.
- **27.19 / 27.20 / 27.21 / 27.22 / 27.23 / 27.24 / 27.25**:
  consistency checks, validation, audit, access control, backup,
  recovery, review cycle.
- **27.26 / 27.26.1 / 27.26.2 / 27.27 / 27.28 / 27.28.1 / 27.28.2**:
  approval workflow (review + approval), change testing and release
  management (preparation + validation).
- **27.29 / 27.30**: acceptance criteria and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 27.5.1 | Version Format | `engine.py` (`version_format_valid`) | `test_governance.py::TestVersioning` |
| 27.5.2 | Version Increment | `engine.py` (`version_increment_valid`) | `test_governance.py::TestVersioning` |
| 27.15 | Change Log | `engine.py` (`documented_after_change`) | `test_governance.py::TestVersioning` |
| 27.9.2 | Change Justification | `engine.py` (`change_justified`) | `test_governance.py::TestChangeControl` |
| 27.10 | Change Impact Analysis | `engine.py` (`impact_risk_assessed`) | `test_governance.py::TestChangeControl` |
| 27.11.1/27.11.2 | Approval Authority/State | `engine.py` (`approval_allowed`) | `test_governance.py::TestChangeControl` |
| 27.11 | Change Approval | `engine.py` (`change_requires_approval`) | `test_governance.py::TestChangeControl` |
| 27.13.2 | Emergency Approval | `engine.py` (`emergency_approval`) | `test_governance.py::TestChangeControl` |
| 27.3 | SRS Authority | `engine.py` (`srs_authority`) | `test_governance.py::TestDocumentGovernance` |
| 27.17 | Document Integrity | `engine.py` (`srs_integrity_ok`) | `test_governance.py::TestDocumentGovernance` |
| 27.19 | SRS Consistency Checks | `engine.py` (`srs_consistent`) | `test_governance.py::TestDocumentGovernance` |
| 27.28.2 | Release Validation | `engine.py` (`release_validated`) | `test_governance.py::TestDocumentGovernance` |
| 27.1 | SRS Governance Objectives | `engine.py` (`GovernanceEngine`) | `test_governance.py::TestEngine` |
| — | Full Topic 27 contract | `registry.py` (+ traceability test) | `test_governance_registry.py` |

## Registry addition

Topic 27 (absent before) added as the authoritative 45-item block.
Captures `Nested Children`: 27.5.1 Version Format, 27.5.2 Version
Increment; 27.8.1 Change Request Content; 27.9.1 Change Proposal,
27.9.2 Change Justification; 27.10.1 Impact Areas, 27.10.2 Risk
Assessment; 27.11.1 Approval Authority, 27.11.2 Approval State;
27.13.1 Emergency Criteria, 27.13.2 Emergency Approval; 27.26.1
Review, 27.26.2 Approval; 27.28.1 Release Preparation, 27.28.2
Release Validation.

## Validation

- `python -m pytest -m unit` → **539 passed** (20 from Topic 27)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (108 files)

## Notes / decisions

- Versioning uses strict `major.minor.patch`; only forward increments
  are legal (27.5.1/27.5.2).
- Major changes always require formal approval; emergency changes
  require both emergency criteria and approval authority (27.11/27.13).
- Document integrity and consistency checks guard the baseline: any
  checksum mismatch or cross-reference break blocks the change before
  it can be released (27.17/27.19/27.28.2).