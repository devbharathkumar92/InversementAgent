"""Topic 1.10 — scheduled and event-triggered document review cycle."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import Enum


class ReviewOutcome(Enum):
    """Outcomes of a document review (REQ 1.10)."""

    ACCEPTED = "accepted"
    CHANGE_REQUIRED = "change_required"
    REBASELINE_REQUIRED = "rebaseline_required"


@dataclass
class ReviewCycle:
    """Review cadence plus event-triggered review conditions.

    A review is triggered when a defined event condition is present. The
    review decision itself is recorded (traceable).
    """

    cadence_days: int
    event_conditions: Mapping[str, bool] = field(default_factory=dict)

    def should_trigger(self, event: Mapping[str, bool] | None = None) -> bool:
        """Return whether a review is required for the given event state."""
        if not event:
            return False
        return any(self.event_conditions.get(k, False) for k in event if event[k])

    def record_outcome(self, outcome: str) -> ReviewOutcome:
        """Validate and return the recorded review outcome."""
        try:
            return ReviewOutcome(outcome)
        except ValueError:
            raise ValueError(
                f"Unknown review outcome: {outcome!r}; expected one of "
                f"{[o.value for o in ReviewOutcome]}"
            ) from None
