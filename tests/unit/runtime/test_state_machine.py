"""Tests for the task-runtime state machine.

Covers the controlled task lifecycle
(``CREATED -> VALIDATING -> RUNNING -> COMPLETED`` with terminal
``REJECTED`` / ``FAILED``), fail-closed transition rejection, and state
lineage recording.
"""

import pytest

from src.task_runtime.state_machine.engine import (
    TERMINAL_STATES,
    InvalidTransitionError,
    TaskState,
    TaskStateMachine,
)


class TestInitialState:
    """A task starts in CREATED with its lineage recorded."""

    def test_starts_created(self):
        machine = TaskStateMachine()
        assert machine.state == TaskState.CREATED

    def test_history_starts_with_created(self):
        machine = TaskStateMachine()
        assert machine.history == [TaskState.CREATED]


class TestHappyPath:
    """The declared lifecycle runs CREATED -> VALIDATING -> RUNNING
    -> COMPLETED and is terminal at COMPLETED (REQ 9.14/9.27)."""

    def test_full_lifecycle(self):
        machine = TaskStateMachine()
        machine.transition(TaskState.VALIDATING)
        machine.transition(TaskState.RUNNING)
        machine.transition(TaskState.COMPLETED)
        assert machine.state == TaskState.COMPLETED
        assert machine.is_terminal() is True

    def test_history_order_preserved(self):
        machine = TaskStateMachine()
        machine.transition(TaskState.VALIDATING)
        machine.transition(TaskState.RUNNING)
        assert machine.history == [
            TaskState.CREATED,
            TaskState.VALIDATING,
            TaskState.RUNNING,
        ]


class TestRejectionAndFailure:
    """REJECTED and FAILED stop execution and are terminal."""

    def test_validation_rejected(self):
        machine = TaskStateMachine()
        machine.transition(TaskState.REJECTED)
        assert machine.state == TaskState.REJECTED
        assert machine.is_terminal() is True

    def test_running_failed(self):
        machine = TaskStateMachine()
        machine.transition(TaskState.VALIDATING)
        machine.transition(TaskState.RUNNING)
        machine.transition(TaskState.FAILED)
        assert machine.is_terminal() is True

    def test_terminal_states_are_closed(self):
        assert TERMINAL_STATES == {
            TaskState.COMPLETED,
            TaskState.REJECTED,
            TaskState.FAILED,
        }


class TestInvalidTransitions:
    """Undefined transitions fail closed and never mutate state."""

    def test_created_cannot_jump_to_running(self):
        machine = TaskStateMachine()
        with pytest.raises(InvalidTransitionError):
            machine.transition(TaskState.RUNNING)
        assert machine.state == TaskState.CREATED

    def test_terminal_state_is_frozen(self):
        machine = TaskStateMachine()
        machine.transition(TaskState.REJECTED)
        with pytest.raises(InvalidTransitionError):
            machine.transition(TaskState.RUNNING)

    def test_cannot_complete_without_running(self):
        machine = TaskStateMachine()
        machine.transition(TaskState.VALIDATING)
        with pytest.raises(InvalidTransitionError):
            machine.transition(TaskState.COMPLETED)


pytestmark = pytest.mark.unit
