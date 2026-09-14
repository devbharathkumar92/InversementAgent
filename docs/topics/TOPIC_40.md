# Topic 40 — Appendices

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-40-appendices`

## Decision

**Implementation required (reference/core).** Topic 40 provides the
controlled reference layer that keeps the SRS self-contained and
auditable:

- **40.1 / 40.2 / 40.3**: glossary, acronyms/abbreviations and system
  definitions.
- **40.4 / 40.5 / 40.6 / 40.7 / 40.8**: requirement ID, versioning,
  status, priority and severity conventions.
- **40.9 / 40.9.1 / 40.9.2 / 40.9.3 / 40.10 / 40.10.1 / 40.10.2 /
  40.10.3**: agent and task state definitions (state list, meaning,
  transition rules).
- **40.11–40.16** (with all children): error, risk, data-source,
  opportunity, decision and notification classifications.
- **40.17 / 40.17.1–40.17.6**: audit event schema (mandatory fields,
  event types, identification, ordering, source/actor, correlation).
- **40.18 / 40.19 / 40.20 / 40.21 / 40.22** (with all children): API,
  data-schema, configuration, environment-variables and technology
  references.
- **40.23 / 40.24 / 40.25 / 40.26** (with all children): architecture,
  data-flow, dependency and agent-interaction diagrams.
- **40.27 / 40.27.1–40.27.5**: test matrix (mapping, test case ID,
  status, expected/actual, evidence).
- **40.28 / 40.28.1–40.28.8**: traceability matrix (goal, SRS, task,
  agent, code, test, evidence, coverage).
- **40.29 / 40.29.1–40.29.7**: change log (request ID, description,
  reason, impact, approval, implementation, validation).
- **40.30 / 40.30.1–40.30.5**: reference materials.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 40.4 | Requirement ID Convention | `engine.py` (`requirement_id_valid`) | `test_appendices.py::TestConventions` |
| 40.9.3/40.10.3 | State Transition Rules | `engine.py` (`state_transition_ok`) | `test_appendices.py::TestConventions` |
| 40.17.1/40.17.2 | Audit Fields / Event Types | `engine.py` (`audit_fields_ok`) | `test_appendices.py::TestSchema` |
| 40.23/40.24 | Architecture / Data-Flow Diagrams | `engine.py` (`diagram_present`) | `test_appendices.py::TestDiagrams` |
| 40.27 | Test Matrix | `engine.py` (`matrix_mapping_ok`) | `test_appendices.py::TestMatrices` |
| 40.28 | Traceability Matrix | `engine.py` (`traceability_matrix_ok`) | `test_appendices.py::TestMatrices` |
| 40.29/40.30 | Change Log / Reference Materials | `engine.py` (`matrix_complete`) | `test_appendices.py::TestMatrices` |
| 40.1 | Glossary | `engine.py` (`AppendicesEngine`) | `test_appendices.py::TestEngine` |
| — | Full Topic 40 contract | `registry.py` (+ traceability test) | `test_appendices_registry.py` |

## Registry addition

Topic 40 (absent before) added as the authoritative **126-item**
block — the largest topic, covering 30 top-level and 96 nested-child
IDs. The full nested child set (each 2.1-2.8 child groups) is
captured. Names were programmatically extracted from the frozen
SRS hierarchy and verified against the "Nested Children" runs.

## Validation

- `python -m pytest -m unit` → **787 passed** (15 from Topic 40 +
  full 126-ID registry traceability test)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (134 files)

## Notes / decisions

- Requirement IDs must follow the convention and stay unique (40.4);
  uniqueness failures block acceptance.
- Audit events require mandatory fields AND typed event classes
  (40.17).
- The test matrix and traceability matrix both require evidence
  references — mapping alone is insufficient (40.27/40.28).
- The helper was named `matrix_mapping_ok` (not `test_*`) to avoid
  pytest collecting it as a test function.