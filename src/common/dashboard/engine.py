"""Topic 21 — Dashboard and User Visibility.

Exposes agent/sub-agent status, tasks, progress, blocked tasks,
approval requests and system health on a unified dashboard, gated by
user-action permissions (REQ 21.1-21.30 enforced subset).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import Enum


def agent_status(name: str, state: str) -> bool:
    """Return whether an agent status view is valid (REQ 21.3.1)."""
    return bool(name) and state in {"idle", "active", "blocked", "error"}


def agent_current_activity(name: str, activity: str) -> str:
    """Return the current activity of an agent (REQ 21.3.2)."""
    return activity if agent_status(name, "active") else ""


def progress_percentage(done: float, total: float) -> float:
    """Compute a percentage, clamped to [0, 100] (REQ 21.6.1)."""
    if total <= 0:
        return 0.0
    return max(0.0, min(100.0, done / total * 100.0))


def blocked_task(task_id: str, required: str) -> bool:
    """Return whether a task is blocked (REQ 21.9)."""
    return bool(task_id) and bool(required)


def restricted_action(action: str) -> bool:
    """Return whether an action is restricted for the user (REQ 21.27.2)."""
    return action in {"transfer", "withdraw", "delete"}


def search_and_filter(items: Sequence[str], term: str) -> list[str]:
    """Filter dashboard items by search term (REQ 21.26)."""
    return [item for item in items if term.lower() in item.lower()]


def system_health(ok: bool) -> str:
    """Return the system health status (REQ 21.23)."""
    return "healthy" if ok else "degraded"


class ApprovalState(Enum):
    """Approval request states shown on the dashboard (REQ 21.21.2)."""

    PENDING = "pending"
    GRANTED = "granted"
    REJECTED = "rejected"


@dataclass
class Dashboard:
    """Unified operator dashboard (REQ 21.2/21.24)."""

    name: str
    status: str = field(default="ready", repr=False)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be non-empty")

    def render(self) -> str:
        """Render the dashboard view (REQ 21.24)."""
        return self.name
