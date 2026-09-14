"""Generate the 40 topic prompt files from topic metadata.

Usage:
    python scripts/gen_topic_prompts.py

The authoritative topic decomposition lives in this script so future prompts
can be regenerated deterministically. If the SRS changes topic metadata,
update the TOPICS table here and re-run.
"""

from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(os.path.dirname(HERE), "prompts", "TOPICS")

# phase key -> phase name
PHASES = {
    1: "Phase 1 — Foundation",
    2: "Phase 2 — Architecture & Technical Specification",
    3: "Phase 3 — Data & Intelligence",
    4: "Phase 4 — Trading / Investment Simulation & Safety",
    5: "Phase 5 — User Visibility & Reliability",
    6: "Phase 6 — Multi-Agent Development",
    7: "Phase 7 — QA & Release",
}

# topic number -> (name, short-name, phase key, dependency topic numbers)
TOPICS: dict[int, tuple[str, str, int, list[int]]] = {
    1: ("Document Control and Versioning", "document-control", 1, []),
    2: ("Core Goal and Mission", "core-goal-mission", 1, [1]),
    3: ("Proof of Value Definition", "proof-of-value-definition", 1, [2]),
    4: ("System Scope and Boundaries", "system-scope-and-boundaries", 1, [2, 3]),
    5: ("System Principles and Non-Negotiable Rules", "system-principles", 1, [4]),
    6: ("High-Level System Architecture", "high-level-architecture", 2, [5]),
    7: ("Technology Stack and Technical Feasibility", "technology-stack", 2, [6]),
    8: ("Agent Determinism and Specification Completeness", "agent-determinism", 2, [6, 7]),
    9: ("System Execution Lifecycle", "execution-lifecycle", 2, [6, 7, 8]),
    10: ("Data Acquisition Layer", "data-acquisition", 3, [9]),
    11: ("Data Validation and Quality Layer", "data-validation-quality", 3, [10]),
    12: ("Opportunity Discovery Engine", "opportunity-discovery", 3, [10, 11]),
    13: ("Market Analysis Engine", "market-analysis", 3, [11, 12]),
    14: ("Opportunity Scoring Engine", "opportunity-scoring", 3, [12, 13]),
    15: ("Strategy Engine", "strategy-engine", 3, [13, 14]),
    16: ("Risk and Safety Engine", "risk-safety", 4, [11, 15]),
    17: ("Backtesting and Simulation", "backtesting", 4, [15, 16]),
    18: ("Paper Trading Engine", "paper-trading", 4, [16, 17]),
    19: ("Decision Engine", "decision-engine", 4, [15, 16, 17, 18]),
    20: ("Monitoring and P&L Management", "monitoring-pnl", 4, [18, 19]),
    21: ("Dashboard and User Visibility", "dashboard", 5, [20]),
    22: ("Human Interaction and Notifications", "human-interaction", 5, [21]),
    23: ("Audit Trail and Observability", "observability", 5, [20, 21, 22]),
    24: ("Error Detection and Recovery", "error-management", 5, [23]),
    25: ("Self-Evaluation", "self-evaluation", 5, [23, 24]),
    26: ("Self-Improvement and Change Management", "self-improvement", 5, [25]),
    27: ("SRS Version Control and Governance", "srs-governance", 6, list(range(1, 27))),
    28: ("Requirement Traceability", "traceability", 6, [27]),
    29: ("Sub-Agent Architecture", "sub-agent-architecture", 6, [27, 28]),
    30: ("Sub-Agent Task Specification", "sub-agent-task-spec", 6, [29]),
    31: ("Dependency and Execution Plan", "dependency-execution", 6, [30]),
    32: ("Parallel Development Plan", "parallel-development", 6, [31]),
    33: ("Testing Strategy", "testing-strategy", 7, [8, 9, 27, 28, 29, 30, 31, 32]),
    34: ("SRS Self-Validation", "srs-self-validation", 7, [33]),
    35: ("Definition of Done", "definition-of-done", 7, [33, 34]),
    36: ("Integration and Deployment", "integration-deployment", 7, list(range(10, 36))),
    37: ("Security and Secrets Management", "security-secrets", 7, [36]),
    38: ("PoV Release Criteria", "pov-release-criteria", 7, [36, 37]),
    39: ("Future Expansion Framework", "future-expansion", 7, [38]),
    40: ("Appendices", "appendices", 7, []),
}


TEMPLATE = """# TOPIC {n} — {name}

> {phase}
> Generated from the SRS. Authoritative requirements: `SRS.md` and `srs/topics/`.
> Governance: `MASTER.md`. Follow `docs/AUTONOMOUS_WORKFLOW.md` and
> `prompts/PROMPT_00_PROJECT_BOOTSTRAP.md`.

## Objective

Implement **Topic {n} — {name}** in full, consistent with the authoritative
requirements in `srs/topics/TOPIC_{n:02d}.md` and the governance rules in
`MASTER.md`, without silently altering any frozen requirement or implementing
future topics.

## SRS Requirements Covered

`srs/topics/TOPIC_{n:02d}.md` (Topic {n} — {name})

## MASTER.md References

- §2 Source-of-Truth Hierarchy
- §3 Frozen SRS Hierarchy
- §5 Mandatory Specification Contract
- §8 Branching Strategy
- §9 Scope Discipline
- §11 Dependency Management
- §13 Testing Policy
- §14 Validation Policy
- §15 Security and Secrets
- §16 Financial Safety
- §19 Project Status
- §20 Agent Handoff
- §23 Git Commit Rules
- §24 Evidence and Traceability

## Preconditions

- Dependencies recorded `COMPLETED` in `PROJECT_STATUS.md`.
- No open governance conflicts affecting this topic (escalate via `docs/DECISIONS.md`).

## Dependencies

{dep_table}

## Existing Components To Reuse

- Bootstrap skeleton under `src/` relevant to this topic.
- `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/TESTING.md`.

## Files To Create

Define exact paths during planning; place code in the layer(s) this topic owns.

## Files To Modify

- `PROJECT_STATUS.md`
- `docs/AGENT_HANDOFF.md`
- `docs/DECISIONS.md` (only if material decisions are made)

## Implementation Requirements

Implement **only** Topic {n} as specified in `srs/topics/TOPIC_{n:02d}.md`. Do
not implement future topics. Document any minimum supporting change required by
a dependency in `docs/DECISIONS.md`.

## Database Requirements

Defined by the topic requirements and dependency contracts. If none applies,
write: `Not Applicable — <reason>`.

## API Requirements

Defined by the topic requirements and external-system contracts. If none
applies, write: `Not Applicable — <reason>`.

## UI Requirements

Defined by the topic requirements. If none applies, write:
`Not Applicable — <reason>`.

## Business Logic Requirements

- Implement deterministic rules exactly as specified.
- Validate inputs before use; preserve identifiers, timestamps, provenance,
  authority, and state lineage.
- Reject ambiguity rather than inventing intent; fail closed when correctness
  is uncertain.

## Error Handling

Classify errors, preserve evidence, retry only when explicitly recoverable,
and escalate material failures. Record blocked-state and unblocking conditions
per the SRS contract.

## Security Requirements

- No secrets committed (`MASTER.md` §15).
- Respect the SRS safety boundary (`MASTER.md` §16): no simulated results
  presented as real, no unauthorized live action, no fabricated data/evidence.

## Testing Requirements

Map behavioural tests to the requirements of this topic (`MASTER.md` §13,
`docs/TESTING.md`): positive, negative, boundary, invalid/stale input,
authz/authn, safety, error handling, recovery, concurrency/idempotency,
integration, regression.

## Unit Tests

List the concrete unit tests required for this topic's components.

## Integration Tests

List the integration tests required at this topic's boundaries.

## End-to-End Tests

List the end-to-end tests or write `Not Applicable — <reason>`.

## Validation Commands

```bash
# Examples (only run commands supported by the project):
# pytest
# ruff check src tests
# mypy src
```

Run all applicable commands and record the exact results.

## Acceptance Criteria

- All Topic {n} requirements implemented, validated, traceable, tested, and
  within scope.
- No unresolved blocking defects, no silent requirement changes.
- Evidence and traceability recorded.

## Self-Review Checklist

- [ ] Every Topic {n} requirement implemented (no silent omissions).
- [ ] Tests validate behaviour and map to requirements.
- [ ] No unrelated/future-topic changes introduced.
- [ ] No secrets or generated junk staged.
- [ ] `PROJECT_STATUS.md`, `docs/AGENT_HANDOFF.md`, `docs/DECISIONS.md` updated.
- [ ] Validation actually executed (never claimed without running).

## Completion Criteria

Mark this topic `COMPLETED` only after every acceptance criterion, test, and
validation gate passes and evidence is recorded (`MASTER.md` §19).

## Git Branch

```text
feature/topic-{n:02d}-{short}
```

Create it from the current default branch after pulling. Never force-push.

## Commit Requirements

```text
feat(topic-{n:02d}): <concise description>
```

## Final Report

Report: branch, commit SHA, requirements implemented, tests executed,
validation results, evidence, known limitations, unresolved blockers, and the
next recommended topic.
"""


def dep_table(n: int, deps: list[int]) -> str:
    if not deps:
        return "| — | — | — |"
    rows = [f"| TOPIC_{d:02d} — {TOPICS[d][0]} | hard | see PROJECT_STATUS.md |" for d in deps]
    return "\n".join(rows)


def main() -> None:
    os.makedirs(PROMPTS_DIR, exist_ok=True)
    for n in sorted(TOPICS):
        name, short, phase_key, deps = TOPICS[n]
        content = TEMPLATE.format(
            n=n,
            name=name,
            short=short,
            phase=PHASES[phase_key],
            dep_table=dep_table(n, deps),
        )
        with open(os.path.join(PROMPTS_DIR, f"TOPIC_{n:02d}.md"), "w") as f:
            f.write(content)
    print(f"Generated {len(TOPICS)} topic prompts in {PROMPTS_DIR}")


if __name__ == "__main__":
    main()
