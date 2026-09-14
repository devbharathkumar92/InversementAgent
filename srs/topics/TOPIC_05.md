# Topic 5 --- System Principles and Non-Negotiable Rules

> Authoritative source slice from the uploaded Full Master SRS. Source
> PDF pages 139--202. Preserve numbering and requirement wording.

## Source Requirements

```{=html}
<!-- Source PDF page 139 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline AI Investment
Opportunity Agent --- SRS Topic 5 --- System Principles and
Non-Negotiable Rules BASELINE-READY TOPIC DOCUMENT --- Phase 1 /
Foundation Status: BASELINE-READY Topic: 5 Baseline: T5-BL-001 1.0
Reference and Validation Basis This standalone Topic 5 document
preserves the frozen Phase 1 hierarchy for "System Principles and
Non-Negotiable Rules" and presents every numbered item using the same
two-column specification-table format used by the Topic 1 and Topic 2
baseline documents. Topic 3 and Topic 4 are also treated as preceding
controlled inputs. No numbered item or specification field is silently
omitted. 1.0A Mandatory Specification Contract for Every Item Every
numbered item contains the full controlled contract: Purpose, Objective,
Requirement, Scope, Inputs, Input Source, Processing / Method / Rules,
Outputs, Output Destination, Responsible Agent / Component,
Prerequisites, Dependency, Dependency Type, Parallelization Eligibility,
Parallelization Restrictions, Technical Details, Tools / Resources,
Constraints, Prohibited Actions, Expected Behaviour, Error Handling,
Blocked-State Conditions, Unblocking Conditions, Human Escalation,
Validation Method, Testing Requirements, Evidence Required, Acceptance
Criteria, Failure / Rejection Criteria, Recovery / Corrective Action,
Audit / Traceability, Change Control, Rationale / Assumptions, and
Verification Method. If a field is genuinely not applicable to a
specific item, the controlled version shall explicitly state "Not
Applicable --- \[reason\]"; silent omission is not permitted. 5.1 Core
System Principles Purpose Define and control core system principles as
an enforceable part of the system's governing principle and rule
framework. Objective Make core system principles explicit, testable,
traceable, enforceable, and usable by SRS, development, runtime, QA,
monitoring, and governance components. Requirement The system shall
define and apply a coherent set of core principles governing
requirements, agents, data, decisions, safety, security, execution, and
governance. Scope Applies to core system principles and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret core system principles as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for core system principles, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 140 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Constraints Initial
system boundaries, India/INR PoV limits, safety controls, human approval
gates, frozen numbering, least privilege, auditability, evidence
retention, and approved infrastructure/API limits remain binding unless
changed through governance. Prohibited Actions Silent weakening or
alteration of core system principles, fabricated evidence, hidden
assumptions, unauthorized writes, bypassing safety/security/approval
controls, false approval claims, and untracked changes are prohibited.
Expected Behaviour The responsible component shall apply core system
principles consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for core system principles are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that core system principles is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
core system principles is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if core system principles is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.1 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires core system
principles to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.2 Non-Negotiable Rules Purpose Define and control
non-negotiable rules as an enforceable part of the system's governing
principle and rule framework. Objective Make non-negotiable rules
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall enforce the defined non-negotiable rules as
mandatory controls that no runtime or development agent may bypass.
Scope Applies to non-negotiable rules and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret non-negotiable rules as an explicit controlled
rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for non-negotiable rules, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 141 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Responsible Agent /
Component SRS Governance Owner / SRS Writer Agent for specification;
applicable Policy/Enforcement, Agent Runtime, QA, Security,
Observability, or Change-Control component for implementation and
validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
non-negotiable rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply non-negotiable rules
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for non-negotiable rules are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that non-negotiable rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
non-negotiable rules is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if non-negotiable rules is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.2 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires non-negotiable
rules to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.3 Goal Immutability Principle Purpose Define and control
goal immutability principle as an enforceable part of the system's
governing principle and rule framework.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 142 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Objective Make goal
immutability principle explicit, testable, traceable, enforceable, and
usable by SRS, development, runtime, QA, monitoring, and governance
components. Requirement The system shall treat approved goal elements as
immutable during normal operation and shall require controlled
governance for any permitted modification. Scope Applies to goal
immutability principle and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
goal immutability principle as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for goal immutability
principle, including applicable rule state, validation state, ownership,
evidence references, and any exception or escalation record. Output
Destination Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of goal
immutability principle, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply goal immutability
principle consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for goal immutability principle
are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that goal immutability principle is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
goal immutability principle is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if goal immutability principle is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 143 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Recovery /
Corrective Action Preserve evidence; stop or contain unsafe processing;
restore the last known valid state where applicable; identify root
cause; correct through controlled change; rerun validation and
regression tests; and re-accept only after the gate passes. Audit /
Traceability All material events involving 5.3 shall record the
requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires goal immutability principle to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.3.1 Immutable Goal Elements Purpose Define and control
immutable goal elements as an enforceable part of the system's governing
principle and rule framework. Objective Make immutable goal elements
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall identify and version the specific goal
elements that are immutable and shall make those elements
machine-checkable. Scope Applies to immutable goal elements and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret immutable goal elements as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for immutable goal elements, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of immutable goal elements, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply immutable goal elements consistently, expose relevant state
and evidence, reject or block invalid conditions, preserve traceability,
and escalate material unresolved issues rather than guessing. Error
Handling Invalid, missing, stale, contradictory, unauthorized, or
unverifiable inputs shall be rejected or classified; the event, affected
item, version, actor, and evidence shall be logged; retry is permitted
only where safe and explicitly allowed.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 144 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
immutable goal elements are missing, contradictory, stale, or unsafe to
use. Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that immutable goal elements is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
immutable goal elements is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if immutable goal elements is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.3.1 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires immutable goal
elements to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.3.2 Goal Change Prohibition Purpose Define and control goal
change prohibition as an enforceable part of the system's governing
principle and rule framework. Objective Make goal change prohibition
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall prohibit any agent or component from
changing an immutable goal element without the controlled exception
process and authorized approval. Scope Applies to goal change
prohibition and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
goal change prohibition as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for goal change prohibition,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 145 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Parallelization
Eligibility Drafting, evidence collection, test design, control-schema
preparation, and independent validation may run in parallel after
governing inputs are frozen and provided that no competing authoritative
write is created. Parallelization Restrictions Parallel workers shall
not redefine the goal, expand scope, weaken safety or security controls,
grant authority, bypass approval gates, alter a locked baseline, or
overwrite another authoritative result. Technical Details Use stable
requirement IDs, versioned machine-readable policy/configuration,
explicit state models, immutable audit records, schema validation,
deterministic evaluation where required, access controls, and automated
traceability from requirement to test/evidence. Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of goal
change prohibition, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply goal change prohibition
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for goal change prohibition are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that goal change prohibition is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
goal change prohibition is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if goal change prohibition is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.3.2 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires goal change
prohibition to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.4 Specification Completeness Principle Purpose Define and
control specification completeness principle as an enforceable part of
the system's governing principle and rule framework. Objective Make
specification completeness principle explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The SRS shall contain complete,
explicit, testable, traceable, and implementation-ready specifications
for all required system behaviour within the approved scope. Scope
Applies to specification completeness principle and every requirement,
agent, component, workflow, configuration, decision, action, and
governance record that is governed by or can materially affect this
item. Inputs Approved higher-level requirements, the frozen Phase 1
hierarchy, relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 146 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Input Source
Controlled SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
specification completeness principle as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for specification
completeness principle, including applicable rule state, validation
state, ownership, evidence references, and any exception or escalation
record. Output Destination Controlled SRS/repository, requirements
registry, policy and configuration store, agent registry, enforcement
layer, QA evidence store, dashboard/observability, and audit trail as
applicable. Responsible Agent / Component SRS Governance Owner / SRS
Writer Agent for specification; applicable Policy/Enforcement, Agent
Runtime, QA, Security, Observability, or Change-Control component for
implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of specification completeness principle,
fabricated evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply specification completeness principle consistently, expose
relevant state and evidence, reject or block invalid conditions,
preserve traceability, and escalate material unresolved issues rather
than guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
specification completeness principle are missing, contradictory, stale,
or unsafe to use. Unblocking Conditions Resume only after the blocker is
resolved by supplying or correcting the required
input/evidence/approval/control, re-running affected validation, and
recording the resulting state. Human Escalation Human governance is
required for material principle changes, approval-controlled actions,
safety/security/scope exceptions, unresolved conflicts, baseline
acceptance, and any case where the defined authority cannot safely
resolve the issue. Validation Method Inspect the requirement, its
traceability, policy/control mapping, version state, authorization
behaviour, evidence, and implementation outcome; verify that
specification completeness principle is explicit, testable, enforceable,
and aligned with higher-level baselines. Testing Requirements Positive,
negative, boundary, conflict, unauthorized-action, stale-version,
regression, failure/recovery, audit-trail, and concurrency tests shall
be performed as applicable to the item. Evidence Required Approved
requirement record, versions, configurations, test cases/results, logs,
policy decisions, approvals, defects, recovery records, traceability
links, and relevant screenshots or reports shall be retained. Acceptance
Criteria Accepted only when specification completeness principle is
explicit, complete, unambiguous, traceable, testable, enforceable,
consistent with higher-level baselines, and supported by reproducible
evidence. Failure / Rejection Criteria Rejected if specification
completeness principle is ambiguous, incomplete, contradictory,
untestable, unenforceable, unsupported by evidence, capable of
unauthorized bypass, or inconsistent with a locked/higher-level
baseline. Recovery / Corrective Action Preserve evidence; stop or
contain unsafe processing; restore the last known valid state where
applicable; identify root cause; correct through controlled change;
rerun validation and regression tests; and re-accept only after the gate
passes. Audit / Traceability All material events involving 5.4 shall
record the requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 147 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Rationale /
Assumptions The project requires specification completeness principle to
be explicit because multiple autonomous and semi-autonomous components
will otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.5 Agent Determinism Principle Purpose Define and control
agent determinism principle as an enforceable part of the system's
governing principle and rule framework. Objective Make agent determinism
principle explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement Each agent shall produce deterministic behaviour for the
same approved inputs, configuration, policy version, and execution
state, subject only to explicitly declared nondeterministic
dependencies. Scope Applies to agent determinism principle and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret agent determinism principle as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for agent determinism principle, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of agent determinism principle,
fabricated evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply agent determinism principle consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for agent
determinism principle are missing, contradictory, stale, or unsafe to
use. Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 148 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that agent determinism principle is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
agent determinism principle is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if agent determinism principle is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.5 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires agent determinism
principle to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.6 No-Assumption Principle Purpose Define and control
no-assumption principle as an enforceable part of the system's governing
principle and rule framework. Objective Make no-assumption principle
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement Agents shall not fill missing, ambiguous, or conflicting
requirements by assumption; unresolved information shall be represented
explicitly and routed through the defined resolution path. Scope Applies
to no-assumption principle and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
no-assumption principle as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for no-assumption principle,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 149 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
no-assumption principle, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply no-assumption principle
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for no-assumption principle are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that no-assumption principle is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
no-assumption principle is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if no-assumption principle is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.6 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires no-assumption
principle to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.7 No Unauthorized Change Principle Purpose Define and
control no unauthorized change principle as an enforceable part of the
system's governing principle and rule framework. Objective Make no
unauthorized change principle explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall prevent
unauthorized modification of requirements, configurations, policies,
code, data contracts, decisions, baselines, and runtime controls. Scope
Applies to no unauthorized change principle and every requirement,
agent, component, workflow, configuration, decision, action, and
governance record that is governed by or can materially affect this
item. Inputs Approved higher-level requirements, the frozen Phase 1
hierarchy, relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret no unauthorized change principle as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for no unauthorized change principle, including applicable rule
state, validation state, ownership, evidence references, and any
exception or escalation record.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 150 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of no
unauthorized change principle, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply no unauthorized change
principle consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for no unauthorized change
principle are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that no unauthorized change principle is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when no
unauthorized change principle is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if no unauthorized change principle is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.7 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires no unauthorized
change principle to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 151 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline 5.8 Human Approval
Requirement Purpose Define and control human approval requirement as an
enforceable part of the system's governing principle and rule framework.
Objective Make human approval requirement explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall require human
approval for all actions classified as approval-controlled and shall
block execution until the required approval is valid and traceable.
Scope Applies to human approval requirement and every requirement,
agent, component, workflow, configuration, decision, action, and
governance record that is governed by or can materially affect this
item. Inputs Approved higher-level requirements, the frozen Phase 1
hierarchy, relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret human approval requirement as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for human approval requirement, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of human approval requirement, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply human approval requirement consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for human
approval requirement are missing, contradictory, stale, or unsafe to
use. Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that human approval requirement is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 152 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Evidence Required
Approved requirement record, versions, configurations, test
cases/results, logs, policy decisions, approvals, defects, recovery
records, traceability links, and relevant screenshots or reports shall
be retained. Acceptance Criteria Accepted only when human approval
requirement is explicit, complete, unambiguous, traceable, testable,
enforceable, consistent with higher-level baselines, and supported by
reproducible evidence. Failure / Rejection Criteria Rejected if human
approval requirement is ambiguous, incomplete, contradictory,
untestable, unenforceable, unsupported by evidence, capable of
unauthorized bypass, or inconsistent with a locked/higher-level
baseline. Recovery / Corrective Action Preserve evidence; stop or
contain unsafe processing; restore the last known valid state where
applicable; identify root cause; correct through controlled change;
rerun validation and regression tests; and re-accept only after the gate
passes. Audit / Traceability All material events involving 5.8 shall
record the requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires human approval requirement to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.8.1 Approval-Required Actions Purpose Define and control
approval-required actions as an enforceable part of the system's
governing principle and rule framework. Objective Make approval-required
actions explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall maintain an explicit, versioned list of
actions that require human approval before execution or adoption. Scope
Applies to approval-required actions and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret approval-required actions as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for approval-required actions, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 153 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Prohibited Actions
Silent weakening or alteration of approval-required actions, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply approval-required actions consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
approval-required actions are missing, contradictory, stale, or unsafe
to use. Unblocking Conditions Resume only after the blocker is resolved
by supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that approval-required actions is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
approval-required actions is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if approval-required actions is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.8.1 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires approval-required
actions to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.8.2 Non-Approval Actions Purpose Define and control
non-approval actions as an enforceable part of the system's governing
principle and rule framework. Objective Make non-approval actions
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall explicitly classify actions that may
proceed without human approval and shall prevent that classification
from being used to bypass an approval-controlled action. Scope Applies
to non-approval actions and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
non-approval actions as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for non-approval actions, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 154 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Prerequisites
Topics 1--4 shall be completed and baseline-ready/approved as required
by governance; directly preceding parent/child items shall also be
satisfied where the hierarchy creates a logical dependency. Dependency
Depends on the immutable project goal and mission, approved PoV, defined
system scope and boundaries, and the relevant preceding principles or
child controls within Topic 5. Dependency Type Blocking for any
dependency that affects safety, authority, scope, approval, security,
baseline integrity, or validity; read-only/downstream for analytical or
documentation dependencies that do not alter the governing rule.
Parallelization Eligibility Drafting, evidence collection, test design,
control-schema preparation, and independent validation may run in
parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
non-approval actions, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply non-approval actions
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for non-approval actions are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that non-approval actions is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
non-approval actions is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if non-approval actions is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.8.2 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires non-approval
actions to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.9 Scope Compliance Principle Purpose Define and control
scope compliance principle as an enforceable part of the system's
governing principle and rule framework. Objective Make scope compliance
principle explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 155 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Requirement Every
system and agent action shall comply with the approved scope, including
market, currency, capability, authority, data, execution, and
operational boundaries. Scope Applies to scope compliance principle and
every requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret scope compliance principle as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for scope compliance principle, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of scope compliance principle, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply scope compliance principle consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for scope
compliance principle are missing, contradictory, stale, or unsafe to
use. Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that scope compliance principle is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
scope compliance principle is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if scope compliance principle is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 156 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Recovery /
Corrective Action Preserve evidence; stop or contain unsafe processing;
restore the last known valid state where applicable; identify root
cause; correct through controlled change; rerun validation and
regression tests; and re-accept only after the gate passes. Audit /
Traceability All material events involving 5.9 shall record the
requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires scope compliance principle to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.10 Safety First Principle Purpose Define and control safety
first principle as an enforceable part of the system's governing
principle and rule framework. Objective Make safety first principle
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement Safety controls shall take precedence over performance,
convenience, opportunity capture, or autonomous execution when a
conflict exists. Scope Applies to safety first principle and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret safety first principle as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for safety first principle, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of safety first principle, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply safety first principle consistently, expose relevant state
and evidence, reject or block invalid conditions, preserve traceability,
and escalate material unresolved issues rather than guessing. Error
Handling Invalid, missing, stale, contradictory, unauthorized, or
unverifiable inputs shall be rejected or classified; the event, affected
item, version, actor, and evidence shall be logged; retry is permitted
only where safe and explicitly allowed. Blocked-State Conditions Blocked
when required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for safety first
principle are missing, contradictory, stale, or unsafe to use.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 157 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that safety first principle is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
safety first principle is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if safety first principle is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.10 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires safety first
principle to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.11 Risk Control Principles Purpose Define and control risk
control principles as an enforceable part of the system's governing
principle and rule framework. Objective Make risk control principles
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall apply defined risk controls before, during,
and after opportunity analysis, simulation, paper trading, and any
separately approved live action. Scope Applies to risk control
principles and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
risk control principles as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for risk control principles,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 158 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Parallelization
Restrictions Parallel workers shall not redefine the goal, expand scope,
weaken safety or security controls, grant authority, bypass approval
gates, alter a locked baseline, or overwrite another authoritative
result. Technical Details Use stable requirement IDs, versioned
machine-readable policy/configuration, explicit state models, immutable
audit records, schema validation, deterministic evaluation where
required, access controls, and automated traceability from requirement
to test/evidence. Tools / Resources Version-control repository,
requirements registry, policy/configuration store, schema validators,
automated test harness, CI checks, logging/observability, dashboard,
audit store, and approved development/analysis tools. Constraints
Initial system boundaries, India/INR PoV limits, safety controls, human
approval gates, frozen numbering, least privilege, auditability,
evidence retention, and approved infrastructure/API limits remain
binding unless changed through governance. Prohibited Actions Silent
weakening or alteration of risk control principles, fabricated evidence,
hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply risk control principles consistently, expose relevant state
and evidence, reject or block invalid conditions, preserve traceability,
and escalate material unresolved issues rather than guessing. Error
Handling Invalid, missing, stale, contradictory, unauthorized, or
unverifiable inputs shall be rejected or classified; the event, affected
item, version, actor, and evidence shall be logged; retry is permitted
only where safe and explicitly allowed. Blocked-State Conditions Blocked
when required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for risk control
principles are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that risk control principles is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
risk control principles is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if risk control principles is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.11 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires risk control
principles to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.12 Data Integrity Principles Purpose Define and control data
integrity principles as an enforceable part of the system's governing
principle and rule framework. Objective Make data integrity principles
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall preserve data accuracy, completeness,
provenance, freshness, consistency, and integrity throughout
acquisition, transformation, storage, analysis, and use. Scope Applies
to data integrity principles and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 159 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Processing / Method
/ Rules Interpret data integrity principles as an explicit controlled
rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for data integrity principles, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of data integrity principles, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply data integrity principles consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for data
integrity principles are missing, contradictory, stale, or unsafe to
use. Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that data integrity principles is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
data integrity principles is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if data integrity principles is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.12 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires data integrity
principles to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 160 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Verification Method
Perform document inspection, schema/structure validation, traceability
checks, controlled positive/negative tests, unauthorized-action tests
where applicable, and evidence review; confirm the result against the
approved Topic 5 baseline. 5.13 Decision Integrity Principles Purpose
Define and control decision integrity principles as an enforceable part
of the system's governing principle and rule framework. Objective Make
decision integrity principles explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall preserve the
integrity of decisions by linking decisions to valid inputs, applicable
rules, analysis, uncertainty, approvals, and evidence. Scope Applies to
decision integrity principles and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
decision integrity principles as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for decision integrity
principles, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.
Output Destination Controlled SRS/repository, requirements registry,
policy and configuration store, agent registry, enforcement layer, QA
evidence store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
decision integrity principles, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply decision integrity
principles consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for decision integrity principles
are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that decision integrity principles is explicit,
testable, enforceable, and aligned with higher-level baselines.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 161 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
decision integrity principles is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if decision integrity principles is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.13 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires decision integrity
principles to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.14 Transparency and Explainability Rules Purpose Define and
control transparency and explainability rules as an enforceable part of
the system's governing principle and rule framework. Objective Make
transparency and explainability rules explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall provide
sufficient transparency and explanation for material requirements,
opportunity assessments, decisions, risk states, failures, and
controlled changes. Scope Applies to transparency and explainability
rules and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret transparency and
explainability rules as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for transparency and explainability
rules, including applicable rule state, validation state, ownership,
evidence references, and any exception or escalation record. Output
Destination Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 162 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Constraints Initial
system boundaries, India/INR PoV limits, safety controls, human approval
gates, frozen numbering, least privilege, auditability, evidence
retention, and approved infrastructure/API limits remain binding unless
changed through governance. Prohibited Actions Silent weakening or
alteration of transparency and explainability rules, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply transparency and explainability rules consistently, expose
relevant state and evidence, reject or block invalid conditions,
preserve traceability, and escalate material unresolved issues rather
than guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
transparency and explainability rules are missing, contradictory, stale,
or unsafe to use. Unblocking Conditions Resume only after the blocker is
resolved by supplying or correcting the required
input/evidence/approval/control, re-running affected validation, and
recording the resulting state. Human Escalation Human governance is
required for material principle changes, approval-controlled actions,
safety/security/scope exceptions, unresolved conflicts, baseline
acceptance, and any case where the defined authority cannot safely
resolve the issue. Validation Method Inspect the requirement, its
traceability, policy/control mapping, version state, authorization
behaviour, evidence, and implementation outcome; verify that
transparency and explainability rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
transparency and explainability rules is explicit, complete,
unambiguous, traceable, testable, enforceable, consistent with
higher-level baselines, and supported by reproducible evidence. Failure
/ Rejection Criteria Rejected if transparency and explainability rules
is ambiguous, incomplete, contradictory, untestable, unenforceable,
unsupported by evidence, capable of unauthorized bypass, or inconsistent
with a locked/higher-level baseline. Recovery / Corrective Action
Preserve evidence; stop or contain unsafe processing; restore the last
known valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.14 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires transparency and
explainability rules to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.15 Auditability Requirements Purpose Define and control
auditability requirements as an enforceable part of the system's
governing principle and rule framework. Objective Make auditability
requirements explicit, testable, traceable, enforceable, and usable by
SRS, development, runtime, QA, monitoring, and governance components.
Requirement The system shall retain auditable records for material
requirements, actions, decisions, changes, approvals, failures,
recoveries, and baseline transitions. Scope Applies to auditability
requirements and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
auditability requirements as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for auditability requirements,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 163 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Responsible Agent /
Component SRS Governance Owner / SRS Writer Agent for specification;
applicable Policy/Enforcement, Agent Runtime, QA, Security,
Observability, or Change-Control component for implementation and
validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
auditability requirements, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply auditability
requirements consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for auditability requirements are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that auditability requirements is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
auditability requirements is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if auditability requirements is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.15 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires auditability
requirements to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.16 Traceability Requirements Purpose Define and control
traceability requirements as an enforceable part of the system's
governing principle and rule framework.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 164 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Objective Make
traceability requirements explicit, testable, traceable, enforceable,
and usable by SRS, development, runtime, QA, monitoring, and governance
components. Requirement The system shall maintain bidirectional
traceability between goals, requirements, designs, agents, tasks, tests,
evidence, decisions, defects, changes, and releases. Scope Applies to
traceability requirements and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
traceability requirements as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for traceability requirements,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
traceability requirements, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply traceability
requirements consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for traceability requirements are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that traceability requirements is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
traceability requirements is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if traceability requirements is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 165 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Recovery /
Corrective Action Preserve evidence; stop or contain unsafe processing;
restore the last known valid state where applicable; identify root
cause; correct through controlled change; rerun validation and
regression tests; and re-accept only after the gate passes. Audit /
Traceability All material events involving 5.16 shall record the
requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires traceability requirements to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.17 Error Handling Principles Purpose Define and control
error handling principles as an enforceable part of the system's
governing principle and rule framework. Objective Make error handling
principles explicit, testable, traceable, enforceable, and usable by
SRS, development, runtime, QA, monitoring, and governance components.
Requirement Error handling shall classify, contain, record, recover,
retry, or escalate errors according to predefined severity and safety
rules. Scope Applies to error handling principles and every requirement,
agent, component, workflow, configuration, decision, action, and
governance record that is governed by or can materially affect this
item. Inputs Approved higher-level requirements, the frozen Phase 1
hierarchy, relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret error handling principles as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for error handling principles, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of error handling principles, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply error handling principles consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 166 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for error
handling principles are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that error handling principles is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
error handling principles is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if error handling principles is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.17 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires error handling
principles to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.18 Failure and Recovery Rules Purpose Define and control
failure and recovery rules as an enforceable part of the system's
governing principle and rule framework. Objective Make failure and
recovery rules explicit, testable, traceable, enforceable, and usable by
SRS, development, runtime, QA, monitoring, and governance components.
Requirement The system shall detect failure states, preserve evidence,
restore a valid state where safe, and prevent unsafe continuation until
recovery criteria are satisfied. Scope Applies to failure and recovery
rules and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret failure and recovery
rules as an explicit controlled rule; map applicable conditions to
enforceable controls and verification; preserve ambiguity or conflict as
an unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for failure and recovery rules, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 167 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Parallelization
Eligibility Drafting, evidence collection, test design, control-schema
preparation, and independent validation may run in parallel after
governing inputs are frozen and provided that no competing authoritative
write is created. Parallelization Restrictions Parallel workers shall
not redefine the goal, expand scope, weaken safety or security controls,
grant authority, bypass approval gates, alter a locked baseline, or
overwrite another authoritative result. Technical Details Use stable
requirement IDs, versioned machine-readable policy/configuration,
explicit state models, immutable audit records, schema validation,
deterministic evaluation where required, access controls, and automated
traceability from requirement to test/evidence. Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of failure
and recovery rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply failure and recovery
rules consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for failure and recovery rules are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that failure and recovery rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
failure and recovery rules is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if failure and recovery rules is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.18 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires failure and
recovery rules to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.19 Blocked-State and Escalation Rules Purpose Define and
control blocked-state and escalation rules as an enforceable part of the
system's governing principle and rule framework. Objective Make
blocked-state and escalation rules explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall represent
blocked states explicitly and shall escalate blockers according to
severity, ownership, timeout, safety impact, and required human
authority. Scope Applies to blocked-state and escalation rules and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 168 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Input Source
Controlled SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
blocked-state and escalation rules as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for blocked-state and
escalation rules, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.
Output Destination Controlled SRS/repository, requirements registry,
policy and configuration store, agent registry, enforcement layer, QA
evidence store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
blocked-state and escalation rules, fabricated evidence, hidden
assumptions, unauthorized writes, bypassing safety/security/approval
controls, false approval claims, and untracked changes are prohibited.
Expected Behaviour The responsible component shall apply blocked-state
and escalation rules consistently, expose relevant state and evidence,
reject or block invalid conditions, preserve traceability, and escalate
material unresolved issues rather than guessing. Error Handling Invalid,
missing, stale, contradictory, unauthorized, or unverifiable inputs
shall be rejected or classified; the event, affected item, version,
actor, and evidence shall be logged; retry is permitted only where safe
and explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for blocked-state and escalation
rules are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that blocked-state and escalation rules is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
blocked-state and escalation rules is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if blocked-state and escalation rules is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.19 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 169 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Rationale /
Assumptions The project requires blocked-state and escalation rules to
be explicit because multiple autonomous and semi-autonomous components
will otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.20 Security and Access Principles Purpose Define and control
security and access principles as an enforceable part of the system's
governing principle and rule framework. Objective Make security and
access principles explicit, testable, traceable, enforceable, and usable
by SRS, development, runtime, QA, monitoring, and governance components.
Requirement The system shall enforce least-privilege access, secure
credential handling, environment separation, authorization checks, and
protection of sensitive system resources. Scope Applies to security and
access principles and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
security and access principles as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for security and access
principles, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.
Output Destination Controlled SRS/repository, requirements registry,
policy and configuration store, agent registry, enforcement layer, QA
evidence store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
security and access principles, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply security and access
principles consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for security and access principles
are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 170 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that security and access principles is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
security and access principles is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if security and access principles is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.20 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires security and access
principles to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.21 Agent-to-Agent Communication Rules Purpose Define and
control agent-to-agent communication rules as an enforceable part of the
system's governing principle and rule framework. Objective Make
agent-to-agent communication rules explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement Agents shall communicate through
defined, versioned, validated contracts and shall preserve message
provenance, correlation, state, and authorization context. Scope Applies
to agent-to-agent communication rules and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret agent-to-agent communication rules as an
explicit controlled rule; map applicable conditions to enforceable
controls and verification; preserve ambiguity or conflict as an
unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for agent-to-agent communication rules, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 171 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
agent-to-agent communication rules, fabricated evidence, hidden
assumptions, unauthorized writes, bypassing safety/security/approval
controls, false approval claims, and untracked changes are prohibited.
Expected Behaviour The responsible component shall apply agent-to-agent
communication rules consistently, expose relevant state and evidence,
reject or block invalid conditions, preserve traceability, and escalate
material unresolved issues rather than guessing. Error Handling Invalid,
missing, stale, contradictory, unauthorized, or unverifiable inputs
shall be rejected or classified; the event, affected item, version,
actor, and evidence shall be logged; retry is permitted only where safe
and explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for agent-to-agent communication
rules are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that agent-to-agent communication rules is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
agent-to-agent communication rules is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if agent-to-agent communication rules is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.21 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires agent-to-agent
communication rules to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.22 Sub-Agent Behaviour Constraints Purpose Define and
control sub-agent behaviour constraints as an enforceable part of the
system's governing principle and rule framework. Objective Make
sub-agent behaviour constraints explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement Each sub-agent shall operate only
within its assigned task, authority, inputs, outputs, tools,
dependencies, and prohibited-action boundaries. Scope Applies to
sub-agent behaviour constraints and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
sub-agent behaviour constraints as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for sub-agent behaviour
constraints, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 172 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
sub-agent behaviour constraints, fabricated evidence, hidden
assumptions, unauthorized writes, bypassing safety/security/approval
controls, false approval claims, and untracked changes are prohibited.
Expected Behaviour The responsible component shall apply sub-agent
behaviour constraints consistently, expose relevant state and evidence,
reject or block invalid conditions, preserve traceability, and escalate
material unresolved issues rather than guessing. Error Handling Invalid,
missing, stale, contradictory, unauthorized, or unverifiable inputs
shall be rejected or classified; the event, affected item, version,
actor, and evidence shall be logged; retry is permitted only where safe
and explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for sub-agent behaviour
constraints are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that sub-agent behaviour constraints is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
sub-agent behaviour constraints is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if sub-agent behaviour constraints is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.22 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires sub-agent behaviour
constraints to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 173 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline 5.23 Parallel
Execution Rules Purpose Define and control parallel execution rules as
an enforceable part of the system's governing principle and rule
framework. Objective Make parallel execution rules explicit, testable,
traceable, enforceable, and usable by SRS, development, runtime, QA,
monitoring, and governance components. Requirement Parallel execution
shall be permitted only where tasks are dependency-safe, state-safe, and
free from conflicting authoritative writes. Scope Applies to parallel
execution rules and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
parallel execution rules as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for parallel execution rules,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
parallel execution rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply parallel execution rules
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for parallel execution rules are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that parallel execution rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 174 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Acceptance Criteria
Accepted only when parallel execution rules is explicit, complete,
unambiguous, traceable, testable, enforceable, consistent with
higher-level baselines, and supported by reproducible evidence. Failure
/ Rejection Criteria Rejected if parallel execution rules is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.23 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires parallel execution
rules to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.24 Conflict Resolution Rules Purpose Define and control
conflict resolution rules as an enforceable part of the system's
governing principle and rule framework. Objective Make conflict
resolution rules explicit, testable, traceable, enforceable, and usable
by SRS, development, runtime, QA, monitoring, and governance components.
Requirement The system shall detect and resolve requirement, data,
decision, agent, configuration, or execution conflicts using a defined
precedence and escalation model. Scope Applies to conflict resolution
rules and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret conflict resolution rules
as an explicit controlled rule; map applicable conditions to enforceable
controls and verification; preserve ambiguity or conflict as an
unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for conflict resolution rules, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
conflict resolution rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 175 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Expected Behaviour
The responsible component shall apply conflict resolution rules
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for conflict resolution rules are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that conflict resolution rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
conflict resolution rules is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if conflict resolution rules is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.24 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires conflict resolution
rules to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.25 Self-Evaluation Rules Purpose Define and control
self-evaluation rules as an enforceable part of the system's governing
principle and rule framework. Objective Make self-evaluation rules
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall evaluate its own outputs and behaviour
against approved requirements, quality thresholds, safety controls,
evidence, and acceptance criteria. Scope Applies to self-evaluation
rules and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret self-evaluation rules as
an explicit controlled rule; map applicable conditions to enforceable
controls and verification; preserve ambiguity or conflict as an
unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for self-evaluation rules, including applicable
rule state, validation state, ownership, evidence references, and any
exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 176 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Dependency Depends
on the immutable project goal and mission, approved PoV, defined system
scope and boundaries, and the relevant preceding principles or child
controls within Topic 5. Dependency Type Blocking for any dependency
that affects safety, authority, scope, approval, security, baseline
integrity, or validity; read-only/downstream for analytical or
documentation dependencies that do not alter the governing rule.
Parallelization Eligibility Drafting, evidence collection, test design,
control-schema preparation, and independent validation may run in
parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
self-evaluation rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply self-evaluation rules
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for self-evaluation rules are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that self-evaluation rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
self-evaluation rules is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if self-evaluation rules is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.25 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires self-evaluation
rules to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.26 Self-Improvement Restrictions Purpose Define and control
self-improvement restrictions as an enforceable part of the system's
governing principle and rule framework. Objective Make self-improvement
restrictions explicit, testable, traceable, enforceable, and usable by
SRS, development, runtime, QA, monitoring, and governance components.
Requirement Self-improvement shall be limited to controlled,
evidence-based changes and shall not permit autonomous alteration of
immutable goals, safety boundaries, authority, or approval requirements.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 177 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Scope Applies to
self-improvement restrictions and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
self-improvement restrictions as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for self-improvement
restrictions, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.
Output Destination Controlled SRS/repository, requirements registry,
policy and configuration store, agent registry, enforcement layer, QA
evidence store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
self-improvement restrictions, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply self-improvement
restrictions consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for self-improvement restrictions
are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that self-improvement restrictions is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
self-improvement restrictions is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if self-improvement restrictions is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 178 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Audit /
Traceability All material events involving 5.26 shall record the
requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires self-improvement restrictions to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.26.1 Allowed Improvements Purpose Define and control allowed
improvements as an enforceable part of the system's governing principle
and rule framework. Objective Make allowed improvements explicit,
testable, traceable, enforceable, and usable by SRS, development,
runtime, QA, monitoring, and governance components. Requirement The
system may propose improvements that are evidence-based, bounded,
testable, reversible, and submitted to the defined approval and
change-control process. Scope Applies to allowed improvements and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret allowed improvements as an explicit controlled
rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for allowed improvements, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of allowed improvements, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply allowed improvements consistently, expose relevant state and
evidence, reject or block invalid conditions, preserve traceability, and
escalate material unresolved issues rather than guessing. Error Handling
Invalid, missing, stale, contradictory, unauthorized, or unverifiable
inputs shall be rejected or classified; the event, affected item,
version, actor, and evidence shall be logged; retry is permitted only
where safe and explicitly allowed. Blocked-State Conditions Blocked when
required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for allowed
improvements are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 179 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that allowed improvements is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
allowed improvements is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if allowed improvements is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.26.1 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires allowed
improvements to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.26.2 Prohibited Self-Modifications Purpose Define and
control prohibited self-modifications as an enforceable part of the
system's governing principle and rule framework. Objective Make
prohibited self-modifications explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall prohibit
autonomous self-modification of immutable goals, approval gates, safety
limits, security controls, scope boundaries, audit requirements, or
governance authority. Scope Applies to prohibited self-modifications and
every requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret prohibited self-modifications as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for prohibited self-modifications, including applicable rule
state, validation state, ownership, evidence references, and any
exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 180 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Technical Details
Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
prohibited self-modifications, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply prohibited
self-modifications consistently, expose relevant state and evidence,
reject or block invalid conditions, preserve traceability, and escalate
material unresolved issues rather than guessing. Error Handling Invalid,
missing, stale, contradictory, unauthorized, or unverifiable inputs
shall be rejected or classified; the event, affected item, version,
actor, and evidence shall be logged; retry is permitted only where safe
and explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for prohibited self-modifications
are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that prohibited self-modifications is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
prohibited self-modifications is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if prohibited self-modifications is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.26.2 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires prohibited
self-modifications to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.27 Change Proposal and Approval Rules Purpose Define and
control change proposal and approval rules as an enforceable part of the
system's governing principle and rule framework. Objective Make change
proposal and approval rules explicit, testable, traceable, enforceable,
and usable by SRS, development, runtime, QA, monitoring, and governance
components. Requirement All material changes shall follow a controlled
proposal, impact assessment, approval, validation, versioning, and
adoption workflow. Scope Applies to change proposal and approval rules
and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret change proposal and
approval rules as an explicit controlled rule; map applicable conditions
to enforceable controls and verification; preserve ambiguity or conflict
as an unresolved state rather than inventing a rule; and maintain stable
identifiers and version references.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 181 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Outputs A versioned
specification and enforcement record for change proposal and approval
rules, including applicable rule state, validation state, ownership,
evidence references, and any exception or escalation record. Output
Destination Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of change
proposal and approval rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply change proposal and
approval rules consistently, expose relevant state and evidence, reject
or block invalid conditions, preserve traceability, and escalate
material unresolved issues rather than guessing. Error Handling Invalid,
missing, stale, contradictory, unauthorized, or unverifiable inputs
shall be rejected or classified; the event, affected item, version,
actor, and evidence shall be logged; retry is permitted only where safe
and explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for change proposal and approval
rules are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that change proposal and approval rules is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
change proposal and approval rules is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if change proposal and approval rules is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.27 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires change proposal and
approval rules to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 182 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline 5.27.1 Change
Proposal Purpose Define and control change proposal as an enforceable
part of the system's governing principle and rule framework. Objective
Make change proposal explicit, testable, traceable, enforceable, and
usable by SRS, development, runtime, QA, monitoring, and governance
components. Requirement A material change shall be represented as a
structured change proposal containing the reason, affected items,
evidence, expected outcome, risks, and rollback approach. Scope Applies
to change proposal and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
change proposal as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for change proposal, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of change
proposal, fabricated evidence, hidden assumptions, unauthorized writes,
bypassing safety/security/approval controls, false approval claims, and
untracked changes are prohibited. Expected Behaviour The responsible
component shall apply change proposal consistently, expose relevant
state and evidence, reject or block invalid conditions, preserve
traceability, and escalate material unresolved issues rather than
guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
change proposal are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that change proposal is explicit, testable, enforceable,
and aligned with higher-level baselines. Testing Requirements Positive,
negative, boundary, conflict, unauthorized-action, stale-version,
regression, failure/recovery, audit-trail, and concurrency tests shall
be performed as applicable to the item. Evidence Required Approved
requirement record, versions, configurations, test cases/results, logs,
policy decisions, approvals, defects, recovery records, traceability
links, and relevant screenshots or reports shall be retained.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 183 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Acceptance Criteria
Accepted only when change proposal is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if change proposal is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.27.1 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires change proposal to
be explicit because multiple autonomous and semi-autonomous components
will otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.27.2 Impact Assessment Purpose Define and control impact
assessment as an enforceable part of the system's governing principle
and rule framework. Objective Make impact assessment explicit, testable,
traceable, enforceable, and usable by SRS, development, runtime, QA,
monitoring, and governance components. Requirement Each material change
shall receive an impact assessment covering functional, technical, data,
safety, security, operational, governance, and traceability effects.
Scope Applies to impact assessment and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret impact assessment as an explicit controlled
rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for impact assessment, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of impact assessment, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply impact assessment consistently, expose relevant state and
evidence, reject or block invalid conditions, preserve traceability, and
escalate material unresolved issues rather than guessing.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 184 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Error Handling
Invalid, missing, stale, contradictory, unauthorized, or unverifiable
inputs shall be rejected or classified; the event, affected item,
version, actor, and evidence shall be logged; retry is permitted only
where safe and explicitly allowed. Blocked-State Conditions Blocked when
required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for impact
assessment are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that impact assessment is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
impact assessment is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if impact assessment is ambiguous, incomplete, contradictory,
untestable, unenforceable, unsupported by evidence, capable of
unauthorized bypass, or inconsistent with a locked/higher-level
baseline. Recovery / Corrective Action Preserve evidence; stop or
contain unsafe processing; restore the last known valid state where
applicable; identify root cause; correct through controlled change;
rerun validation and regression tests; and re-accept only after the gate
passes. Audit / Traceability All material events involving 5.27.2 shall
record the requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires impact assessment to be explicit
because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.27.3 Approval Gate Purpose Define and control approval gate
as an enforceable part of the system's governing principle and rule
framework. Objective Make approval gate explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall prevent adoption
of an approval-controlled change until the authorized approval gate is
satisfied and recorded. Scope Applies to approval gate and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret approval gate as an explicit controlled rule;
map applicable conditions to enforceable controls and verification;
preserve ambiguity or conflict as an unresolved state rather than
inventing a rule; and maintain stable identifiers and version
references. Outputs A versioned specification and enforcement record for
approval gate, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.
Output Destination Controlled SRS/repository, requirements registry,
policy and configuration store, agent registry, enforcement layer, QA
evidence store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 185 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Parallelization
Eligibility Drafting, evidence collection, test design, control-schema
preparation, and independent validation may run in parallel after
governing inputs are frozen and provided that no competing authoritative
write is created. Parallelization Restrictions Parallel workers shall
not redefine the goal, expand scope, weaken safety or security controls,
grant authority, bypass approval gates, alter a locked baseline, or
overwrite another authoritative result. Technical Details Use stable
requirement IDs, versioned machine-readable policy/configuration,
explicit state models, immutable audit records, schema validation,
deterministic evaluation where required, access controls, and automated
traceability from requirement to test/evidence. Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
approval gate, fabricated evidence, hidden assumptions, unauthorized
writes, bypassing safety/security/approval controls, false approval
claims, and untracked changes are prohibited. Expected Behaviour The
responsible component shall apply approval gate consistently, expose
relevant state and evidence, reject or block invalid conditions,
preserve traceability, and escalate material unresolved issues rather
than guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
approval gate are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that approval gate is explicit, testable, enforceable,
and aligned with higher-level baselines. Testing Requirements Positive,
negative, boundary, conflict, unauthorized-action, stale-version,
regression, failure/recovery, audit-trail, and concurrency tests shall
be performed as applicable to the item. Evidence Required Approved
requirement record, versions, configurations, test cases/results, logs,
policy decisions, approvals, defects, recovery records, traceability
links, and relevant screenshots or reports shall be retained. Acceptance
Criteria Accepted only when approval gate is explicit, complete,
unambiguous, traceable, testable, enforceable, consistent with
higher-level baselines, and supported by reproducible evidence. Failure
/ Rejection Criteria Rejected if approval gate is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.27.3 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires approval gate to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.27.4 Validation Before Adoption Purpose Define and control
validation before adoption as an enforceable part of the system's
governing principle and rule framework. Objective Make validation before
adoption explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement A change shall not become authoritative until required
tests, validation, evidence review, regression checks, and acceptance
conditions pass. Scope Applies to validation before adoption and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 186 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Input Source
Controlled SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
validation before adoption as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for validation before
adoption, including applicable rule state, validation state, ownership,
evidence references, and any exception or escalation record. Output
Destination Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
validation before adoption, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply validation before
adoption consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for validation before adoption are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that validation before adoption is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
validation before adoption is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if validation before adoption is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.27.4 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 187 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Rationale /
Assumptions The project requires validation before adoption to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.28 System Consistency Rules Purpose Define and control
system consistency rules as an enforceable part of the system's
governing principle and rule framework. Objective Make system
consistency rules explicit, testable, traceable, enforceable, and usable
by SRS, development, runtime, QA, monitoring, and governance components.
Requirement System components, agents, requirements, configurations,
data contracts, and operational states shall remain mutually consistent
with their governing baselines. Scope Applies to system consistency
rules and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret system consistency rules
as an explicit controlled rule; map applicable conditions to enforceable
controls and verification; preserve ambiguity or conflict as an
unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for system consistency rules, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of system
consistency rules, fabricated evidence, hidden assumptions, unauthorized
writes, bypassing safety/security/approval controls, false approval
claims, and untracked changes are prohibited. Expected Behaviour The
responsible component shall apply system consistency rules consistently,
expose relevant state and evidence, reject or block invalid conditions,
preserve traceability, and escalate material unresolved issues rather
than guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
system consistency rules are missing, contradictory, stale, or unsafe to
use. Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 188 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that system consistency rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
system consistency rules is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if system consistency rules is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.28 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires system consistency
rules to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.29 Rule Violation Detection Purpose Define and control rule
violation detection as an enforceable part of the system's governing
principle and rule framework. Objective Make rule violation detection
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement The system shall detect violations of principles and
non-negotiable rules, record evidence, classify severity, and initiate
enforcement or escalation. Scope Applies to rule violation detection and
every requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret rule violation detection as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for rule violation detection, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 189 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of rule
violation detection, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply rule violation detection
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for rule violation detection are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that rule violation detection is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
rule violation detection is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if rule violation detection is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.29 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires rule violation
detection to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.30 Rule Enforcement Mechanism Purpose Define and control
rule enforcement mechanism as an enforceable part of the system's
governing principle and rule framework. Objective Make rule enforcement
mechanism explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement Applicable principles and rules shall be implemented through
enforceable controls at specification, development, deployment, and
runtime layers. Scope Applies to rule enforcement mechanism and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions. Input Source Controlled SRS repository, baselined
Topics 1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret rule enforcement mechanism as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for rule enforcement mechanism, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 190 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of rule
enforcement mechanism, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply rule enforcement
mechanism consistently, expose relevant state and evidence, reject or
block invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for rule enforcement mechanism are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that rule enforcement mechanism is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
rule enforcement mechanism is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if rule enforcement mechanism is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.30 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires rule enforcement
mechanism to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 191 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline 5.31 Exception
Handling Rules Purpose Define and control exception handling rules as an
enforceable part of the system's governing principle and rule framework.
Objective Make exception handling rules explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The system shall define a
controlled process for identifying, classifying, approving, handling,
recording, and closing exceptions. Scope Applies to exception handling
rules and every requirement, agent, component, workflow, configuration,
decision, action, and governance record that is governed by or can
materially affect this item. Inputs Approved higher-level requirements,
the frozen Phase 1 hierarchy, relevant preceding Topic 1--4 baselines,
applicable policies, configurations, evidence, test results, and
authorized governance decisions. Input Source Controlled SRS repository,
baselined Topics 1--4, requirements registry, policy/configuration
repository, QA evidence, audit records, and authorized governance
records. Processing / Method / Rules Interpret exception handling rules
as an explicit controlled rule; map applicable conditions to enforceable
controls and verification; preserve ambiguity or conflict as an
unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for exception handling rules, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
exception handling rules, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply exception handling rules
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for exception handling rules are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that exception handling rules is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 192 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Acceptance Criteria
Accepted only when exception handling rules is explicit, complete,
unambiguous, traceable, testable, enforceable, consistent with
higher-level baselines, and supported by reproducible evidence. Failure
/ Rejection Criteria Rejected if exception handling rules is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.31 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires exception handling
rules to be explicit because multiple autonomous and semi-autonomous
components will otherwise be able to interpret or modify governing
behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.31.1 Exception Definition Purpose Define and control
exception definition as an enforceable part of the system's governing
principle and rule framework. Objective Make exception definition
explicit, testable, traceable, enforceable, and usable by SRS,
development, runtime, QA, monitoring, and governance components.
Requirement An exception shall be represented as a bounded, explicit
deviation from a normally applicable rule with a documented reason,
owner, duration, impact, and authority. Scope Applies to exception
definition and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
exception definition as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for exception definition, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
exception definition, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply exception definition
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 193 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Error Handling
Invalid, missing, stale, contradictory, unauthorized, or unverifiable
inputs shall be rejected or classified; the event, affected item,
version, actor, and evidence shall be logged; retry is permitted only
where safe and explicitly allowed. Blocked-State Conditions Blocked when
required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for exception
definition are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that exception definition is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
exception definition is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if exception definition is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.31.1 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update. Rationale / Assumptions The project requires exception
definition to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.31.2 Exception Handling Purpose Define and control exception
handling as an enforceable part of the system's governing principle and
rule framework. Objective Make exception handling explicit, testable,
traceable, enforceable, and usable by SRS, development, runtime, QA,
monitoring, and governance components. Requirement Exceptions shall be
handled through defined containment, approval, monitoring, expiry,
evidence, and closure controls without silently changing the underlying
rule. Scope Applies to exception handling and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret exception handling as an explicit controlled
rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for exception handling, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 194 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Parallelization
Eligibility Drafting, evidence collection, test design, control-schema
preparation, and independent validation may run in parallel after
governing inputs are frozen and provided that no competing authoritative
write is created. Parallelization Restrictions Parallel workers shall
not redefine the goal, expand scope, weaken safety or security controls,
grant authority, bypass approval gates, alter a locked baseline, or
overwrite another authoritative result. Technical Details Use stable
requirement IDs, versioned machine-readable policy/configuration,
explicit state models, immutable audit records, schema validation,
deterministic evaluation where required, access controls, and automated
traceability from requirement to test/evidence. Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
exception handling, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply exception handling
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for exception handling are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that exception handling is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
exception handling is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if exception handling is ambiguous, incomplete, contradictory,
untestable, unenforceable, unsupported by evidence, capable of
unauthorized bypass, or inconsistent with a locked/higher-level
baseline. Recovery / Corrective Action Preserve evidence; stop or
contain unsafe processing; restore the last known valid state where
applicable; identify root cause; correct through controlled change;
rerun validation and regression tests; and re-accept only after the gate
passes. Audit / Traceability All material events involving 5.31.2 shall
record the requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires exception handling to be explicit
because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.32 Principle Validation and Review Purpose Define and
control principle validation and review as an enforceable part of the
system's governing principle and rule framework. Objective Make
principle validation and review explicit, testable, traceable,
enforceable, and usable by SRS, development, runtime, QA, monitoring,
and governance components. Requirement The principles shall be
periodically and event-driven validated for completeness, consistency,
enforceability, effectiveness, and continued alignment with approved
baselines. Scope Applies to principle validation and review and every
requirement, agent, component, workflow, configuration, decision,
action, and governance record that is governed by or can materially
affect this item. Inputs Approved higher-level requirements, the frozen
Phase 1 hierarchy, relevant preceding Topic 1--4 baselines, applicable
policies, configurations, evidence, test results, and authorized
governance decisions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 195 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Input Source
Controlled SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
principle validation and review as an explicit controlled rule; map
applicable conditions to enforceable controls and verification; preserve
ambiguity or conflict as an unresolved state rather than inventing a
rule; and maintain stable identifiers and version references. Outputs A
versioned specification and enforcement record for principle validation
and review, including applicable rule state, validation state,
ownership, evidence references, and any exception or escalation record.
Output Destination Controlled SRS/repository, requirements registry,
policy and configuration store, agent registry, enforcement layer, QA
evidence store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
principle validation and review, fabricated evidence, hidden
assumptions, unauthorized writes, bypassing safety/security/approval
controls, false approval claims, and untracked changes are prohibited.
Expected Behaviour The responsible component shall apply principle
validation and review consistently, expose relevant state and evidence,
reject or block invalid conditions, preserve traceability, and escalate
material unresolved issues rather than guessing. Error Handling Invalid,
missing, stale, contradictory, unauthorized, or unverifiable inputs
shall be rejected or classified; the event, affected item, version,
actor, and evidence shall be logged; retry is permitted only where safe
and explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for principle validation and
review are missing, contradictory, stale, or unsafe to use. Unblocking
Conditions Resume only after the blocker is resolved by supplying or
correcting the required input/evidence/approval/control, re-running
affected validation, and recording the resulting state. Human Escalation
Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that principle validation and review is explicit,
testable, enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
principle validation and review is explicit, complete, unambiguous,
traceable, testable, enforceable, consistent with higher-level
baselines, and supported by reproducible evidence. Failure / Rejection
Criteria Rejected if principle validation and review is ambiguous,
incomplete, contradictory, untestable, unenforceable, unsupported by
evidence, capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline. Recovery / Corrective Action Preserve
evidence; stop or contain unsafe processing; restore the last known
valid state where applicable; identify root cause; correct through
controlled change; rerun validation and regression tests; and re-accept
only after the gate passes. Audit / Traceability All material events
involving 5.32 shall record the requirement/item ID, version,
actor/component, timestamp, input/configuration versions,
decision/state, evidence references, and related change or incident IDs.
Change Control Material changes shall follow Topic 1 change control:
change request, impact assessment, authorized approval, implementation,
validation, evidence capture, version increment, and controlled baseline
update.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 196 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Rationale /
Assumptions The project requires principle validation and review to be
explicit because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.33 Baseline Lock and Controlled Modification Purpose Define
and control baseline lock and controlled modification as an enforceable
part of the system's governing principle and rule framework. Objective
Make baseline lock and controlled modification explicit, testable,
traceable, enforceable, and usable by SRS, development, runtime, QA,
monitoring, and governance components. Requirement Approved baselines
shall be locked against unauthorized modification, while legitimate
changes shall use controlled versioned replacement. Scope Applies to
baseline lock and controlled modification and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret baseline lock and controlled modification as an
explicit controlled rule; map applicable conditions to enforceable
controls and verification; preserve ambiguity or conflict as an
unresolved state rather than inventing a rule; and maintain stable
identifiers and version references. Outputs A versioned specification
and enforcement record for baseline lock and controlled modification,
including applicable rule state, validation state, ownership, evidence
references, and any exception or escalation record. Output Destination
Controlled SRS/repository, requirements registry, policy and
configuration store, agent registry, enforcement layer, QA evidence
store, dashboard/observability, and audit trail as applicable.
Responsible Agent / Component SRS Governance Owner / SRS Writer Agent
for specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
baseline lock and controlled modification, fabricated evidence, hidden
assumptions, unauthorized writes, bypassing safety/security/approval
controls, false approval claims, and untracked changes are prohibited.
Expected Behaviour The responsible component shall apply baseline lock
and controlled modification consistently, expose relevant state and
evidence, reject or block invalid conditions, preserve traceability, and
escalate material unresolved issues rather than guessing. Error Handling
Invalid, missing, stale, contradictory, unauthorized, or unverifiable
inputs shall be rejected or classified; the event, affected item,
version, actor, and evidence shall be logged; retry is permitted only
where safe and explicitly allowed. Blocked-State Conditions Blocked when
required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for baseline lock
and controlled modification are missing, contradictory, stale, or unsafe
to use. Unblocking Conditions Resume only after the blocker is resolved
by supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 197 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that baseline lock and controlled modification is
explicit, testable, enforceable, and aligned with higher-level
baselines. Testing Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
baseline lock and controlled modification is explicit, complete,
unambiguous, traceable, testable, enforceable, consistent with
higher-level baselines, and supported by reproducible evidence. Failure
/ Rejection Criteria Rejected if baseline lock and controlled
modification is ambiguous, incomplete, contradictory, untestable,
unenforceable, unsupported by evidence, capable of unauthorized bypass,
or inconsistent with a locked/higher-level baseline. Recovery /
Corrective Action Preserve evidence; stop or contain unsafe processing;
restore the last known valid state where applicable; identify root
cause; correct through controlled change; rerun validation and
regression tests; and re-accept only after the gate passes. Audit /
Traceability All material events involving 5.33 shall record the
requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires baseline lock and controlled
modification to be explicit because multiple autonomous and
semi-autonomous components will otherwise be able to interpret or modify
governing behaviour inconsistently. Verification Method Perform document
inspection, schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.33.1 Baseline Creation Purpose Define and control baseline
creation as an enforceable part of the system's governing principle and
rule framework. Objective Make baseline creation explicit, testable,
traceable, enforceable, and usable by SRS, development, runtime, QA,
monitoring, and governance components. Requirement A baseline shall be
created only after completeness, consistency, traceability, validation,
acceptance, and approval conditions are satisfied. Scope Applies to
baseline creation and every requirement, agent, component, workflow,
configuration, decision, action, and governance record that is governed
by or can materially affect this item. Inputs Approved higher-level
requirements, the frozen Phase 1 hierarchy, relevant preceding Topic
1--4 baselines, applicable policies, configurations, evidence, test
results, and authorized governance decisions. Input Source Controlled
SRS repository, baselined Topics 1--4, requirements registry,
policy/configuration repository, QA evidence, audit records, and
authorized governance records. Processing / Method / Rules Interpret
baseline creation as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for baseline creation, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable. Responsible
Agent / Component SRS Governance Owner / SRS Writer Agent for
specification; applicable Policy/Enforcement, Agent Runtime, QA,
Security, Observability, or Change-Control component for implementation
and validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 198 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Tools / Resources
Version-control repository, requirements registry, policy/configuration
store, schema validators, automated test harness, CI checks,
logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
baseline creation, fabricated evidence, hidden assumptions, unauthorized
writes, bypassing safety/security/approval controls, false approval
claims, and untracked changes are prohibited. Expected Behaviour The
responsible component shall apply baseline creation consistently, expose
relevant state and evidence, reject or block invalid conditions,
preserve traceability, and escalate material unresolved issues rather
than guessing. Error Handling Invalid, missing, stale, contradictory,
unauthorized, or unverifiable inputs shall be rejected or classified;
the event, affected item, version, actor, and evidence shall be logged;
retry is permitted only where safe and explicitly allowed. Blocked-State
Conditions Blocked when required governing baselines, inputs, approvals,
evidence, authorization, validation, or enforcement capability for
baseline creation are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that baseline creation is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
baseline creation is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if baseline creation is ambiguous, incomplete, contradictory,
untestable, unenforceable, unsupported by evidence, capable of
unauthorized bypass, or inconsistent with a locked/higher-level
baseline. Recovery / Corrective Action Preserve evidence; stop or
contain unsafe processing; restore the last known valid state where
applicable; identify root cause; correct through controlled change;
rerun validation and regression tests; and re-accept only after the gate
passes. Audit / Traceability All material events involving 5.33.1 shall
record the requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires baseline creation to be explicit
because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.33.2 Baseline Protection Purpose Define and control baseline
protection as an enforceable part of the system's governing principle
and rule framework. Objective Make baseline protection explicit,
testable, traceable, enforceable, and usable by SRS, development,
runtime, QA, monitoring, and governance components. Requirement A locked
baseline shall be protected against unauthorized writes, deletion,
silent replacement, history loss, or untracked mutation. Scope Applies
to baseline protection and every requirement, agent, component,
workflow, configuration, decision, action, and governance record that is
governed by or can materially affect this item. Inputs Approved
higher-level requirements, the frozen Phase 1 hierarchy, relevant
preceding Topic 1--4 baselines, applicable policies, configurations,
evidence, test results, and authorized governance decisions. Input
Source Controlled SRS repository, baselined Topics 1--4, requirements
registry, policy/configuration repository, QA evidence, audit records,
and authorized governance records. Processing / Method / Rules Interpret
baseline protection as an explicit controlled rule; map applicable
conditions to enforceable controls and verification; preserve ambiguity
or conflict as an unresolved state rather than inventing a rule; and
maintain stable identifiers and version references. Outputs A versioned
specification and enforcement record for baseline protection, including
applicable rule state, validation state, ownership, evidence references,
and any exception or escalation record. Output Destination Controlled
SRS/repository, requirements registry, policy and configuration store,
agent registry, enforcement layer, QA evidence store,
dashboard/observability, and audit trail as applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 199 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Responsible Agent /
Component SRS Governance Owner / SRS Writer Agent for specification;
applicable Policy/Enforcement, Agent Runtime, QA, Security,
Observability, or Change-Control component for implementation and
validation; authorized human governance for controlled approvals.
Prerequisites Topics 1--4 shall be completed and baseline-ready/approved
as required by governance; directly preceding parent/child items shall
also be satisfied where the hierarchy creates a logical dependency.
Dependency Depends on the immutable project goal and mission, approved
PoV, defined system scope and boundaries, and the relevant preceding
principles or child controls within Topic 5. Dependency Type Blocking
for any dependency that affects safety, authority, scope, approval,
security, baseline integrity, or validity; read-only/downstream for
analytical or documentation dependencies that do not alter the governing
rule. Parallelization Eligibility Drafting, evidence collection, test
design, control-schema preparation, and independent validation may run
in parallel after governing inputs are frozen and provided that no
competing authoritative write is created. Parallelization Restrictions
Parallel workers shall not redefine the goal, expand scope, weaken
safety or security controls, grant authority, bypass approval gates,
alter a locked baseline, or overwrite another authoritative result.
Technical Details Use stable requirement IDs, versioned machine-readable
policy/configuration, explicit state models, immutable audit records,
schema validation, deterministic evaluation where required, access
controls, and automated traceability from requirement to test/evidence.
Tools / Resources Version-control repository, requirements registry,
policy/configuration store, schema validators, automated test harness,
CI checks, logging/observability, dashboard, audit store, and approved
development/analysis tools. Constraints Initial system boundaries,
India/INR PoV limits, safety controls, human approval gates, frozen
numbering, least privilege, auditability, evidence retention, and
approved infrastructure/API limits remain binding unless changed through
governance. Prohibited Actions Silent weakening or alteration of
baseline protection, fabricated evidence, hidden assumptions,
unauthorized writes, bypassing safety/security/approval controls, false
approval claims, and untracked changes are prohibited. Expected
Behaviour The responsible component shall apply baseline protection
consistently, expose relevant state and evidence, reject or block
invalid conditions, preserve traceability, and escalate material
unresolved issues rather than guessing. Error Handling Invalid, missing,
stale, contradictory, unauthorized, or unverifiable inputs shall be
rejected or classified; the event, affected item, version, actor, and
evidence shall be logged; retry is permitted only where safe and
explicitly allowed. Blocked-State Conditions Blocked when required
governing baselines, inputs, approvals, evidence, authorization,
validation, or enforcement capability for baseline protection are
missing, contradictory, stale, or unsafe to use. Unblocking Conditions
Resume only after the blocker is resolved by supplying or correcting the
required input/evidence/approval/control, re-running affected
validation, and recording the resulting state. Human Escalation Human
governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that baseline protection is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
baseline protection is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if baseline protection is ambiguous, incomplete, contradictory,
untestable, unenforceable, unsupported by evidence, capable of
unauthorized bypass, or inconsistent with a locked/higher-level
baseline. Recovery / Corrective Action Preserve evidence; stop or
contain unsafe processing; restore the last known valid state where
applicable; identify root cause; correct through controlled change;
rerun validation and regression tests; and re-accept only after the gate
passes. Audit / Traceability All material events involving 5.33.2 shall
record the requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires baseline protection to be explicit
because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. 5.34 Governance of Principles Purpose Define and control
governance of principles as an enforceable part of the system's
governing principle and rule framework.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 200 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Objective Make
governance of principles explicit, testable, traceable, enforceable, and
usable by SRS, development, runtime, QA, monitoring, and governance
components. Requirement Governance shall define ownership, approval
authority, review cadence, enforcement responsibility, exception
authority, evidence retention, and change control for the principles.
Scope Applies to governance of principles and every requirement, agent,
component, workflow, configuration, decision, action, and governance
record that is governed by or can materially affect this item. Inputs
Approved higher-level requirements, the frozen Phase 1 hierarchy,
relevant preceding Topic 1--4 baselines, applicable policies,
configurations, evidence, test results, and authorized governance
decisions. Input Source Controlled SRS repository, baselined Topics
1--4, requirements registry, policy/configuration repository, QA
evidence, audit records, and authorized governance records. Processing /
Method / Rules Interpret governance of principles as an explicit
controlled rule; map applicable conditions to enforceable controls and
verification; preserve ambiguity or conflict as an unresolved state
rather than inventing a rule; and maintain stable identifiers and
version references. Outputs A versioned specification and enforcement
record for governance of principles, including applicable rule state,
validation state, ownership, evidence references, and any exception or
escalation record. Output Destination Controlled SRS/repository,
requirements registry, policy and configuration store, agent registry,
enforcement layer, QA evidence store, dashboard/observability, and audit
trail as applicable. Responsible Agent / Component SRS Governance Owner
/ SRS Writer Agent for specification; applicable Policy/Enforcement,
Agent Runtime, QA, Security, Observability, or Change-Control component
for implementation and validation; authorized human governance for
controlled approvals. Prerequisites Topics 1--4 shall be completed and
baseline-ready/approved as required by governance; directly preceding
parent/child items shall also be satisfied where the hierarchy creates a
logical dependency. Dependency Depends on the immutable project goal and
mission, approved PoV, defined system scope and boundaries, and the
relevant preceding principles or child controls within Topic 5.
Dependency Type Blocking for any dependency that affects safety,
authority, scope, approval, security, baseline integrity, or validity;
read-only/downstream for analytical or documentation dependencies that
do not alter the governing rule. Parallelization Eligibility Drafting,
evidence collection, test design, control-schema preparation, and
independent validation may run in parallel after governing inputs are
frozen and provided that no competing authoritative write is created.
Parallelization Restrictions Parallel workers shall not redefine the
goal, expand scope, weaken safety or security controls, grant authority,
bypass approval gates, alter a locked baseline, or overwrite another
authoritative result. Technical Details Use stable requirement IDs,
versioned machine-readable policy/configuration, explicit state models,
immutable audit records, schema validation, deterministic evaluation
where required, access controls, and automated traceability from
requirement to test/evidence. Tools / Resources Version-control
repository, requirements registry, policy/configuration store, schema
validators, automated test harness, CI checks, logging/observability,
dashboard, audit store, and approved development/analysis tools.
Constraints Initial system boundaries, India/INR PoV limits, safety
controls, human approval gates, frozen numbering, least privilege,
auditability, evidence retention, and approved infrastructure/API limits
remain binding unless changed through governance. Prohibited Actions
Silent weakening or alteration of governance of principles, fabricated
evidence, hidden assumptions, unauthorized writes, bypassing
safety/security/approval controls, false approval claims, and untracked
changes are prohibited. Expected Behaviour The responsible component
shall apply governance of principles consistently, expose relevant state
and evidence, reject or block invalid conditions, preserve traceability,
and escalate material unresolved issues rather than guessing. Error
Handling Invalid, missing, stale, contradictory, unauthorized, or
unverifiable inputs shall be rejected or classified; the event, affected
item, version, actor, and evidence shall be logged; retry is permitted
only where safe and explicitly allowed. Blocked-State Conditions Blocked
when required governing baselines, inputs, approvals, evidence,
authorization, validation, or enforcement capability for governance of
principles are missing, contradictory, stale, or unsafe to use.
Unblocking Conditions Resume only after the blocker is resolved by
supplying or correcting the required input/evidence/approval/control,
re-running affected validation, and recording the resulting state. Human
Escalation Human governance is required for material principle changes,
approval-controlled actions, safety/security/scope exceptions,
unresolved conflicts, baseline acceptance, and any case where the
defined authority cannot safely resolve the issue. Validation Method
Inspect the requirement, its traceability, policy/control mapping,
version state, authorization behaviour, evidence, and implementation
outcome; verify that governance of principles is explicit, testable,
enforceable, and aligned with higher-level baselines. Testing
Requirements Positive, negative, boundary, conflict,
unauthorized-action, stale-version, regression, failure/recovery,
audit-trail, and concurrency tests shall be performed as applicable to
the item. Evidence Required Approved requirement record, versions,
configurations, test cases/results, logs, policy decisions, approvals,
defects, recovery records, traceability links, and relevant screenshots
or reports shall be retained. Acceptance Criteria Accepted only when
governance of principles is explicit, complete, unambiguous, traceable,
testable, enforceable, consistent with higher-level baselines, and
supported by reproducible evidence. Failure / Rejection Criteria
Rejected if governance of principles is ambiguous, incomplete,
contradictory, untestable, unenforceable, unsupported by evidence,
capable of unauthorized bypass, or inconsistent with a
locked/higher-level baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 201 -->
```
AI Investment Opportunity Agent --- Topic 5 Baseline Recovery /
Corrective Action Preserve evidence; stop or contain unsafe processing;
restore the last known valid state where applicable; identify root
cause; correct through controlled change; rerun validation and
regression tests; and re-accept only after the gate passes. Audit /
Traceability All material events involving 5.34 shall record the
requirement/item ID, version, actor/component, timestamp,
input/configuration versions, decision/state, evidence references, and
related change or incident IDs. Change Control Material changes shall
follow Topic 1 change control: change request, impact assessment,
authorized approval, implementation, validation, evidence capture,
version increment, and controlled baseline update. Rationale /
Assumptions The project requires governance of principles to be explicit
because multiple autonomous and semi-autonomous components will
otherwise be able to interpret or modify governing behaviour
inconsistently. Verification Method Perform document inspection,
schema/structure validation, traceability checks, controlled
positive/negative tests, unauthorized-action tests where applicable, and
evidence review; confirm the result against the approved Topic 5
baseline. FINAL VALIDATION GATE --- TOPIC 5 Hierarchy validation: All
frozen Topic 5 numbers from 5.1 through 5.34, including the defined
child items under 5.3, 5.8, 5.26, 5.27, 5.31, and 5.33, are included
without renumbering or omission. Format validation: Every numbered item
is presented in the same two-column bordered table structure: field name
in the left column, complete specification text in the right column,
with a light-gray field-label column, visible grid lines, and
top-aligned cells. Specification validation: Every item contains the
complete mandatory specification contract plus Rationale / Assumptions
and Verification Method. Material requirements use normative "shall"
language, and the document explicitly prohibits silent assumptions,
unauthorized changes, and baseline bypass. Baseline status:
BASELINE-READY. Formal governance approval remains a human-controlled
gate. This document must not be treated as formally approved until the
designated governance authority records approval under Topic 1 change
and baseline controls.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 202 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy AI Investment Opportunity Agent FULL MASTER SRS --- TOPICS
6--15 Corrected hierarchy + complete 34-field specification contract
This section supplies the missing full SRS detail for Topics 6--15 using
the authoritative numbered hierarchy. It restores every nested child
exactly as specified for these topics and gives every numbered item all
34 mandatory fields. It does not use the earlier artificial equal-child
decomposition.
