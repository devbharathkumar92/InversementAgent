# Topic 4 --- System Scope and Boundaries

> Authoritative source slice from the uploaded Full Master SRS. Source
> PDF pages 97--138. Preserve numbering and requirement wording.

## Source Requirements

```{=html}
<!-- Source PDF page 97 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline AI Investment
Opportunity Agent --- SRS Topic 4 --- System Scope and Boundaries
BASELINE-READY TOPIC DOCUMENT --- Phase 1 / Foundation Status:
BASELINE-READY Topic: 4 Baseline: T4-BL-001 1.0 Reference and Validation
Basis This standalone Topic 4 document preserves the frozen Topic 4
hierarchy and presents every numbered item using the same two-column
specification-table format used by the Topic 1 and Topic 2 baseline
documents. The left column contains the field name and the right column
contains the complete specification text. No specification field is
silently omitted. 1.0A Mandatory Specification Contract for Every Item
Every numbered item contains the full controlled contract: Purpose,
Objective, Requirement, Scope, Inputs, Input Source, Processing / Rules,
Outputs, Output Destination, Prerequisites, Dependencies, Dependency
Type, Parallelization Eligibility, Parallelization Restrictions,
Responsible Owner, Technical Details, Tools / Resources, Constraints,
Prohibited Actions, Expected Behaviour, Error Handling, Blocked-State
Conditions, Unblocking Conditions, Human Escalation, Validation Method,
Testing Requirements, Evidence Required, Acceptance Criteria, Failure /
Rejection Criteria, Recovery / Corrective Action, Audit / Traceability,
Change Control, Rationale / Assumptions, and Verification Method.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 98 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.1 System Scope
Definition Purpose Define system scope definition as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make system scope definition
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce system scope definition within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions System Scope Definition is isolated as a controlled boundary
so implementation and runtime agents cannot infer additional authority
from adjacent requirements. Verification Method Inspect the rule,
execute positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 99 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.2 In-Scope
Capabilities Purpose Define in-scope capabilities as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make in-scope capabilities
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce in-scope capabilities within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions In-Scope Capabilities is isolated as a controlled boundary
so implementation and runtime agents cannot infer additional authority
from adjacent requirements. Verification Method Inspect the rule,
execute positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 100 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.2.1 Included
Capabilities Purpose Define included capabilities as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make included capabilities
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce included capabilities within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Included Capabilities is isolated as a controlled boundary
so implementation and runtime agents cannot infer additional authority
from adjacent requirements. Verification Method Inspect the rule,
execute positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 101 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.2.2 Capability
Limits Purpose Define capability limits as an explicit and enforceable
part of the system boundary model, preventing unintended authority or
scope expansion. Objective Make capability limits unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
capability limits within the authoritative, version-controlled scope
model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Capability Limits is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 102 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.3 Out-of-Scope
Capabilities Purpose Define out-of-scope capabilities as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make out-of-scope capabilities
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce out-of-scope capabilities within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Out-of-Scope Capabilities is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 103 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.3.1 Explicitly
Excluded Functions Purpose Define explicitly excluded functions as an
explicit and enforceable part of the system boundary model, preventing
unintended authority or scope expansion. Objective Make explicitly
excluded functions unambiguous for requirements, implementation, runtime
agents, QA, monitoring, and governance. Requirement The system shall
explicitly define and enforce explicitly excluded functions within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Explicitly Excluded Functions is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 104 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.4 Functional
Boundaries Purpose Define functional boundaries as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make functional boundaries
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce functional boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Functional Boundaries is isolated as a controlled boundary
so implementation and runtime agents cannot infer additional authority
from adjacent requirements. Verification Method Inspect the rule,
execute positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 105 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.5 Technical
Boundaries Purpose Define technical boundaries as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make technical boundaries
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce technical boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Technical Boundaries is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 106 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.6 Data Boundaries
Purpose Define data boundaries as an explicit and enforceable part of
the system boundary model, preventing unintended authority or scope
expansion. Objective Make data boundaries unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce data
boundaries within the authoritative, version-controlled scope model.
Scope Applies to every system capability, component, agent, interface,
dataset, environment, decision, output, action, and workflow affected by
this boundary. Inputs Approved higher-level requirements, relevant
configurations, records, and evidence needed by this item. Input Source
Baselined Topics 1--3, controlled SRS records, approved configuration,
API/data documentation, security policies, infrastructure limits, QA
findings, and governance decisions. Processing / Rules Classify the item
as permitted, prohibited, conditionally permitted, or unresolved; map it
to an enforceable control and validation; never infer ambiguous
authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Data Boundaries is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 107 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.7 Market and
Geographic Boundaries Purpose Define market and geographic boundaries as
an explicit and enforceable part of the system boundary model,
preventing unintended authority or scope expansion. Objective Make
market and geographic boundaries unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce market and
geographic boundaries within the authoritative, version-controlled scope
model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Market and Geographic Boundaries is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 108 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.7.1 Geographic
Scope Purpose Define geographic scope as an explicit and enforceable
part of the system boundary model, preventing unintended authority or
scope expansion. Objective Make geographic scope unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
geographic scope within the authoritative, version-controlled scope
model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Geographic Scope is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 109 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.7.2 Market Scope
Purpose Define market scope as an explicit and enforceable part of the
system boundary model, preventing unintended authority or scope
expansion. Objective Make market scope unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce market scope
within the authoritative, version-controlled scope model. Scope Applies
to every system capability, component, agent, interface, dataset,
environment, decision, output, action, and workflow affected by this
boundary. Inputs Approved higher-level requirements, relevant
configurations, records, and evidence needed by this item. Input Source
Baselined Topics 1--3, controlled SRS records, approved configuration,
API/data documentation, security policies, infrastructure limits, QA
findings, and governance decisions. Processing / Rules Classify the item
as permitted, prohibited, conditionally permitted, or unresolved; map it
to an enforceable control and validation; never infer ambiguous
authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Market Scope is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 110 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.7.3 Currency
Scope Purpose Define currency scope as an explicit and enforceable part
of the system boundary model, preventing unintended authority or scope
expansion. Objective Make currency scope unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce currency
scope within the authoritative, version-controlled scope model. Scope
Applies to every system capability, component, agent, interface,
dataset, environment, decision, output, action, and workflow affected by
this boundary. Inputs Approved higher-level requirements, relevant
configurations, records, and evidence needed by this item. Input Source
Baselined Topics 1--3, controlled SRS records, approved configuration,
API/data documentation, security policies, infrastructure limits, QA
findings, and governance decisions. Processing / Rules Classify the item
as permitted, prohibited, conditionally permitted, or unresolved; map it
to an enforceable control and validation; never infer ambiguous
authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Currency Scope is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 111 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.8 Operational
Boundaries Purpose Define operational boundaries as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make operational boundaries
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce operational boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Operational Boundaries is isolated as a controlled boundary
so implementation and runtime agents cannot infer additional authority
from adjacent requirements. Verification Method Inspect the rule,
execute positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 112 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.9 User
Interaction Boundaries Purpose Define user interaction boundaries as an
explicit and enforceable part of the system boundary model, preventing
unintended authority or scope expansion. Objective Make user interaction
boundaries unambiguous for requirements, implementation, runtime agents,
QA, monitoring, and governance. Requirement The system shall explicitly
define and enforce user interaction boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions User Interaction Boundaries is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 113 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline 4.10 Agent
Authority Boundaries Purpose Define agent authority boundaries as an
explicit and enforceable part of the system boundary model, preventing
unintended authority or scope expansion. Objective Make agent authority
boundaries unambiguous for requirements, implementation, runtime agents,
QA, monitoring, and governance. Requirement The system shall explicitly
define and enforce agent authority boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Agent Authority Boundaries is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 114 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Verification Method
Inspect the rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.10.1 Allowed Agent Authority Purpose Define
allowed agent authority as an explicit and enforceable part of the
system boundary model, preventing unintended authority or scope
expansion. Objective Make allowed agent authority unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
allowed agent authority within the authoritative, version-controlled
scope model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Allowed Agent Authority is isolated as a controlled boundary
so implementation and runtime agents cannot infer additional authority
from adjacent requirements.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 115 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Verification Method
Inspect the rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.10.2 Prohibited Agent Authority Purpose Define
prohibited agent authority as an explicit and enforceable part of the
system boundary model, preventing unintended authority or scope
expansion. Objective Make prohibited agent authority unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
prohibited agent authority within the authoritative, version-controlled
scope model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 116 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Rationale /
Assumptions Prohibited Agent Authority is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.11 Sub-Agent Scope Boundaries Purpose Define
sub-agent scope boundaries as an explicit and enforceable part of the
system boundary model, preventing unintended authority or scope
expansion. Objective Make sub-agent scope boundaries unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
sub-agent scope boundaries within the authoritative, version-controlled
scope model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 117 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Change Control Any
material boundary change requires change request, impact assessment,
authorized approval, version increment, validation, and controlled
baseline update. Rationale / Assumptions Sub-Agent Scope Boundaries is
isolated as a controlled boundary so implementation and runtime agents
cannot infer additional authority from adjacent requirements.
Verification Method Inspect the rule, execute positive/negative boundary
tests, attempt prohibited/ambiguous operations, and verify enforcement,
traceability, and audit evidence. 4.12 Input Boundaries Purpose Define
input boundaries as an explicit and enforceable part of the system
boundary model, preventing unintended authority or scope expansion.
Objective Make input boundaries unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce input
boundaries within the authoritative, version-controlled scope model.
Scope Applies to every system capability, component, agent, interface,
dataset, environment, decision, output, action, and workflow affected by
this boundary. Inputs Approved higher-level requirements, relevant
configurations, records, and evidence needed by this item. Input Source
Baselined Topics 1--3, controlled SRS records, approved configuration,
API/data documentation, security policies, infrastructure limits, QA
findings, and governance decisions. Processing / Rules Classify the item
as permitted, prohibited, conditionally permitted, or unresolved; map it
to an enforceable control and validation; never infer ambiguous
authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 118 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Change Control Any
material boundary change requires change request, impact assessment,
authorized approval, version increment, validation, and controlled
baseline update. Rationale / Assumptions Input Boundaries is isolated as
a controlled boundary so implementation and runtime agents cannot infer
additional authority from adjacent requirements. Verification Method
Inspect the rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.13 Output Boundaries Purpose Define output
boundaries as an explicit and enforceable part of the system boundary
model, preventing unintended authority or scope expansion. Objective
Make output boundaries unambiguous for requirements, implementation,
runtime agents, QA, monitoring, and governance. Requirement The system
shall explicitly define and enforce output boundaries within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 119 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Change Control Any
material boundary change requires change request, impact assessment,
authorized approval, version increment, validation, and controlled
baseline update. Rationale / Assumptions Output Boundaries is isolated
as a controlled boundary so implementation and runtime agents cannot
infer additional authority from adjacent requirements. Verification
Method Inspect the rule, execute positive/negative boundary tests,
attempt prohibited/ambiguous operations, and verify enforcement,
traceability, and audit evidence. 4.14 Decision-Making Boundaries
Purpose Define decision-making boundaries as an explicit and enforceable
part of the system boundary model, preventing unintended authority or
scope expansion. Objective Make decision-making boundaries unambiguous
for requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
decision-making boundaries within the authoritative, version-controlled
scope model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 120 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Decision-Making Boundaries is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.15 Execution and Action Boundaries Purpose Define
execution and action boundaries as an explicit and enforceable part of
the system boundary model, preventing unintended authority or scope
expansion. Objective Make execution and action boundaries unambiguous
for requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
execution and action boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 121 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Recovery /
Corrective Action Restore the last valid scope baseline where necessary,
correct the boundary through change control, rerun regression
validation, and preserve evidence. Audit / Traceability Trace each
boundary to its source requirement, enforcement control, responsible
component, tests, evidence, violations, changes, and baseline. Change
Control Any material boundary change requires change request, impact
assessment, authorized approval, version increment, validation, and
controlled baseline update. Rationale / Assumptions Execution and Action
Boundaries is isolated as a controlled boundary so implementation and
runtime agents cannot infer additional authority from adjacent
requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.15.1 Simulation Actions Purpose Define simulation actions as an
explicit and enforceable part of the system boundary model, preventing
unintended authority or scope expansion. Objective Make simulation
actions unambiguous for requirements, implementation, runtime agents,
QA, monitoring, and governance. Requirement The system shall explicitly
define and enforce simulation actions within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 122 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Recovery /
Corrective Action Restore the last valid scope baseline where necessary,
correct the boundary through change control, rerun regression
validation, and preserve evidence. Audit / Traceability Trace each
boundary to its source requirement, enforcement control, responsible
component, tests, evidence, violations, changes, and baseline. Change
Control Any material boundary change requires change request, impact
assessment, authorized approval, version increment, validation, and
controlled baseline update. Rationale / Assumptions Simulation Actions
is isolated as a controlled boundary so implementation and runtime
agents cannot infer additional authority from adjacent requirements.
Verification Method Inspect the rule, execute positive/negative boundary
tests, attempt prohibited/ambiguous operations, and verify enforcement,
traceability, and audit evidence. 4.15.2 Live-Action Restrictions
Purpose Define live-action restrictions as an explicit and enforceable
part of the system boundary model, preventing unintended authority or
scope expansion. Objective Make live-action restrictions unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
live-action restrictions within the authoritative, version-controlled
scope model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 123 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Recovery /
Corrective Action Restore the last valid scope baseline where necessary,
correct the boundary through change control, rerun regression
validation, and preserve evidence. Audit / Traceability Trace each
boundary to its source requirement, enforcement control, responsible
component, tests, evidence, violations, changes, and baseline. Change
Control Any material boundary change requires change request, impact
assessment, authorized approval, version increment, validation, and
controlled baseline update. Rationale / Assumptions Live-Action
Restrictions is isolated as a controlled boundary so implementation and
runtime agents cannot infer additional authority from adjacent
requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.16 Risk and Safety Boundaries Purpose Define risk and safety
boundaries as an explicit and enforceable part of the system boundary
model, preventing unintended authority or scope expansion. Objective
Make risk and safety boundaries unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce risk and
safety boundaries within the authoritative, version-controlled scope
model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 124 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Failure / Rejection
Criteria Ambiguity, missing exclusions, undefined authority,
unenforceable rules, absent tests/evidence, executable prohibited
actions, or uncontrolled changes cause rejection/hold. Recovery /
Corrective Action Restore the last valid scope baseline where necessary,
correct the boundary through change control, rerun regression
validation, and preserve evidence. Audit / Traceability Trace each
boundary to its source requirement, enforcement control, responsible
component, tests, evidence, violations, changes, and baseline. Change
Control Any material boundary change requires change request, impact
assessment, authorized approval, version increment, validation, and
controlled baseline update. Rationale / Assumptions Risk and Safety
Boundaries is isolated as a controlled boundary so implementation and
runtime agents cannot infer additional authority from adjacent
requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.17 External System and API Boundaries Purpose Define external system
and api boundaries as an explicit and enforceable part of the system
boundary model, preventing unintended authority or scope expansion.
Objective Make external system and api boundaries unambiguous for
requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
external system and api boundaries within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 125 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Acceptance Criteria
The boundary is explicit, enforceable/testably rejectable, owned,
traceable, reproducible from its baseline, and free of unauthorized
execution paths. Failure / Rejection Criteria Ambiguity, missing
exclusions, undefined authority, unenforceable rules, absent
tests/evidence, executable prohibited actions, or uncontrolled changes
cause rejection/hold. Recovery / Corrective Action Restore the last
valid scope baseline where necessary, correct the boundary through
change control, rerun regression validation, and preserve evidence.
Audit / Traceability Trace each boundary to its source requirement,
enforcement control, responsible component, tests, evidence, violations,
changes, and baseline. Change Control Any material boundary change
requires change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions External System and API Boundaries is isolated as a
controlled boundary so implementation and runtime agents cannot infer
additional authority from adjacent requirements. Verification Method
Inspect the rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.18 Resource and Infrastructure Boundaries Purpose
Define resource and infrastructure boundaries as an explicit and
enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make resource and infrastructure
boundaries unambiguous for requirements, implementation, runtime agents,
QA, monitoring, and governance. Requirement The system shall explicitly
define and enforce resource and infrastructure boundaries within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 126 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Evidence Required
Scope/policy versions, inventories, mappings, test results,
denied-operation logs, violations, change requests, impact assessments,
approvals, and validation reports. Acceptance Criteria The boundary is
explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Resource and Infrastructure Boundaries is isolated as a
controlled boundary so implementation and runtime agents cannot infer
additional authority from adjacent requirements. Verification Method
Inspect the rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.19 Scope Violation Detection Purpose Define scope
violation detection as an explicit and enforceable part of the system
boundary model, preventing unintended authority or scope expansion.
Objective Make scope violation detection unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce scope
violation detection within the authoritative, version-controlled scope
model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 127 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Testing
Requirements Test permitted operations, prohibited operations, ambiguous
requests, authority boundaries, input/output limits, execution limits,
API permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Scope Violation Detection is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.20 Boundary Enforcement Purpose Define boundary
enforcement as an explicit and enforceable part of the system boundary
model, preventing unintended authority or scope expansion. Objective
Make boundary enforcement unambiguous for requirements, implementation,
runtime agents, QA, monitoring, and governance. Requirement The system
shall explicitly define and enforce boundary enforcement within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 128 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Testing
Requirements Test permitted operations, prohibited operations, ambiguous
requests, authority boundaries, input/output limits, execution limits,
API permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Boundary Enforcement is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.21 Scope Expansion Restriction Purpose Define scope expansion
restriction as an explicit and enforceable part of the system boundary
model, preventing unintended authority or scope expansion. Objective
Make scope expansion restriction unambiguous for requirements,
implementation, runtime agents, QA, monitoring, and governance.
Requirement The system shall explicitly define and enforce scope
expansion restriction within the authoritative, version-controlled scope
model. Scope Applies to every system capability, component, agent,
interface, dataset, environment, decision, output, action, and workflow
affected by this boundary. Inputs Approved higher-level requirements,
relevant configurations, records, and evidence needed by this item.
Input Source Baselined Topics 1--3, controlled SRS records, approved
configuration, API/data documentation, security policies, infrastructure
limits, QA findings, and governance decisions. Processing / Rules
Classify the item as permitted, prohibited, conditionally permitted, or
unresolved; map it to an enforceable control and validation; never infer
ambiguous authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 129 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Validation Method
Static review, policy/schema validation, positive and negative tests,
runtime enforcement tests, integration tests, and regression after
changes. Testing Requirements Test permitted operations, prohibited
operations, ambiguous requests, authority boundaries, input/output
limits, execution limits, API permissions, resource limits, violation
detection, and recovery. Evidence Required Scope/policy versions,
inventories, mappings, test results, denied-operation logs, violations,
change requests, impact assessments, approvals, and validation reports.
Acceptance Criteria The boundary is explicit, enforceable/testably
rejectable, owned, traceable, reproducible from its baseline, and free
of unauthorized execution paths. Failure / Rejection Criteria Ambiguity,
missing exclusions, undefined authority, unenforceable rules, absent
tests/evidence, executable prohibited actions, or uncontrolled changes
cause rejection/hold. Recovery / Corrective Action Restore the last
valid scope baseline where necessary, correct the boundary through
change control, rerun regression validation, and preserve evidence.
Audit / Traceability Trace each boundary to its source requirement,
enforcement control, responsible component, tests, evidence, violations,
changes, and baseline. Change Control Any material boundary change
requires change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Scope Expansion Restriction is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.21.1 Expansion Trigger Purpose Define expansion
trigger as an explicit and enforceable part of the system boundary
model, preventing unintended authority or scope expansion. Objective
Make expansion trigger unambiguous for requirements, implementation,
runtime agents, QA, monitoring, and governance. Requirement The system
shall explicitly define and enforce expansion trigger within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 130 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Validation Method
Static review, policy/schema validation, positive and negative tests,
runtime enforcement tests, integration tests, and regression after
changes. Testing Requirements Test permitted operations, prohibited
operations, ambiguous requests, authority boundaries, input/output
limits, execution limits, API permissions, resource limits, violation
detection, and recovery. Evidence Required Scope/policy versions,
inventories, mappings, test results, denied-operation logs, violations,
change requests, impact assessments, approvals, and validation reports.
Acceptance Criteria The boundary is explicit, enforceable/testably
rejectable, owned, traceable, reproducible from its baseline, and free
of unauthorized execution paths. Failure / Rejection Criteria Ambiguity,
missing exclusions, undefined authority, unenforceable rules, absent
tests/evidence, executable prohibited actions, or uncontrolled changes
cause rejection/hold. Recovery / Corrective Action Restore the last
valid scope baseline where necessary, correct the boundary through
change control, rerun regression validation, and preserve evidence.
Audit / Traceability Trace each boundary to its source requirement,
enforcement control, responsible component, tests, evidence, violations,
changes, and baseline. Change Control Any material boundary change
requires change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Expansion Trigger is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.21.2 Expansion Approval Purpose Define expansion approval as an
explicit and enforceable part of the system boundary model, preventing
unintended authority or scope expansion. Objective Make expansion
approval unambiguous for requirements, implementation, runtime agents,
QA, monitoring, and governance. Requirement The system shall explicitly
define and enforce expansion approval within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 131 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Validation Method
Static review, policy/schema validation, positive and negative tests,
runtime enforcement tests, integration tests, and regression after
changes. Testing Requirements Test permitted operations, prohibited
operations, ambiguous requests, authority boundaries, input/output
limits, execution limits, API permissions, resource limits, violation
detection, and recovery. Evidence Required Scope/policy versions,
inventories, mappings, test results, denied-operation logs, violations,
change requests, impact assessments, approvals, and validation reports.
Acceptance Criteria The boundary is explicit, enforceable/testably
rejectable, owned, traceable, reproducible from its baseline, and free
of unauthorized execution paths. Failure / Rejection Criteria Ambiguity,
missing exclusions, undefined authority, unenforceable rules, absent
tests/evidence, executable prohibited actions, or uncontrolled changes
cause rejection/hold. Recovery / Corrective Action Restore the last
valid scope baseline where necessary, correct the boundary through
change control, rerun regression validation, and preserve evidence.
Audit / Traceability Trace each boundary to its source requirement,
enforcement control, responsible component, tests, evidence, violations,
changes, and baseline. Change Control Any material boundary change
requires change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Expansion Approval is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.22 Scope Change Control Purpose Define scope change control as an
explicit and enforceable part of the system boundary model, preventing
unintended authority or scope expansion. Objective Make scope change
control unambiguous for requirements, implementation, runtime agents,
QA, monitoring, and governance. Requirement The system shall explicitly
define and enforce scope change control within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 132 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Validation Method
Static review, policy/schema validation, positive and negative tests,
runtime enforcement tests, integration tests, and regression after
changes. Testing Requirements Test permitted operations, prohibited
operations, ambiguous requests, authority boundaries, input/output
limits, execution limits, API permissions, resource limits, violation
detection, and recovery. Evidence Required Scope/policy versions,
inventories, mappings, test results, denied-operation logs, violations,
change requests, impact assessments, approvals, and validation reports.
Acceptance Criteria The boundary is explicit, enforceable/testably
rejectable, owned, traceable, reproducible from its baseline, and free
of unauthorized execution paths. Failure / Rejection Criteria Ambiguity,
missing exclusions, undefined authority, unenforceable rules, absent
tests/evidence, executable prohibited actions, or uncontrolled changes
cause rejection/hold. Recovery / Corrective Action Restore the last
valid scope baseline where necessary, correct the boundary through
change control, rerun regression validation, and preserve evidence.
Audit / Traceability Trace each boundary to its source requirement,
enforcement control, responsible component, tests, evidence, violations,
changes, and baseline. Change Control Any material boundary change
requires change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Scope Change Control is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.23 Scope Validation and Review Purpose Define scope validation and
review as an explicit and enforceable part of the system boundary model,
preventing unintended authority or scope expansion. Objective Make scope
validation and review unambiguous for requirements, implementation,
runtime agents, QA, monitoring, and governance. Requirement The system
shall explicitly define and enforce scope validation and review within
the authoritative, version-controlled scope model. Scope Applies to
every system capability, component, agent, interface, dataset,
environment, decision, output, action, and workflow affected by this
boundary. Inputs Approved higher-level requirements, relevant
configurations, records, and evidence needed by this item. Input Source
Baselined Topics 1--3, controlled SRS records, approved configuration,
API/data documentation, security policies, infrastructure limits, QA
findings, and governance decisions. Processing / Rules Classify the item
as permitted, prohibited, conditionally permitted, or unresolved; map it
to an enforceable control and validation; never infer ambiguous
authority. Outputs A versioned boundary rule, applicable
permission/prohibition, responsible owner, enforcement mapping,
validation state, and exception/escalation record where applicable.
Output Destination Controlled SRS, policy/configuration store, agent
registry, enforcement layer, QA evidence, dashboard/observability, and
audit trail. Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 133 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Human Escalation
Required for material scope expansion, new market/geographic/currency
coverage, new execution authority, new external access, changed
prohibitions, unresolved conflicts, and baseline changes. Validation
Method Static review, policy/schema validation, positive and negative
tests, runtime enforcement tests, integration tests, and regression
after changes. Testing Requirements Test permitted operations,
prohibited operations, ambiguous requests, authority boundaries,
input/output limits, execution limits, API permissions, resource limits,
violation detection, and recovery. Evidence Required Scope/policy
versions, inventories, mappings, test results, denied-operation logs,
violations, change requests, impact assessments, approvals, and
validation reports. Acceptance Criteria The boundary is explicit,
enforceable/testably rejectable, owned, traceable, reproducible from its
baseline, and free of unauthorized execution paths. Failure / Rejection
Criteria Ambiguity, missing exclusions, undefined authority,
unenforceable rules, absent tests/evidence, executable prohibited
actions, or uncontrolled changes cause rejection/hold. Recovery /
Corrective Action Restore the last valid scope baseline where necessary,
correct the boundary through change control, rerun regression
validation, and preserve evidence. Audit / Traceability Trace each
boundary to its source requirement, enforcement control, responsible
component, tests, evidence, violations, changes, and baseline. Change
Control Any material boundary change requires change request, impact
assessment, authorized approval, version increment, validation, and
controlled baseline update. Rationale / Assumptions Scope Validation and
Review is isolated as a controlled boundary so implementation and
runtime agents cannot infer additional authority from adjacent
requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.24 Scope Freeze and Baseline Purpose Define scope freeze and baseline
as an explicit and enforceable part of the system boundary model,
preventing unintended authority or scope expansion. Objective Make scope
freeze and baseline unambiguous for requirements, implementation,
runtime agents, QA, monitoring, and governance. Requirement The system
shall explicitly define and enforce scope freeze and baseline within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.
Blocked-State Conditions Required policy unavailable/invalid,
authorization indeterminate, prohibited operation detected, or material
boundary conflict unresolved.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 134 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Unblocking
Conditions Provide a valid rule/authorization, resolve the conflict,
version the policy/configuration, and complete required
validation/approval. Human Escalation Required for material scope
expansion, new market/geographic/currency coverage, new execution
authority, new external access, changed prohibitions, unresolved
conflicts, and baseline changes. Validation Method Static review,
policy/schema validation, positive and negative tests, runtime
enforcement tests, integration tests, and regression after changes.
Testing Requirements Test permitted operations, prohibited operations,
ambiguous requests, authority boundaries, input/output limits, execution
limits, API permissions, resource limits, violation detection, and
recovery. Evidence Required Scope/policy versions, inventories,
mappings, test results, denied-operation logs, violations, change
requests, impact assessments, approvals, and validation reports.
Acceptance Criteria The boundary is explicit, enforceable/testably
rejectable, owned, traceable, reproducible from its baseline, and free
of unauthorized execution paths. Failure / Rejection Criteria Ambiguity,
missing exclusions, undefined authority, unenforceable rules, absent
tests/evidence, executable prohibited actions, or uncontrolled changes
cause rejection/hold. Recovery / Corrective Action Restore the last
valid scope baseline where necessary, correct the boundary through
change control, rerun regression validation, and preserve evidence.
Audit / Traceability Trace each boundary to its source requirement,
enforcement control, responsible component, tests, evidence, violations,
changes, and baseline. Change Control Any material boundary change
requires change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Scope Freeze and Baseline is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.25 Scope Exceptions and Escalation Purpose Define
scope exceptions and escalation as an explicit and enforceable part of
the system boundary model, preventing unintended authority or scope
expansion. Objective Make scope exceptions and escalation unambiguous
for requirements, implementation, runtime agents, QA, monitoring, and
governance. Requirement The system shall explicitly define and enforce
scope exceptions and escalation within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 135 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Blocked-State
Conditions Required policy unavailable/invalid, authorization
indeterminate, prohibited operation detected, or material boundary
conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Scope Exceptions and Escalation is isolated as a controlled
boundary so implementation and runtime agents cannot infer additional
authority from adjacent requirements. Verification Method Inspect the
rule, execute positive/negative boundary tests, attempt
prohibited/ambiguous operations, and verify enforcement, traceability,
and audit evidence. 4.25.1 Exception Detection Purpose Define exception
detection as an explicit and enforceable part of the system boundary
model, preventing unintended authority or scope expansion. Objective
Make exception detection unambiguous for requirements, implementation,
runtime agents, QA, monitoring, and governance. Requirement The system
shall explicitly define and enforce exception detection within the
authoritative, version-controlled scope model. Scope Applies to every
system capability, component, agent, interface, dataset, environment,
decision, output, action, and workflow affected by this boundary. Inputs
Approved higher-level requirements, relevant configurations, records,
and evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 136 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Blocked-State
Conditions Required policy unavailable/invalid, authorization
indeterminate, prohibited operation detected, or material boundary
conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Exception Detection is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.
4.25.2 Escalation Rules Purpose Define escalation rules as an explicit
and enforceable part of the system boundary model, preventing unintended
authority or scope expansion. Objective Make escalation rules
unambiguous for requirements, implementation, runtime agents, QA,
monitoring, and governance. Requirement The system shall explicitly
define and enforce escalation rules within the authoritative,
version-controlled scope model. Scope Applies to every system
capability, component, agent, interface, dataset, environment, decision,
output, action, and workflow affected by this boundary. Inputs Approved
higher-level requirements, relevant configurations, records, and
evidence needed by this item. Input Source Baselined Topics 1--3,
controlled SRS records, approved configuration, API/data documentation,
security policies, infrastructure limits, QA findings, and governance
decisions. Processing / Rules Classify the item as permitted,
prohibited, conditionally permitted, or unresolved; map it to an
enforceable control and validation; never infer ambiguous authority.
Outputs A versioned boundary rule, applicable permission/prohibition,
responsible owner, enforcement mapping, validation state, and
exception/escalation record where applicable. Output Destination
Controlled SRS, policy/configuration store, agent registry, enforcement
layer, QA evidence, dashboard/observability, and audit trail.
Prerequisites Topics 1, 2, and 3 shall be completed and
baseline-ready/approved as required by governance before this Topic 4
item is finalized. Dependencies Immutable goal/mission, approved PoV,
system principles, safety model, and the relevant preceding
scope/boundary definitions. Dependency Type Blocking for goal, safety,
authority, and governance dependencies; downstream for implementation
details that do not change the boundary. Parallelization Eligibility
Boundary inventories, authority matrices, test cases, policy schemas,
and documentation may be drafted in parallel after governing inputs are
frozen. Parallelization Restrictions No parallel worker may expand
markets/currencies, grant authority, remove prohibitions, redefine the
goal, or modify a locked boundary baseline. Responsible Owner SRS
Governance Owner / SRS Writer Agent for specification;
Policy/Enforcement layer for runtime control; QA for validation;
authorized human governance for material changes. Technical Details
Represent boundaries with stable IDs, allowlists/denylists, policy
rules, capability-to-agent mappings, environment identifiers, API
permissions, and versioned configuration. Tools / Resources SRS
repository, version control, policy/configuration store, agent registry,
API gateway, authorization layer, data-source registry, test harness,
logging, and dashboard. Constraints Initial system scope remains
India-focused and INR-focused, uses only approved markets/data sources,
respects PoV limits, and assumes no unapproved authority or
infrastructure. Prohibited Actions Silent addition of capabilities,
markets, countries, currencies, data sources, external integrations,
financial-account access, live execution authority, or other
out-of-scope actions. Expected Behaviour Clearly in-scope actions may
proceed under authorization; out-of-scope or ambiguous actions shall be
blocked or denied with a traceable reason. Error Handling Log the
attempted operation, applicable boundary, component, policy version,
timestamp, and decision; unsafe ambiguity defaults to blocking.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 137 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Blocked-State
Conditions Required policy unavailable/invalid, authorization
indeterminate, prohibited operation detected, or material boundary
conflict unresolved. Unblocking Conditions Provide a valid
rule/authorization, resolve the conflict, version the
policy/configuration, and complete required validation/approval. Human
Escalation Required for material scope expansion, new
market/geographic/currency coverage, new execution authority, new
external access, changed prohibitions, unresolved conflicts, and
baseline changes. Validation Method Static review, policy/schema
validation, positive and negative tests, runtime enforcement tests,
integration tests, and regression after changes. Testing Requirements
Test permitted operations, prohibited operations, ambiguous requests,
authority boundaries, input/output limits, execution limits, API
permissions, resource limits, violation detection, and recovery.
Evidence Required Scope/policy versions, inventories, mappings, test
results, denied-operation logs, violations, change requests, impact
assessments, approvals, and validation reports. Acceptance Criteria The
boundary is explicit, enforceable/testably rejectable, owned, traceable,
reproducible from its baseline, and free of unauthorized execution
paths. Failure / Rejection Criteria Ambiguity, missing exclusions,
undefined authority, unenforceable rules, absent tests/evidence,
executable prohibited actions, or uncontrolled changes cause
rejection/hold. Recovery / Corrective Action Restore the last valid
scope baseline where necessary, correct the boundary through change
control, rerun regression validation, and preserve evidence. Audit /
Traceability Trace each boundary to its source requirement, enforcement
control, responsible component, tests, evidence, violations, changes,
and baseline. Change Control Any material boundary change requires
change request, impact assessment, authorized approval, version
increment, validation, and controlled baseline update. Rationale /
Assumptions Escalation Rules is isolated as a controlled boundary so
implementation and runtime agents cannot infer additional authority from
adjacent requirements. Verification Method Inspect the rule, execute
positive/negative boundary tests, attempt prohibited/ambiguous
operations, and verify enforcement, traceability, and audit evidence.

------------------------------------------------------------------------

```{=html}
<!-- Source PDF page 138 -->
```
AI Investment Opportunity Agent --- Topic 4 Baseline Topic 4 Final
Validation Gate • Hierarchy and numbering: PASS --- the frozen hierarchy
is preserved. • Table-format parity: PASS --- every item is rendered as
a two-column field/value table matching the Topic 1 and Topic 2
presentation style. • Specification completeness: PASS --- all mandatory
contract fields are present for every numbered item. • Content
preservation: PASS --- the table conversion uses the existing corrected
Topic specification content rather than silently replacing it with new
requirements. • Dependency and governance control: PASS --- earlier
topics remain governing inputs and are not silently modified. • Safety
and authority control: PASS --- prohibited and ambiguous actions remain
blocked and material changes remain governance-controlled. • Baseline
status: PASS --- T4-BL-001 is ready for governance approval; formal
governance approval is not claimed without the authorized human action.
Baseline Statement Topic 4 is BASELINE-READY --- T4-BL-001. This
corrected version is the table-format working copy for governance
review. Formal governance approval remains a human gate.
