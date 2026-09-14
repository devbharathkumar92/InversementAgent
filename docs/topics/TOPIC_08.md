# Topic 8 — Agent Determinism and Specification Completeness

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-08-determinism`

## Decision

**Implementation required.** Topic 8 is the determinism contract for
agents; most of its items are enforced, deterministic controls:

- **8.1 / 8.7.2**: determinism objectives; decision rules applied in
  declared priority order.
- **8.16 / 8.17 / 8.17.1**: no-assumption enforcement — forbidden
  assumptions list; agents must have supporting evidence.
- **8.18 / 8.18.1 / 8.18.2**: ambiguity detection and resolution against
  an explicit reference.
- **8.20 / 8.20.1 / 8.20.2**: undefined-state handling — unknown state
  falls back to a safe (blocked) behaviour.
- **8.21 / 8.21.2**: blocked → escalation state.
- **8.26**: agent self-verification before continuing.

Schema items (8.4.1/8.5.1) and mapping/completeness items (8.22–8.31)
are covered by the registry traceability block; their deeper validation
is delegated to topic-10+ validation layers.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 8.1 | Determinism Objectives | `engine.py` (`DeterminismEngine`) | `test_determinism.py::TestDeterminismObjectives` |
| 8.7.2 | Rule Priority | `engine.py` (`determine_rule_priority`) | `test_determinism.py::TestRulePriority` |
| 8.16/8.17/8.17.1 | No-Assumption / Forbidden Assumptions | `engine.py` (`assumption_forbidden`, `has_supporting_evidence`) | `test_determinism.py::TestForbiddenAssumptions` |
| 8.18/8.18.1/8.18.2 | Ambiguity Detection / Resolution | `engine.py` (`detect_ambiguity`, `AmbiguityDetector.detect/resolve`) | `test_determinism.py::TestAmbiguityDetection` |
| 8.20/8.20.1/8.20.2 | Undefined-State / Safe Behaviour | `engine.py` (`safe_behaviour_for`) | `test_determinism.py::TestUndefinedStateSafeBehaviour` |
| 8.21/8.21.2 | Blocked → Escalation State | `engine.py` (`escalation_states`) | `test_determinism.py::TestEscalationState` |
| 8.26 | Agent Self-Verification | `engine.py` (`self_verification_required`) | `test_determinism.py::TestAgentSelfVerification` |
| — | Full Topic 8 contract | `registry.py` (+ traceability test) | `test_determinism_registry.py` |

## Registry addition

Topic 8 (absent before) added as the authoritative 45-item block, exactly
matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **203 passed** (17 from Topic 8)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (70 files)

## Notes / decisions

- Ambiguity resolution (8.18.2): when a full reference instruction is
  supplied the detector resolves to `use-reference`; an empty reference
  escalates instead.
- Undefined state (8.20.2): any state not explicitly recognised by the
  engine maps to the safe `blocked` behaviour.
- Rule priority (8.7.2): higher numeric priority wins; ties resolve to
  the lexicographically smallest rule id so ordering is fully
  deterministic.