"""Bounded synthetic/paper runtime API (SRS Topics 9/18/20/31).

Exposes exactly one execution endpoint that runs the deterministic,
synthetic-only runtime pipeline. It never requires live market data,
broker credentials, or network access, and it cannot place a real order:
the only downstream stage is the paper-trading engine.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.task_runtime.orchestration import RuntimeOrchestrator, RuntimePolicy, SyntheticInput

router = APIRouter(prefix="/run", tags=["runtime"])

#: Request fields that configure the runtime policy rather than the input.
_POLICY_FIELDS = frozenset({"min_score", "max_exposure_fraction", "position_fraction"})


class SyntheticRunRequest(BaseModel):
    """A deterministic synthetic input for a bounded paper-only run."""

    asset: str = Field(min_length=1)
    price: float = Field(gt=0)
    prior_price: float = Field(gt=0)
    volume: float = Field(ge=0)
    avg_volume: float = Field(gt=0)
    volatility: float = Field(ge=0)
    normal_volatility: float = Field(gt=0)
    liquidity: float = Field(ge=0, le=1)
    regime_ok: bool = True
    projected_return: float = 0.10
    risk: float = Field(default=0.15, ge=0, le=1)
    reward: float = Field(default=4.0, ge=0)
    risk_amount: float = Field(default=1.5, gt=0)
    signal: str = Field(default="buy", pattern="^(buy|sell|hold)$")
    fetched_at: str
    as_of: str
    capital: float = Field(default=100_000.0, gt=0)
    virtual_capital: float = Field(default=100_000.0, gt=0)
    data_confidence: float = Field(default=0.9, ge=0, le=1)
    signal_confidence: float = Field(default=0.9, ge=0, le=1)
    #: Deterministic policy overrides (defaults match the frozen paper policy).
    min_score: float = 60.0
    max_exposure_fraction: float = 0.25
    position_fraction: float = 0.10


@router.post("/paper")
def run_paper(request: SyntheticRunRequest) -> dict[str, Any]:
    """Execute one bounded synthetic/paper run through the real runtime."""
    try:
        synthetic = SyntheticInput(**request.model_dump(exclude=set(_POLICY_FIELDS)))
    except (TypeError, ValueError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    policy = RuntimePolicy(
        min_score=request.min_score,
        max_exposure_fraction=request.max_exposure_fraction,
        position_fraction=request.position_fraction,
    )
    result = RuntimeOrchestrator(name="api-runtime", policy=policy).run(synthetic)
    return result.to_dict()
