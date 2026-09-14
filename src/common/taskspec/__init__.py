"""Topic 30 — Sub-Agent Task Specification.

Defines tasks by objective, scope, schema-validated IO, execution
constraints, acceptance criteria and handoff requirements
(REQ 30.1-30.30 subset).
"""

from .engine import (
    TaskSpecEngine,
    acceptance_met,
    blocked_action_defined,
    constraints_ok,
    error_recoverable,
    handoff_package_ok,
    implementation_specified,
    input_valid,
    no_prohibited_actions,
    objective_defined,
    output_valid,
    prerequisites_met,
    requirements_met,
)

__all__ = [
    "TaskSpecEngine",
    "acceptance_met",
    "blocked_action_defined",
    "constraints_ok",
    "error_recoverable",
    "handoff_package_ok",
    "implementation_specified",
    "input_valid",
    "no_prohibited_actions",
    "objective_defined",
    "output_valid",
    "prerequisites_met",
    "requirements_met",
]
