"""Topic 33 — Testing Strategy.

Defines the layered test strategy (unit → integration → system),
domain suites, quality-attribute coverage and automated acceptance
with audit evidence (REQ 33.1-33.30 subset).
"""

from .engine import (
    TestStrategyEngine,
    acceptance_passed,
    agent_compliance_tested,
    automated,
    decision_tested,
    evidence_recorded,
    failure_recovery_tested,
    integration_covered,
    regression_testing,
    reliability_tested,
    risk_tested,
    security_tested,
    system_covered,
    unit_case_defined,
)

__all__ = [
    "TestStrategyEngine",
    "acceptance_passed",
    "agent_compliance_tested",
    "automated",
    "decision_tested",
    "evidence_recorded",
    "failure_recovery_tested",
    "integration_covered",
    "regression_testing",
    "reliability_tested",
    "risk_tested",
    "security_tested",
    "system_covered",
    "unit_case_defined",
]
