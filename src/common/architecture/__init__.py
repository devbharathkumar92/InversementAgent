"""Topic 6 — High-Level System Architecture.

Declares the architectural layer contract, execution-mode gating
(simulation / paper-trading first, live strictly authorized), and the
guarded system state machine.
"""

from .system import (
    ArchitectureLayer,
    ExecutionMode,
    SystemArchitecture,
    SystemState,
    allow_execution,
    is_execution_layer,
    transition_state,
)

__all__ = [
    "ArchitectureLayer",
    "ExecutionMode",
    "SystemArchitecture",
    "SystemState",
    "allow_execution",
    "is_execution_layer",
    "transition_state",
]
