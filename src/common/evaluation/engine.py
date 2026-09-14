"""Topic 25 — Self-Evaluation.

Evaluates the agent's own performance against goals and the SRS
(25.2/25.3), detects stuck or deviating behaviour (25.20/25.21),
scores runs against thresholds (25.24/25.25), and routes failed
evaluations to recovery or escalation (25.26). (REQ 25.1-25.30
enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def goal_met(result: bool, expected: bool) -> bool:
    """Return whether a goal was satisfied (25.2.2)."""
    return result == expected


def violation_detected(delta: float, tolerance: float) -> bool:
    """Return whether an SRS deviation exceeds tolerance (25.3.2)."""
    return delta > tolerance


def methodology_compliant(scope: bool, requirements: bool) -> bool:
    """Return whether execution stayed in scope (25.4/25.5)."""
    return scope and requirements


def stuck_detected(progress_made: bool, since_turns: int) -> bool:
    """Return whether the agent is stuck (25.20.2)."""
    return not progress_made and since_turns >= 3


def deviation_severity(delta: float) -> str:
    """Classify the severity of a deviation (25.21.2)."""
    if delta >= 0.8:
        return "high"
    if delta >= 0.4:
        return "medium"
    return "low"


def evidence_captured(run_id: str, saved: bool) -> bool:
    """Return whether evaluation evidence was retained (25.23)."""
    return bool(run_id) and saved


def score_threshold_met(score: float, threshold: float) -> bool:
    """Return whether a score passes its threshold (25.24.2)."""
    return score >= threshold


def failed_evaluation_recovery(escalated: bool) -> str:
    """Return the handling action for a failed run (25.26.2)."""
    return "escalated" if escalated else "retry"


@dataclass
class EvaluationEngine:
    """Self-evaluation lifecycle (25.1)."""

    name: str
    _running: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._running = True

    def status(self) -> str:
        """Return the evaluation engine state."""
        return "evaluating" if self._running else "idle"
