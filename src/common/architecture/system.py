"""Topic 6 — High-Level System Architecture.

The architecture enforces declared layers, a guarded system state
machine, and strict execution-mode gating: simulation/paper-trading
first, live execution only after explicit governance authorization
(REQ 6.4/6.12/6.22).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


def _require_non_empty(value: object, label: str) -> None:
    if value is None:
        raise ValueError(f"{label} must be provided")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{label} must be non-empty")


class SystemState(StrEnum):
    """The defined architectural system states (REQ 6.22.1)."""

    INIT = "INIT"
    RUNNING = "RUNNING"
    BLOCKED = "BLOCKED"
    RECOVERING = "RECOVERING"
    TERMINAL = "TERMINAL"


class ExecutionMode(StrEnum):
    """Run-time execution modes; live is strictly gated (REQ 6.12)."""

    SIMULATION = "SIMULATION"
    PAPER = "PAPER"
    LIVE = "LIVE"


# how each of the topological layers may transition; simple guarded table
_VALID_TRANSITIONS: dict[SystemState, set[SystemState]] = {
    SystemState.INIT: {SystemState.RUNNING},
    SystemState.RUNNING: {SystemState.BLOCKED, SystemState.TERMINAL},
    SystemState.BLOCKED: {SystemState.RECOVERING, SystemState.TERMINAL},
    SystemState.RECOVERING: {SystemState.RUNNING, SystemState.BLOCKED, SystemState.TERMINAL},
    SystemState.TERMINAL: set(),
}


def transition_state(current: SystemState, target: SystemState) -> bool:
    """Return whether a state transition is permitted (REQ 6.22.2)."""
    return target in _VALID_TRANSITIONS.get(current, set())


@dataclass
class ArchitectureLayer:
    """A declared architectural layer (REQ 6.4/6.19)."""

    name: str
    component_id: str
    supports_simulation: bool

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")
        _require_non_empty(self.component_id, "component_id")


def is_execution_layer(layer: ArchitectureLayer) -> bool:
    """Return whether a layer is part of the live execution authority.

    Execution layers do NOT participate in simulation mode; the
    analysis/decision authority is separated from live execution.
    """
    return not layer.supports_simulation


def allow_execution(mode: ExecutionMode, layer_name: str) -> bool:
    """Return whether the mode permits the named execution layer."""
    if layer_name == "execution":
        return mode == ExecutionMode.LIVE
    return mode in {ExecutionMode.SIMULATION, ExecutionMode.PAPER}


@dataclass
class SystemArchitecture:
    """The controlled system architecture definition (REQ 6.1/6.4)."""

    name: str = ""
    layers: list[ArchitectureLayer] = field(default_factory=list)
    state: SystemState = SystemState.INIT
    _execution_mode: ExecutionMode = ExecutionMode.SIMULATION
    _live_authorization: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        _require_non_empty(self.name, "name")
        self._live_authorization = []

    def has_layer(self, name: str) -> bool:
        return any(layer.name == name for layer in self.layers)

    def layer_by_id(self, component_id: str) -> ArchitectureLayer | None:
        for layer in self.layers:
            if layer.component_id == component_id:
                return layer
        return None

    def execution_mode(self) -> ExecutionMode:
        return self._execution_mode

    def set_execution_mode(self, mode: object) -> None:
        """Set the run-time execution mode; unknown modes rejected."""
        if not isinstance(mode, ExecutionMode):
            raise ValueError(f"unknown execution mode: {mode}")
        if mode == ExecutionMode.LIVE and not self._live_authorization:
            raise ValueError("live execution requires governance authorization")
        self._execution_mode = mode

    def authorize_live(self, authorization_id: str) -> None:
        """Record explicit governance authorization for live mode."""
        _require_non_empty(authorization_id, "authorization_id")
        self._live_authorization.append(authorization_id)

    def live_allowed(self) -> bool:
        return self._execution_mode == ExecutionMode.LIVE and bool(self._live_authorization)

    def enter_blocked(self, reason: str) -> None:
        _require_non_empty(reason, "reason")
        self.state = SystemState.BLOCKED

    def recover(self) -> bool:
        if transition_state(self.state, SystemState.RECOVERING):
            self.state = SystemState.RECOVERING
            return True
        if self.state == SystemState.BLOCKED:
            self.state = SystemState.RECOVERING
            return True
        return False

    def start_execution(self) -> bool:
        """Start execution only if the layer is expected in current mode."""
        if not allow_execution(self._execution_mode, "execution"):
            return False
        if self.state != SystemState.INIT:
            return False
        return True
