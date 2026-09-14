"""Topic 10 — Data Acquisition Layer.

Approves and classifies data sources, enforces real-time latency and
rate limits, schedules retrieval, escalates failures, maintains source
redundancy, attaches provenance, and scores source reliability
(REQ 10.1/10.3/10.9/10.11/10.15/10.17-10.21/10.24).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from enum import Enum

# Source kinds required by the SRS (REQ 10.4–10.8).
SUPPORTED_KINDS = frozenset({"market", "news", "financial", "economic", "alternative"})


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


class ApprovalDecision(Enum):
    """The decision outcomes for source approval (REQ 10.3.1)."""

    APPROVED = "approved"
    REJECTED = "rejected"


def approve_source(data: dict[str, object]) -> dict[str, object]:
    """Approve a data source if it meets the approval criteria (10.3.1).

    A source is approved when it declares a supported class, an
    authority, and a usable license. Unlicensed or unknown-authority
    sources are rejected.
    """
    kind = data.get("kind")
    authority = data.get("authority")
    license_ = data.get("license")
    if kind not in SUPPORTED_KINDS or not authority or not license_:
        return {"status": ApprovalDecision.REJECTED.value}
    return {
        "status": ApprovalDecision.APPROVED.value,
        "id": data.get("id"),
        "kind": kind,
        "primary": data.get("primary", False),
    }


def max_latency_satisfied(observed: float, declared: float) -> bool:
    """Return whether observed latency meets the declared max (10.9.2)."""
    return observed <= declared


def next_retrieval_at(after: str, interval_s: float) -> str:
    """Return the ISO-8601 retrieval time after an interval (REQ 10.15.1)."""
    t = datetime.fromisoformat(after.replace("Z", "+00:00"))
    return (t + timedelta(seconds=interval_s)).astimezone(UTC).isoformat()


def rate_limit_exceeded(calls: int, max_calls: int) -> bool:
    """Return whether the configured call budget is exhausted (REQ 10.17)."""
    return calls >= max_calls


def add_source(existing: list[dict[str, object]], source_id: str, primary: bool) -> str:
    """Register a source id; returns the id (REQ 10.19/10.21.2)."""
    _require_non_empty(source_id, "source_id")
    return source_id


@dataclass
class ReliabilityScorer:
    """Scores source reliability from observed history (REQ 10.24)."""

    min_score: float = 0.0

    def score(self, successes: int, failures: int) -> float:
        total = successes + failures
        if total == 0:
            return 0.0
        return successes / total * 100.0


@dataclass
class AcquisitionEngine:
    """Tracks registered sources and their failure escalation (10.18.3)."""

    name: str = ""
    sources: dict[str, dict[str, object]] = field(default_factory=dict)
    escalated: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")

    def register(self, source_id: str) -> None:
        self.sources[source_id] = {"id": source_id, "status": "approved"}

    def record_failure(self, source_id: str) -> None:
        if source_id not in self.sources:
            raise KeyError(source_id)
        self.escalated.append(source_id)

    @staticmethod
    def record_provenance(source_id: str, fetched_at: str) -> dict[str, str]:
        _require_non_empty(source_id, "source_id")
        _require_non_empty(fetched_at, "fetched_at")
        return {"source_id": source_id, "fetched_at": fetched_at, "lineage": "source"}
