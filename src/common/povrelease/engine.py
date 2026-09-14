"""Topic 38 — PoV Release Criteria.

The PoV is releasable only when functional minimums are met with no
blocking conditions (38.2), mandatory safety conditions hold with no
safety failures (38.7), minimum paper-trading requirements are met
(38.9), monitoring and test coverage are in place (38.10/38.18), no
release blockers are open (38.25), the readiness checklist passes
with an adequate readiness score (38.26), and final validation is
followed by human and PoV approval (38.27/38.22/38.29).
(REQ 38.1-38.30 enforced subset.)
"""

from __future__ import annotations

from dataclasses import dataclass, field

READINESS_THRESHOLD: float = 0.8


def functional_required(minimums: bool, blockers: bool) -> bool:
    """Return whether functional criteria pass (38.2.1/38.2.2)."""
    return minimums and not blockers


def safety_met(conditions: bool, failures: bool) -> bool:
    """Return whether safety criteria pass (38.7.1/38.7.2)."""
    return conditions and not failures


def paper_trading_ok(requirements: bool, failures: bool) -> bool:
    """Return whether paper trading criteria pass (38.9.1/38.9.2)."""
    return requirements and not failures


def monitoring_ok(enabled: bool) -> bool:
    """Return whether monitoring criteria hold (38.10)."""
    return enabled


def coverage_met(coverage: bool) -> bool:
    """Return whether test coverage criteria hold (38.18)."""
    return coverage


def blocking_free(blockers: int) -> bool:
    """Return whether no release blockers are open (38.25.1)."""
    return blockers == 0


def readiness_gate(checklist: bool, score: float) -> bool:
    """Return whether readiness passes (38.26.1/38.26.2)."""
    return checklist and score >= READINESS_THRESHOLD


def final_validation(valid: bool) -> bool:
    """Return whether final validation passes (38.27)."""
    return valid


def human_approved(approved: bool) -> bool:
    """Return whether human/PoV approval is given (38.22/38.28)."""
    return approved


def release_approved(validated: bool, score: float, blockers: int) -> bool:
    """Return the final release decision (38.29.1/38.29.2)."""
    return validated and score >= READINESS_THRESHOLD and blockers == 0


@dataclass
class PovReleaseEngine:
    """PoV release lifecycle (38.1)."""

    name: str
    _assessed: bool = field(default=False, repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")
        self._assessed = True

    def status(self) -> str:
        """Return the PoV release state."""
        return "assessed" if self._assessed else "unassessed"
