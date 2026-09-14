# Topic 2 --- Core Goal and Mission

> Authoritative source slice from the uploaded Full Master SRS. Source
> PDF pages 26--57. Preserve numbering and requirement wording.

## Source Requirements

```{=html}
<!-- Source PDF page 26 -->
```
AI Investment Opportunity Agent --- Topic 1 Baseline 1.13 Topic 1 Final
Validation and Baseline Gate The following gate is mandatory before
Topic 1 is declared baselined. Check Acceptance Condition Status
Hierarchy coverage All frozen Topic-1 items 1.1 through 1.12 and their
defined sub-items 1.3.1, 1.3.2, 1.5.1--1.5.3, 1.6.1--1.6.2, and
1.11.1--1.11.3 are explicitly specified. PASS Purpose/Objectives Every
numbered item has an explicit purpose and objective. PASS Requirement
quality Requirements are written as normative, testable statements and
avoid ambiguous language. PASS Inputs/Outputs Inputs, sources, outputs,
and destinations are defined for each item. PASS
Prerequisites/Dependencies Prerequisites and dependency relationships
are explicit. PASS Parallelization Parallelization eligibility and
restrictions are explicitly defined. PASS Technical/resource detail
Applicable technical controls, tools, repositories, schemas, and
mechanisms are identified. PASS Constraints/prohibitions Constraints and
prohibited actions are explicit. PASS Error/blocked/recovery Failure,
blocked-state, unblocking, escalation, and recovery behaviour is
defined. PASS Validation/testing Each item has validation and testing
expectations. PASS Evidence/acceptance Evidence and acceptance criteria
are explicit. PASS Audit/traceability Lifecycle actions are traceable
and auditable. PASS Change control Every item is protected by controlled
change management. PASS Baseline protection Baseline creation, lock,
modification, integrity, and recovery are defined. PASS Governance
Approval authority and state transitions are defined. PASS Baseline
Decision: ACCEPTED FOR TOPIC BASELINE, subject to project governance
approval of the baseline record. The document is intentionally
standalone so Topic 1 can be stored separately and used as the
authoritative Foundation Topic 1 reference. Baseline ID: T1-BL-001
Status: Baseline Candidate → Governance Approval Required Next Topic:
Topic 2 --- Core Goal and Mission. Topic 2 shall not modify this Topic 1
baseline; it shall reference it as a completed dependency. Reference
quality note: NASA requirements guidance recommends requirements that
are complete, correct, consistent, traceable, independent, unambiguous,
necessary, measurable, testable, maintainable, and feasible, and
recommends defining testing strategy as requirements are specified.
IciteIturn0search1Iturn0search3I

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 27 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline AI Investment
Opportunity Agent --- SRS Topic 2 --- Core Goal and Mission PHASE 1 /
FOUNDATION --- STANDALONE TOPIC BASELINE Baseline Candidate: T2-BL-001
Status: Ready for governance approval Prerequisite: Topic 1 --- Document
Control and Versioning is the completed dependency. Topic 2 does not
modify Topic 1. Source basis: The frozen project hierarchy defines Topic
2 as Core Goal and Mission with items 2.1--2.15 and the listed child
items. This document preserves that hierarchy and expands each item into
an implementation-ready specification contract. Completeness rule: Every
numbered item below contains the full 32-field contract. No field is
silently omitted. 2.1 Goal Statement Purpose Define the single
authoritative purpose of the project. Objective Make the project's
intended outcome explicit enough for every downstream requirement to be
tested for alignment. Requirement The system shall research and evaluate
short-term investment/trading opportunities within the approved initial
India and INR boundaries using validated evidence, analysis,
simulation/paper trading, risk controls, monitoring, and transparent
decision support. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs Approved project intent, Topic 1 baseline, and approved scope
assumptions. Input Source Project governance and SRS baseline.
Processing / Rules Normalize the project intent into one versioned
authoritative goal statement; alternative interpretations shall not
become authoritative. Outputs One approved goal statement with version
and status. Output Destination SRS baseline, goal registry, and
traceability records. Prerequisites Topic 1 baseline and project
identity. Dependencies Topic 1; Topic 4 for detailed boundaries.
Dependency Type Hard dependency for any action that must preserve the
approved goal; analytical checks may be parallel where they only read
the same immutable baseline. Parallelization Eligibility Independent
evidence collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details The goal shall be stored as structured versioned content so
automated alignment checks can compare downstream artifacts against it.
Tools / Resources Version-control repository, requirements registry,
validation scripts. Constraints The approved goal is immutable during
normal operation; initial India/INR scope and safety constraints remain
binding unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 28 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Unblocking
Conditions Resume only after the correct baseline, evidence,
clarification, or governance decision is available and affected
validation passes. Human Escalation Human governance is required for
immutable-goal changes, unresolved material conflicts, scope/mission
changes, and final goal-baseline approval. Validation Method Requirement
inspection, goal-to-requirement traceability checks, policy checks,
conflict tests, deviation tests, and approval/baseline verification.
Testing Requirements Positive alignment, negative violation,
conflicting-instruction, unauthorized-change, stale-version, regression,
and recovery tests shall be performed as applicable. Evidence Required
Goal/mission records, baseline/version IDs, traceability mappings,
validation results, test results, approval records, and audit events.
Acceptance Criteria The item is accepted only when it is unambiguous,
testable, traceable, consistent with higher-level rules, and protected
against unauthorized alteration. Failure / Rejection Criteria Failure
occurs if the item is ambiguous, contradictory, untestable, unsupported
by evidence, unauthorized, or capable of allowing silent goal drift.
Recovery / Corrective Action Restore the last approved baseline,
preserve evidence, identify root cause, correct through Topic 1 change
control, and rerun validation. Audit / Traceability Material goal
decisions, changes, conflicts, deviations, reviews, and approvals shall
identify version, actor, timestamp, affected item, decision, reason, and
evidence. Change Control Material changes require change request, impact
assessment, authorized approval, validation, new version, and controlled
baseline update under Topic 1. 2.2 Mission Statement Purpose Translate
the goal into an operational mission. Objective Keep the system's
ongoing activities connected to the approved purpose. Requirement The
mission shall be to acquire and validate relevant data, discover and
analyze opportunities, evaluate strategies and risks, simulate outcomes,
monitor paper performance, provide evidence-based decision support, and
expose system state transparently while respecting authority and safety
boundaries. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs Approved goal and system scope. Input Source 2.1 and Topic 4.
Processing / Rules Translate the goal into operational capabilities
without introducing a new independent business objective. Outputs
Approved mission statement. Output Destination SRS mission section and
goal registry. Prerequisites 2.1. Dependencies 2.1 and Topic 4.
Dependency Type Hard dependency for any action that must preserve the
approved goal; analytical checks may be parallel where they only read
the same immutable baseline. Parallelization Eligibility Independent
evidence collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Mission text shall be versioned and linked to the goal version
it operationalizes. Tools / Resources SRS repository and traceability
matrix.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 29 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Constraints The
approved goal is immutable during normal operation; initial India/INR
scope and safety constraints remain binding unless formally changed.
Prohibited Actions Silent goal changes, unapproved scope expansion,
safety bypass, fabricated evidence, guaranteed-profit claims, and
self-approval are prohibited. Expected Behaviour The system shall
continuously use the approved goal as the highest-level reference for
downstream requirements and actions. Error Handling Ambiguity, conflict,
missing approval, stale baseline, or unauthorized modification shall be
rejected or moved to blocked/escalated state, with evidence preserved.
Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.3 Primary Objective Purpose Define the highest-priority
measurable objective derived from the mission. Objective Make the
central system outcome explicit and testable. Requirement The primary
objective shall be to identify and evaluate short-term opportunities
using validated evidence and risk-aware analysis, and determine whether
each merits simulation/paper-trading consideration or no action. Scope
This item applies to the authoritative project goal/mission definition
and to downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs Goal, mission,
validated data, and opportunity candidates. Input Source Approved
goal/mission and later approved data and intelligence components.
Processing / Rules Apply approved discovery, analysis, scoring,
strategy, and risk rules; opportunity detection shall not be treated as
guaranteed profitability. Outputs Evaluated opportunity and decision
state. Output Destination Decision pipeline, dashboard, and audit trail.
Prerequisites 2.1 and 2.2. Dependencies 2.1, 2.2; later Topics 12--19.
Dependency Type Hard dependency for any action that must preserve the
approved goal; analytical checks may be parallel where they only read
the same immutable baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 30 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Parallelization
Eligibility Independent evidence collection, alignment checks, metric
calculations, and review preparation may run in parallel when they do
not create competing authoritative writes. Parallelization Restrictions
No parallel agent may create a competing authoritative goal baseline,
alter immutable goal elements, or approve its own goal change.
Responsible Owner SRS Governance Owner / SRS Writer Agent for
specification; authorized human governance for controlled approval or
goal modification. Technical Details Represent the objective as a
traceable requirement with stable ID rather than embedding it only in
agent prompts. Tools / Resources Requirements registry, test framework,
decision records. Constraints The approved goal is immutable during
normal operation; initial India/INR scope and safety constraints remain
binding unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.3.1 Primary Objective Definition Purpose Define exactly what
constitutes completion of the primary objective for one opportunity.
Objective Remove ambiguity from the terms identify and evaluate.
Requirement An evaluation shall require a valid opportunity definition,
evidence, data-quality status, analysis result, risk assessment,
applicable strategy assessment, confidence, and a defined decision
outcome. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs Opportunity candidate and supporting records. Input Source
Discovery, data-quality, analysis, strategy, and risk layers.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 31 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Processing / Rules
Validate all mandatory fields; reject incomplete evaluation rather than
inventing missing values. Outputs Complete opportunity-evaluation
package. Output Destination Decision engine, dashboard, and audit trail.
Prerequisites 2.3. Dependencies 2.3; later Topics 10--19. Dependency
Type Hard dependency for any action that must preserve the approved
goal; analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Use a versioned evaluation schema with mandatory-field
validation and evidence references. Tools / Resources Schema validator
and traceability system. Constraints The approved goal is immutable
during normal operation; initial India/INR scope and safety constraints
remain binding unless formally changed. Prohibited Actions Silent goal
changes, unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.3.2 Secondary Objectives Purpose Define supporting objectives
without allowing them to compete with the primary objective. Objective
Explicitly cover supporting reliability, safety, analysis, monitoring,
and improvement capabilities.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 32 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Requirement
Secondary objectives shall include data-quality improvement, opportunity
ranking, strategy comparison, backtesting, paper trading, risk
monitoring, P&L; tracking, explainability, auditability, reliability,
and evidence-based controlled improvement. Scope This item applies to
the authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Primary objective and system
principles. Input Source 2.3 and Topic 5. Processing / Rules Classify
each as supporting; none may override the primary objective, scope, or
safety rules. Outputs Versioned secondary-objective set and priority
relationships. Output Destination SRS and traceability matrix.
Prerequisites 2.3. Dependencies 2.3 and Topic 5. Dependency Type Hard
dependency for any action that must preserve the approved goal;
analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Each objective shall have a stable identifier and explicit
relationship to the primary objective. Tools / Resources Requirements
registry and validation tests. Constraints The approved goal is
immutable during normal operation; initial India/INR scope and safety
constraints remain binding unless formally changed. Prohibited Actions
Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions. Error Handling Ambiguity, conflict, missing approval, stale
baseline, or unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria Every secondary objective
is traceable to the primary objective and has no authority to override
safety or goal constraints. Failure / Rejection Criteria Failure occurs
if the item is ambiguous, contradictory, untestable, unsupported by
evidence, unauthorized, or capable of allowing silent goal drift.
Recovery / Corrective Action Restore the last approved baseline,
preserve evidence, identify root cause, correct through Topic 1 change
control, and rerun validation.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 33 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Audit /
Traceability Material goal decisions, changes, conflicts, deviations,
reviews, and approvals shall identify version, actor, timestamp,
affected item, decision, reason, and evidence. Change Control Material
changes require change request, impact assessment, authorized approval,
validation, new version, and controlled baseline update under Topic 1.
2.4 Expected System Outcome Purpose Define what a complete goal-level
opportunity output must contain. Objective Prevent the system from
reducing complex evaluation to unsupported buy/sell labels. Requirement
For each evaluated opportunity, the system shall provide, where
applicable, asset, opportunity reason, evidence, data freshness/quality,
analysis, strategy context, expected-return estimate, risk,
costs/charges, confidence, time horizon, decision outcome, and
simulation/paper result. Scope This item applies to the authoritative
project goal/mission definition and to downstream requirements, tasks,
agents, decisions, outputs, and governance actions that must remain
aligned with it. It does not replace the detailed system-scope
definition in Topic 4. Inputs Validated opportunity, analysis, risk,
strategy, and simulation records. Input Source Downstream intelligence
and evaluation components. Processing / Rules Assemble only traceable
records; missing mandatory context makes the evaluation incomplete.
Outputs Complete decision-context package. Output Destination Decision
engine, dashboard, and audit trail. Prerequisites 2.3.1. Dependencies
Topics 11--20. Dependency Type Hard dependency for any action that must
preserve the approved goal; analytical checks may be parallel where they
only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details Use a versioned output schema with
mandatory-field and provenance validation. Tools / Resources Schema
validation and reporting pipeline. Constraints The approved goal is
immutable during normal operation; initial India/INR scope and safety
constraints remain binding unless formally changed. Prohibited Actions
Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions. Error Handling Ambiguity, conflict, missing approval, stale
baseline, or unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 34 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Evidence Required
Goal/mission records, baseline/version IDs, traceability mappings,
validation results, test results, approval records, and audit events.
Acceptance Criteria The item is accepted only when it is unambiguous,
testable, traceable, consistent with higher-level rules, and protected
against unauthorized alteration. Failure / Rejection Criteria Failure
occurs if the item is ambiguous, contradictory, untestable, unsupported
by evidence, unauthorized, or capable of allowing silent goal drift.
Recovery / Corrective Action Restore the last approved baseline,
preserve evidence, identify root cause, correct through Topic 1 change
control, and rerun validation. Audit / Traceability Material goal
decisions, changes, conflicts, deviations, reviews, and approvals shall
identify version, actor, timestamp, affected item, decision, reason, and
evidence. Change Control Material changes require change request, impact
assessment, authorized approval, validation, new version, and controlled
baseline update under Topic 1. 2.5 Goal Scope Purpose Define what the
goal covers at the highest level. Objective Keep the project focused
while allowing future controlled expansion. Requirement The goal
initially covers India-focused, INR-based short-term opportunity
research, analysis, simulation, paper trading, monitoring, and decision
support; it does not authorize unrestricted live financial execution or
uncontrolled geographic/currency expansion. Scope This item applies to
the authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Approved scope boundaries.
Input Source Topic 4. Processing / Rules Classify proposed capability as
in-scope, out-of-scope, or requiring controlled expansion. Outputs
Goal-scope statement and boundary references. Output Destination SRS and
scope registry. Prerequisites 2.1. Dependencies Topic 4. Dependency Type
Hard dependency for any action that must preserve the approved goal;
analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Scope elements shall use stable identifiers for automated
alignment checks. Tools / Resources Scope registry and traceability
system. Constraints The approved goal is immutable during normal
operation; initial India/INR scope and safety constraints remain binding
unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 35 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Unblocking
Conditions Resume only after the correct baseline, evidence,
clarification, or governance decision is available and affected
validation passes. Human Escalation Human governance is required for
immutable-goal changes, unresolved material conflicts, scope/mission
changes, and final goal-baseline approval. Validation Method Requirement
inspection, goal-to-requirement traceability checks, policy checks,
conflict tests, deviation tests, and approval/baseline verification.
Testing Requirements Positive alignment, negative violation,
conflicting-instruction, unauthorized-change, stale-version, regression,
and recovery tests shall be performed as applicable. Evidence Required
Goal/mission records, baseline/version IDs, traceability mappings,
validation results, test results, approval records, and audit events.
Acceptance Criteria The item is accepted only when it is unambiguous,
testable, traceable, consistent with higher-level rules, and protected
against unauthorized alteration. Failure / Rejection Criteria Failure
occurs if the item is ambiguous, contradictory, untestable, unsupported
by evidence, unauthorized, or capable of allowing silent goal drift.
Recovery / Corrective Action Restore the last approved baseline,
preserve evidence, identify root cause, correct through Topic 1 change
control, and rerun validation. Audit / Traceability Material goal
decisions, changes, conflicts, deviations, reviews, and approvals shall
identify version, actor, timestamp, affected item, decision, reason, and
evidence. Change Control Material changes require change request, impact
assessment, authorized approval, validation, new version, and controlled
baseline update under Topic 1. 2.6 Goal Constraints Purpose Define
constraints that remain binding while pursuing the goal. Objective
Prevent speed or return optimization from overriding safety, evidence,
scope, or governance. Requirement The system shall operate within
approved India/INR boundaries, use validated evidence, apply safety/risk
controls, prefer simulation/paper trading before live deployment,
maintain auditability, and prohibit silent goal or scope changes. Scope
This item applies to the authoritative project goal/mission definition
and to downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs Goal, scope,
principles, and safety constraints. Input Source 2.1--2.5 and Topic 5.
Processing / Rules Apply constraints as preconditions to downstream
tasks and restricted actions. Outputs Machine-checkable goal constraint
set. Output Destination Validation gates and governance controls.
Prerequisites 2.1--2.5. Dependencies Topic 5 and later risk
requirements. Dependency Type Hard dependency for any action that must
preserve the approved goal; analytical checks may be parallel where they
only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details Constraints should be represented as
policy rules wherever technically feasible. Tools / Resources
Policy/configuration validation and automated gates. Constraints The
approved goal is immutable during normal operation; initial India/INR
scope and safety constraints remain binding unless formally changed.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 36 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Prohibited Actions
Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions. Error Handling Ambiguity, conflict, missing approval, stale
baseline, or unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.7 Non-Negotiable Goal Conditions Purpose Define conditions
that must always remain true. Objective Protect project identity and
safety under all agent behaviours. Requirement The system shall preserve
the approved goal, initial India/INR scope, safety controls, evidence
requirements, traceability, auditability, and required human approval
gates. Scope This item applies to the authoritative project goal/mission
definition and to downstream requirements, tasks, agents, decisions,
outputs, and governance actions that must remain aligned with it. It
does not replace the detailed system-scope definition in Topic 4. Inputs
Approved goal and principles. Input Source 2.1, 2.6, and Topic 5.
Processing / Rules Check applicable conditions before accepting material
workflow or state transitions. Outputs Pass/fail condition set. Output
Destination Governance and runtime validation. Prerequisites 2.6.
Dependencies Topic 5. Dependency Type Hard dependency for any action
that must preserve the approved goal; analytical checks may be parallel
where they only read the same immutable baseline. Parallelization
Eligibility Independent evidence collection, alignment checks, metric
calculations, and review preparation may run in parallel when they do
not create competing authoritative writes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 37 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Parallelization
Restrictions No parallel agent may create a competing authoritative goal
baseline, alter immutable goal elements, or approve its own goal change.
Responsible Owner SRS Governance Owner / SRS Writer Agent for
specification; authorized human governance for controlled approval or
goal modification. Technical Details Represent conditions as executable
policy rules where feasible. Tools / Resources Policy engine and test
suite. Constraints The approved goal is immutable during normal
operation; initial India/INR scope and safety constraints remain binding
unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.7.1 Mandatory Conditions Purpose Enumerate conditions that
cannot be omitted. Objective Make goal protections objectively testable.
Requirement Mandatory conditions shall include goal immutability, scope
compliance, safety compliance, evidence-backed outputs, traceability,
auditability, and required approval gates. Scope This item applies to
the authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs 2.7 condition set. Input
Source Approved goal and principles. Processing / Rules Evaluate each
condition at its applicable workflow gate and attach evidence. Outputs
Condition checklist and validation result.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 38 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Output Destination
Governance dashboard and audit trail. Prerequisites 2.7. Dependencies
2.7 and Topic 5. Dependency Type Hard dependency for any action that
must preserve the approved goal; analytical checks may be parallel where
they only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details Each condition should have an explicit
validation outcome and evidence reference. Tools / Resources Automated
policy tests. Constraints The approved goal is immutable during normal
operation; initial India/INR scope and safety constraints remain binding
unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.7.2 Goal Violation Conditions Purpose Define events that
constitute direct goal violation. Objective Enable deterministic
detection and safe handling of goal drift. Requirement Goal violation
shall include unapproved purpose change, unapproved geographic/currency
expansion, safety bypass, unauthorized live-capital action, fabricated
evidence, hidden material uncertainty/failure, or another explicit
baseline violation.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 39 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Scope This item
applies to the authoritative project goal/mission definition and to
downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs Runtime actions,
proposed changes, outputs, and audit events. Input Source Execution
records and governance controls. Processing / Rules Compare observed
action/state with immutable goal and constraints; classify severity.
Outputs Goal-violation event with severity and evidence. Output
Destination Audit trail, dashboard, and escalation workflow.
Prerequisites 2.7.1. Dependencies 2.8, 2.13, Topic 5. Dependency Type
Hard dependency for any action that must preserve the approved goal;
analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Run policy checks before restricted actions and post-event
monitoring. Tools / Resources Policy engine and monitoring agent.
Constraints The approved goal is immutable during normal operation;
initial India/INR scope and safety constraints remain binding unless
formally changed. Prohibited Actions Silent goal changes, unapproved
scope expansion, safety bypass, fabricated evidence, guaranteed-profit
claims, and self-approval are prohibited. Expected Behaviour The system
shall continuously use the approved goal as the highest-level reference
for downstream requirements and actions. Error Handling Ambiguity,
conflict, missing approval, stale baseline, or unauthorized modification
shall be rejected or moved to blocked/escalated state, with evidence
preserved. Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 40 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline 2.8 Goal
Immutability Purpose Protect the core goal from autonomous drift.
Objective Prevent optimization agents from redefining success.
Requirement The core goal shall be immutable during normal operation; an
approved change shall use controlled governance and create a new
version/baseline. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs Current approved goal and change proposal. Input Source Topic 1
change-control workflow. Processing / Rules Lock baseline; route
proposals through impact assessment, approval, validation, and
re-baselining. Outputs Locked baseline or approved successor version.
Output Destination SRS repository and goal registry. Prerequisites 2.1
and Topic 1. Dependencies Topic 1.5, 1.6, 1.11. Dependency Type Hard
dependency for any action that must preserve the approved goal;
analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Use protected repository permissions and versioned immutable
goal records. Tools / Resources VCS protections and governance workflow.
Constraints The approved goal is immutable during normal operation;
initial India/INR scope and safety constraints remain binding unless
formally changed. Prohibited Actions Silent goal changes, unapproved
scope expansion, safety bypass, fabricated evidence, guaranteed-profit
claims, and self-approval are prohibited. Expected Behaviour The system
shall continuously use the approved goal as the highest-level reference
for downstream requirements and actions. Error Handling Ambiguity,
conflict, missing approval, stale baseline, or unauthorized modification
shall be rejected or moved to blocked/escalated state, with evidence
preserved. Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 41 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Recovery /
Corrective Action Restore the last approved baseline, preserve evidence,
identify root cause, correct through Topic 1 change control, and rerun
validation. Audit / Traceability Material goal decisions, changes,
conflicts, deviations, reviews, and approvals shall identify version,
actor, timestamp, affected item, decision, reason, and evidence. Change
Control Material changes require change request, impact assessment,
authorized approval, validation, new version, and controlled baseline
update under Topic 1. 2.8.1 Immutable Goal Elements Purpose Identify
exactly what ordinary agents cannot change. Objective Remove ambiguity
about protected goal content. Requirement Immutable elements shall
include fundamental purpose, primary objective, initial
geographic/currency scope, safety-first requirement, and governance
requirement unless formally changed. Scope This item applies to the
authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Approved goal baseline. Input
Source 2.1--2.7 and Topics 4/5. Processing / Rules Tag immutable fields
and enforce write protection. Outputs Immutable-field definition. Output
Destination Goal registry and policy engine. Prerequisites 2.8.
Dependencies Topic 1 and Topic 5. Dependency Type Hard dependency for
any action that must preserve the approved goal; analytical checks may
be parallel where they only read the same immutable baseline.
Parallelization Eligibility Independent evidence collection, alignment
checks, metric calculations, and review preparation may run in parallel
when they do not create competing authoritative writes. Parallelization
Restrictions No parallel agent may create a competing authoritative goal
baseline, alter immutable goal elements, or approve its own goal change.
Responsible Owner SRS Governance Owner / SRS Writer Agent for
specification; authorized human governance for controlled approval or
goal modification. Technical Details Immutable fields shall have stable
identifiers for automated comparison. Tools / Resources Schema,
access-control, and regression tests. Constraints The approved goal is
immutable during normal operation; initial India/INR scope and safety
constraints remain binding unless formally changed. Prohibited Actions
Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions. Error Handling Ambiguity, conflict, missing approval, stale
baseline, or unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 42 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Testing
Requirements Positive alignment, negative violation,
conflicting-instruction, unauthorized-change, stale-version, regression,
and recovery tests shall be performed as applicable. Evidence Required
Goal/mission records, baseline/version IDs, traceability mappings,
validation results, test results, approval records, and audit events.
Acceptance Criteria The item is accepted only when it is unambiguous,
testable, traceable, consistent with higher-level rules, and protected
against unauthorized alteration. Failure / Rejection Criteria Failure
occurs if the item is ambiguous, contradictory, untestable, unsupported
by evidence, unauthorized, or capable of allowing silent goal drift.
Recovery / Corrective Action Restore the last approved baseline,
preserve evidence, identify root cause, correct through Topic 1 change
control, and rerun validation. Audit / Traceability Material goal
decisions, changes, conflicts, deviations, reviews, and approvals shall
identify version, actor, timestamp, affected item, decision, reason, and
evidence. Change Control Material changes require change request, impact
assessment, authorized approval, validation, new version, and controlled
baseline update under Topic 1. 2.8.2 Controlled Modification Exception
Purpose Define the only permitted path for changing an immutable goal
element. Objective Permit legitimate strategic change without enabling
autonomous goal drift. Requirement A goal change shall require a formal
change request, impact assessment, authorized approval, new version,
validation, and new baseline before adoption. Scope This item applies to
the authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Change request and impact
evidence. Input Source Topic 1.5 and governance. Processing / Rules Do
not apply the proposed goal until every required gate passes. Outputs
Approved successor goal or rejection record. Output Destination SRS
repository and governance audit. Prerequisites 2.8.1. Dependencies Topic
1.5, 1.6, 1.11. Dependency Type Hard dependency for any action that must
preserve the approved goal; analytical checks may be parallel where they
only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details The previous goal baseline must remain
recoverable after a change. Tools / Resources Change tracker, VCS,
approval workflow. Constraints The approved goal is immutable during
normal operation; initial India/INR scope and safety constraints remain
binding unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 43 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.9 Goal Evaluation Criteria Purpose Define how goal compliance
is judged. Objective Provide objective criteria for deciding whether
work serves the goal. Requirement Goal evaluation shall check functional
alignment, scope alignment, safety alignment, evidence quality,
traceability, expected outcome, and governance compliance. Scope This
item applies to the authoritative project goal/mission definition and to
downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs
Requirement/task/output and current goal baseline. Input Source Goal
registry and traceability records. Processing / Rules Run applicable
criteria and record pass/fail/exception with evidence. Outputs
Goal-alignment evaluation result. Output Destination Self-evaluation and
governance reports. Prerequisites 2.8 and current baseline. Dependencies
2.10, 2.11, 2.13. Dependency Type Hard dependency for any action that
must preserve the approved goal; analytical checks may be parallel where
they only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details Criteria should be machine-checkable
where possible and reviewable for qualitative dimensions. Tools /
Resources Validation engine and traceability matrix.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 44 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Constraints The
approved goal is immutable during normal operation; initial India/INR
scope and safety constraints remain binding unless formally changed.
Prohibited Actions Silent goal changes, unapproved scope expansion,
safety bypass, fabricated evidence, guaranteed-profit claims, and
self-approval are prohibited. Expected Behaviour The system shall
continuously use the approved goal as the highest-level reference for
downstream requirements and actions. Error Handling Ambiguity, conflict,
missing approval, stale baseline, or unauthorized modification shall be
rejected or moved to blocked/escalated state, with evidence preserved.
Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.10 Goal Success Metrics Purpose Define how success of the
goal is measured without assuming guaranteed profit. Objective Provide
quantitative and qualitative measures of system effectiveness and
reliability. Requirement Goal success metrics shall cover opportunity
detection quality, data quality/freshness, analysis quality, decision
quality, simulation reproducibility, paper-trading evaluation, risk
compliance, reliability, transparency, and auditability. Scope This item
applies to the authoritative project goal/mission definition and to
downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs Goal, PoV
objectives, and system outputs. Input Source Topic 3 and later approved
performance/risk requirements. Processing / Rules Measure against
pre-approved thresholds where defined; never invent post-hoc thresholds
to force acceptance. Outputs Goal metric set and evaluation result.
Output Destination PoV reports, dashboard, release gate. Prerequisites
2.9 and Topic 3. Dependencies 3.7 and later performance/risk
requirements. Dependency Type Hard dependency for any action that must
preserve the approved goal; analytical checks may be parallel where they
only read the same immutable baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 45 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Parallelization
Eligibility Independent evidence collection, alignment checks, metric
calculations, and review preparation may run in parallel when they do
not create competing authoritative writes. Parallelization Restrictions
No parallel agent may create a competing authoritative goal baseline,
alter immutable goal elements, or approve its own goal change.
Responsible Owner SRS Governance Owner / SRS Writer Agent for
specification; authorized human governance for controlled approval or
goal modification. Technical Details Each numerical metric shall define
formula, unit, timeframe, source, and interpretation. Tools / Resources
Metrics store, test framework, dashboard. Constraints The approved goal
is immutable during normal operation; initial India/INR scope and safety
constraints remain binding unless formally changed. Prohibited Actions
Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions. Error Handling Ambiguity, conflict, missing approval, stale
baseline, or unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.10.1 Quantitative Success Metrics Purpose Define numerical
indicators of goal performance. Objective Make objective claims
reproducible and comparable across versions. Requirement Each
quantitative metric shall define a name, formula, unit, data source,
measurement period, threshold where applicable, and acceptance
interpretation. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs Metric definitions and measured system data. Input Source 2.10
and PoV baseline. Processing / Rules Calculate from versioned data and
record calculation context.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 46 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Outputs Numerical
metric results. Output Destination PoV report and dashboard.
Prerequisites 2.10. Dependencies Topic 3 and performance/risk
requirements. Dependency Type Hard dependency for any action that must
preserve the approved goal; analytical checks may be parallel where they
only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details Calculations shall be deterministic and
versioned. Tools / Resources Metrics pipeline and reproducible analysis
environment. Constraints The approved goal is immutable during normal
operation; initial India/INR scope and safety constraints remain binding
unless formally changed. Prohibited Actions Silent goal changes,
unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.10.2 Qualitative Success Metrics Purpose Define non-numerical
qualities required for goal success. Objective Ensure explainability,
transparency, controlled autonomy, and predictable failure behaviour are
evaluated.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 47 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Requirement
Qualitative evaluation shall cover explainability, consistency,
transparency, auditability, controlled autonomy, and predictable failure
behaviour. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs System evidence and review records. Input Source Testing,
observability, and governance systems. Processing / Rules Use explicit
review criteria and evidence rather than unsupported subjective claims.
Outputs Qualitative assessment result. Output Destination Review report
and acceptance gate. Prerequisites 2.10. Dependencies Topics 21--26 and
33--35. Dependency Type Hard dependency for any action that must
preserve the approved goal; analytical checks may be parallel where they
only read the same immutable baseline. Parallelization Eligibility
Independent evidence collection, alignment checks, metric calculations,
and review preparation may run in parallel when they do not create
competing authoritative writes. Parallelization Restrictions No parallel
agent may create a competing authoritative goal baseline, alter
immutable goal elements, or approve its own goal change. Responsible
Owner SRS Governance Owner / SRS Writer Agent for specification;
authorized human governance for controlled approval or goal
modification. Technical Details Use a rubric with explicit pass/fail or
graded criteria and evidence references. Tools / Resources Review
checklist and audit records. Constraints The approved goal is immutable
during normal operation; initial India/INR scope and safety constraints
remain binding unless formally changed. Prohibited Actions Silent goal
changes, unapproved scope expansion, safety bypass, fabricated evidence,
guaranteed-profit claims, and self-approval are prohibited. Expected
Behaviour The system shall continuously use the approved goal as the
highest-level reference for downstream requirements and actions. Error
Handling Ambiguity, conflict, missing approval, stale baseline, or
unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 48 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.11 Goal Alignment Requirements Purpose Ensure every material
downstream requirement can be related to the approved goal. Objective
Prevent feature creep and disconnected implementation work. Requirement
Every material requirement, agent task, code capability, and release
criterion shall map directly or indirectly to an approved goal/objective
element, or be explicitly classified as required
infrastructure/governance support. Scope This item applies to the
authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Requirement, task, code,
test, and release records. Input Source Traceability system. Processing
/ Rules Create and validate goal-to-requirement mappings; reject
unexplained material functionality. Outputs Alignment mapping and
coverage result. Output Destination Traceability matrix. Prerequisites
2.9 and 2.10. Dependencies Topic 28 later defines detailed traceability.
Dependency Type Hard dependency for any action that must preserve the
approved goal; analytical checks may be parallel where they only read
the same immutable baseline. Parallelization Eligibility Independent
evidence collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Use stable requirement IDs and relationship types. Tools /
Resources Requirements registry and traceability validator. Constraints
The approved goal is immutable during normal operation; initial
India/INR scope and safety constraints remain binding unless formally
changed. Prohibited Actions Silent goal changes, unapproved scope
expansion, safety bypass, fabricated evidence, guaranteed-profit claims,
and self-approval are prohibited. Expected Behaviour The system shall
continuously use the approved goal as the highest-level reference for
downstream requirements and actions. Error Handling Ambiguity, conflict,
missing approval, stale baseline, or unauthorized modification shall be
rejected or moved to blocked/escalated state, with evidence preserved.
Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 49 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Acceptance Criteria
The item is accepted only when it is unambiguous, testable, traceable,
consistent with higher-level rules, and protected against unauthorized
alteration. Failure / Rejection Criteria Failure occurs if the item is
ambiguous, contradictory, untestable, unsupported by evidence,
unauthorized, or capable of allowing silent goal drift. Recovery /
Corrective Action Restore the last approved baseline, preserve evidence,
identify root cause, correct through Topic 1 change control, and rerun
validation. Audit / Traceability Material goal decisions, changes,
conflicts, deviations, reviews, and approvals shall identify version,
actor, timestamp, affected item, decision, reason, and evidence. Change
Control Material changes require change request, impact assessment,
authorized approval, validation, new version, and controlled baseline
update under Topic 1. 2.12 Goal Conflict Resolution Purpose Define how
incompatible instructions or requirements are handled. Objective Prevent
lower-level optimization from overriding the goal or safety. Requirement
Conflicts shall be detected, classified, prioritized, resolved by
approved rules, and recorded. Scope This item applies to the
authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Conflicting requirements,
instructions, constraints, or proposed changes. Input Source SRS, goal
baseline, principles, task/dependency records. Processing / Rules Detect
→ classify → apply priority → resolve when deterministic → otherwise
block and escalate. Outputs Conflict record and resolution decision.
Output Destination Audit trail, blocked task, governance record.
Prerequisites 2.11 and Topic 5. Dependencies 2.12.1 and 2.12.2.
Dependency Type Hard dependency for any action that must preserve the
approved goal; analytical checks may be parallel where they only read
the same immutable baseline. Parallelization Eligibility Independent
evidence collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Conflict rules shall use explicit identifiers and precedence.
Tools / Resources Policy engine and validation tests. Constraints The
approved goal is immutable during normal operation; initial India/INR
scope and safety constraints remain binding unless formally changed.
Prohibited Actions Silent goal changes, unapproved scope expansion,
safety bypass, fabricated evidence, guaranteed-profit claims, and
self-approval are prohibited. Expected Behaviour The system shall
continuously use the approved goal as the highest-level reference for
downstream requirements and actions. Error Handling Ambiguity, conflict,
missing approval, stale baseline, or unauthorized modification shall be
rejected or moved to blocked/escalated state, with evidence preserved.
Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 50 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Validation Method
Requirement inspection, goal-to-requirement traceability checks, policy
checks, conflict tests, deviation tests, and approval/baseline
verification. Testing Requirements Positive alignment, negative
violation, conflicting-instruction, unauthorized-change, stale-version,
regression, and recovery tests shall be performed as applicable.
Evidence Required Goal/mission records, baseline/version IDs,
traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.12.1 Conflict Detection Purpose Detect incompatible
instructions or states before unauthorized results occur. Objective
Identify direct and indirect goal conflicts. Requirement The system
shall detect conflicts involving goal, scope, safety, authority,
dependencies, requirements, tasks, and proposed changes. Scope This item
applies to the authoritative project goal/mission definition and to
downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs Current
instructions, requirements, policies, and state. Input Source SRS
registry, task queue, agent messages, governance records. Processing /
Rules Compare constraints and obligations; classify severity and
affected authority level. Outputs Conflict event with evidence and
severity. Output Destination Conflict registry and dashboard.
Prerequisites 2.12. Dependencies Topic 5 and Topic 8. Dependency Type
Hard dependency for any action that must preserve the approved goal;
analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Use stable identifiers and central policy precedence. Tools /
Resources Policy checker and dependency graph. Constraints The approved
goal is immutable during normal operation; initial India/INR scope and
safety constraints remain binding unless formally changed. Prohibited
Actions Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 51 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Error Handling
Ambiguity, conflict, missing approval, stale baseline, or unauthorized
modification shall be rejected or moved to blocked/escalated state, with
evidence preserved. Blocked-State Conditions Blocked when the applicable
approved goal/version cannot be established, material goal elements
conflict, or required approval/evidence is missing. Unblocking
Conditions Resume only after the correct baseline, evidence,
clarification, or governance decision is available and affected
validation passes. Human Escalation Human governance is required for
immutable-goal changes, unresolved material conflicts, scope/mission
changes, and final goal-baseline approval. Validation Method Requirement
inspection, goal-to-requirement traceability checks, policy checks,
conflict tests, deviation tests, and approval/baseline verification.
Testing Requirements Positive alignment, negative violation,
conflicting-instruction, unauthorized-change, stale-version, regression,
and recovery tests shall be performed as applicable. Evidence Required
Goal/mission records, baseline/version IDs, traceability mappings,
validation results, test results, approval records, and audit events.
Acceptance Criteria The item is accepted only when it is unambiguous,
testable, traceable, consistent with higher-level rules, and protected
against unauthorized alteration. Failure / Rejection Criteria Failure
occurs if the item is ambiguous, contradictory, untestable, unsupported
by evidence, unauthorized, or capable of allowing silent goal drift.
Recovery / Corrective Action Restore the last approved baseline,
preserve evidence, identify root cause, correct through Topic 1 change
control, and rerun validation. Audit / Traceability Material goal
decisions, changes, conflicts, deviations, reviews, and approvals shall
identify version, actor, timestamp, affected item, decision, reason, and
evidence. Change Control Material changes require change request, impact
assessment, authorized approval, validation, new version, and controlled
baseline update under Topic 1. 2.12.2 Conflict Resolution Priority
Purpose Define precedence for resolving conflicts. Objective Ensure all
agents apply one consistent priority model. Requirement Priority shall
be safety/non-negotiable rules → approved core goal → approved SRS
requirements → validated dependencies → task instructions → optimization
preferences; same-level unresolved conflicts shall block and escalate.
Scope This item applies to the authoritative project goal/mission
definition and to downstream requirements, tasks, agents, decisions,
outputs, and governance actions that must remain aligned with it. It
does not replace the detailed system-scope definition in Topic 4. Inputs
Conflict record and applicable requirements. Input Source Goal, SRS,
principles, and dependency baselines. Processing / Rules Apply the fixed
precedence; never invent a same-level resolution. Outputs Resolution or
blocked-state decision. Output Destination Task state, audit trail,
governance workflow. Prerequisites 2.12.1. Dependencies Topic 5.
Dependency Type Hard dependency for any action that must preserve the
approved goal; analytical checks may be parallel where they only read
the same immutable baseline. Parallelization Eligibility Independent
evidence collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 52 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Technical Details
Encode precedence centrally to prevent agent-specific interpretation.
Tools / Resources Policy engine and conflict test suite. Constraints The
approved goal is immutable during normal operation; initial India/INR
scope and safety constraints remain binding unless formally changed.
Prohibited Actions Silent goal changes, unapproved scope expansion,
safety bypass, fabricated evidence, guaranteed-profit claims, and
self-approval are prohibited. Expected Behaviour The system shall
continuously use the approved goal as the highest-level reference for
downstream requirements and actions. Error Handling Ambiguity, conflict,
missing approval, stale baseline, or unauthorized modification shall be
rejected or moved to blocked/escalated state, with evidence preserved.
Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.13 Goal Deviation Detection Purpose Detect when work or
runtime behaviour moves away from the approved goal. Objective Provide
continuous protection against gradual goal drift. Requirement The system
shall monitor requirements, tasks, outputs, agent actions, and material
configuration changes for deviation from the approved goal and create a
deviation record when detected. Scope This item applies to the
authoritative project goal/mission definition and to downstream
requirements, tasks, agents, decisions, outputs, and governance actions
that must remain aligned with it. It does not replace the detailed
system-scope definition in Topic 4. Inputs Task state, outputs, changes,
current goal baseline. Input Source Master/Background Checker, audit
trail, traceability system. Processing / Rules Compare observed state
with approved goal and alignment mappings; classify severity and trigger
recovery/escalation. Outputs Deviation event, severity, evidence,
affected task, and recommended action. Output Destination Dashboard,
audit trail, escalation workflow. Prerequisites 2.11 and 2.12.
Dependencies Topic 25 Self-Evaluation.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 53 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Dependency Type
Hard dependency for any action that must preserve the approved goal;
analytical checks may be parallel where they only read the same
immutable baseline. Parallelization Eligibility Independent evidence
collection, alignment checks, metric calculations, and review
preparation may run in parallel when they do not create competing
authoritative writes. Parallelization Restrictions No parallel agent may
create a competing authoritative goal baseline, alter immutable goal
elements, or approve its own goal change. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification; authorized human
governance for controlled approval or goal modification. Technical
Details Run checks at workflow gates and periodically for long-running
tasks. Tools / Resources Monitoring agent, policy engine, dashboard.
Constraints The approved goal is immutable during normal operation;
initial India/INR scope and safety constraints remain binding unless
formally changed. Prohibited Actions Silent goal changes, unapproved
scope expansion, safety bypass, fabricated evidence, guaranteed-profit
claims, and self-approval are prohibited. Expected Behaviour The system
shall continuously use the approved goal as the highest-level reference
for downstream requirements and actions. Error Handling Ambiguity,
conflict, missing approval, stale baseline, or unauthorized modification
shall be rejected or moved to blocked/escalated state, with evidence
preserved. Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.14 Goal Validation and Review Purpose Ensure the goal remains
valid and aligned with the controlled project baseline. Objective Define
when and how the goal must be reviewed. Requirement Goal validation
shall occur at initial baseline, major SRS changes, material
architecture/scope changes, PoV completion, major failures, and
pre-release gates. Scope This item applies to the authoritative project
goal/mission definition and to downstream requirements, tasks, agents,
decisions, outputs, and governance actions that must remain aligned with
it. It does not replace the detailed system-scope definition in Topic 4.
Inputs Goal baseline, review trigger, and supporting evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 54 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Input Source
Governance lifecycle and release process. Processing / Rules Run
consistency, scope, safety, and traceability checks and record the
review outcome. Outputs Accepted / Change Required / Re-baseline
Required / Escalated review result. Output Destination Governance record
and SRS history. Prerequisites 2.8--2.13 and Topic 1. Dependencies
Topics 25, 27, and 34. Dependency Type Hard dependency for any action
that must preserve the approved goal; analytical checks may be parallel
where they only read the same immutable baseline. Parallelization
Eligibility Independent evidence collection, alignment checks, metric
calculations, and review preparation may run in parallel when they do
not create competing authoritative writes. Parallelization Restrictions
No parallel agent may create a competing authoritative goal baseline,
alter immutable goal elements, or approve its own goal change.
Responsible Owner SRS Governance Owner / SRS Writer Agent for
specification; authorized human governance for controlled approval or
goal modification. Technical Details Review must be reproducible from
the exact baseline/version under review. Tools / Resources Validation
pipeline and review checklist. Constraints The approved goal is
immutable during normal operation; initial India/INR scope and safety
constraints remain binding unless formally changed. Prohibited Actions
Silent goal changes, unapproved scope expansion, safety bypass,
fabricated evidence, guaranteed-profit claims, and self-approval are
prohibited. Expected Behaviour The system shall continuously use the
approved goal as the highest-level reference for downstream requirements
and actions. Error Handling Ambiguity, conflict, missing approval, stale
baseline, or unauthorized modification shall be rejected or moved to
blocked/escalated state, with evidence preserved. Blocked-State
Conditions Blocked when the applicable approved goal/version cannot be
established, material goal elements conflict, or required
approval/evidence is missing. Unblocking Conditions Resume only after
the correct baseline, evidence, clarification, or governance decision is
available and affected validation passes. Human Escalation Human
governance is required for immutable-goal changes, unresolved material
conflicts, scope/mission changes, and final goal-baseline approval.
Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.
Audit / Traceability Material goal decisions, changes, conflicts,
deviations, reviews, and approvals shall identify version, actor,
timestamp, affected item, decision, reason, and evidence. Change Control
Material changes require change request, impact assessment, authorized
approval, validation, new version, and controlled baseline update under
Topic 1. 2.15 Goal Baseline and Approval Purpose Formally establish the
approved goal as the authoritative project reference.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 55 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Objective Prevent
implementation from starting against an unapproved interpretation.
Requirement The goal shall be versioned, validated, approved by
authorized governance, and associated with a baseline identifier before
downstream requirements are treated as authoritative. Scope This item
applies to the authoritative project goal/mission definition and to
downstream requirements, tasks, agents, decisions, outputs, and
governance actions that must remain aligned with it. It does not replace
the detailed system-scope definition in Topic 4. Inputs Validated goal,
mission, objectives, and approval evidence. Input Source Topic 1
governance workflow. Processing / Rules Validate completeness and
consistency → obtain approval → create baseline → lock baseline. Outputs
Approved goal baseline with ID, version, integrity record, approval
evidence, and timestamp. Output Destination SRS repository, baseline
registry, and traceability matrix. Prerequisites Topic 1.6 and 1.11.
Dependencies Topic 1.6, 1.8, 1.11. Dependency Type Hard dependency for
any action that must preserve the approved goal; analytical checks may
be parallel where they only read the same immutable baseline.
Parallelization Eligibility Independent evidence collection, alignment
checks, metric calculations, and review preparation may run in parallel
when they do not create competing authoritative writes. Parallelization
Restrictions No parallel agent may create a competing authoritative goal
baseline, alter immutable goal elements, or approve its own goal change.
Responsible Owner SRS Governance Owner / SRS Writer Agent for
specification; authorized human governance for controlled approval or
goal modification. Technical Details Goal baseline shall link to the
exact SRS version defining it and retain the previous baseline for
recovery. Tools / Resources VCS, baseline registry, approval workflow.
Constraints The approved goal is immutable during normal operation;
initial India/INR scope and safety constraints remain binding unless
formally changed. Prohibited Actions Silent goal changes, unapproved
scope expansion, safety bypass, fabricated evidence, guaranteed-profit
claims, and self-approval are prohibited. Expected Behaviour The system
shall continuously use the approved goal as the highest-level reference
for downstream requirements and actions. Error Handling Ambiguity,
conflict, missing approval, stale baseline, or unauthorized modification
shall be rejected or moved to blocked/escalated state, with evidence
preserved. Blocked-State Conditions Blocked when the applicable approved
goal/version cannot be established, material goal elements conflict, or
required approval/evidence is missing. Unblocking Conditions Resume only
after the correct baseline, evidence, clarification, or governance
decision is available and affected validation passes. Human Escalation
Human governance is required for immutable-goal changes, unresolved
material conflicts, scope/mission changes, and final goal-baseline
approval. Validation Method Requirement inspection, goal-to-requirement
traceability checks, policy checks, conflict tests, deviation tests, and
approval/baseline verification. Testing Requirements Positive alignment,
negative violation, conflicting-instruction, unauthorized-change,
stale-version, regression, and recovery tests shall be performed as
applicable. Evidence Required Goal/mission records, baseline/version
IDs, traceability mappings, validation results, test results, approval
records, and audit events. Acceptance Criteria The item is accepted only
when it is unambiguous, testable, traceable, consistent with
higher-level rules, and protected against unauthorized alteration.
Failure / Rejection Criteria Failure occurs if the item is ambiguous,
contradictory, untestable, unsupported by evidence, unauthorized, or
capable of allowing silent goal drift. Recovery / Corrective Action
Restore the last approved baseline, preserve evidence, identify root
cause, correct through Topic 1 change control, and rerun validation.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 56 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline Audit /
Traceability Material goal decisions, changes, conflicts, deviations,
reviews, and approvals shall identify version, actor, timestamp,
affected item, decision, reason, and evidence. Change Control Material
changes require change request, impact assessment, authorized approval,
validation, new version, and controlled baseline update under Topic 1.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 57 -->
```
AI Investment Opportunity Agent --- Topic 2 Baseline 2.16 Topic 2 Final
Validation Checklist Topic 2 is considered baseline-ready only if every
check below passes. Check Acceptance condition Status Hierarchy coverage
2.1--2.15 and all frozen child items are individually specified. PASS
Purpose & Objective Every numbered item has both. PASS Requirement
quality Every item has an explicit, bounded, testable requirement. PASS
Input / Output Inputs, sources, outputs, and destinations are defined.
PASS Prerequisites / Dependencies Dependencies and prerequisites are
explicit. PASS Parallelization Eligibility and restrictions are
explicit. PASS Technical / Resources Applicable mechanisms and resources
are defined. PASS Constraints / Prohibitions Goal protections are
explicit. PASS Expected behaviour Normal behaviour is specified. PASS
Error / Blocked / Recovery Failure, blocked, unblocking, escalation, and
recovery are specified. PASS Validation / Testing Validation and testing
are defined. PASS Evidence / Acceptance Evidence and acceptance gates
are defined. PASS Audit / Traceability Goal decisions and changes are
traceable. PASS Immutability Protected elements and controlled
exceptions are defined. PASS Conflict handling Detection and
deterministic priority are defined. PASS Deviation detection Goal drift
detection and escalation are defined. PASS Baseline / Approval Baseline
creation, approval, and protection are defined. PASS Topic boundary
Topic 2 does not silently redefine Topic 1 or Topic 4. PASS Baseline
Decision: TOPIC 2 BASELINE-READY --- T2-BL-001. Formal governance
approval remains the final human gate. Once approved, this file is the
standalone Topic 2 reference and Topic 3 shall treat it as a completed
hard dependency.
