"""Topic 33 — Testing Strategy.

Defines a layered testing strategy: unit cases with expected
results (33.4), integration cases validating interfaces (33.6),
system/E2E coverage (33.7/33.8), domain suites (33.10-33.14),
quality-attribute coverage (33.19-33.23), acceptance gates
(33.26) and automated, evidenced execution (33.27/33.29).
(REQ 33.1-33.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def unit_case_defined(case: bool, expected: bool) -> bool:
    """Return whether a unit test case is defined (33.4.1/33.4.2)."""
    return case and expected


def integration_covered(cases: bool, interfaces: bool) -> bool:
    """Return whether integration testing covers interfaces (33.6)."""
    return cases and interfaces


def system_covered(e2e: bool, api: bool) -> bool:
    """Return whether system/E2E/API coverage holds (33.7/33.8/33.9)."""
    return e2e and api


def risk_tested(scenarios: bool) -> bool:
    """Return whether risk scenarios are tested (33.14)."""
    return scenarios


def agent_compliance_tested(behaviour: bool, compliance: bool) -> bool:
    """Return whether agent behaviour/compliance are tested (33.11)."""
    return behaviour and compliance


def decision_tested(rules: bool) -> bool:
    """Return whether decision rules are tested (33.13)."""
    return rules


def security_tested(auth: bool, injected: bool) -> bool:
    """Return whether security is tested (33.19)."""
    return auth and injected


def regression_testing(previous: bool) -> bool:
    """Return whether regression coverage exists (33.23)."""
    return previous


def reliability_tested(failover: bool) -> bool:
    """Return whether reliability is tested (33.21)."""
    return failover


def failure_recovery_tested(restart: bool) -> bool:
    """Return whether failure recovery is tested (33.22)."""
    return restart


def acceptance_passed(criteria: bool, passed: bool) -> bool:
    """Return whether acceptance testing passed (33.26.1/33.26.2)."""
    return criteria and passed


def automated(ci: bool, repeatable: bool) -> bool:
    """Return whether tests are automated and repeatable (33.27)."""
    return ci and repeatable


def evidence_recorded(stored: bool, auditable: bool) -> bool:
    """Return whether test evidence is auditable (33.29)."""
    return stored and auditable


@dataclass
class TestStrategyEngine:
    """Testing strategy lifecycle (33.1)."""

    name: str
    _defined: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._defined = True

    def status(self) -> str:
        """Return the testing strategy state."""
        return "defined" if self._defined else "undefined"
