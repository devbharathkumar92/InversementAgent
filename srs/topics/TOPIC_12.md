# Topic 12 --- Opportunity Discovery Engine

> Authoritative source slice from the uploaded Full Master SRS. Source
> PDF pages 459--499. Preserve numbering and requirement wording.

## Source Requirements

```{=html}
<!-- Source PDF page 459 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Testing Requirements Unit, component,
contract, integration, negative, boundary, concurrency/idempotency,
failure/recovery, audit-traceability, and regression tests shall cover
applicable behaviours. Evidence Required Input snapshots/references,
output state, version, rule/configuration version, execution/trace ID,
validation results, test results, errors/recovery records, and
approval/change evidence where applicable. Acceptance Criteria 11.30 is
accepted only when the specified behaviour is implemented, validated,
traceable, test-covered, within scope, and free of unresolved blocking
defects. Failure / Rejection Criteria Reject when Data Validation
Baseline and Change Control is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 11.30 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 11.30 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 11.30. 12. Opportunity
Discovery Engine Opportunity discovery shall identify short-term
India/INR opportunities from validated market, news, financial,
economic, and approved alternative data while applying hard/soft
filters, evidence requirements, expiry, risk pre-filtering, confidence,
and deduplication. 12.1 --- Opportunity Discovery Objectives Field
Specification Purpose Define and control Opportunity Discovery
Objectives as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Discovery Objectives unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Opportunity Discovery
Objectives as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Discovery
Objectives, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Discovery Objectives. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Discovery Objectives; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Discovery Objectives
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.1 is finalized. Dependencies Topic 12 parent and
adjacent controls, plus the approved upstream contracts relevant to
Opportunity Discovery Objectives. Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Discovery Objectives may run in
parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.1, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Discovery
Objectives consistently for the same validated inputs and configuration,
expose its state and evidence, and fail closed when required safety,
authority, or integrity conditions are not satisfied. Error Handling
Classify errors, preserve evidence, retry only when the error is
explicitly recoverable, use an approved fallback when available,
transition to a safe state when correctness is uncertain, and escalate
material failures. Blocked-State Conditions Blocked when required
inputs, parent state, dependency, approval, schema, evidence, authority,
or validation result for Opportunity Discovery Objectives is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 460 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Validation Method Validate hierarchy/ID,
schema, business/control rules, dependencies, state transitions,
provenance, authorization, evidence completeness, and cross-topic
consistency for 12.1. Testing Requirements Unit, component, contract,
integration, negative, boundary, concurrency/idempotency,
failure/recovery, audit-traceability, and regression tests shall cover
applicable behaviours. Evidence Required Input snapshots/references,
output state, version, rule/configuration version, execution/trace ID,
validation results, test results, errors/recovery records, and
approval/change evidence where applicable. Acceptance Criteria 12.1 is
accepted only when the specified behaviour is implemented, validated,
traceable, test-covered, within scope, and free of unresolved blocking
defects. Failure / Rejection Criteria Reject when Opportunity Discovery
Objectives is incomplete, ambiguous, unverifiable, inconsistent with
governing requirements, unsafe, unauthorized, materially untraceable, or
based on invalid/stale data. Recovery / Corrective Action Restore the
last known valid state, preserve evidence, isolate the fault, correct
through controlled change, rerun impacted tests/validation, and
reconcile downstream state before acceptance. Audit / Traceability Every
material event for 12.1 shall record requirement ID, version,
actor/component, timestamp, input/output references, decision/state,
evidence, test result, and change linkage. Change Control Material
changes to 12.1 shall follow Topic 27 governance/change control: request
→ impact/risk assessment → authorized approval → implementation →
validation → version/baseline update → audit evidence. Rationale /
Assumptions The frozen hierarchy and approved project constraints are
authoritative. This item must be implementable without hidden
assumptions; where source detail is not explicit, the implementation
shall use the controlled project governance process rather than invent
authority. Verification Method Inspect the generated specification
against the authoritative hierarchy, execute mapped tests and negative
cases, verify evidence/traceability, and confirm no prohibited scope or
authority change for 12.1. 12.2 --- Opportunity Definition Field
Specification Purpose Define and control Opportunity Definition as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Opportunity Definition unambiguous, deterministic where applicable,
testable, traceable, and usable by implementation agents and runtime
components without hidden assumptions. Requirement The system shall
define and enforce Opportunity Definition as a version-controlled,
testable control within Topic 12, consistent with the approved project
goal, PoV, scope, safety rules, and upstream/downstream contracts.
Opportunity discovery shall identify short-term India/INR opportunities
from validated market, news, financial, economic, and approved
alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Scope Applies to Opportunity Definition, its directly affected inputs,
outputs, states, interfaces, evidence, dependencies, permissions, and
governance controls; it shall not silently expand the frozen project
goal or scope. Inputs Approved Topic 12 requirements, upstream validated
state, configuration, schemas, relevant evidence, and authorized
governance decisions required for Opportunity Definition. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Definition; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Definition
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.2 is finalized. Dependencies Topic 12 parent and
adjacent controls, plus the approved upstream contracts relevant to
Opportunity Definition. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Definition may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.2, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Definition consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Definition is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.2. Testing Requirements
Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 461 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Evidence Required Input
snapshots/references, output state, version, rule/configuration version,
execution/trace ID, validation results, test results, errors/recovery
records, and approval/change evidence where applicable. Acceptance
Criteria 12.2 is accepted only when the specified behaviour is
implemented, validated, traceable, test-covered, within scope, and free
of unresolved blocking defects. Failure / Rejection Criteria Reject when
Opportunity Definition is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.2 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.2. 12.3 --- Market Scanning
Field Specification Purpose Define and control Market Scanning as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Market Scanning unambiguous, deterministic where applicable,
testable, traceable, and usable by implementation agents and runtime
components without hidden assumptions. Requirement The system shall
define and enforce Market Scanning as a version-controlled, testable
control within Topic 12, consistent with the approved project goal, PoV,
scope, safety rules, and upstream/downstream contracts. Opportunity
discovery shall identify short-term India/INR opportunities from
validated market, news, financial, economic, and approved alternative
data while applying hard/soft filters, evidence requirements, expiry,
risk pre-filtering, confidence, and deduplication. Scope Applies to
Market Scanning, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Market Scanning. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Market Scanning; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated Market Scanning state/specification, decision or
control result where applicable, validation status, evidence references,
and trace information. Output Destination Controlled SRS/requirements
registry, owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.3 is
finalized. Dependencies Topic 12 parent and adjacent controls, plus the
approved upstream contracts relevant to Market Scanning. Dependency Type
Blocking where goal, safety, authority, data integrity, schema, or
governance correctness is material; otherwise downstream/read-only.
Parallelization Eligibility Independent design, test preparation,
evidence-template work, and read-only analysis for Market Scanning may
run in parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.3, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Market Scanning
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for Market
Scanning is missing, stale, contradictory, or invalid. Unblocking
Conditions Supply or restore the missing/invalid prerequisite, reconcile
conflicting state, obtain required approval, and rerun all affected
validation before resuming dependent work. Human Escalation Escalate
material safety, governance, security, scope, goal, unresolved
ambiguity, repeated recovery failure, or approval-required conditions to
authorized human governance; routine non-blocking issues remain
automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.3. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.3 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 462 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Failure / Rejection Criteria Reject when
Market Scanning is incomplete, ambiguous, unverifiable, inconsistent
with governing requirements, unsafe, unauthorized, materially
untraceable, or based on invalid/stale data. Recovery / Corrective
Action Restore the last known valid state, preserve evidence, isolate
the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.3 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.3 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.3. 12.4 --- Asset Universe
Definition Field Specification Purpose Define and control Asset Universe
Definition as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Asset Universe Definition unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Asset Universe
Definition as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Asset Universe
Definition, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Asset Universe Definition. Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for Asset
Universe Definition; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated Asset Universe Definition state/specification,
decision or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.4 is
finalized. Dependencies Topic 12 parent and adjacent controls, plus the
approved upstream contracts relevant to Asset Universe Definition.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Asset Universe Definition may run in parallel after governing contracts
and versions are frozen. Parallelization Restrictions Parallel workers
shall not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.4, versioned schemas/configuration,
deterministic validation, structured state transitions,
correlation/trace IDs, and idempotent processing where repeat execution
is possible. Tools / Resources Approved source repository, requirements
registry, version control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Asset Universe Definition
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for Asset
Universe Definition is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.4. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.4 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Asset Universe Definition is
incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 463 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Audit / Traceability Every material event
for 12.4 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.4
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.4. 12.5 --- Opportunity Identification Field Specification
Purpose Define and control Opportunity Identification as an explicit
part of Topic 12 --- Opportunity Discovery Engine. Objective Make
Opportunity Identification unambiguous, deterministic where applicable,
testable, traceable, and usable by implementation agents and runtime
components without hidden assumptions. Requirement The system shall
define and enforce Opportunity Identification as a version-controlled,
testable control within Topic 12, consistent with the approved project
goal, PoV, scope, safety rules, and upstream/downstream contracts.
Opportunity discovery shall identify short-term India/INR opportunities
from validated market, news, financial, economic, and approved
alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Scope Applies to Opportunity Identification, its directly affected
inputs, outputs, states, interfaces, evidence, dependencies,
permissions, and governance controls; it shall not silently expand the
frozen project goal or scope. Inputs Approved Topic 12 requirements,
upstream validated state, configuration, schemas, relevant evidence, and
authorized governance decisions required for Opportunity Identification.
Input Source Controlled SRS repository, approved upstream topic
interfaces, versioned configuration/state stores, QA evidence, audit
records, and authorized change records. Processing / Method / Rules Use
explicit versioned rules for Opportunity Identification; validate inputs
before use; preserve identifiers, timestamps, versions, provenance,
authority, and state lineage; reject ambiguity rather than infer missing
intent; record material transitions. Outputs Validated Opportunity
Identification state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.5 is
finalized. Dependencies Topic 12 parent and adjacent controls, plus the
approved upstream contracts relevant to Opportunity Identification.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Identification may run in parallel after governing contracts
and versions are frozen. Parallelization Restrictions Parallel workers
shall not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.5, versioned schemas/configuration,
deterministic validation, structured state transitions,
correlation/trace IDs, and idempotent processing where repeat execution
is possible. Tools / Resources Approved source repository, requirements
registry, version control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity
Identification consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Identification is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.5. Testing Requirements
Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.5 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Identification is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.5 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.5 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 464 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Rationale / Assumptions The frozen
hierarchy and approved project constraints are authoritative. This item
must be implementable without hidden assumptions; where source detail is
not explicit, the implementation shall use the controlled project
governance process rather than invent authority. Verification Method
Inspect the generated specification against the authoritative hierarchy,
execute mapped tests and negative cases, verify evidence/traceability,
and confirm no prohibited scope or authority change for 12.5. 12.5.1 ---
Detection Signals Field Specification Purpose Define and control
Detection Signals as an explicit part of Topic 12 --- Opportunity
Discovery Engine. Objective Make Detection Signals unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall compute or evaluate deterministically and
explainably Detection Signals as a version-controlled, testable control
within Topic 12, consistent with the approved project goal, PoV, scope,
safety rules, and upstream/downstream contracts. Opportunity discovery
shall identify short-term India/INR opportunities from validated market,
news, financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Detection Signals, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Detection Signals. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Detection Signals;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Detection Signals state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.5 shall be defined and validated before
12.5.1 is finalized. Dependencies Topic 12 parent and adjacent controls,
plus the approved upstream contracts relevant to Detection Signals.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Detection Signals may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.5.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Detection Signals consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Detection Signals is missing, stale,
contradictory, or invalid. Unblocking Conditions Supply or restore the
missing/invalid prerequisite, reconcile conflicting state, obtain
required approval, and rerun all affected validation before resuming
dependent work. Human Escalation Escalate material safety, governance,
security, scope, goal, unresolved ambiguity, repeated recovery failure,
or approval-required conditions to authorized human governance; routine
non-blocking issues remain automated. Validation Method Validate
hierarchy/ID, schema, business/control rules, dependencies, state
transitions, provenance, authorization, evidence completeness, and
cross-topic consistency for 12.5.1. Testing Requirements Unit,
component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.5.1 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Detection Signals is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.5.1 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.5.1 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.5.1.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 465 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy 12.5.2 --- Detection Conditions Field Specification Purpose
Define and control Detection Conditions as an explicit part of Topic 12
--- Opportunity Discovery Engine. Objective Make Detection Conditions
unambiguous, deterministic where applicable, testable, traceable, and
usable by implementation agents and runtime components without hidden
assumptions. Requirement The system shall compute or evaluate
deterministically and explainably Detection Conditions as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Detection Conditions,
its directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Detection Conditions. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Detection Conditions;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Detection Conditions state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.5 shall be defined and validated before
12.5.2 is finalized. Dependencies Topic 12 parent and adjacent controls,
plus the approved upstream contracts relevant to Detection Conditions.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Detection Conditions may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.5.2, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Detection Conditions consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Detection Conditions is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.5.2. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.5.2 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Detection Conditions is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.5.2 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.5.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.5.2. 12.6 --- Opportunity
Filtering Field Specification Purpose Define and control Opportunity
Filtering as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Filtering unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 466 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Requirement The system shall define and
enforce Opportunity Filtering as a version-controlled, testable control
within Topic 12, consistent with the approved project goal, PoV, scope,
safety rules, and upstream/downstream contracts. Opportunity discovery
shall identify short-term India/INR opportunities from validated market,
news, financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Filtering,
its directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Filtering. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Opportunity Filtering;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Opportunity Filtering state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.6 is
finalized. Dependencies Topic 12 parent and adjacent controls, plus the
approved upstream contracts relevant to Opportunity Filtering.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Filtering may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.6, versioned schemas/configuration,
deterministic validation, structured state transitions,
correlation/trace IDs, and idempotent processing where repeat execution
is possible. Tools / Resources Approved source repository, requirements
registry, version control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Filtering
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for
Opportunity Filtering is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.6. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.6 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Opportunity Filtering is
incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance. Audit / Traceability Every material
event for 12.6 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.6
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.6. 12.6.1 --- Hard Filters Field Specification Purpose
Define and control Hard Filters as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Hard Filters unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Hard Filters as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 467 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Scope Applies to Hard Filters, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for Hard
Filters. Input Source Controlled SRS repository, approved upstream topic
interfaces, versioned configuration/state stores, QA evidence, audit
records, and authorized change records. Processing / Method / Rules Use
explicit versioned rules for Hard Filters; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Hard Filters
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12.6 shall be
defined and validated before 12.6.1 is finalized. Dependencies Topic 12
parent and adjacent controls, plus the approved upstream contracts
relevant to Hard Filters. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Hard Filters may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.6.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process Hard
Filters consistently for the same validated inputs and configuration,
expose its state and evidence, and fail closed when required safety,
authority, or integrity conditions are not satisfied. Error Handling
Classify errors, preserve evidence, retry only when the error is
explicitly recoverable, use an approved fallback when available,
transition to a safe state when correctness is uncertain, and escalate
material failures. Blocked-State Conditions Blocked when required
inputs, parent state, dependency, approval, schema, evidence, authority,
or validation result for Hard Filters is missing, stale, contradictory,
or invalid. Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.6.1. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.6.1 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Hard Filters is incomplete,
ambiguous, unverifiable, inconsistent with governing requirements,
unsafe, unauthorized, materially untraceable, or based on invalid/stale
data. Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.6.1 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.6.1 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.6.1. 12.6.2 --- Soft Filters
Field Specification Purpose Define and control Soft Filters as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Soft Filters unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall define and
enforce Soft Filters as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Soft Filters, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for Soft
Filters.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 468 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for Soft
Filters; validate inputs before use; preserve identifiers, timestamps,
versions, provenance, authority, and state lineage; reject ambiguity
rather than infer missing intent; record material transitions. Outputs
Validated Soft Filters state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.6 shall be defined and validated before
12.6.2 is finalized. Dependencies Topic 12 parent and adjacent controls,
plus the approved upstream contracts relevant to Soft Filters.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Soft Filters may run in parallel after governing contracts and versions
are frozen. Parallelization Restrictions Parallel workers shall not
create conflicting authoritative state, bypass approval/safety gates,
alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.6.2, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process Soft
Filters consistently for the same validated inputs and configuration,
expose its state and evidence, and fail closed when required safety,
authority, or integrity conditions are not satisfied. Error Handling
Classify errors, preserve evidence, retry only when the error is
explicitly recoverable, use an approved fallback when available,
transition to a safe state when correctness is uncertain, and escalate
material failures. Blocked-State Conditions Blocked when required
inputs, parent state, dependency, approval, schema, evidence, authority,
or validation result for Soft Filters is missing, stale, contradictory,
or invalid. Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.6.2. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.6.2 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Soft Filters is incomplete,
ambiguous, unverifiable, inconsistent with governing requirements,
unsafe, unauthorized, materially untraceable, or based on invalid/stale
data. Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.6.2 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.6.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.6.2. 12.7 --- Short-Term
Opportunity Detection Field Specification Purpose Define and control
Short-Term Opportunity Detection as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Short-Term Opportunity
Detection unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall compute or
evaluate deterministically and explainably Short-Term Opportunity
Detection as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Short-Term Opportunity
Detection, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Short-Term Opportunity Detection. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Short-Term Opportunity Detection; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 469 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Outputs Validated Short-Term Opportunity
Detection state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.7 is
finalized. Dependencies Topic 12 parent and adjacent controls, plus the
approved upstream contracts relevant to Short-Term Opportunity
Detection. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Short-Term Opportunity Detection may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.7, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Short-Term Opportunity Detection consistently for the same validated
inputs and configuration, expose its state and evidence, and fail closed
when required safety, authority, or integrity conditions are not
satisfied. Error Handling Classify errors, preserve evidence, retry only
when the error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Short-Term Opportunity Detection is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.7. Testing Requirements
Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.7 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Short-Term Opportunity Detection is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.7 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.7 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.7. 12.8 --- Market Event
Detection Field Specification Purpose Define and control Market Event
Detection as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Market Event Detection unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall compute or evaluate deterministically and explainably
Market Event Detection as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Market Event Detection,
its directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Market Event Detection. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Market Event Detection;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Market Event Detection state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 470 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.8 is finalized. Dependencies Topic 12 parent and
adjacent controls, plus the approved upstream contracts relevant to
Market Event Detection. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Market Event Detection may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.8, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Market Event Detection consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Market Event Detection is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.8. Testing Requirements
Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.8 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Market Event Detection is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.8 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.8 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.8. 12.9 --- News-Driven
Opportunity Detection Field Specification Purpose Define and control
News-Driven Opportunity Detection as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make News-Driven Opportunity
Detection unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall compute or
evaluate deterministically and explainably News-Driven Opportunity
Detection as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to News-Driven Opportunity
Detection, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
News-Driven Opportunity Detection. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for News-Driven Opportunity Detection; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated News-Driven Opportunity
Detection state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.9 is
finalized. Dependencies Topic 12 parent and adjacent controls, plus the
approved upstream contracts relevant to News-Driven Opportunity
Detection.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 471 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for News-Driven Opportunity Detection may run in
parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.9, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process News-Driven Opportunity
Detection consistently for the same validated inputs and configuration,
expose its state and evidence, and fail closed when required safety,
authority, or integrity conditions are not satisfied. Error Handling
Classify errors, preserve evidence, retry only when the error is
explicitly recoverable, use an approved fallback when available,
transition to a safe state when correctness is uncertain, and escalate
material failures. Blocked-State Conditions Blocked when required
inputs, parent state, dependency, approval, schema, evidence, authority,
or validation result for News-Driven Opportunity Detection is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.9. Testing Requirements
Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.9 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when News-Driven Opportunity Detection is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.9 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.9 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.9. 12.10 --- Price-Movement
Detection Field Specification Purpose Define and control Price-Movement
Detection as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Price-Movement Detection unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall compute or evaluate deterministically and
explainably Price-Movement Detection as a version-controlled, testable
control within Topic 12, consistent with the approved project goal, PoV,
scope, safety rules, and upstream/downstream contracts. Opportunity
discovery shall identify short-term India/INR opportunities from
validated market, news, financial, economic, and approved alternative
data while applying hard/soft filters, evidence requirements, expiry,
risk pre-filtering, confidence, and deduplication. Scope Applies to
Price-Movement Detection, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Price-Movement Detection. Input Source Controlled
SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Price-Movement Detection; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Price-Movement Detection
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.10 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Price-Movement Detection. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Price-Movement Detection may run in parallel
after governing contracts and versions are frozen.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 472 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.10, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Price-Movement Detection consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Price-Movement Detection is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.10. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.10 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Price-Movement Detection is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.10 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.10 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.10. 12.11 --- Volume-Based
Opportunity Detection Field Specification Purpose Define and control
Volume-Based Opportunity Detection as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Volume-Based Opportunity
Detection unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall compute or
evaluate deterministically and explainably Volume-Based Opportunity
Detection as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Volume-Based Opportunity
Detection, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Volume-Based Opportunity Detection. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Volume-Based Opportunity Detection; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Volume-Based Opportunity
Detection state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.11
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Volume-Based Opportunity
Detection. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Volume-Based Opportunity Detection may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.11, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 473 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Volume-Based Opportunity Detection consistently for the same validated
inputs and configuration, expose its state and evidence, and fail closed
when required safety, authority, or integrity conditions are not
satisfied. Error Handling Classify errors, preserve evidence, retry only
when the error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Volume-Based Opportunity Detection
is missing, stale, contradictory, or invalid. Unblocking Conditions
Supply or restore the missing/invalid prerequisite, reconcile
conflicting state, obtain required approval, and rerun all affected
validation before resuming dependent work. Human Escalation Escalate
material safety, governance, security, scope, goal, unresolved
ambiguity, repeated recovery failure, or approval-required conditions to
authorized human governance; routine non-blocking issues remain
automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.11. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.11 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Volume-Based Opportunity
Detection is incomplete, ambiguous, unverifiable, inconsistent with
governing requirements, unsafe, unauthorized, materially untraceable, or
based on invalid/stale data. Recovery / Corrective Action Restore the
last known valid state, preserve evidence, isolate the fault, correct
through controlled change, rerun impacted tests/validation, and
reconcile downstream state before acceptance. Audit / Traceability Every
material event for 12.11 shall record requirement ID, version,
actor/component, timestamp, input/output references, decision/state,
evidence, test result, and change linkage. Change Control Material
changes to 12.11 shall follow Topic 27 governance/change control:
request → impact/risk assessment → authorized approval → implementation
→ validation → version/baseline update → audit evidence. Rationale /
Assumptions The frozen hierarchy and approved project constraints are
authoritative. This item must be implementable without hidden
assumptions; where source detail is not explicit, the implementation
shall use the controlled project governance process rather than invent
authority. Verification Method Inspect the generated specification
against the authoritative hierarchy, execute mapped tests and negative
cases, verify evidence/traceability, and confirm no prohibited scope or
authority change for 12.11. 12.12 --- Volatility-Based Opportunity
Detection Field Specification Purpose Define and control
Volatility-Based Opportunity Detection as an explicit part of Topic 12
--- Opportunity Discovery Engine. Objective Make Volatility-Based
Opportunity Detection unambiguous, deterministic where applicable,
testable, traceable, and usable by implementation agents and runtime
components without hidden assumptions. Requirement The system shall
compute or evaluate deterministically and explainably Volatility-Based
Opportunity Detection as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Volatility-Based
Opportunity Detection, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Volatility-Based Opportunity Detection. Input
Source Controlled SRS repository, approved upstream topic interfaces,
versioned configuration/state stores, QA evidence, audit records, and
authorized change records. Processing / Method / Rules Use explicit
versioned rules for Volatility-Based Opportunity Detection; validate
inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Volatility-Based Opportunity Detection state/specification, decision or
control result where applicable, validation status, evidence references,
and trace information. Output Destination Controlled SRS/requirements
registry, owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.12
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Volatility-Based Opportunity
Detection. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Volatility-Based Opportunity Detection may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.12, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 474 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Volatility-Based Opportunity Detection consistently for the same
validated inputs and configuration, expose its state and evidence, and
fail closed when required safety, authority, or integrity conditions are
not satisfied. Error Handling Classify errors, preserve evidence, retry
only when the error is explicitly recoverable, use an approved fallback
when available, transition to a safe state when correctness is
uncertain, and escalate material failures. Blocked-State Conditions
Blocked when required inputs, parent state, dependency, approval,
schema, evidence, authority, or validation result for Volatility-Based
Opportunity Detection is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.12. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.12 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Volatility-Based Opportunity
Detection is incomplete, ambiguous, unverifiable, inconsistent with
governing requirements, unsafe, unauthorized, materially untraceable, or
based on invalid/stale data. Recovery / Corrective Action Restore the
last known valid state, preserve evidence, isolate the fault, correct
through controlled change, rerun impacted tests/validation, and
reconcile downstream state before acceptance. Audit / Traceability Every
material event for 12.12 shall record requirement ID, version,
actor/component, timestamp, input/output references, decision/state,
evidence, test result, and change linkage. Change Control Material
changes to 12.12 shall follow Topic 27 governance/change control:
request → impact/risk assessment → authorized approval → implementation
→ validation → version/baseline update → audit evidence. Rationale /
Assumptions The frozen hierarchy and approved project constraints are
authoritative. This item must be implementable without hidden
assumptions; where source detail is not explicit, the implementation
shall use the controlled project governance process rather than invent
authority. Verification Method Inspect the generated specification
against the authoritative hierarchy, execute mapped tests and negative
cases, verify evidence/traceability, and confirm no prohibited scope or
authority change for 12.12. 12.13 --- Liquidity Filtering Field
Specification Purpose Define and control Liquidity Filtering as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Liquidity Filtering unambiguous, deterministic where applicable,
testable, traceable, and usable by implementation agents and runtime
components without hidden assumptions. Requirement The system shall
define and enforce Liquidity Filtering as a version-controlled, testable
control within Topic 12, consistent with the approved project goal, PoV,
scope, safety rules, and upstream/downstream contracts. Opportunity
discovery shall identify short-term India/INR opportunities from
validated market, news, financial, economic, and approved alternative
data while applying hard/soft filters, evidence requirements, expiry,
risk pre-filtering, confidence, and deduplication. Scope Applies to
Liquidity Filtering, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Liquidity Filtering. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Liquidity Filtering; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Liquidity Filtering
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.13 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Liquidity Filtering. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Liquidity Filtering may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.13, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Liquidity Filtering consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 475 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Error Handling Classify errors, preserve
evidence, retry only when the error is explicitly recoverable, use an
approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for
Liquidity Filtering is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.13. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.13 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Liquidity Filtering is
incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance. Audit / Traceability Every material
event for 12.13 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.13
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.13. 12.14 --- Opportunity Qualification Field
Specification Purpose Define and control Opportunity Qualification as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Opportunity Qualification unambiguous, deterministic where
applicable, testable, traceable, and usable by implementation agents and
runtime components without hidden assumptions. Requirement The system
shall define and enforce Opportunity Qualification as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity
Qualification, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Opportunity Qualification. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Qualification; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Qualification
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.14 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Qualification. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Qualification may run in parallel
after governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.14, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Qualification consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Qualification is
missing, stale, contradictory, or invalid.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 476 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Unblocking Conditions Supply or restore
the missing/invalid prerequisite, reconcile conflicting state, obtain
required approval, and rerun all affected validation before resuming
dependent work. Human Escalation Escalate material safety, governance,
security, scope, goal, unresolved ambiguity, repeated recovery failure,
or approval-required conditions to authorized human governance; routine
non-blocking issues remain automated. Validation Method Validate
hierarchy/ID, schema, business/control rules, dependencies, state
transitions, provenance, authorization, evidence completeness, and
cross-topic consistency for 12.14. Testing Requirements Unit, component,
contract, integration, negative, boundary, concurrency/idempotency,
failure/recovery, audit-traceability, and regression tests shall cover
applicable behaviours. Evidence Required Input snapshots/references,
output state, version, rule/configuration version, execution/trace ID,
validation results, test results, errors/recovery records, and
approval/change evidence where applicable. Acceptance Criteria 12.14 is
accepted only when the specified behaviour is implemented, validated,
traceable, test-covered, within scope, and free of unresolved blocking
defects. Failure / Rejection Criteria Reject when Opportunity
Qualification is incomplete, ambiguous, unverifiable, inconsistent with
governing requirements, unsafe, unauthorized, materially untraceable, or
based on invalid/stale data. Recovery / Corrective Action Restore the
last known valid state, preserve evidence, isolate the fault, correct
through controlled change, rerun impacted tests/validation, and
reconcile downstream state before acceptance. Audit / Traceability Every
material event for 12.14 shall record requirement ID, version,
actor/component, timestamp, input/output references, decision/state,
evidence, test result, and change linkage. Change Control Material
changes to 12.14 shall follow Topic 27 governance/change control:
request → impact/risk assessment → authorized approval → implementation
→ validation → version/baseline update → audit evidence. Rationale /
Assumptions The frozen hierarchy and approved project constraints are
authoritative. This item must be implementable without hidden
assumptions; where source detail is not explicit, the implementation
shall use the controlled project governance process rather than invent
authority. Verification Method Inspect the generated specification
against the authoritative hierarchy, execute mapped tests and negative
cases, verify evidence/traceability, and confirm no prohibited scope or
authority change for 12.14. 12.14.1 --- Qualification Criteria Field
Specification Purpose Define and control Qualification Criteria as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Qualification Criteria unambiguous, deterministic where applicable,
testable, traceable, and usable by implementation agents and runtime
components without hidden assumptions. Requirement The system shall
define and enforce Qualification Criteria as a version-controlled,
testable control within Topic 12, consistent with the approved project
goal, PoV, scope, safety rules, and upstream/downstream contracts.
Opportunity discovery shall identify short-term India/INR opportunities
from validated market, news, financial, economic, and approved
alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Scope Applies to Qualification Criteria, its directly affected inputs,
outputs, states, interfaces, evidence, dependencies, permissions, and
governance controls; it shall not silently expand the frozen project
goal or scope. Inputs Approved Topic 12 requirements, upstream validated
state, configuration, schemas, relevant evidence, and authorized
governance decisions required for Qualification Criteria. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Qualification Criteria; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Qualification Criteria
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12.14 shall be
defined and validated before 12.14.1 is finalized. Dependencies Topic 12
parent and adjacent controls, plus the approved upstream contracts
relevant to Qualification Criteria. Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Qualification Criteria may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.14.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Qualification Criteria consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Qualification Criteria is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 477 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Validation Method Validate hierarchy/ID,
schema, business/control rules, dependencies, state transitions,
provenance, authorization, evidence completeness, and cross-topic
consistency for 12.14.1. Testing Requirements Unit, component, contract,
integration, negative, boundary, concurrency/idempotency,
failure/recovery, audit-traceability, and regression tests shall cover
applicable behaviours. Evidence Required Input snapshots/references,
output state, version, rule/configuration version, execution/trace ID,
validation results, test results, errors/recovery records, and
approval/change evidence where applicable. Acceptance Criteria 12.14.1
is accepted only when the specified behaviour is implemented, validated,
traceable, test-covered, within scope, and free of unresolved blocking
defects. Failure / Rejection Criteria Reject when Qualification Criteria
is incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance. Audit / Traceability Every material
event for 12.14.1 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.14.1
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.14.1. 12.14.2 --- Disqualification Criteria Field
Specification Purpose Define and control Disqualification Criteria as an
explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make Disqualification Criteria unambiguous, deterministic where
applicable, testable, traceable, and usable by implementation agents and
runtime components without hidden assumptions. Requirement The system
shall define and enforce Disqualification Criteria as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Disqualification
Criteria, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Disqualification Criteria. Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for
Disqualification Criteria; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Disqualification Criteria
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12.14 shall be
defined and validated before 12.14.2 is finalized. Dependencies Topic 12
parent and adjacent controls, plus the approved upstream contracts
relevant to Disqualification Criteria. Dependency Type Blocking where
goal, safety, authority, data integrity, schema, or governance
correctness is material; otherwise downstream/read-only. Parallelization
Eligibility Independent design, test preparation, evidence-template
work, and read-only analysis for Disqualification Criteria may run in
parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.14.2, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Disqualification Criteria
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for
Disqualification Criteria is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.14.2. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 478 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Evidence Required Input
snapshots/references, output state, version, rule/configuration version,
execution/trace ID, validation results, test results, errors/recovery
records, and approval/change evidence where applicable. Acceptance
Criteria 12.14.2 is accepted only when the specified behaviour is
implemented, validated, traceable, test-covered, within scope, and free
of unresolved blocking defects. Failure / Rejection Criteria Reject when
Disqualification Criteria is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.14.2 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.14.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.14.2. 12.15 --- Opportunity
Ranking Field Specification Purpose Define and control Opportunity
Ranking as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Ranking unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall compute or evaluate deterministically and explainably
Opportunity Ranking as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Ranking, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Ranking. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Opportunity Ranking;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Opportunity Ranking state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.15
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Opportunity Ranking.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Ranking may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.15, versioned schemas/configuration,
deterministic validation, structured state transitions,
correlation/trace IDs, and idempotent processing where repeat execution
is possible. Tools / Resources Approved source repository, requirements
registry, version control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Ranking
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for
Opportunity Ranking is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.15. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.15 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 479 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Failure / Rejection Criteria Reject when
Opportunity Ranking is incomplete, ambiguous, unverifiable, inconsistent
with governing requirements, unsafe, unauthorized, materially
untraceable, or based on invalid/stale data. Recovery / Corrective
Action Restore the last known valid state, preserve evidence, isolate
the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.15 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.15 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.15. 12.16 --- Opportunity
Deduplication Field Specification Purpose Define and control Opportunity
Deduplication as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Deduplication unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Opportunity
Deduplication as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity
Deduplication, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Opportunity Deduplication. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Deduplication; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Deduplication
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.16 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Deduplication. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Deduplication may run in parallel
after governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.16, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Deduplication consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Deduplication is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.16. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.16 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Deduplication is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 480 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Audit / Traceability Every material event
for 12.16 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.16
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.16. 12.17 --- Opportunity Evidence Collection Field
Specification Purpose Define and control Opportunity Evidence Collection
as an explicit part of Topic 12 --- Opportunity Discovery Engine.
Objective Make Opportunity Evidence Collection unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Opportunity Evidence
Collection as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Evidence
Collection, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Evidence Collection. Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for Opportunity
Evidence Collection; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated Opportunity Evidence Collection state/specification,
decision or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.17
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Opportunity Evidence
Collection. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Evidence Collection may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.17, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Evidence Collection consistently for the same validated
inputs and configuration, expose its state and evidence, and fail closed
when required safety, authority, or integrity conditions are not
satisfied. Error Handling Classify errors, preserve evidence, retry only
when the error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Evidence Collection is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.17. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.17 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Evidence Collection is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.17 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.17 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 481 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Rationale / Assumptions The frozen
hierarchy and approved project constraints are authoritative. This item
must be implementable without hidden assumptions; where source detail is
not explicit, the implementation shall use the controlled project
governance process rather than invent authority. Verification Method
Inspect the generated specification against the authoritative hierarchy,
execute mapped tests and negative cases, verify evidence/traceability,
and confirm no prohibited scope or authority change for 12.17. 12.17.1
--- Required Evidence Field Specification Purpose Define and control
Required Evidence as an explicit part of Topic 12 --- Opportunity
Discovery Engine. Objective Make Required Evidence unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Required Evidence as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Required Evidence, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Required Evidence. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Required Evidence;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Required Evidence state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.17 shall be defined and validated before
12.17.1 is finalized. Dependencies Topic 12 parent and adjacent
controls, plus the approved upstream contracts relevant to Required
Evidence. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Required Evidence may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.17.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Required Evidence consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Required Evidence is missing, stale,
contradictory, or invalid. Unblocking Conditions Supply or restore the
missing/invalid prerequisite, reconcile conflicting state, obtain
required approval, and rerun all affected validation before resuming
dependent work. Human Escalation Escalate material safety, governance,
security, scope, goal, unresolved ambiguity, repeated recovery failure,
or approval-required conditions to authorized human governance; routine
non-blocking issues remain automated. Validation Method Validate
hierarchy/ID, schema, business/control rules, dependencies, state
transitions, provenance, authorization, evidence completeness, and
cross-topic consistency for 12.17.1. Testing Requirements Unit,
component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.17.1 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when Required Evidence is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.17.1 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.17.1 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.17.1.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 482 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy 12.17.2 --- Evidence Freshness Field Specification Purpose
Define and control Evidence Freshness as an explicit part of Topic 12
--- Opportunity Discovery Engine. Objective Make Evidence Freshness
unambiguous, deterministic where applicable, testable, traceable, and
usable by implementation agents and runtime components without hidden
assumptions. Requirement The system shall define and enforce Evidence
Freshness as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Evidence Freshness, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Evidence Freshness. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Evidence Freshness;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Evidence Freshness state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.17 shall be defined and validated before
12.17.2 is finalized. Dependencies Topic 12 parent and adjacent
controls, plus the approved upstream contracts relevant to Evidence
Freshness. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Evidence Freshness may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.17.2, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Evidence Freshness consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Evidence Freshness is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.17.2. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.17.2 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when Evidence Freshness is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.17.2 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.17.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.17.2. 12.18 --- Opportunity
Confidence Score Field Specification Purpose Define and control
Opportunity Confidence Score as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Opportunity Confidence
Score unambiguous, deterministic where applicable, testable, traceable,
and usable by implementation agents and runtime components without
hidden assumptions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 483 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Requirement The system shall define and
enforce Opportunity Confidence Score as a version-controlled, testable
control within Topic 12, consistent with the approved project goal, PoV,
scope, safety rules, and upstream/downstream contracts. Opportunity
discovery shall identify short-term India/INR opportunities from
validated market, news, financial, economic, and approved alternative
data while applying hard/soft filters, evidence requirements, expiry,
risk pre-filtering, confidence, and deduplication. Scope Applies to
Opportunity Confidence Score, its directly affected inputs, outputs,
states, interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Opportunity Confidence Score. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Confidence Score; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Confidence Score
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.18 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Confidence Score. Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Confidence Score may run in parallel
after governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.18, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Confidence Score consistently for the same validated inputs
and configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Confidence Score is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.18. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.18 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Confidence Score is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.18 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.18 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.18. 12.18.1 --- Confidence
Inputs Field Specification Purpose Define and control Confidence Inputs
as an explicit part of Topic 12 --- Opportunity Discovery Engine.
Objective Make Confidence Inputs unambiguous, deterministic where
applicable, testable, traceable, and usable by implementation agents and
runtime components without hidden assumptions. Requirement The system
shall specify, validate, and exchange Confidence Inputs as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 484 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Scope Applies to Confidence Inputs, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Confidence Inputs. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Confidence Inputs;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Confidence Inputs state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.18 shall be defined and validated before
12.18.1 is finalized. Dependencies Topic 12 parent and adjacent
controls, plus the approved upstream contracts relevant to Confidence
Inputs. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Confidence Inputs may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.18.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Confidence Inputs consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Confidence Inputs is missing, stale,
contradictory, or invalid. Unblocking Conditions Supply or restore the
missing/invalid prerequisite, reconcile conflicting state, obtain
required approval, and rerun all affected validation before resuming
dependent work. Human Escalation Escalate material safety, governance,
security, scope, goal, unresolved ambiguity, repeated recovery failure,
or approval-required conditions to authorized human governance; routine
non-blocking issues remain automated. Validation Method Validate
hierarchy/ID, schema, business/control rules, dependencies, state
transitions, provenance, authorization, evidence completeness, and
cross-topic consistency for 12.18.1. Testing Requirements Unit,
component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.18.1 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when Confidence Inputs is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.18.1 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.18.1 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.18.1. 12.18.2 --- Confidence
Threshold Field Specification Purpose Define and control Confidence
Threshold as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Confidence Threshold unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall define and enforce Confidence Threshold as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Confidence Threshold,
its directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Confidence Threshold.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 485 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for Confidence
Threshold; validate inputs before use; preserve identifiers, timestamps,
versions, provenance, authority, and state lineage; reject ambiguity
rather than infer missing intent; record material transitions. Outputs
Validated Confidence Threshold state/specification, decision or control
result where applicable, validation status, evidence references, and
trace information. Output Destination Controlled SRS/requirements
registry, owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.18 shall be defined and validated before
12.18.2 is finalized. Dependencies Topic 12 parent and adjacent
controls, plus the approved upstream contracts relevant to Confidence
Threshold. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Confidence Threshold may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.18.2, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Confidence Threshold consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Confidence Threshold is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.18.2. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.18.2 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when Confidence Threshold is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.18.2 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.18.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.18.2. 12.19 --- Opportunity
Expiry Field Specification Purpose Define and control Opportunity Expiry
as an explicit part of Topic 12 --- Opportunity Discovery Engine.
Objective Make Opportunity Expiry unambiguous, deterministic where
applicable, testable, traceable, and usable by implementation agents and
runtime components without hidden assumptions. Requirement The system
shall define and enforce Opportunity Expiry as a version-controlled,
testable control within Topic 12, consistent with the approved project
goal, PoV, scope, safety rules, and upstream/downstream contracts.
Opportunity discovery shall identify short-term India/INR opportunities
from validated market, news, financial, economic, and approved
alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Scope Applies to Opportunity Expiry, its directly affected inputs,
outputs, states, interfaces, evidence, dependencies, permissions, and
governance controls; it shall not silently expand the frozen project
goal or scope. Inputs Approved Topic 12 requirements, upstream validated
state, configuration, schemas, relevant evidence, and authorized
governance decisions required for Opportunity Expiry. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Expiry; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 486 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Outputs Validated Opportunity Expiry
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.19 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Expiry. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Expiry may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.19, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Expiry consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Expiry is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.19. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.19 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Expiry is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.19 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.19 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.19. 12.19.1 --- Expiry
Conditions Field Specification Purpose Define and control Expiry
Conditions as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Expiry Conditions unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall define and enforce Expiry Conditions as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Expiry Conditions, its
directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Expiry Conditions. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Expiry Conditions;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Expiry Conditions state/specification, decision or control result where
applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 487 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12.19 shall be
defined and validated before 12.19.1 is finalized. Dependencies Topic 12
parent and adjacent controls, plus the approved upstream contracts
relevant to Expiry Conditions. Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Expiry Conditions may run in parallel after
governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state. Technical
Details Use stable machine-readable identifiers for 12.19.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Expiry Conditions consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Expiry Conditions is missing, stale,
contradictory, or invalid. Unblocking Conditions Supply or restore the
missing/invalid prerequisite, reconcile conflicting state, obtain
required approval, and rerun all affected validation before resuming
dependent work. Human Escalation Escalate material safety, governance,
security, scope, goal, unresolved ambiguity, repeated recovery failure,
or approval-required conditions to authorized human governance; routine
non-blocking issues remain automated. Validation Method Validate
hierarchy/ID, schema, business/control rules, dependencies, state
transitions, provenance, authorization, evidence completeness, and
cross-topic consistency for 12.19.1. Testing Requirements Unit,
component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.19.1 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when Expiry Conditions is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.19.1 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.19.1 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.19.1. 12.19.2 --- Expired
Opportunity Handling Field Specification Purpose Define and control
Expired Opportunity Handling as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Expired Opportunity
Handling unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall define and
enforce Expired Opportunity Handling as a version-controlled, testable
control within Topic 12, consistent with the approved project goal, PoV,
scope, safety rules, and upstream/downstream contracts. Opportunity
discovery shall identify short-term India/INR opportunities from
validated market, news, financial, economic, and approved alternative
data while applying hard/soft filters, evidence requirements, expiry,
risk pre-filtering, confidence, and deduplication. Scope Applies to
Expired Opportunity Handling, its directly affected inputs, outputs,
states, interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Expired Opportunity Handling. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Expired Opportunity Handling; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Expired Opportunity Handling
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12.19 shall be
defined and validated before 12.19.2 is finalized. Dependencies Topic 12
parent and adjacent controls, plus the approved upstream contracts
relevant to Expired Opportunity Handling. Dependency Type Blocking where
goal, safety, authority, data integrity, schema, or governance
correctness is material; otherwise downstream/read-only.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 488 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Parallelization Eligibility Independent
design, test preparation, evidence-template work, and read-only analysis
for Expired Opportunity Handling may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.19.2, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Expired Opportunity Handling consistently for the same validated inputs
and configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Expired Opportunity Handling is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.19.2. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.19.2 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when Expired Opportunity Handling is incomplete,
ambiguous, unverifiable, inconsistent with governing requirements,
unsafe, unauthorized, materially untraceable, or based on invalid/stale
data. Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.19.2 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.19.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.19.2. 12.20 --- Opportunity
Re-Evaluation Field Specification Purpose Define and control Opportunity
Re-Evaluation as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Re-Evaluation unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall define and enforce Opportunity
Re-Evaluation as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity
Re-Evaluation, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Opportunity Re-Evaluation. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Re-Evaluation; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Re-Evaluation
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.20 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Re-Evaluation. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Re-Evaluation may run in parallel
after governing contracts and versions are frozen. Parallelization
Restrictions Parallel workers shall not create conflicting authoritative
state, bypass approval/safety gates, alter locked baselines, duplicate
unique identifiers, or consume unvalidated upstream state.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 489 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Technical Details Use stable
machine-readable identifiers for 12.20, versioned schemas/configuration,
deterministic validation, structured state transitions,
correlation/trace IDs, and idempotent processing where repeat execution
is possible. Tools / Resources Approved source repository, requirements
registry, version control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Re-Evaluation
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for
Opportunity Re-Evaluation is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.20. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.20 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Opportunity Re-Evaluation is
incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance. Audit / Traceability Every material
event for 12.20 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.20
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.20. 12.21 --- False Opportunity Detection Field
Specification Purpose Define and control False Opportunity Detection as
an explicit part of Topic 12 --- Opportunity Discovery Engine. Objective
Make False Opportunity Detection unambiguous, deterministic where
applicable, testable, traceable, and usable by implementation agents and
runtime components without hidden assumptions. Requirement The system
shall compute or evaluate deterministically and explainably False
Opportunity Detection as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to False Opportunity
Detection, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
False Opportunity Detection. Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for False
Opportunity Detection; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated False Opportunity Detection state/specification,
decision or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.21
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to False Opportunity Detection.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
False Opportunity Detection may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.21, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 490 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
False Opportunity Detection consistently for the same validated inputs
and configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for False Opportunity Detection is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.21. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.21 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when False Opportunity Detection is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.21 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.21 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.21. 12.21.1 --- False Signal
Detection Field Specification Purpose Define and control False Signal
Detection as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make False Signal Detection unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall compute or evaluate deterministically and explainably
False Signal Detection as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to False Signal Detection,
its directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
False Signal Detection. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for False Signal Detection;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
False Signal Detection state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12.21 shall be defined and validated before
12.21.1 is finalized. Dependencies Topic 12 parent and adjacent
controls, plus the approved upstream contracts relevant to False Signal
Detection. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
False Signal Detection may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.21.1, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 491 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Expected Behaviour The component shall
process False Signal Detection consistently for the same validated
inputs and configuration, expose its state and evidence, and fail closed
when required safety, authority, or integrity conditions are not
satisfied. Error Handling Classify errors, preserve evidence, retry only
when the error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for False Signal Detection is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.21.1. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.21.1 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when False Signal Detection is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.21.1 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.21.1 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.21.1. 12.21.2 --- False
Signal Classification Field Specification Purpose Define and control
False Signal Classification as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make False Signal Classification
unambiguous, deterministic where applicable, testable, traceable, and
usable by implementation agents and runtime components without hidden
assumptions. Requirement The system shall compute or evaluate
deterministically and explainably False Signal Classification as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to False Signal
Classification, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for False Signal Classification. Input Source
Controlled SRS repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for False Signal Classification; validate inputs before use; preserve
identifiers, timestamps, versions, provenance, authority, and state
lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated False Signal Classification
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12.21 shall be
defined and validated before 12.21.2 is finalized. Dependencies Topic 12
parent and adjacent controls, plus the approved upstream contracts
relevant to False Signal Classification. Dependency Type Blocking where
goal, safety, authority, data integrity, schema, or governance
correctness is material; otherwise downstream/read-only. Parallelization
Eligibility Independent design, test preparation, evidence-template
work, and read-only analysis for False Signal Classification may run in
parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.21.2, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process False Signal
Classification consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 492 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for False Signal Classification is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.21.2. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.21.2 is accepted only when the specified
behaviour is implemented, validated, traceable, test-covered, within
scope, and free of unresolved blocking defects. Failure / Rejection
Criteria Reject when False Signal Classification is incomplete,
ambiguous, unverifiable, inconsistent with governing requirements,
unsafe, unauthorized, materially untraceable, or based on invalid/stale
data. Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.21.2 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.21.2 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.21.2. 12.22 --- Opportunity
Risk Pre-Filter Field Specification Purpose Define and control
Opportunity Risk Pre-Filter as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Opportunity Risk Pre-Filter
unambiguous, deterministic where applicable, testable, traceable, and
usable by implementation agents and runtime components without hidden
assumptions. Requirement The system shall define and enforce Opportunity
Risk Pre-Filter as a version-controlled, testable control within Topic
12, consistent with the approved project goal, PoV, scope, safety rules,
and upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Risk
Pre-Filter, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Risk Pre-Filter. Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for Opportunity
Risk Pre-Filter; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated Opportunity Risk Pre-Filter state/specification,
decision or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA / Risk Agent Prerequisites 12 shall be defined and validated
before 12.22 is finalized. Dependencies Topic 12 parent and adjacent
controls, plus the approved upstream contracts relevant to Opportunity
Risk Pre-Filter. Dependency Type Blocking where goal, safety, authority,
data integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Risk Pre-Filter may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.22, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Risk Pre-Filter consistently for the same validated inputs
and configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Risk Pre-Filter is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 493 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.22. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.22 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Risk Pre-Filter is incomplete, ambiguous, unverifiable,
inconsistent with governing requirements, unsafe, unauthorized,
materially untraceable, or based on invalid/stale data. Recovery /
Corrective Action Restore the last known valid state, preserve evidence,
isolate the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.22 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.22 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.22. 12.23 --- Opportunity
Monitoring Field Specification Purpose Define and control Opportunity
Monitoring as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Monitoring unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall perform, record, and validate Opportunity Monitoring as
a version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Monitoring,
its directly affected inputs, outputs, states, interfaces, evidence,
dependencies, permissions, and governance controls; it shall not
silently expand the frozen project goal or scope. Inputs Approved Topic
12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Monitoring. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Opportunity Monitoring;
validate inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Opportunity Monitoring state/specification, decision or control result
where applicable, validation status, evidence references, and trace
information. Output Destination Controlled SRS/requirements registry,
owning component state store, QA evidence store,
dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.23
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Opportunity Monitoring.
Dependency Type Blocking where goal, safety, authority, data integrity,
schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Monitoring may run in parallel after governing contracts and
versions are frozen. Parallelization Restrictions Parallel workers shall
not create conflicting authoritative state, bypass approval/safety
gates, alter locked baselines, duplicate unique identifiers, or consume
unvalidated upstream state. Technical Details Use stable
machine-readable identifiers for 12.23, versioned schemas/configuration,
deterministic validation, structured state transitions,
correlation/trace IDs, and idempotent processing where repeat execution
is possible. Tools / Resources Approved source repository, requirements
registry, version control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Monitoring
consistently for the same validated inputs and configuration, expose its
state and evidence, and fail closed when required safety, authority, or
integrity conditions are not satisfied. Error Handling Classify errors,
preserve evidence, retry only when the error is explicitly recoverable,
use an approved fallback when available, transition to a safe state when
correctness is uncertain, and escalate material failures. Blocked-State
Conditions Blocked when required inputs, parent state, dependency,
approval, schema, evidence, authority, or validation result for
Opportunity Monitoring is missing, stale, contradictory, or invalid.
Unblocking Conditions Supply or restore the missing/invalid
prerequisite, reconcile conflicting state, obtain required approval, and
rerun all affected validation before resuming dependent work. Human
Escalation Escalate material safety, governance, security, scope, goal,
unresolved ambiguity, repeated recovery failure, or approval-required
conditions to authorized human governance; routine non-blocking issues
remain automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.23.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 494 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Testing Requirements Unit, component,
contract, integration, negative, boundary, concurrency/idempotency,
failure/recovery, audit-traceability, and regression tests shall cover
applicable behaviours. Evidence Required Input snapshots/references,
output state, version, rule/configuration version, execution/trace ID,
validation results, test results, errors/recovery records, and
approval/change evidence where applicable. Acceptance Criteria 12.23 is
accepted only when the specified behaviour is implemented, validated,
traceable, test-covered, within scope, and free of unresolved blocking
defects. Failure / Rejection Criteria Reject when Opportunity Monitoring
is incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance. Audit / Traceability Every material
event for 12.23 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.23
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.23. 12.24 --- Opportunity Discovery Testing Field
Specification Purpose Define and control Opportunity Discovery Testing
as an explicit part of Topic 12 --- Opportunity Discovery Engine.
Objective Make Opportunity Discovery Testing unambiguous, deterministic
where applicable, testable, traceable, and usable by implementation
agents and runtime components without hidden assumptions. Requirement
The system shall perform, record, and validate Opportunity Discovery
Testing as a version-controlled, testable control within Topic 12,
consistent with the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Discovery
Testing, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Discovery Testing. Input Source Controlled SRS repository,
approved upstream topic interfaces, versioned configuration/state
stores, QA evidence, audit records, and authorized change records.
Processing / Method / Rules Use explicit versioned rules for Opportunity
Discovery Testing; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated Opportunity Discovery Testing state/specification,
decision or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.24
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Opportunity Discovery
Testing. Dependency Type Blocking where goal, safety, authority, data
integrity, schema, or governance correctness is material; otherwise
downstream/read-only. Parallelization Eligibility Independent design,
test preparation, evidence-template work, and read-only analysis for
Opportunity Discovery Testing may run in parallel after governing
contracts and versions are frozen. Parallelization Restrictions Parallel
workers shall not create conflicting authoritative state, bypass
approval/safety gates, alter locked baselines, duplicate unique
identifiers, or consume unvalidated upstream state. Technical Details
Use stable machine-readable identifiers for 12.24, versioned
schemas/configuration, deterministic validation, structured state
transitions, correlation/trace IDs, and idempotent processing where
repeat execution is possible. Tools / Resources Approved source
repository, requirements registry, version control, CI/test framework,
structured configuration, observability/audit services, and only
authorized APIs/data sources. Constraints Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Prohibited Actions No silent requirement
change, unsupported assumption, fabricated data/evidence, unauthorized
live financial action, safety-gate bypass, or modification of frozen
goal/scope/baseline. Expected Behaviour The component shall process
Opportunity Discovery Testing consistently for the same validated inputs
and configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Discovery Testing is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.24. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 495 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Acceptance Criteria 12.24 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Opportunity Discovery Testing
is incomplete, ambiguous, unverifiable, inconsistent with governing
requirements, unsafe, unauthorized, materially untraceable, or based on
invalid/stale data. Recovery / Corrective Action Restore the last known
valid state, preserve evidence, isolate the fault, correct through
controlled change, rerun impacted tests/validation, and reconcile
downstream state before acceptance. Audit / Traceability Every material
event for 12.24 shall record requirement ID, version, actor/component,
timestamp, input/output references, decision/state, evidence, test
result, and change linkage. Change Control Material changes to 12.24
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.24. 12.25 --- Opportunity Discovery Failure Handling Field
Specification Purpose Define and control Opportunity Discovery Failure
Handling as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Discovery Failure Handling
unambiguous, deterministic where applicable, testable, traceable, and
usable by implementation agents and runtime components without hidden
assumptions. Requirement The system shall detect, contain, and recover
from Opportunity Discovery Failure Handling as a version-controlled,
testable control within Topic 12, consistent with the approved project
goal, PoV, scope, safety rules, and upstream/downstream contracts.
Opportunity discovery shall identify short-term India/INR opportunities
from validated market, news, financial, economic, and approved
alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Scope Applies to Opportunity Discovery Failure Handling, its directly
affected inputs, outputs, states, interfaces, evidence, dependencies,
permissions, and governance controls; it shall not silently expand the
frozen project goal or scope. Inputs Approved Topic 12 requirements,
upstream validated state, configuration, schemas, relevant evidence, and
authorized governance decisions required for Opportunity Discovery
Failure Handling. Input Source Controlled SRS repository, approved
upstream topic interfaces, versioned configuration/state stores, QA
evidence, audit records, and authorized change records. Processing /
Method / Rules Use explicit versioned rules for Opportunity Discovery
Failure Handling; validate inputs before use; preserve identifiers,
timestamps, versions, provenance, authority, and state lineage; reject
ambiguity rather than infer missing intent; record material transitions.
Outputs Validated Opportunity Discovery Failure Handling
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.25 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Discovery Failure Handling. Dependency Type Blocking where
goal, safety, authority, data integrity, schema, or governance
correctness is material; otherwise downstream/read-only. Parallelization
Eligibility Independent design, test preparation, evidence-template
work, and read-only analysis for Opportunity Discovery Failure Handling
may run in parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.25, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Discovery
Failure Handling consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Discovery Failure
Handling is missing, stale, contradictory, or invalid. Unblocking
Conditions Supply or restore the missing/invalid prerequisite, reconcile
conflicting state, obtain required approval, and rerun all affected
validation before resuming dependent work. Human Escalation Escalate
material safety, governance, security, scope, goal, unresolved
ambiguity, repeated recovery failure, or approval-required conditions to
authorized human governance; routine non-blocking issues remain
automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.25. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.25 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Opportunity Discovery Failure
Handling is incomplete, ambiguous, unverifiable, inconsistent with
governing requirements, unsafe, unauthorized, materially untraceable, or
based on invalid/stale data.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 496 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Recovery / Corrective Action Restore the
last known valid state, preserve evidence, isolate the fault, correct
through controlled change, rerun impacted tests/validation, and
reconcile downstream state before acceptance. Audit / Traceability Every
material event for 12.25 shall record requirement ID, version,
actor/component, timestamp, input/output references, decision/state,
evidence, test result, and change linkage. Change Control Material
changes to 12.25 shall follow Topic 27 governance/change control:
request → impact/risk assessment → authorized approval → implementation
→ validation → version/baseline update → audit evidence. Rationale /
Assumptions The frozen hierarchy and approved project constraints are
authoritative. This item must be implementable without hidden
assumptions; where source detail is not explicit, the implementation
shall use the controlled project governance process rather than invent
authority. Verification Method Inspect the generated specification
against the authoritative hierarchy, execute mapped tests and negative
cases, verify evidence/traceability, and confirm no prohibited scope or
authority change for 12.25. 12.26 --- Opportunity Discovery Audit Trail
Field Specification Purpose Define and control Opportunity Discovery
Audit Trail as an explicit part of Topic 12 --- Opportunity Discovery
Engine. Objective Make Opportunity Discovery Audit Trail unambiguous,
deterministic where applicable, testable, traceable, and usable by
implementation agents and runtime components without hidden assumptions.
Requirement The system shall perform, record, and validate Opportunity
Discovery Audit Trail as a version-controlled, testable control within
Topic 12, consistent with the approved project goal, PoV, scope, safety
rules, and upstream/downstream contracts. Opportunity discovery shall
identify short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Discovery
Audit Trail, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Discovery Audit Trail. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Discovery Audit Trail; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Discovery Audit
Trail state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.26 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Discovery Audit Trail. Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Discovery Audit Trail may run in
parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.26, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Discovery
Audit Trail consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Discovery Audit Trail is
missing, stale, contradictory, or invalid. Unblocking Conditions Supply
or restore the missing/invalid prerequisite, reconcile conflicting
state, obtain required approval, and rerun all affected validation
before resuming dependent work. Human Escalation Escalate material
safety, governance, security, scope, goal, unresolved ambiguity,
repeated recovery failure, or approval-required conditions to authorized
human governance; routine non-blocking issues remain automated.
Validation Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.26. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.26 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Discovery Audit Trail is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.26 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 497 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Change Control Material changes to 12.26
shall follow Topic 27 governance/change control: request → impact/risk
assessment → authorized approval → implementation → validation →
version/baseline update → audit evidence. Rationale / Assumptions The
frozen hierarchy and approved project constraints are authoritative.
This item must be implementable without hidden assumptions; where source
detail is not explicit, the implementation shall use the controlled
project governance process rather than invent authority. Verification
Method Inspect the generated specification against the authoritative
hierarchy, execute mapped tests and negative cases, verify
evidence/traceability, and confirm no prohibited scope or authority
change for 12.26. 12.27 --- Opportunity Discovery Performance Metrics
Field Specification Purpose Define and control Opportunity Discovery
Performance Metrics as an explicit part of Topic 12 --- Opportunity
Discovery Engine. Objective Make Opportunity Discovery Performance
Metrics unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall define and
enforce Opportunity Discovery Performance Metrics as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Discovery
Performance Metrics, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Opportunity Discovery Performance Metrics. Input
Source Controlled SRS repository, approved upstream topic interfaces,
versioned configuration/state stores, QA evidence, audit records, and
authorized change records. Processing / Method / Rules Use explicit
versioned rules for Opportunity Discovery Performance Metrics; validate
inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Opportunity Discovery Performance Metrics state/specification, decision
or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.27
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Opportunity Discovery
Performance Metrics. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Discovery Performance Metrics may run
in parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.27, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Discovery
Performance Metrics consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Discovery Performance
Metrics is missing, stale, contradictory, or invalid. Unblocking
Conditions Supply or restore the missing/invalid prerequisite, reconcile
conflicting state, obtain required approval, and rerun all affected
validation before resuming dependent work. Human Escalation Escalate
material safety, governance, security, scope, goal, unresolved
ambiguity, repeated recovery failure, or approval-required conditions to
authorized human governance; routine non-blocking issues remain
automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.27. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.27 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Opportunity Discovery
Performance Metrics is incomplete, ambiguous, unverifiable, inconsistent
with governing requirements, unsafe, unauthorized, materially
untraceable, or based on invalid/stale data. Recovery / Corrective
Action Restore the last known valid state, preserve evidence, isolate
the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.27 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.27 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 498 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy Field Specification Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.27. 12.28 --- Opportunity
Discovery Validation Field Specification Purpose Define and control
Opportunity Discovery Validation as an explicit part of Topic 12 ---
Opportunity Discovery Engine. Objective Make Opportunity Discovery
Validation unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall perform,
record, and validate Opportunity Discovery Validation as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Discovery
Validation, its directly affected inputs, outputs, states, interfaces,
evidence, dependencies, permissions, and governance controls; it shall
not silently expand the frozen project goal or scope. Inputs Approved
Topic 12 requirements, upstream validated state, configuration, schemas,
relevant evidence, and authorized governance decisions required for
Opportunity Discovery Validation. Input Source Controlled SRS
repository, approved upstream topic interfaces, versioned
configuration/state stores, QA evidence, audit records, and authorized
change records. Processing / Method / Rules Use explicit versioned rules
for Opportunity Discovery Validation; validate inputs before use;
preserve identifiers, timestamps, versions, provenance, authority, and
state lineage; reject ambiguity rather than infer missing intent; record
material transitions. Outputs Validated Opportunity Discovery Validation
state/specification, decision or control result where applicable,
validation status, evidence references, and trace information. Output
Destination Controlled SRS/requirements registry, owning component state
store, QA evidence store, dashboard/observability, and audit/change
records as applicable. Responsible Agent / Component Opportunity
Discovery Agent / Analysis / Risk / QA Prerequisites 12 shall be defined
and validated before 12.28 is finalized. Dependencies Topic 12 parent
and adjacent controls, plus the approved upstream contracts relevant to
Opportunity Discovery Validation. Dependency Type Blocking where goal,
safety, authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Discovery Validation may run in
parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.28, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Discovery
Validation consistently for the same validated inputs and configuration,
expose its state and evidence, and fail closed when required safety,
authority, or integrity conditions are not satisfied. Error Handling
Classify errors, preserve evidence, retry only when the error is
explicitly recoverable, use an approved fallback when available,
transition to a safe state when correctness is uncertain, and escalate
material failures. Blocked-State Conditions Blocked when required
inputs, parent state, dependency, approval, schema, evidence, authority,
or validation result for Opportunity Discovery Validation is missing,
stale, contradictory, or invalid. Unblocking Conditions Supply or
restore the missing/invalid prerequisite, reconcile conflicting state,
obtain required approval, and rerun all affected validation before
resuming dependent work. Human Escalation Escalate material safety,
governance, security, scope, goal, unresolved ambiguity, repeated
recovery failure, or approval-required conditions to authorized human
governance; routine non-blocking issues remain automated. Validation
Method Validate hierarchy/ID, schema, business/control rules,
dependencies, state transitions, provenance, authorization, evidence
completeness, and cross-topic consistency for 12.28. Testing
Requirements Unit, component, contract, integration, negative, boundary,
concurrency/idempotency, failure/recovery, audit-traceability, and
regression tests shall cover applicable behaviours. Evidence Required
Input snapshots/references, output state, version, rule/configuration
version, execution/trace ID, validation results, test results,
errors/recovery records, and approval/change evidence where applicable.
Acceptance Criteria 12.28 is accepted only when the specified behaviour
is implemented, validated, traceable, test-covered, within scope, and
free of unresolved blocking defects. Failure / Rejection Criteria Reject
when Opportunity Discovery Validation is incomplete, ambiguous,
unverifiable, inconsistent with governing requirements, unsafe,
unauthorized, materially untraceable, or based on invalid/stale data.
Recovery / Corrective Action Restore the last known valid state,
preserve evidence, isolate the fault, correct through controlled change,
rerun impacted tests/validation, and reconcile downstream state before
acceptance. Audit / Traceability Every material event for 12.28 shall
record requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.28 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.28.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 499 -->
```
AI Investment Opportunity Agent --- Full Master SRS --- Corrected
Hierarchy 12.29 --- Opportunity Discovery Acceptance Criteria Field
Specification Purpose Define and control Opportunity Discovery
Acceptance Criteria as an explicit part of Topic 12 --- Opportunity
Discovery Engine. Objective Make Opportunity Discovery Acceptance
Criteria unambiguous, deterministic where applicable, testable,
traceable, and usable by implementation agents and runtime components
without hidden assumptions. Requirement The system shall perform,
record, and validate Opportunity Discovery Acceptance Criteria as a
version-controlled, testable control within Topic 12, consistent with
the approved project goal, PoV, scope, safety rules, and
upstream/downstream contracts. Opportunity discovery shall identify
short-term India/INR opportunities from validated market, news,
financial, economic, and approved alternative data while applying
hard/soft filters, evidence requirements, expiry, risk pre-filtering,
confidence, and deduplication. Scope Applies to Opportunity Discovery
Acceptance Criteria, its directly affected inputs, outputs, states,
interfaces, evidence, dependencies, permissions, and governance
controls; it shall not silently expand the frozen project goal or scope.
Inputs Approved Topic 12 requirements, upstream validated state,
configuration, schemas, relevant evidence, and authorized governance
decisions required for Opportunity Discovery Acceptance Criteria. Input
Source Controlled SRS repository, approved upstream topic interfaces,
versioned configuration/state stores, QA evidence, audit records, and
authorized change records. Processing / Method / Rules Use explicit
versioned rules for Opportunity Discovery Acceptance Criteria; validate
inputs before use; preserve identifiers, timestamps, versions,
provenance, authority, and state lineage; reject ambiguity rather than
infer missing intent; record material transitions. Outputs Validated
Opportunity Discovery Acceptance Criteria state/specification, decision
or control result where applicable, validation status, evidence
references, and trace information. Output Destination Controlled
SRS/requirements registry, owning component state store, QA evidence
store, dashboard/observability, and audit/change records as applicable.
Responsible Agent / Component Opportunity Discovery Agent / Analysis /
Risk / QA Prerequisites 12 shall be defined and validated before 12.29
is finalized. Dependencies Topic 12 parent and adjacent controls, plus
the approved upstream contracts relevant to Opportunity Discovery
Acceptance Criteria. Dependency Type Blocking where goal, safety,
authority, data integrity, schema, or governance correctness is
material; otherwise downstream/read-only. Parallelization Eligibility
Independent design, test preparation, evidence-template work, and
read-only analysis for Opportunity Discovery Acceptance Criteria may run
in parallel after governing contracts and versions are frozen.
Parallelization Restrictions Parallel workers shall not create
conflicting authoritative state, bypass approval/safety gates, alter
locked baselines, duplicate unique identifiers, or consume unvalidated
upstream state. Technical Details Use stable machine-readable
identifiers for 12.29, versioned schemas/configuration, deterministic
validation, structured state transitions, correlation/trace IDs, and
idempotent processing where repeat execution is possible. Tools /
Resources Approved source repository, requirements registry, version
control, CI/test framework, structured configuration,
observability/audit services, and only authorized APIs/data sources.
Constraints Opportunity discovery shall identify short-term India/INR
opportunities from validated market, news, financial, economic, and
approved alternative data while applying hard/soft filters, evidence
requirements, expiry, risk pre-filtering, confidence, and deduplication.
Prohibited Actions No silent requirement change, unsupported assumption,
fabricated data/evidence, unauthorized live financial action,
safety-gate bypass, or modification of frozen goal/scope/baseline.
Expected Behaviour The component shall process Opportunity Discovery
Acceptance Criteria consistently for the same validated inputs and
configuration, expose its state and evidence, and fail closed when
required safety, authority, or integrity conditions are not satisfied.
Error Handling Classify errors, preserve evidence, retry only when the
error is explicitly recoverable, use an approved fallback when
available, transition to a safe state when correctness is uncertain, and
escalate material failures. Blocked-State Conditions Blocked when
required inputs, parent state, dependency, approval, schema, evidence,
authority, or validation result for Opportunity Discovery Acceptance
Criteria is missing, stale, contradictory, or invalid. Unblocking
Conditions Supply or restore the missing/invalid prerequisite, reconcile
conflicting state, obtain required approval, and rerun all affected
validation before resuming dependent work. Human Escalation Escalate
material safety, governance, security, scope, goal, unresolved
ambiguity, repeated recovery failure, or approval-required conditions to
authorized human governance; routine non-blocking issues remain
automated. Validation Method Validate hierarchy/ID, schema,
business/control rules, dependencies, state transitions, provenance,
authorization, evidence completeness, and cross-topic consistency for
12.29. Testing Requirements Unit, component, contract, integration,
negative, boundary, concurrency/idempotency, failure/recovery,
audit-traceability, and regression tests shall cover applicable
behaviours. Evidence Required Input snapshots/references, output state,
version, rule/configuration version, execution/trace ID, validation
results, test results, errors/recovery records, and approval/change
evidence where applicable. Acceptance Criteria 12.29 is accepted only
when the specified behaviour is implemented, validated, traceable,
test-covered, within scope, and free of unresolved blocking defects.
Failure / Rejection Criteria Reject when Opportunity Discovery
Acceptance Criteria is incomplete, ambiguous, unverifiable, inconsistent
with governing requirements, unsafe, unauthorized, materially
untraceable, or based on invalid/stale data. Recovery / Corrective
Action Restore the last known valid state, preserve evidence, isolate
the fault, correct through controlled change, rerun impacted
tests/validation, and reconcile downstream state before acceptance.
Audit / Traceability Every material event for 12.29 shall record
requirement ID, version, actor/component, timestamp, input/output
references, decision/state, evidence, test result, and change linkage.
Change Control Material changes to 12.29 shall follow Topic 27
governance/change control: request → impact/risk assessment → authorized
approval → implementation → validation → version/baseline update → audit
evidence. Rationale / Assumptions The frozen hierarchy and approved
project constraints are authoritative. This item must be implementable
without hidden assumptions; where source detail is not explicit, the
implementation shall use the controlled project governance process
rather than invent authority. Verification Method Inspect the generated
specification against the authoritative hierarchy, execute mapped tests
and negative cases, verify evidence/traceability, and confirm no
prohibited scope or authority change for 12.29. 12.30 --- Opportunity
Discovery Change Control Field Specification Purpose Define and control
Opportunity Discovery Change Control as an explicit part of Topic 12 ---
Opportunity Discovery Engine.
