"""Topic 2.13 — goal deviation detection (drift away from the approved goal)."""

from __future__ import annotations


class GoalDeviation(Exception):
    """Raised when work moves away from the approved goal."""


def _shares_vocabulary(work_item: str, current_goal: str) -> bool:
    item_words = set(work_item.lower().replace("-", " ").split())
    goal_words = set(current_goal.lower().replace("-", " ").split())
    return bool(item_words & goal_words)


class GoalDeviationDetector:
    """Detects gradual drift by checking topic vocabulary alignment."""

    def monitor(self, work_item: str, current_goal: str) -> GoalDeviation | None:
        if not work_item or not work_item.strip():
            raise GoalDeviation("work_item must be non-empty")
        if not _shares_vocabulary(work_item, current_goal):
            return GoalDeviation(
                f"work item {work_item!r} does not align with the approved goal {current_goal!r}"
            )
        return None
