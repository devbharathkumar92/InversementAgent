"""Topic 2.7/2.7.1/2.7.2 — non-negotiable goal conditions and violation detection."""

from __future__ import annotations

from collections.abc import Mapping
from enum import Enum


class GoalViolation(Enum):
    """Direct goal violations (Topic 2.7.2)."""

    UNAPPROVED_PURPOSE_CHANGE = "unapproved_purpose_change"
    GEOGRAPHIC_SCOPE_EXPANSION = "geographic_scope_expansion"
    CURRENCY_SCOPE_EXPANSION = "currency_scope_expansion"
    SAFETY_BYPASS = "safety_bypass"
    UNAUTHORIZED_EXECUTION = "unauthorized_execution"
    EVIDENCE_BYPASS = "evidence_bypass"


class GoalViolationDetector:
    """Deterministically detect direct goal violations from events."""

    def detect(
        self, event: Mapping[str, object], current: Mapping[str, object]
    ) -> GoalViolation | None:
        event_type = event.get("type")

        if event_type == "safety_bypass":
            return GoalViolation.SAFETY_BYPASS
        if event_type == "evidence_bypass":
            return GoalViolation.EVIDENCE_BYPASS
        if event_type == "unauthorized_execution":
            return GoalViolation.UNAUTHORIZED_EXECUTION
        if event_type == "purpose_change" and not current.get("approved"):
            return GoalViolation.UNAPPROVED_PURPOSE_CHANGE
        if event_type == "scope_change":
            geo = event.get("geography")
            cur = event.get("currency")
            current_geo = current.get("geography")
            current_cur = current.get("currency")
            if geo and current_geo and geo != current_geo:
                return GoalViolation.GEOGRAPHIC_SCOPE_EXPANSION
            if cur and current_cur and cur != current_cur:
                return GoalViolation.CURRENCY_SCOPE_EXPANSION
        return None
