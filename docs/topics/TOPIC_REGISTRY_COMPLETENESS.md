# Topic Registry Completeness — Regression Fix

> Status: ✅ **DONE** — branch `fix/registry-completeness`

## Problem

A cross-check of every frozen SRS topic file against
`REQ_REGISTRY` found 8 genuine requirement headings that were
referenced in the SRS documents but missing from the registry.
Earlier extraction patterns skipped them because of unusual
numbering/formatting:

| Requirement | Heading | Why it was skipped |
|---|---|---|
| 7.11 | Real-Time Data Processing Technologies | `7.11 ---` separated headlines |
| 7.27 | Performance and Resource Requirements | `7.27 ---` separated headline |
| 8.6.2 | Processing Constraints | `8.6.2 ---` separated headline |
| 19.15.1 | No-Action Conditions | nested child wrapped across page breaks |
| 20.9.1 | P&L Inputs | heading contained a semicolon (`Real-Time P&L;`) |
| 20.9.2 | P&L Calculation | same semicolon issue |
| 20.9.3 | P&L Update | same semicolon issue |
| 26.25.2 | Unauthorized Change Prevention | nested child wrapped across line |

## Non-gap (false positive)

`2.16` appears in `TOPIC_02.md` only inside the PDF checklist page
marker `"Topic 2 Baseline 2.16 ... Validation Checklist"`. The
frozen Topic 2 contract explicitly defines items `2.1–2.15`
("Completeness rule ... 2.1--2.15"), so `2.16` is **not** a
requirement heading and is intentionally absent from the registry.

## Fix

- Added the 8 missing headings to `src/common/requirements/registry.py`.
- Cleaned two `Decision Outcome Classification` / `Agent Interaction
  Diagrams` heading values that carried stray `----` markers from
  PDF page-break artifacts.
- Added `tests/unit/requirements/test_registry_gaps.py` (6 tests)
  locking the 8 headings into the registry and asserting that every
  registered ID actually appears in its SRS source document.
- Updated the exact-set registry tests of topics 7, 8, 19, 20 and 26
  to include the newly registered IDs.
- Removed 3 unused-variable lint errors in
  `tests/unit/topic_09/test_lifecycle.py` that blocked a clean
  `ruff check`.

## Validation

- `python -m pytest -m unit` → **793 passed** (was 787)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues

## Registry totals

- **1,758 requirement IDs** registered across 40 topics,
  verified 1:1 against the frozen SRS hierarchy.