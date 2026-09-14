"""Tests for Topic 6 — High-Level System Architecture.

Covers architecture layer registry (6.4), layer authority separation
(6.5/6.12), system state machine (6.22), PoV-mode gating (6.4/6.12),
and failure/blocked handling (6.23/6.24).
"""

import pytest

from src.common.architecture.system import (
    ArchitectureLayer,
    ExecutionMode,
    SystemArchitecture,
    SystemState,
    allow_execution,
    is_execution_layer,
    transition_state,
)


def make_architecture(**overrides):
    data = {
        "name": "InversementAgent Architecture",
        "layers": [
            ArchitectureLayer("data", "data-acquisition", supports_simulation=True),
            ArchitectureLayer("intelligence", "market-analysis", supports_simulation=True),
            ArchitectureLayer("decision", "decision-engine", supports_simulation=True),
            ArchitectureLayer("execution", "execution-engine", supports_simulation=False),
            ArchitectureLayer("monitoring", "monitoring", supports_simulation=True),
        ],
    }
    data.update(overrides)
    return SystemArchitecture(**data)


class TestArchitectureLayers:
    """REQ 6.4/6.5 — core layers are declared with authority."""

    def test_required_layer_registered(self):
        arch = make_architecture()
        assert arch.has_layer("execution") is True

    def test_layer_ids_machine_readable(self):
        arch = make_architecture()
        assert arch.layer_by_id("decision-engine").name == "decision"

    def test_unknown_layer_not_found(self):
        arch = make_architecture()
        assert arch.layer_by_id("nexus") is None


class TestExecutionSeparation:
    """REQ 6.4/6.12 — analysis/decision/execution authority separation."""

    def test_execution_layer_flagged(self):
        assert is_execution_layer(ArchitectureLayer("x", "exec", supports_simulation=False)) is True

    def test_analysis_layer_not_execution(self):
        assert (
            is_execution_layer(ArchitectureLayer("decision", "d", supports_simulation=True))
            is False
        )

    def test_execution_requires_live(self):
        # Execution layers do not participate in simulation mode.
        arch = make_architecture()
        assert allow_execution(arch.execution_mode(), "execution") is False


class TestStateMachine:
    """REQ 6.22/6.22.1/6.22.2 — defined states + guarded transitions."""

    def test_initial_state(self):
        arch = make_architecture()
        assert arch.state == SystemState.INIT

    def test_valid_init_to_running(self):
        assert transition_state(SystemState.INIT, SystemState.RUNNING) is True

    def test_invalid_run_to_init(self):
        assert transition_state(SystemState.RUNNING, SystemState.INIT) is False

    def test_blocked_and_recovery(self):
        assert transition_state(SystemState.RUNNING, SystemState.BLOCKED) is True
        assert transition_state(SystemState.BLOCKED, SystemState.RECOVERING) is True

    def test_terminal_rejects_further(self):
        assert transition_state(SystemState.TERMINAL, SystemState.RUNNING) is False


class TestPoVGating:
    """REQ 6.4/6.12 — PoV restricts execution to simulation/paper."""

    def test_default_mode_is_simulation(self):
        arch = make_architecture()
        assert arch.execution_mode() == ExecutionMode.SIMULATION

    def test_live_mode_rejected_by_default(self):
        arch = make_architecture()
        assert arch.live_allowed() is False

    def test_mode_override_to_paper(self):
        arch = make_architecture()
        arch.set_execution_mode(ExecutionMode.PAPER)
        assert arch.execution_mode() == ExecutionMode.PAPER

    def test_live_only_after_authorization(self):
        arch = make_architecture()
        arch.authorize_live("governance-approval-001")
        arch.set_execution_mode(ExecutionMode.LIVE)
        assert arch.live_allowed() is True

    def test_live_without_authorization_rejected(self):
        arch = make_architecture()
        with pytest.raises(ValueError):
            arch.set_execution_mode(ExecutionMode.LIVE)

    def test_invalid_mode_rejected(self):
        arch = make_architecture()
        with pytest.raises(ValueError):
            arch.set_execution_mode("rocket-mode")


class TestFailureArchitecture:
    """REQ 6.23/6.24 — failure isolation and recovery states."""

    def test_blocked_arch_can_recover(self):
        arch = make_architecture()
        arch.enter_blocked("exec-engine-failure")
        assert arch.state == SystemState.BLOCKED
        assert arch.recover() is True

    def test_failed_execution_cannot_start(self):
        arch = make_architecture()
        arch.set_execution_mode(ExecutionMode.PAPER)
        arch.enter_blocked("no-funds")
        assert arch.start_execution() is False


pytestmark = pytest.mark.unit
