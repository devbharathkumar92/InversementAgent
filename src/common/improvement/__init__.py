"""Topic 26 — Self-Improvement and Change Management.

Gates improvement proposals behind evidence, impact/risk analysis,
testing and human approval, and protects SRS/goal baselines
(REQ 26.1-26.30 subset).
"""

from .engine import (
    ImprovementEngine,
    approval_required,
    benefit_possible,
    change_expected_value_positive,
    change_validated,
    impact_assessed,
    proposal_action,
    risk_accepted,
    root_cause_evidence_sufficient,
    srs_baseline_protected,
    version_created,
)

__all__ = [
    "ImprovementEngine",
    "approval_required",
    "benefit_possible",
    "change_expected_value_positive",
    "change_validated",
    "impact_assessed",
    "proposal_action",
    "risk_accepted",
    "root_cause_evidence_sufficient",
    "srs_baseline_protected",
    "version_created",
]
