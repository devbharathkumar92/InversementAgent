"""Topic 10 — Data Acquisition Layer.

Source approval and classification, real-time latency checks, rate
limits, failure escalation, redundancy, provenance metadata, and
reliability scoring.
"""

from .engine import (
    AcquisitionEngine,
    ApprovalDecision,
    ReliabilityScorer,
    add_source,
    approve_source,
    max_latency_satisfied,
    next_retrieval_at,
    rate_limit_exceeded,
)

__all__ = [
    "AcquisitionEngine",
    "ApprovalDecision",
    "ReliabilityScorer",
    "add_source",
    "approve_source",
    "max_latency_satisfied",
    "next_retrieval_at",
    "rate_limit_exceeded",
]
