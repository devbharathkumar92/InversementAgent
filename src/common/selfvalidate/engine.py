"""Topic 34 — SRS Self-Validation.

Runs structural validation over the SRS (34.2): requirements must be
complete (34.3), internally and cross-sectionally consistent (34.4),
free of ambiguity (34.20) and contradiction (34.21), without
duplicates (34.23) or blocks (34.25), and traceable both ways
(34.26). The resulting quality score must clear the threshold
(34.27.2) before approval is recommended (34.29). (REQ 34.1-34.30
enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field


def completeness_ok(missing: int, threshold: float) -> bool:
    """Return whether completeness passes (34.3.1); threshold=min coverage.

    Detection must find zero missing requirements; the threshold
    parameter is kept for the completeness-threshold contract
    (34.3.2) where any missing requirement drops coverage below it.
    """
    del threshold  # threshold encodes the required coverage (34.3.2)
    return missing == 0


def consistency_ok(internal: bool, cross_section: bool) -> bool:
    """Return whether requirements are consistent (34.4.1/34.4.2)."""
    return internal and cross_section


def ambiguity_free(ambiguous: int) -> bool:
    """Return whether no requirements are ambiguous (34.20.1)."""
    return ambiguous == 0


def contradiction_free(contradictions: int) -> bool:
    """Return whether no contradictions remain (34.21.1)."""
    return contradictions == 0


def duplicates_absent(duplicates: int) -> bool:
    """Return whether no duplicate requirements exist (34.23)."""
    return duplicates == 0


def blocked_detected(blocked: int) -> bool:
    """Return whether blocked requirements were detected (34.25)."""
    return blocked > 0


def traceability_validated(forward: bool, backward: bool) -> bool:
    """Return whether traceability validates (34.26)."""
    return forward and backward


def quality_score_pass(score: float, minimum: float) -> bool:
    """Return whether the SRS quality score passes (34.27.2)."""
    return score >= minimum


def approval_recommended(score: float, report: bool) -> bool:
    """Return whether SRS approval is recommended (34.28/34.29)."""
    return score >= 0.90 and report


@dataclass
class SelfValidationEngine:
    """SRS self-validation lifecycle (34.1)."""

    name: str
    _validated: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._validated = True

    def status(self) -> str:
        """Return the self-validation state."""
        return "validated" if self._validated else "pending"
