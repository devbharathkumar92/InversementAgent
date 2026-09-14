"""Topic 3 — Proof of Value definition and decision rules.

The PoV contract requires explicit, measurable, traceable success/failure
criteria so PoV outcomes are objectively governable (REQ 3.1).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from numbers import Real


class PoVStatus(Enum):
    """Lifecycle status of the controlled PoV definition."""

    DEFINED = "defined"
    EVALUATING = "evaluating"
    COMPLETED = "completed"
    EXPANDED = "expanded"
    FAILED = "failed"


class FailureClass(Enum):
    """Failure severity classification (REQ 3.18.1 / 3.18.2)."""

    CRITICAL = "critical"
    NON_CRITICAL = "non_critical"


class ReleaseGate:
    """Outcome of the release-blocking gate (REQ 3.5.2)."""

    def __init__(self, active_blockers: list[str], release_approved: bool) -> None:
        self.active_blockers = list(active_blockers)
        self.release_approved = release_approved

    @property
    def blockers(self) -> list[str]:
        return list(self.active_blockers)


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


@dataclass
class PoVDefinition:
    """A controlled Proof-of-Value definition (REQ 3.1).

    ``objectives`` must cover functional, technical, and outcome
    categories; ``minimum_success_thresholds`` and
    ``release_blocking_conditions`` are explicit and recorded.
    """

    name: str = ""
    objectives: dict[str, str] = field(default_factory=dict)
    success_conditions: list[str] = field(default_factory=list)
    minimum_success_thresholds: dict[str, float] = field(default_factory=dict)
    release_blocking_conditions: list[str] = field(default_factory=list)
    acceptance_criteria: dict[str, str] = field(default_factory=dict)
    status: PoVStatus = PoVStatus.DEFINED

    REQUIRED_OBJECTIVE_TYPES = frozenset({"functional", "technical", "outcome"})

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")
        if not self.objectives:
            raise ValueError("objectives must be provided")
        missing = self.REQUIRED_OBJECTIVE_TYPES - set(self.objectives)
        if missing:
            raise ValueError(f"missing objective types: {sorted(missing)}")

    def objective_traceability(self) -> set[str]:
        """Map objective categories to SRS item IDs (3.3.1/3.3.2/3.3.3)."""
        mapping = {
            "functional": "3.3.1",
            "technical": "3.3.2",
            "outcome": "3.3.3",
        }
        return {mapping[obj] for obj in mapping if obj in self.objectives}


def meets_success_threshold(value: object, threshold: object) -> bool:
    """Return whether a measured value meets or exceeds its threshold."""
    if not isinstance(value, Real):
        raise ValueError("measured value must be numeric")
    if not isinstance(threshold, Real):
        raise ValueError("threshold must be numeric")
    return float(value) >= float(threshold)


def evaluate_release_gate(
    pov: PoVDefinition,
    active_blockers: list[str],
) -> ReleaseGate:
    """Evaluate whether active release-blocking conditions block the release."""
    known = set(pov.release_blocking_conditions)
    present = [b for b in active_blockers if b in known]
    return ReleaseGate(active_blockers=present, release_approved=not present)


def failure_class(failure: str) -> FailureClass:
    """Classify a failure as critical or non-critical (REQ 3.18.x)."""
    lowered = failure.lower()
    critical_keywords = ("safety", "violation", "bypass", "evidence", "critical")
    if any(keyword in lowered for keyword in critical_keywords):
        return FailureClass.CRITICAL
    return FailureClass.NON_CRITICAL


def validate_completion(
    pov: PoVDefinition,
    functional_acceptance: bool,
    safety_acceptance: bool,
) -> bool:
    """Validate completion criteria (REQ 3.21): both acceptance gates required."""
    if not functional_acceptance:
        raise ValueError("functional acceptance not met")
    if not safety_acceptance:
        raise ValueError("safety acceptance not met")
    return True


def completion_status(
    functional_acceptance: bool,
    safety_acceptance: bool,
) -> PoVStatus:
    """Derive the nominal completion status from acceptance gates."""
    if functional_acceptance and safety_acceptance:
        return PoVStatus.COMPLETED
    return PoVStatus.FAILED
