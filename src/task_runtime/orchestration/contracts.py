"""Runtime orchestration contracts (SRS Topics 9/18/20/31).

Declares the bounded, deterministic contract used to connect the
existing engines into one executable path:

    INPUT -> VALIDATION -> DISCOVERY -> MARKET ANALYSIS -> SCORING
          -> STRATEGY -> RISK -> DECISION -> PAPER TRADING -> P&L
          -> AUDIT/EVIDENCE

The scope is synthetic/paper only: there is no broker, no live market
data source, and no real-money path anywhere in this module.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field, fields, is_dataclass
from enum import StrEnum
from typing import Any

from src.task_runtime.state_machine.engine import TaskState


class Stage(StrEnum):
    """The ordered pipeline stages of the runtime."""

    INPUT = "INPUT"
    VALIDATION = "VALIDATION"
    DISCOVERY = "DISCOVERY"
    MARKET_ANALYSIS = "MARKET_ANALYSIS"
    SCORING = "SCORING"
    STRATEGY = "STRATEGY"
    RISK = "RISK"
    DECISION = "DECISION"
    PAPER_TRADING = "PAPER_TRADING"
    PNL = "PNL"
    AUDIT = "AUDIT"


#: The explicit, frozen stage ordering the orchestrator executes.
STAGE_ORDER: tuple[Stage, ...] = tuple(Stage)


class RunStatus(StrEnum):
    """The terminal status of a runtime execution."""

    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class SyntheticInput:
    """A fully-specified synthetic market input (no live data required)."""

    asset: str
    price: float
    prior_price: float
    volume: float
    avg_volume: float
    volatility: float
    normal_volatility: float
    liquidity: float
    regime_ok: bool
    projected_return: float
    risk: float
    reward: float
    risk_amount: float
    signal: str
    fetched_at: str
    as_of: str
    capital: float
    virtual_capital: float
    data_confidence: float = 0.9
    signal_confidence: float = 0.9


@dataclass
class RuntimePolicy:
    """Deterministic, explicit thresholds and gates for one runtime."""

    max_data_age_s: float = 3600.0
    position_fraction: float = 0.10
    max_exposure_fraction: float = 0.25
    max_concentration_fraction: float = 0.20
    max_loss_fraction: float = 0.05
    max_drawdown: float = 0.20
    slippage: float = 0.001
    fee: float = 0.001
    tax: float = 0.10
    min_score: float = 60.0
    risk_reward_min: float = 1.5
    min_liquidity: float = 0.5
    momentum_threshold: float = 3.0
    paper_window_days: int = 30
    audit_retention_days: float = 730.0
    score_weights: dict[str, float] = field(
        default_factory=lambda: {
            "return": 0.30,
            "risk": 0.25,
            "risk_reward": 0.20,
            "prob": 0.15,
            "data_confidence": 0.10,
        }
    )


@dataclass(frozen=True)
class StageRecord:
    """The observable outcome of a single pipeline stage."""

    stage: Stage
    status: str
    detail: str = ""


def _plain(value: Any) -> Any:
    """Recursively convert a value into deterministic, JSON-safe data."""
    if isinstance(value, StrEnum):
        return value.value
    if is_dataclass(value) and not isinstance(value, type):
        return {f.name: _plain(getattr(value, f.name)) for f in fields(value)}
    if isinstance(value, Mapping):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


@dataclass
class ExecutionResult:
    """The bounded, serialisable outcome of one runtime execution."""

    trace_id: str
    status: RunStatus
    state: TaskState
    stages: list[StageRecord]
    stage_order: list[str]
    input: dict[str, Any]
    validation: dict[str, Any] = field(default_factory=dict)
    discovery: dict[str, Any] = field(default_factory=dict)
    market: dict[str, Any] = field(default_factory=dict)
    scoring: dict[str, Any] = field(default_factory=dict)
    strategy: dict[str, Any] = field(default_factory=dict)
    risk: dict[str, Any] = field(default_factory=dict)
    decision: dict[str, Any] = field(default_factory=dict)
    paper: dict[str, Any] = field(default_factory=dict)
    pnl: dict[str, Any] = field(default_factory=dict)
    audit: dict[str, Any] = field(default_factory=dict)
    failure: dict[str, Any] = field(default_factory=dict)
    paper_only: bool = True

    def to_dict(self) -> dict[str, Any]:
        """Return a deterministic, serialisable representation."""
        return _plain(self)  # type: ignore[no-any-return]
