# AI Investment Opportunity Agent --- MASTER.md

## 1. Purpose

`MASTER.md` defines the technical governance and autonomous-development
operating rules for implementing the authoritative `SRS.md`.

`SRS.md` is the requirements source of truth.

`MASTER.md` is the implementation-governance source of truth.

Neither document may be silently altered by an implementation agent.

------------------------------------------------------------------------

## 2. Source-of-Truth Hierarchy

When interpreting requirements, use this order:

1.  Approved SRS baseline and its controlled versions
2.  Approved governance/change-control decisions
3.  This MASTER.md
4.  Topic-specific implementation prompts
5.  Agent assumptions

An agent must never use an assumption to override an explicit
requirement.

If two authoritative requirements conflict:

-   stop the affected implementation;
-   identify the exact conflicting requirement IDs;
-   preserve evidence;
-   record the conflict;
-   escalate through the defined governance path;
-   do not silently choose a convenient interpretation.

------------------------------------------------------------------------

## 3. Frozen SRS Hierarchy

The SRS explicitly establishes a corrected frozen hierarchy covering
Topics 1--40.

The master sequence is:

### Phase 1 --- Foundation

-   Topics 1--5

### Phase 2 --- Architecture and Technical Specification

-   Topics 6--9

### Phase 3 --- Data and Intelligence

-   Topics 10--15

### Phase 4 --- Trading / Investment Simulation and Safety

-   Topics 16--20

### Phase 5 --- User Visibility and Reliability

-   Topics 21--26

### Phase 6 --- Multi-Agent Development

-   Topics 27--32

### Phase 7 --- QA and Release

-   Topics 33--40

The hierarchy and nested numbering are frozen. Agents must not invent
equal child counts, renumber requirements, or omit nested requirements.

------------------------------------------------------------------------

## 4. Core Project Constraints

The source SRS establishes the following major architectural and
governance constraints:

-   The Proof of Value is India/INR scoped.
-   The system operates as a bounded multi-agent system.
-   Data flow must be validated.
-   Simulation and paper trading come before live execution.
-   Dashboard visibility is required.
-   Auditability is required.
-   Analysis/decision authority must remain strictly separated from live
    execution authority.
-   Safety controls must be enforceable.
-   Unsupported assumptions must not become implementation facts.
-   Fabricated data or fabricated evidence is prohibited.
-   Unauthorized live financial action is prohibited.
-   Silent requirement changes are prohibited.
-   Safety-gate bypass is prohibited.
-   Frozen goal, scope, and baselines must not be modified outside
    controlled change governance.

These constraints are reflected throughout the SRS architecture and
individual numbered requirements.

------------------------------------------------------------------------

## 5. Mandatory Specification Contract

Every numbered SRS item must be treated as a complete specification.

The source baseline requires the following fields:

1.  Purpose
2.  Objective
3.  Requirement
4.  Scope
5.  Inputs
6.  Input Source
7.  Processing / Method / Rules
8.  Outputs
9.  Output Destination
10. Responsible Agent / Component
11. Prerequisites
12. Dependencies
13. Dependency Type
14. Parallelization Eligibility
15. Parallelization Restrictions
16. Technical Details
17. Tools / Resources
18. Constraints
19. Prohibited Actions
20. Expected Behaviour
21. Error Handling
22. Blocked-State Conditions
23. Unblocking Conditions
24. Human Escalation
25. Validation Method
26. Testing Requirements
27. Evidence Required
28. Acceptance Criteria
29. Failure / Rejection Criteria
30. Recovery / Corrective Action
31. Audit / Traceability
32. Change Control
33. Rationale / Assumptions
34. Verification Method

If a field is genuinely not applicable, explicitly record:

`Not Applicable — <reason>`

Never silently omit a field.

------------------------------------------------------------------------

## 6. Autonomous Topic Execution Model

Each implementation topic is executed independently.

The canonical lifecycle is:

``` text
READ
  ↓
UNDERSTAND
  ↓
AUDIT CURRENT REPOSITORY
  ↓
CHECK DEPENDENCIES
  ↓
PLAN
  ↓
CREATE FEATURE BRANCH
  ↓
IMPLEMENT ONLY CURRENT TOPIC
  ↓
WRITE / UPDATE TESTS
  ↓
RUN VALIDATION
  ↓
SELF-REVIEW
  ↓
FIX FAILURES
  ↓
RUN REGRESSION TESTS
  ↓
CAPTURE EVIDENCE
  ↓
UPDATE TRACEABILITY / STATUS
  ↓
COMMIT
  ↓
PUSH
  ↓
HAND OFF TO NEXT TOPIC
```

An agent must not skip verification merely because implementation
appears correct.

------------------------------------------------------------------------

## 7. Required Reading Before Every Topic

Before implementing a topic, the agent must read:

``` text
SRS.md
MASTER.md
current topic prompt
relevant preceding topic requirements
relevant architecture documentation
PROJECT_STATUS.md
AGENT_HANDOFF.md
relevant existing source code
relevant tests
relevant decision/change records
```

The agent must determine whether prerequisites are satisfied before
modifying code.

------------------------------------------------------------------------

## 8. Branching Strategy

Use one feature branch per implementation topic.

Preferred naming:

``` text
feature/topic-01-<short-name>
feature/topic-02-<short-name>
...
feature/topic-40-<short-name>
```

Do not develop multiple unrelated topics in one branch.

Do not force-push.

Do not rewrite protected history.

Do not bypass repository protection.

The default branch is the integration baseline unless the repository
defines another protected default branch.

------------------------------------------------------------------------

## 9. Scope Discipline

An agent implementing Topic N must implement Topic N and only the
minimum supporting changes required by its dependencies.

Do not:

-   implement future topics prematurely;
-   modify unrelated modules;
-   change frozen requirements;
-   remove functionality without requirement-backed justification;
-   introduce technology solely because it is convenient;
-   fabricate external integrations;
-   create fake data/evidence;
-   weaken safety controls to make tests pass.

If an adjacent change is genuinely required, document why and link it to
the relevant SRS requirement.

------------------------------------------------------------------------

## 10. Determinism and Explicitness

Where the SRS requires deterministic behaviour:

-   use explicit rules;
-   version configuration;
-   preserve identifiers;
-   preserve timestamps;
-   preserve provenance;
-   preserve authority;
-   preserve state lineage;
-   validate inputs;
-   reject ambiguity rather than invent intent;
-   record material state transitions.

For repeated execution, use idempotent behaviour where applicable.

When correctness is uncertain, fail closed rather than guessing.

------------------------------------------------------------------------

## 11. Dependency Management

Before implementation, identify:

-   hard dependencies;
-   soft dependencies;
-   blocking dependencies;
-   downstream consumers;
-   upstream contracts;
-   schema dependencies;
-   configuration dependencies;
-   governance/approval dependencies.

A blocked prerequisite must not be silently bypassed.

A blocked topic must record:

``` text
Blocker
Affected requirement
Reason
Evidence
Required unblocking condition
Owner / escalation path
```

------------------------------------------------------------------------

## 12. Parallelization

Parallel work is permitted only where the SRS marks the work as
eligible.

Parallel workers must not:

-   create competing authoritative state;
-   bypass approval gates;
-   alter locked baselines;
-   duplicate unique identifiers;
-   consume unvalidated upstream state;
-   approve their own changes;
-   create conflicting versions.

Independent design, read-only analysis, test preparation, and
evidence-template work may run in parallel only when governing contracts
and versions are frozen.

------------------------------------------------------------------------

## 13. Testing Policy

Testing must map to requirements.

As applicable, tests must cover:

-   positive cases;
-   negative cases;
-   boundary cases;
-   invalid input;
-   stale data;
-   contradictory state;
-   authorization;
-   authentication;
-   safety controls;
-   error handling;
-   recovery;
-   concurrency/conflict;
-   idempotency;
-   integration boundaries;
-   regression.

A test must validate behaviour, not merely the existence of a file,
function, class, or endpoint.

------------------------------------------------------------------------

## 14. Validation Policy

Every topic must define and execute appropriate validation.

Typical validation layers include:

``` text
Syntax / formatting
        ↓
Static analysis
        ↓
Type checking
        ↓
Unit tests
        ↓
Integration tests
        ↓
End-to-end tests
        ↓
Security checks
        ↓
Requirement traceability
        ↓
Acceptance criteria
```

Use only commands supported by the actual project.

Never claim a check passed if it was not executed.

If a required validation cannot run, report the exact reason.

------------------------------------------------------------------------

## 15. Security and Secrets

Never commit:

-   GitHub tokens;
-   API keys;
-   passwords;
-   private keys;
-   credentials;
-   production secrets;
-   real `.env` secret files.

Use environment variables and secret-management mechanisms.

Provide `.env.example` where required.

Before every commit, inspect the staged diff for secrets and unintended
files.

------------------------------------------------------------------------

## 16. Financial Safety

This is an investment-opportunity system.

The implementation must respect the SRS safety boundary.

Agents must not:

-   execute unauthorized live financial actions;
-   represent simulated results as real results;
-   fabricate market data;
-   fabricate performance evidence;
-   claim guaranteed profit;
-   bypass risk controls;
-   bypass paper-trading/simulation gates;
-   grant analysis components live execution authority.

The architecture must preserve separation between:

``` text
Data
  ↓
Analysis
  ↓
Opportunity
  ↓
Scoring
  ↓
Strategy
  ↓
Risk / Safety
  ↓
Simulation / Paper Trading
  ↓
Decision
```

and any live-execution authority, which must remain separately governed.

------------------------------------------------------------------------

## 17. Documentation Requirements

Maintain, as applicable:

``` text
README.md
PROJECT_STATUS.md
docs/ARCHITECTURE.md
docs/DEVELOPMENT.md
docs/TESTING.md
docs/AUTONOMOUS_WORKFLOW.md
docs/AGENT_HANDOFF.md
docs/DECISIONS.md
docs/TOPIC_DEPENDENCY_GRAPH.md
```

Documentation changes must remain consistent with the SRS.

------------------------------------------------------------------------

## 18. Prompt Repository

Maintain:

``` text
prompts/
├── PROMPT_00_PROJECT_BOOTSTRAP.md
├── TOPICS/
│   ├── TOPIC_01.md
│   ├── TOPIC_02.md
│   ├── ...
│   └── TOPIC_40.md
└── templates/
    └── TOPIC_PROMPT_TEMPLATE.md
```

Each topic prompt must:

-   identify the exact topic;
-   identify requirements covered;
-   identify prerequisites;
-   identify dependencies;
-   specify implementation expectations;
-   specify tests;
-   specify validation;
-   specify acceptance criteria;
-   specify evidence;
-   specify completion conditions;
-   require branch/commit discipline;
-   require project-status updates.

------------------------------------------------------------------------

## 19. Project Status

`PROJECT_STATUS.md` must track every topic.

Minimum state vocabulary:

``` text
NOT_STARTED
BLOCKED
IN_PROGRESS
IMPLEMENTED
VALIDATING
FAILED_VALIDATION
READY_FOR_REVIEW
COMPLETED
```

A topic may be marked `COMPLETED` only after all required validation and
evidence gates pass.

------------------------------------------------------------------------

## 20. Agent Handoff

At the end of every topic, update `docs/AGENT_HANDOFF.md`.

The handoff must identify:

-   completed topic;
-   commit;
-   branch;
-   requirements implemented;
-   tests executed;
-   validation results;
-   evidence;
-   known limitations;
-   unresolved blockers;
-   next recommended topic.

The next agent must be able to resume without reconstructing the entire
history manually.

------------------------------------------------------------------------

## 21. Change Control

Material changes to requirements, architecture, safety rules, scope,
goal, or frozen baselines require controlled change.

Canonical flow:

``` text
Change Request
      ↓
Impact / Risk Assessment
      ↓
Authorized Approval
      ↓
Implementation
      ↓
Validation
      ↓
Evidence
      ↓
Version / Baseline Update
      ↓
Audit Record
```

An autonomous coding agent must not self-approve a material change.

------------------------------------------------------------------------

## 22. Failure Handling

When validation fails:

``` text
FAIL
 ↓
CAPTURE ERROR
 ↓
IDENTIFY ROOT CAUSE
 ↓
FIX
 ↓
RERUN VALIDATION
```

Repeat until:

-   the defect is fixed; or
-   the task is genuinely blocked.

Never hide failures.

Never mark a failed task as completed.

Never weaken a test merely to obtain a green build without
requirement-backed justification.

------------------------------------------------------------------------

## 23. Git Commit Rules

Before committing:

``` bash
git status
git diff
git diff --check
```

Then verify:

-   no secrets;
-   no unrelated files;
-   no generated junk;
-   no accidental requirement changes;
-   tests pass;
-   documentation is consistent.

Use meaningful commit messages.

Example:

``` text
feat(topic-12): implement opportunity discovery foundation
```

or:

``` text
chore: initialize autonomous project structure
```

------------------------------------------------------------------------

## 24. Evidence and Traceability

Every completed topic must preserve enough evidence to answer:

``` text
Which SRS requirement was implemented?
Which files implement it?
Which tests verify it?
Which validation commands passed?
Which commit contains it?
Which agent performed the work?
Which configuration/version was used?
```

Where the system supports it, preserve:

-   requirement ID;
-   version;
-   actor/component;
-   timestamp;
-   input/output references;
-   decision/state;
-   evidence;
-   test result;
-   change linkage.

------------------------------------------------------------------------

## 25. Bootstrap Task

`PROMPT_00_PROJECT_BOOTSTRAP.md` is a foundation task.

It must establish the repository without pretending that the complete
application has already been implemented.

Bootstrap should establish:

``` text
project structure
documentation structure
testing foundation
prompt infrastructure
topic decomposition
dependency tracking
status tracking
agent handoff
CI/CD foundation where required
security conventions
development conventions
```

Business functionality should be implemented by the corresponding topic
prompts.

------------------------------------------------------------------------

## 26. Topic Completion Gate

A topic is complete only when:

-   [ ] all applicable SRS requirements are implemented;
-   [ ] no frozen requirement was changed;
-   [ ] prerequisites were satisfied;
-   [ ] dependencies were respected;
-   [ ] tests exist for required behaviour;
-   [ ] tests pass;
-   [ ] applicable static/security checks pass;
-   [ ] acceptance criteria pass;
-   [ ] evidence is captured;
-   [ ] traceability is updated;
-   [ ] documentation is updated;
-   [ ] project status is updated;
-   [ ] handoff is updated;
-   [ ] git diff is reviewed;
-   [ ] commit is created;
-   [ ] branch is pushed.

------------------------------------------------------------------------

## 27. Final Integration Gate

After Topics 1--40:

``` text
All topics complete
      ↓
Full requirement traceability
      ↓
Full regression suite
      ↓
Integration validation
      ↓
Security validation
      ↓
Safety validation
      ↓
PoV validation
      ↓
Release criteria
      ↓
Human governance / release gate
```

The final system must not be declared production-ready solely because
all code compiles.

Release must satisfy the SRS's Topic 38 Proof-of-Value release criteria
and the applicable governance gates.

------------------------------------------------------------------------

## 28. Non-Negotiable Agent Rules

1.  Do not guess requirements.
2.  Do not silently modify the SRS.
3.  Do not silently change the project goal.
4.  Do not expand scope.
5.  Do not fabricate data.
6.  Do not fabricate evidence.
7.  Do not claim tests passed when they were not run.
8.  Do not bypass safety gates.
9.  Do not perform unauthorized live financial actions.
10. Do not commit secrets.
11. Do not approve your own governance change.
12. Do not modify locked baselines.
13. Do not silently renumber requirements.
14. Do not skip dependency checks.
15. Do not mark blocked work as complete.
16. Preserve traceability.
17. Preserve evidence.
18. Fail closed when correctness or safety is uncertain.
19. Escalate unresolved material conflicts.
20. Leave the repository in a recoverable state.

------------------------------------------------------------------------

## 29. Autonomous Development Command Pattern

Each topic agent should conceptually execute:

``` text
1. Load authoritative SRS.
2. Load MASTER.md.
3. Load topic prompt.
4. Inspect repository.
5. Inspect previous topic status.
6. Verify prerequisites.
7. Verify dependencies.
8. Create feature branch.
9. Produce implementation plan.
10. Implement current topic.
11. Add/update tests.
12. Run validation.
13. Fix failures.
14. Run regression.
15. Perform requirement self-review.
16. Capture evidence.
17. Update traceability.
18. Update project status.
19. Update agent handoff.
20. Review git diff.
21. Commit.
22. Push.
23. Report exact result.
```

------------------------------------------------------------------------

## 30. Final Principle

The objective is not merely to produce code.

The objective is to produce a:

``` text
traceable
testable
auditable
safe
reproducible
incrementally developed
governed
autonomous
AI Investment Opportunity Agent
```

Every implementation decision must remain traceable to the authoritative
SRS or an explicitly approved controlled change.
