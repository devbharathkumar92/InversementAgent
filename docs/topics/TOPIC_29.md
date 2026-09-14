# Topic 29 — Sub-Agent Architecture

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-29-subagents`

## Decision

**Implementation required (core).** Topic 29 defines the agent
topology: a master agent (29.2) delegating to specialised sub-agents
(29.3-29.14):

- **29.2 / 29.2.1 / 29.2.2 / 29.3 / 29.3.1 / 29.3.2 / 29.4 / 29.4.1 /
  29.4.2**: master authority/restrictions; background checker and SRS
  writer with their responsibilities.
- **29.5 / 29.6 / 29.7 / 29.8 / 29.9 / 29.10 / 29.11 / 29.12 / 29.13 /
  29.14**: data, analysis, strategy, risk, testing, monitoring,
  dashboard, notification, integration and deployment agents.
- **29.15 / 29.15.1 / 29.15.2 / 29.16 / 29.17 / 29.18**: responsibility
  definition/boundaries, agent boundaries, inputs and outputs.
- **29.19 / 29.19.1 / 29.19.2 / 29.20 / 29.20.1 / 29.20.2**:
  interface/handoff contracts and communication rules/failure handling.
- **29.21 / 29.21.1 / 29.21.2 / 29.22 / 29.23 / 29.24 / 29.25**:
  state management, dependency/priority management, failure isolation
  and recovery.
- **29.26 / 29.27 / 29.28 / 29.29 / 29.30**: security, monitoring,
  testing, acceptance criteria and change control.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 29.2.1 | Master Agent Authority | `engine.py` (`master_authority`) | `test_architecture.py::TestAgentRoles` |
| 29.15.1 | Responsibility Definition | `engine.py` (`responsibility_scope`) | `test_architecture.py::TestAgentRoles` |
| 29.15.2/29.16 | Responsibility/Agent Boundaries | `engine.py` (`boundaries_respected`) | `test_architecture.py::TestInterfaces` |
| 29.17 | Agent Inputs | `engine.py` (`agent_inputs_ok`) | `test_architecture.py::TestInterfaces` |
| 29.18 | Agent Outputs | `engine.py` (`agent_outputs_ok`) | `test_architecture.py::TestInterfaces` |
| 29.19.1 | Interface Contract | `engine.py` (`interface_contract_met`) | `test_architecture.py::TestInterfaces` |
| 29.19.2 | Handoff Contract | `engine.py` (`handoff_valid`) | `test_architecture.py::TestInterfaces` |
| 29.20 | Agent Communication | `engine.py` (`communication_reliable`) | `test_architecture.py::TestCoordination` |
| 29.21.2 | State Transitions | `engine.py` (`state_transition_allowed`) | `test_architecture.py::TestCoordination` |
| 29.22 | Agent Dependency Management | `engine.py` (`dependencies_resolved`) | `test_architecture.py::TestCoordination` |
| 29.25 | Agent Recovery | `engine.py` (`recovery_supported`) | `test_architecture.py::TestCoordination` |
| 29.1 | Sub-Agent Architecture Objectives | `engine.py` (`SubAgentEngine`) | `test_architecture.py::TestEngine` |
| — | Full Topic 29 contract | `registry.py` (+ traceability test) | `test_architecture_registry.py` |

## Registry addition

Topic 29 (absent before) added as the authoritative 44-item block.
Captures `Nested Children`: 29.2.1 Master Agent Authority, 29.2.2
Master Agent Restrictions; 29.3.1 Monitoring Responsibilities, 29.3.2
Escalation Responsibilities; 29.4.1 SRS Writing Responsibilities,
29.4.2 SRS Writer Restrictions; 29.15.1 Responsibility Definition,
29.15.2 Responsibility Boundaries; 29.19.1 Interface Contract,
29.19.2 Handoff Contract; 29.20.1 Message Rules, 29.20.2 Communication
Failure; 29.21.1 Agent States, 29.21.2 State Transitions.

## Validation

- `python -m pytest -m unit` → **579 passed** (21 from Topic 29)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (112 files)

## Notes / decisions

- The master agent is the only authority that can delegate; sub-agent
  boundaries are enforced per handoff (29.2.1/29.16).
- Handoffs require a capable sender, a capable receiver and a message;
  communication reliability is restored by bounded retries
  (29.19.2/29.20.2).
- State transitions are whitelisted; illegal jumps are rejected
  (29.21.2), and dependencies must stay acyclic (29.22).