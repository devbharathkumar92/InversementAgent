"""Topic 25 — Self-Evaluation.

Checks goal/SRS/scope compliance, detects stuck/off-track states,
scores runs against thresholds, and routes failed evaluations
(REQ 25.1-25.30 subset).
"""

from .engine import (
    EvaluationEngine,
    deviation_severity,
    evidence_captured,
    failed_evaluation_recovery,
    goal_met,
    methodology_compliant,
    score_threshold_met,
    stuck_detected,
    violation_detected,
)

__all__ = [
    "EvaluationEngine",
    "deviation_severity",
    "evidence_captured",
    "failed_evaluation_recovery",
    "goal_met",
    "methodology_compliant",
    "score_threshold_met",
    "stuck_detected",
    "violation_detected",
]
