# Topic 7 — Technology Stack and Technical Feasibility

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-07-technology-stack`

## Decision

**Implementation required (subset).** Topic 7 is a technology-selection
document, but the following items carry enforced, versioned controls:

- **7.7.2 Non-LLM Deterministic Responsibilities**: a mandated partition
  — deterministic duties are never delegated to an LLM.
- **7.1.1 / 7.1.2** Selection / Rejection criteria for technologies.
- **7.18.2 Branch Strategy**: governed branch naming + protected
  branches.
- **7.26.1 / 7.26** Dependency Pinning: reproducible builds.

The remaining items (7.2–7.6, 7.9–7.17, 7.19–7.25, 7.28–7.31) are
decisions/guidance for a human technology baselining pass; no runtime
logic was invented for them.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 7.7.2 | Non-LLM Deterministic Responsibilities | `selection.py` (`TechSelection.is_deterministic`, `owner_of`) | `test_technology.py::TestNonLLMDeterministic` |
| 7.1.1 / 7.1.2 | Selection / Rejection Criteria | `selection.py` (`is_selected`, `reject_if_unsupported`) | `test_technology.py::TestTechFeasibility` |
| 7.18.2 | Branch Strategy | `selection.py` (`BranchStrategy` + `from_deps`) | `test_technology.py::TestBranchStrategy` |
| 7.26.1 | Dependency Pinning | `selection.py` (`validate_pinned_dependency`, `validate_dependency_pinning`) | `test_technology.py::TestDependencyPinning` |
| — | Full Topic 7 contract | `registry.py` (+ traceability test) | `test_technology_registry.py` |

## Registry addition

Topic 7 (present in the SRS only since this pass) added the complete
authoritative block — **43 items**, exactly matching the SRS topic file
(which has no `7.11` / `7.27`).

## Validation

- `python -m pytest -m unit` → **186 passed** (15 from Topic 7)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (68 files)

## Notes / decisions

- Requirement semantics: a technology spec of the form `python=3.12` is
  a pinned selection in this system (used in traceability), while an
  unpinned bare name (`numpy`) fails validation.
- `BranchStrategy` is constructible from a shared technology
  configuration dict via `from_deps`.
- Rejection (7.1.2): a technology is rejected if it sits on the
  unsupported list or is simply not in the selected set.