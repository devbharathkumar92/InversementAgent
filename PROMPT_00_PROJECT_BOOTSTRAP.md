# PROMPT 00 — PROJECT BOOTSTRAP & AUTONOMOUS DEVELOPMENT WORKFLOW

## ROLE

You are the autonomous senior software architect and development agent responsible for initializing this project repository and establishing the development workflow.

You must work from the provided:

1. `SRS.md` — complete Software Requirements Specification
2. `MASTER.md` — master technical/project instructions

These two files are the authoritative sources for understanding the project.

Your job in this task is **NOT to implement the complete application**.

Your job is to:

- understand the complete SRS
- understand the complete MASTER.md
- derive the complete architecture
- create the complete project structure
- establish the development conventions
- establish the autonomous topic-by-topic workflow
- create the prompt/task structure that future agents will follow
- create initial configuration and documentation
- create the required test/verification infrastructure
- validate the resulting structure
- commit the bootstrap implementation

Do not prematurely implement application features unless they are required for the project skeleton, configuration, tooling, or validation infrastructure.

---

# 1. AUTHORITATIVE DOCUMENTS

Before doing anything else, locate and read:

```text
SRS.md
MASTER.md
```

Read both files completely.

Do not assume that the information in this prompt overrides requirements explicitly defined in those documents.

Priority of requirements:

```text
SRS.md
   ↓
MASTER.md
   ↓
This prompt
   ↓
Agent assumptions
```

If SRS.md and MASTER.md conflict:

1. Identify the conflict.
2. Follow the explicitly defined priority/rules in MASTER.md if it specifies one.
3. Otherwise do not silently choose an implementation.
4. Record the conflict in `docs/DECISIONS.md`.
5. Continue only where the conflict does not block project initialization.

---

# 2. INITIAL REPOSITORY AUDIT

Before creating files:

Inspect the repository.

Determine:

- current files
- current directories
- existing source code
- existing configuration
- existing package manager
- existing build system
- existing test framework
- existing CI/CD configuration
- existing documentation
- existing `.gitignore`
- existing environment configuration
- existing scripts
- existing branches if accessible

Do NOT blindly overwrite existing files.

Preserve useful existing project assets unless SRS.md explicitly requires replacement.

Create a short internal assessment before modifying the repository.

---

# 3. UNDERSTAND THE COMPLETE SYSTEM

Extract from SRS.md and MASTER.md:

### Product

- product purpose
- target users
- major use cases
- functional requirements
- non-functional requirements

### Architecture

Identify:

- frontend
- backend
- APIs
- database
- authentication
- authorization
- external services
- background jobs
- storage
- caching
- messaging
- integrations
- observability
- deployment infrastructure

Only create components that are actually required by the SRS/Master specification.

Do not invent unnecessary technologies.

---

# 4. CREATE THE COMPLETE PROJECT STRUCTURE

Create a logical project structure that represents the COMPLETE system described by the SRS.

The structure must make it possible to implement the project incrementally.

Use appropriate directories for:

```text
source code
tests
documentation
configuration
scripts
database
API
components/modules
infrastructure
deployment
CI/CD
development prompts
architecture decisions
test plans
```

The exact directory names must be determined from the technology stack and architecture specified by SRS.md and MASTER.md.

Do not force a generic structure onto a project if the SRS specifies another architecture.

---

# 5. PROMPT-DRIVEN DEVELOPMENT ARCHITECTURE

Create a dedicated directory:

```text
prompts/
```

This directory will contain the autonomous development tasks.

Create:

```text
prompts/
├── README.md
├── PROMPT_00_PROJECT_BOOTSTRAP.md
├── TOPICS/
│   ├── README.md
│   ├── TOPIC_01.md
│   ├── TOPIC_02.md
│   ├── TOPIC_03.md
│   └── ...
└── templates/
    └── TOPIC_PROMPT_TEMPLATE.md
```

The number of topic prompts must be derived from the SRS.

Do NOT arbitrarily choose the number of topics.

Each major independent feature/domain/unit from the SRS should become a future implementation topic.

---

# 6. TOPIC DECOMPOSITION

Break the complete SRS into implementation topics.

Each topic must have:

```text
Topic ID
Topic name
Purpose
Dependencies
Requirements covered
Components affected
Files likely affected
Database changes
API changes
UI changes
Business logic
Testing requirements
Acceptance criteria
Verification requirements
Completion criteria
```

Create a dependency-aware order.

Example:

```text
TOPIC_01
    ↓
TOPIC_02
    ↓
TOPIC_03
    ↓
TOPIC_04
```

If topics can run independently, explicitly identify that.

Do not create circular dependencies.

---

# 7. TOPIC PROMPT TEMPLATE

Create:

```text
prompts/templates/TOPIC_PROMPT_TEMPLATE.md
```

The template must require every future autonomous agent to follow this lifecycle:

```text
READ
 ↓
UNDERSTAND
 ↓
PLAN
 ↓
CREATE FEATURE BRANCH
 ↓
IMPLEMENT
 ↓
TEST
 ↓
VERIFY
 ↓
SELF-REVIEW
 ↓
FIX
 ↓
FINAL VALIDATION
 ↓
COMMIT
 ↓
REPORT
```

Every topic prompt must contain the following sections:

```markdown
# TOPIC XX — <NAME>

## Objective

## SRS Requirements Covered

## MASTER.md References

## Preconditions

## Dependencies

## Existing Components To Reuse

## Files To Create

## Files To Modify

## Implementation Requirements

## Database Requirements

## API Requirements

## UI Requirements

## Business Logic Requirements

## Error Handling

## Security Requirements

## Testing Requirements

## Unit Tests

## Integration Tests

## End-to-End Tests

## Validation Commands

## Acceptance Criteria

## Self-Review Checklist

## Completion Criteria

## Git Branch

## Commit Requirements

## Final Report
```

Only include sections relevant to the actual project.

---

# 8. AUTONOMOUS AGENT WORKFLOW

Create:

```text
docs/AUTONOMOUS_WORKFLOW.md
```

Define the standard workflow.

The agent must operate as follows.

## Phase 1 — READ

Read:

```text
SRS.md
MASTER.md
current topic prompt
relevant documentation
relevant existing source code
previous topic completion information
```

Never implement based only on the topic prompt if the SRS or MASTER.md contains additional constraints.

---

## Phase 2 — ANALYZE

Determine:

- what must be implemented
- what already exists
- what must be reused
- what must be changed
- dependencies
- risks
- expected tests

---

## Phase 3 — PLAN

Before writing code, create an implementation plan.

The plan should identify:

```text
files
modules
components
interfaces
database changes
API changes
tests
configuration
```

Avoid unnecessary changes.

---

# 9. FEATURE BRANCH POLICY

Every topic must be implemented on its own branch.

Branch naming convention:

```text
feature/topic-01-<short-name>
feature/topic-02-<short-name>
feature/topic-03-<short-name>
```

Never implement a topic directly on `main` unless MASTER.md explicitly requires it.

Before implementation:

```bash
git checkout main
git pull
git checkout -b feature/topic-XX-<name>
```

Use the repository's actual default branch if it is not `main`.

---

# 10. IMPLEMENTATION POLICY

Implement only the current topic.

Do not silently implement future topics.

However, if the current topic requires a small foundational change required by a dependency, that change is allowed.

Document such changes.

Do not:

- rewrite unrelated modules
- introduce unnecessary dependencies
- change architecture without justification
- remove existing functionality without authorization
- ignore SRS requirements
- create fake implementations merely to make tests pass
- leave unexplained TODOs

---

# 11. TEST-FIRST / TEST-ALONGSIDE DEVELOPMENT

For every feature:

1. Identify expected behavior.
2. Create or update tests.
3. Implement the feature.
4. Run tests.
5. Fix failures.
6. Run regression tests.

Tests must validate actual requirements.

Do not create tests that merely assert that code exists.

Where applicable, test:

```text
happy path
edge cases
invalid input
error handling
authorization
authentication
data validation
failure scenarios
integration boundaries
```

---

# 12. VERIFICATION

Every topic must define executable verification commands.

Examples:

```bash
npm test
npm run lint
npm run typecheck
npm run build
```

or the equivalent commands for the project's actual technology stack.

Do not invent commands that do not exist.

Before completion:

```text
Build → PASS
Tests → PASS
Lint → PASS
Type checking → PASS
Relevant integration tests → PASS
```

If a command cannot be run, document why.

---

# 13. SELF-REVIEW

Before committing, compare the implementation against:

```text
SRS.md
MASTER.md
current topic prompt
acceptance criteria
tests
```

Ask:

- Did I implement every requirement?
- Did I miss an edge case?
- Did I introduce unrelated changes?
- Did I break an existing feature?
- Are tests meaningful?
- Is documentation updated?
- Is configuration correct?
- Are secrets excluded?
- Are error paths handled?
- Are security requirements satisfied?

Fix all issues found during self-review.

---

# 14. SECURITY

Never commit:

```text
GitHub tokens
API keys
passwords
private keys
database credentials
OAuth secrets
`.env` files containing real secrets
```

Use:

```text
.env.example
```

for documented environment variables.

Secrets must come from the execution environment or secret manager.

---

# 15. DOCUMENTATION

Maintain:

```text
README.md
docs/
```

Documentation should explain:

- project purpose
- architecture
- setup
- development
- testing
- environment variables
- deployment
- autonomous workflow
- topic sequence
- important architectural decisions

Create:

```text
docs/ARCHITECTURE.md
docs/DEVELOPMENT.md
docs/TESTING.md
docs/AUTONOMOUS_WORKFLOW.md
docs/DECISIONS.md
```

where applicable.

---

# 16. PROJECT STATUS TRACKING

Create:

```text
PROJECT_STATUS.md
```

Track:

```text
Topic ID
Topic
Status
Dependencies
Branch
Implementation status
Tests
Verification
Commit
Notes
```

Initial status should be:

```text
PROJECT BOOTSTRAP     COMPLETE
TOPIC 01              NOT_STARTED
TOPIC 02              NOT_STARTED
...
```

Do not mark future topics as complete.

---

# 17. AGENT HANDOFF

Create:

```text
docs/AGENT_HANDOFF.md
```

This file must explain how the next autonomous agent continues the project.

The next agent must be able to determine:

1. What has already been completed.
2. What topic should be implemented next.
3. Which branch should be created.
4. Which files are authoritative.
5. Which tests must pass.
6. What previous decisions were made.
7. What remains unfinished.

---

# 18. FAILURE HANDLING

If implementation or verification fails:

Do NOT commit knowingly broken code.

Instead:

```text
Identify failure
↓
Determine root cause
↓
Fix
↓
Run tests again
↓
Repeat until verified
```

If the problem cannot be resolved:

1. Do not fake success.
2. Document the failure.
3. Record the exact error.
4. Record attempted solutions.
5. Leave the repository in the safest valid state.
6. Report the blocker clearly.

---

# 19. GIT COMMIT

After successful validation:

Check:

```bash
git status
git diff
```

Ensure no secrets or unintended files are included.

Then create a meaningful commit.

Example:

```text
chore: initialize project structure and autonomous workflow
```

The commit message should accurately describe the actual work.

Push the branch to GitHub.

Do not force-push.

Do not rewrite unrelated history.

---

# 20. BOOTSTRAP TASK — SPECIAL RULE

For THIS prompt only:

Do NOT implement the application's complete features.

Instead create:

```text
complete project structure
development configuration
testing infrastructure
documentation structure
prompt infrastructure
topic decomposition
autonomous workflow
project status tracking
agent handoff documentation
initial CI/CD structure if required by MASTER.md
```

Create placeholder files only where they are architecturally justified.

Do not create fake business logic.

---

# 21. GENERATE FUTURE TOPIC PROMPTS

After analyzing the SRS, generate the actual topic prompts.

Each prompt must be independently understandable but must reference:

```text
SRS.md
MASTER.md
PROJECT_STATUS.md
docs/ARCHITECTURE.md
```

Each prompt must tell the future agent:

```text
Implement ONLY this topic.
Follow the autonomous workflow.
Create a feature branch.
Inspect existing implementation.
Implement.
Test.
Verify.
Self-review.
Commit.
Push.
Update project status.
Update handoff documentation.
```

---

# 22. TOPIC DEPENDENCY GRAPH

Create:

```text
docs/TOPIC_DEPENDENCY_GRAPH.md
```

Represent dependencies clearly.

For example:

```text
TOPIC 01
   │
   ├── TOPIC 02
   │       │
   │       └── TOPIC 04
   │
   └── TOPIC 03
           │
           └── TOPIC 05
```

Use the actual dependencies discovered from the SRS.

---

# 23. DEFINITION OF DONE

The bootstrap task is complete only when:

- [ ] SRS.md read
- [ ] MASTER.md read
- [ ] Existing repository audited
- [ ] Architecture derived
- [ ] Complete project structure created
- [ ] Documentation structure created
- [ ] Testing infrastructure established
- [ ] Prompt infrastructure created
- [ ] SRS decomposed into implementation topics
- [ ] Topic dependency graph created
- [ ] Topic prompts created
- [ ] Autonomous workflow documented
- [ ] Project status tracking created
- [ ] Agent handoff created
- [ ] Security rules documented
- [ ] Repository validation completed
- [ ] No secrets committed
- [ ] Git diff reviewed
- [ ] Bootstrap commit created
- [ ] Branch pushed to GitHub

Do not claim completion until these checks have been performed.

---

# 24. FINAL AGENT REPORT

At the end provide a concise report containing:

```text
BOOTSTRAP STATUS: COMPLETE / BLOCKED

Repository:
<repository>

Branch:
<branch>

Commit:
<commit hash>

Architecture:
<summary>

Directories created:
<list>

Files created:
<list>

Topics generated:
<list>

Topic dependency order:
<order>

Tests executed:
<commands>

Validation:
PASS / FAIL

Known issues:
<list>

Next task:
TOPIC_01
```

If anything is incomplete, explicitly state it.

Never report PASS when verification failed.

---

# FINAL INSTRUCTION

You are establishing the foundation for a long-running autonomous software-development project.

Optimize for:

```text
correctness
traceability
repeatability
testability
security
maintainability
clear agent handoff
incremental development
```

The SRS and MASTER.md are the source of truth.

Do not guess requirements.

Do not silently omit requirements.

Do not implement future topics during bootstrap.

Build the foundation so that a future autonomous agent can execute:

```text
TOPIC_01
→ test
→ verify
→ commit

TOPIC_02
→ test
→ verify
→ commit

TOPIC_03
→ test
→ verify
→ commit

...

FINAL INTEGRATION
→ full test suite
→ security verification
→ build
→ deployment verification
```

and eventually complete the entire SRS without losing architectural context or development history.