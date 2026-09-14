# Topic 4 — System Scope and Boundaries

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-04-system-scope`

## Decision

**Implementation required.** Topic 4 defines run-time enforceable scope
boundaries (in/out-of-scope, market bounds, agent authority, expansions,
exceptions) that the enforcement agents will invoke on every action. The
decision rules — violation detection, boundary enforcement, expansion
approval — are deterministic and coded as a controlled `SystemScope`
model.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 4.1 | System Scope Definition | `system_scope.py` (`SystemScope`) | `test_system_scope.py::TestSystemScopeDefinition` |
| 4.2 / 4.2.1 / 4.3 / 4.3.1 | In/Out-of-Scope Capabilities | `system_scope.py` (`is_in_scope`) | `test_system_scope.py::TestSystemScopeDefinition` |
| 4.2.2 | Capability Limits | `system_scope.py` (`check_capability_limit`) | `test_system_scope.py::TestCapabilityLimits` |
| 4.7 / 4.7.1–4.7.3 | Geographic/Market/Currency Bounds | `system_scope.py` (`allows_market`) | `test_system_scope.py::TestScopeBoundaries` |
| 4.10 / 4.10.1 / 4.10.2 | Agent Authority Boundaries | `system_scope.py` (`authority_allowed`) | `test_system_scope.py::TestAgentAuthority` |
| 4.15.2 | Live-Action Restrictions | `system_scope.py` (authority model) | `test_system_scope.py::TestAgentAuthority` |
| 4.19 / 4.20 | Scope Violation Detection / Enforcement | `system_scope.py` (`ScopeEnforcer`) | `test_system_scope.py::TestScopeEnforcement` |
| 4.21 / 4.21.2 | Scope Expansion Restriction / Approval | `system_scope.py` (`ExpansionApproval`, `approve_expansion`) | `test_system_scope.py::TestScopeExpansion` |
| 4.25 / 4.25.1 / 4.25.2 | Exceptions and Escalation | `system_scope.py` (`ScopeException`) | `test_system_scope.py::TestExceptionsAndEscalation` |
| 1.0A (traceability) | Full contract per item | `registry.py` + `test_scope_registry.py` | `test_scope_registry.py` |

## Validation

- `python -m pytest -m unit` → **131 passed** (21 from Topic 4)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (62 files)

## Notes / decisions

- Undeclared capabilities default to **out-of-scope** (no silent
  assumptions); only an explicit governance expansion (4.21.2) can add
  them.
- Authority is allow-list based (`allowed_authority`), with an explicit
  `prohibited_authority` block-list as a hard override.
- Capability limits are integer counts (e.g. `max_live_orders_per_day`).
- Scope exceptions always escalate to a human (4.25.2).