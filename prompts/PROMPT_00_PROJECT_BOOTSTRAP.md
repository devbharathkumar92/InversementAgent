# PROMPT_00 --- Repository Bootstrap and SRS-Driven Autonomous Development

## Read first

Read these files from the repository:

1.  `MASTER.md`
2.  `SRS.md`
3.  The relevant `srs/topics/TOPIC_XX.md`

The SRS is already in the repository. **Do not ask the user to upload
the SRS PDF or Markdown file.**

## SRS access model

-   `SRS.md` is the SRS index.
-   `srs/topics/TOPIC_01.md` through `TOPIC_40.md` contain the complete
    topic-level source requirements.
-   Read only the assigned topic plus its required dependencies, unless
    broader inspection is needed for traceability.
-   Never replace the repository SRS with a shortened summary.
-   Never silently alter authoritative requirement wording.

## Bootstrap objective

Inspect the repository and establish the project structure required by
`MASTER.md` and the SRS. Create the documentation, testing, prompt,
status, traceability, and handoff foundations needed for topic-by-topic
autonomous implementation.

Do not pretend business functionality is complete during bootstrap.

## Required behaviour

-   Create a feature branch.
-   Audit the existing repository before changing anything.
-   Verify the SRS/MASTER files are present and readable.
-   Establish `PROJECT_STATUS.md`.
-   Establish `docs/AGENT_HANDOFF.md`.
-   Establish prompt infrastructure for Topics 1--40.
-   Establish testing/CI foundations appropriate to the actual
    technology stack.
-   Preserve the frozen SRS hierarchy.
-   Do not invent missing requirements.
-   Run all applicable validation.
-   Record evidence.
-   Commit and report exact results.

## Topic prompt generation

Generate one implementation prompt per topic:

`prompts/TOPICS/TOPIC_01.md` ... `prompts/TOPICS/TOPIC_40.md`

Each prompt must explicitly reference:

-   `MASTER.md`
-   `SRS.md`
-   its corresponding `srs/topics/TOPIC_XX.md`
-   exact requirement IDs
-   prerequisites
-   dependencies
-   implementation scope
-   tests
-   validation
-   evidence
-   acceptance criteria
-   branch/commit requirements
-   handoff requirements

A topic prompt must instruct the implementation agent to implement
**only that topic and the minimum dependency-supporting work required**.

## Completion

Do not mark bootstrap complete until the repository structure, prompt
framework, status tracking, and validation foundations are actually
present and verified.
