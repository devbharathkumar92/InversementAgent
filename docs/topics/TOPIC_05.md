# Topic 5 — System Principles and Non-Negotiable Rules

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-05-system-principles`

## Decision

**Implementation required.** Topic 5 defines non-negotiable system rules
that must be enforced at every action boundary (human approval, no
assumptions, self-improvement restrictions, baseline lock, change
governance). These are the core safety constraints for the enforcement
runtime and are coded as a controlled `SystemPrinciples` model.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 5.1 / 5.2 | Core System Principles / Non-Negotiable Rules | `system_principles.py` (`SystemPrinciples`) | `test_system_principles.py::TestPrincipleRegistry` |
| 5.4 | Specification Completeness Principle | `PrincipleRegistry` rule-id mapping | `test_system_principles.py::TestPrincipleRegistry` |
| 5.6 | No-Assumption Principle | `system_principles.py` (`has_evidence`) | `test_system_principles.py::TestNoAssumption` |
| 5.8 / 5.8.1 / 5.8.2 | Human Approval (approval by default) | `system_principles.py` (`requires_approval`) | `test_system_principles.py::TestHumanApproval` |
| 5.9–5.25 | Scoped principles (registry traceability) | `registry.py` | `test_principles_registry.py` |
| 5.26 / 5.26.1 / 5.26.2 | Self-Improvement Restrictions | `system_principles.py` (`self_modification_allowed`) | `test_system_principles.py::TestSelfModification` |
| 5.27 / 5.27.1 / 5.27.3 | Change Proposal / Approval Gates | `system_principles.py` (`ChangeProposal`) | `test_system_principles.py::TestChangeGovernance` |
| 5.29 / 5.30 | Rule Violation Detection / Enforcement | `system_principles.py` (`detect_rule_violations`, `RuleEnforcer`) | `test_system_principles.py::TestRuleEnforcement` |
| 5.31 | Exception Handling Rules | `SystemPrinciples` exception-aware enforcement | `test_system_principles.py::TestRuleEnforcement` |
| 5.33 / 5.33.1 / 5.33.2 | Baseline Lock and Controlled Modification | `system_principles.py` (`is_locked_baseline`, `record_baseline`) | `test_system_principles.py::TestBaselineLock` |

## Registry corrections

The Topic 5 registry block did **not** match the authoritative SRS
(TOPIC_05.md preserved numbering):

- Missing items **5.26/5.26.1/5.26.2 … 5.34** (Self-Improvement
  Restrictions, Change Proposal/Approval, Rule Violation Detection,
  Enforcement, Exception Handling, Baseline Lock, Governance).
- Wrong titles for **5.9** ("Safety and Risk" → "Scope Compliance
  Principle"), **5.24** ("Continuous Improvement" → "Conflict Resolution
  Rules"), **5.25** ("Principle Enforcement" → "Self-Evaluation Rules"),
  and several 5.10–5.23 entries.

Rebuilt the block to exactly match the SRS headings; the traceability
test now guards against future drift.

## Validation

- `python -m pytest -m unit` → **151 passed** (20 from Topic 5)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (64 files)

## Notes / decisions

- Human approval (5.8) is **approval-by-default**: only actions explicitly
  listed as non-approval are exempt; undeclared actions require approval.
- No-assumption principle (5.6): a claim is evidenced only if it cites a
  concrete source/timestamp AND is not a forward-looking prediction.
- Baseline lock (5.33): baselines matching the locked naming convention
  are protected from uncontrolled modification.
- Change proposals (5.27) require an explicit governance approval record.