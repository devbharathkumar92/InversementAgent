"""Controlled task lifecycle state machine (SRS Topic 9 / Topic 31).

The runtime executes one bounded task per run. The lifecycle is the
smallest compatible one required by the SRS lifecycle rules
(REQ 9.14/9.17/9.22/9.27):

    CREATED -> VALIDATING -> RUNNING -> COMPLETED

with the controlled terminal states ``REJECTED`` (a gate refused the
task) and ``FAILED`` (an upstream stage errored). Undefined transitions
are rejected fail-closed so no stage can run out of order and no
terminal run can be resumed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class TaskState(StrEnum):
    """The declared task lifecycle states."""

    CREATED = "CREATED"
    VALIDATING = "VALIDATING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


TERMINAL_STATES: frozenset[TaskState] = frozenset(
    {TaskState.COMPLETED, TaskState.REJECTED, TaskState.FAILED}
)

_TRANSITIONS: dict[TaskState, frozenset[TaskState]] = {
    TaskState.CREATED: frozenset({TaskState.VALIDATING, TaskState.REJECTED, TaskState.FAILED}),
    TaskState.VALIDATING: frozenset({TaskState.RUNNING, TaskState.REJECTED, TaskState.FAILED}),
    TaskState.RUNNING: frozenset({TaskState.COMPLETED, TaskState.REJECTED, TaskState.FAILED}),
    TaskState.COMPLETED: frozenset(),
    TaskState.REJECTED: frozenset(),
    TaskState.FAILED: frozenset(),
}


class InvalidTransitionError(ValueError):
    """Raised when a transition is not permitted from the current state."""


@dataclass
class TaskStateMachine:
    """Tracks a single task's state and records its state lineage."""

    state: TaskState = TaskState.CREATED
    history: list[TaskState] = field(default_factory=lambda: [TaskState.CREATED])

    def is_terminal(self) -> bool:
        """Return whether the task has reached a terminal state."""
        return self.state in TERMINAL_STATES

    def allows(self, target: TaskState) -> bool:
        """Return whether a transition to ``target`` is permitted."""
        return target in _TRANSITIONS[self.state]

    def transition(self, target: TaskState) -> TaskState:
        """Move to ``target`` or raise, leaving state unchanged on failure."""
        if not self.allows(target):
            raise InvalidTransitionError(f"{self.state} -> {target} is not permitted")
        self.state = target
        self.history.append(target)
        return self.state
