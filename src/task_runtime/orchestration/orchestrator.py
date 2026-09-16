"""Runtime orchestrator — the executable pipeline entry point.

Connects the existing deterministic engines into one bounded,
paper-only path (SRS Topics 9/10-20/23/31):

    INPUT -> VALIDATION -> DISCOVERY -> MARKET ANALYSIS -> SCORING
          -> STRATEGY -> RISK -> DECISION -> PAPER TRADING -> P&L
          -> AUDIT/EVIDENCE

The orchestrator contains no component business logic: every stage
delegates to the engine that owns it. Engines are injected so the
runtime is testable and remains free of live brokers, live market data,
network state, wall-clock time, and randomness.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from src.common.audit.engine import (
    AuditEngine,
    AuditEvent,
    capture_event,
    event_required_or_optional,
    retention_allowed,
    trace_id_generated,
)
from src.common.decision.engine import (
    DecisionEngine,
    capital_eligible,
    decision_priority,
    decision_rejected,
    eligibility_met,
    entry_decision,
    no_action,
)
from src.common.discovery.engine import (
    DiscoveryEngine,
    confidence_from,
    detect_momentum,
    detect_volatility_expansion,
    detect_volume_spike,
    rank_opportunities,
)
from src.common.market.engine import (
    MarketAnalysisEngine,
    analyze_news_impact,
    sentiment_from,
    trend_direction,
)
from src.common.monitoring.engine import (
    MonitoringEngine,
    anomaly_detected,
    benchmark_comparison,
    capital_level_ok,
    drawdown,
    net_return,
    real_time_pnl,
)
from src.common.paper.engine import (
    PaperEngine,
    cash_after_trade,
    fee_applied,
    position_size,
    slippage_fill,
    validate_order,
    virtual_capital_valid,
)
from src.common.quality.engine import (
    QualityEngine,
    confidence_score,
    is_complete,
    is_fresh,
    is_valid_timestamp,
)
from src.common.risk.engine import (
    RiskEngine,
    concentration_exceeded,
    exposes_within_limit,
    kill_switch_triggered,
    loss_within_limit,
)
from src.common.scoring.engine import ScoringEngine, composite_score
from src.common.strategy.engine import (
    StrategyEngine,
    entry_met,
    fails_requirements,
)
from src.common.strategy.engine import (
    position_size as strategy_position_size,
)
from src.task_runtime.orchestration.contracts import (
    STAGE_ORDER,
    ExecutionResult,
    RunStatus,
    RuntimePolicy,
    Stage,
    StageRecord,
    SyntheticInput,
)
from src.task_runtime.state_machine.engine import TaskState, TaskStateMachine

_REQUIRED_FIELDS: tuple[str, ...] = (
    "asset",
    "price",
    "prior_price",
    "volume",
    "avg_volume",
    "volatility",
    "liquidity",
    "fetched_at",
    "as_of",
)

_EQUITY_PEAK = 100_000.0

StageHook = Callable[[Any, dict[str, Any]], dict[str, Any] | None]


class RuntimeOrchestrator:
    """Executes the bounded synthetic/paper runtime pipeline."""

    def __init__(
        self,
        name: str,
        policy: RuntimePolicy | None = None,
        stages_hooks: dict[Stage, StageHook] | None = None,
    ) -> None:
        if not name.strip():
            raise ValueError("name must be non-empty")
        self.name = name
        self.policy = policy or RuntimePolicy()
        self.stage_hooks: dict[Stage, StageHook] = stages_hooks or {}

        self.quality_engine = QualityEngine(name="quality")
        self.discovery_engine = DiscoveryEngine(name="discovery")
        self.market_engine = MarketAnalysisEngine(name="market")
        self.scoring_engine = ScoringEngine(name="scoring")
        self.strategy_engine = StrategyEngine(name="strategy")
        self.risk_engine = RiskEngine(name="risk")
        self.decision_engine = DecisionEngine(name="decision")
        self.paper_engine = PaperEngine(name="paper", window_days=self.policy.paper_window_days)
        self.monitoring_engine = MonitoringEngine(name="monitoring")
        self.audit_engine = AuditEngine(name="audit")

    # -- public API ---------------------------------------------------------

    def run(self, data: SyntheticInput) -> ExecutionResult:
        """Execute the full pipeline against one synthetic input."""
        context: dict[str, Any] = {"input": data, "policy": self.policy}
        state = TaskStateMachine()
        stages: list[StageRecord] = []
        order: list[str] = []
        audit_events: list[AuditEvent] = []

        result = ExecutionResult(
            trace_id=f"run-{data.asset}-{data.as_of}",
            status=RunStatus.FAILED,
            state=TaskState.CREATED,
            stages=stages,
            stage_order=order,
            input={},
        )

        state.transition(TaskState.VALIDATING)

        for stage, handler in (
            (Stage.INPUT, self._stage_input),
            (Stage.VALIDATION, self._stage_validation),
        ):
            failure = self._guarded(
                result, stages, order, audit_events, state, stage, context, handler
            )
            if failure is not None:
                return self._finalise(result, state, stages, order, audit_events, failure)

        if not result.validation["ok"]:
            state.transition(TaskState.REJECTED)
            return self._finalise(result, state, stages, order, audit_events, None)

        state.transition(TaskState.RUNNING)

        for stage, stage_handler in self._running_stages():
            outcome = self._guarded(
                result, stages, order, audit_events, state, stage, context, stage_handler
            )
            if outcome is not None:
                return self._finalise(result, state, stages, order, audit_events, outcome)
            gate = context.get("gate")
            if gate is not None:
                state.transition(TaskState.REJECTED)
                return self._finalise(result, state, stages, order, audit_events, None)

        state.transition(TaskState.COMPLETED)
        return self._finalise(result, state, stages, order, audit_events, None)

    # -- stage plan ---------------------------------------------------------

    def _running_stages(self) -> list[tuple[Stage, Callable[[dict[str, Any]], dict[str, Any]]]]:
        return [
            (Stage.DISCOVERY, self._stage_discovery),
            (Stage.MARKET_ANALYSIS, self._stage_market),
            (Stage.SCORING, self._stage_scoring),
            (Stage.STRATEGY, self._stage_strategy),
            (Stage.RISK, self._stage_risk),
            (Stage.DECISION, self._stage_decision),
            (Stage.PAPER_TRADING, self._stage_paper),
            (Stage.PNL, self._stage_pnl),
        ]

    def _guarded(
        self,
        result: ExecutionResult,
        stages: list[StageRecord],
        order: list[str],
        audit_events: list[AuditEvent],
        state: TaskStateMachine,
        stage: Stage,
        context: dict[str, Any],
        handler: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    ) -> dict[str, Any] | None:
        """Run one stage, converting any failure into a deterministic result."""
        hook = self.stage_hooks.get(stage)
        try:
            if hook is not None:
                output = hook(self._engine_for(stage), context) or {}
            elif handler is None:
                output = {"accepted": True}
            else:
                output = handler(context)
        except Exception as exc:  # noqa: BLE001 - failure must become a bounded result
            return {"stage": stage.value, "error": f"{type(exc).__name__}: {exc}"}

        stages.append(StageRecord(stage=stage, status="ok"))
        order.append(stage.value)
        audit_events.append(
            AuditEvent(channel="runtime", event_type=stage.value.lower(), trace_id=result.trace_id)
        )
        context.setdefault("stages", {})[stage] = output
        if stage == Stage.INPUT:
            result.input = output
        else:
            setattr(result, _ATTRIBUTE_FOR[stage], output)
        return None

    def _engine_for(self, stage: Stage) -> Any:
        return {
            Stage.INPUT: self.quality_engine,
            Stage.DISCOVERY: self.discovery_engine,
            Stage.MARKET_ANALYSIS: self.market_engine,
            Stage.SCORING: self.scoring_engine,
            Stage.STRATEGY: self.strategy_engine,
            Stage.RISK: self.risk_engine,
            Stage.DECISION: self.decision_engine,
            Stage.PAPER_TRADING: self.paper_engine,
            Stage.PNL: self.monitoring_engine,
            Stage.AUDIT: self.audit_engine,
        }[stage]

    # -- individual stages --------------------------------------------------

    def _stage_input(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        return {
            "engine": "SyntheticInput",
            "asset": data.asset,
            "as_of": data.as_of,
            "source": "synthetic",
            "provenance": {"source_id": "synthetic", "fetched_at": data.fetched_at},
        }

    def _stage_validation(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        record = {name: getattr(data, name) for name in _REQUIRED_FIELDS}
        complete = is_complete(record, _REQUIRED_FIELDS) and self.quality_engine.integrity_ok(
            record, _REQUIRED_FIELDS
        )
        timestamps_ok = is_valid_timestamp(data.fetched_at) and is_valid_timestamp(data.as_of)
        fresh = is_fresh(data.fetched_at, self.policy.max_data_age_s, data.as_of)
        return {
            "engine": "QualityEngine",
            "ok": bool(complete and timestamps_ok and fresh),
            "complete": complete,
            "timestamps_ok": timestamps_ok,
            "fresh": fresh,
            "confidence": confidence_score(1 if fresh else 0, 1),
        }

    def _stage_discovery(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        move_pct = (data.price - data.prior_price) / data.prior_price * 100.0
        record = {
            "liquid": data.liquidity >= self.policy.min_liquidity,
            "regime_ok": data.regime_ok,
        }
        qualified = self.discovery_engine.qualifies(record)
        ranked = rank_opportunities([{"asset": data.asset, "score": abs(move_pct)}])
        confidence = confidence_from(data.signal_confidence, data.data_confidence)
        output = {
            "engine": "DiscoveryEngine",
            "qualified": qualified,
            "momentum": detect_momentum(move_pct, self.policy.momentum_threshold),
            "move_pct": move_pct,
            "volume_spike": detect_volume_spike(data.volume, data.avg_volume),
            "volatility_expansion": detect_volatility_expansion(
                data.volatility, data.normal_volatility
            ),
            "confidence": confidence,
            "ranked": ranked,
        }
        if not qualified:
            context["gate"] = {"stage": Stage.DISCOVERY.value, "reason": "not_qualified"}
        return output

    def _stage_market(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        momentum = (data.price - data.prior_price) / data.prior_price * 100.0
        analysis = self.market_engine.analyze({"momentum": momentum, "volatility": data.volatility})
        score = _SIGNAL_SCORES.get(data.signal, 0.0)
        return {
            "engine": "MarketAnalysisEngine",
            "trend": trend_direction([data.prior_price, data.price]),
            "regime": analysis["regime"],
            "sentiment": sentiment_from(score, 1.0),
            "news_impact": analyze_news_impact(negative=0, positive=1),
            "above_sma": self.market_engine.above_sma(data.price, data.prior_price),
        }

    def _stage_scoring(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        components = {
            "return": self.scoring_engine.return_potential_score(data.projected_return),
            "risk": self.scoring_engine.risk_score(data.risk),
            "risk_reward": self.scoring_engine.risk_reward_score(data.reward, data.risk_amount),
            "prob": confidence_from(data.signal_confidence, data.data_confidence) * 100.0,
            "data_confidence": data.data_confidence * 100.0,
        }
        score = composite_score(components, self.policy.score_weights)
        return {
            "engine": "ScoringEngine",
            "components": components,
            "score": score,
            "acceptable": self.scoring_engine.acceptable(score, self.policy.min_score),
            "ranked": self.scoring_engine.rank([{"asset": data.asset, "score": score}]),
        }

    def _stage_strategy(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        max_size = data.capital * self.policy.max_exposure_fraction
        size = strategy_position_size(data.capital, self.policy.position_fraction, max_size)
        snapshot = {
            "regime": "bull" if data.price > data.prior_price else "bear",
            "signal": data.signal,
        }
        requirements_failed = fails_requirements(
            reward=data.reward,
            risk=data.risk_amount,
            risk_reward_min=self.policy.risk_reward_min,
            liquidity=data.liquidity,
            min_liquidity=self.policy.min_liquidity,
        )
        output = {
            "engine": "StrategyEngine",
            "entry_met": entry_met(snapshot, {"signal": data.signal}),
            "size": size,
            "max_size": max_size,
            "requirements_failed": requirements_failed,
        }
        if requirements_failed:
            context["gate"] = {"stage": Stage.STRATEGY.value, "reason": "requirements_failed"}
        return output

    def _stage_risk(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        requested = data.capital * self.policy.position_fraction
        cap = data.capital * self.policy.max_exposure_fraction
        exposure_ok = exposes_within_limit(requested, cap)
        concentration_ok = not concentration_exceeded(
            requested / data.capital, self.policy.max_concentration_fraction
        )
        potential_loss = requested * data.risk
        loss_ok = loss_within_limit(potential_loss, data.capital * self.policy.max_loss_fraction)
        kill_switch_ok = not kill_switch_triggered(0.0, self.policy.max_drawdown)

        threat = requested / cap if cap > 0 else float("inf")
        if RiskEngine.escalate(threat, 1.0):
            self.risk_engine.escalations.append(threat)

        approved = exposure_ok and concentration_ok and loss_ok and kill_switch_ok
        output = {
            "engine": "RiskEngine",
            "approved": approved,
            "exposure_ok": exposure_ok,
            "concentration_ok": concentration_ok,
            "loss_ok": loss_ok,
            "kill_switch_ok": kill_switch_ok,
            "exposure": requested,
            "exposure_cap": cap,
            "monitor": self.risk_engine.monitor(),
        }
        if not approved:
            context["gate"] = {"stage": Stage.RISK.value, "reason": "risk_rejected"}
        return output

    def _stage_decision(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        score = context["stages"][Stage.SCORING]["score"]
        size = context["stages"][Stage.STRATEGY]["size"]
        self.decision_engine.validate(True)

        entry_ok = entry_decision(score, self.policy.min_score)
        candidates = {"entry": 1.0 if entry_ok else 0.0, "no_action": 0.0 if entry_ok else 1.0}
        action = decision_priority(candidates)
        eligible = eligibility_met(score / 100.0, 1.0, 1.0 - data.risk)
        funded = capital_eligible(size, data.capital)
        not_risk_rejected = not decision_rejected(0.0, self.policy.max_drawdown)
        approved = action == "entry" and eligible and funded and not_risk_rejected
        if not approved and action == "entry":
            action = "no_action"
        if not entry_ok:
            action = "no_action"

        output = {
            "engine": "DecisionEngine",
            "action": action,
            "approved": approved,
            "eligible": eligible,
            "funded": funded,
            "no_action": no_action(score, self.policy.min_score),
            "score": score,
        }
        if not approved:
            context["gate"] = {"stage": Stage.DECISION.value, "reason": output["action"]}
        return output

    def _stage_paper(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        size = context["stages"][Stage.STRATEGY]["size"]
        if not virtual_capital_valid(data.virtual_capital):
            raise ValueError("virtual capital must be positive")

        fill = fee_applied(slippage_fill(data.price, self.policy.slippage), self.policy.fee)
        side = "buy" if data.signal == "buy" else "sell"
        qty = position_size(fill, size)
        validate_order(side=side, qty=qty, price=fill)
        cost = fill * qty
        cash_after = cash_after_trade(data.virtual_capital, cost)
        return {
            "engine": "PaperEngine",
            "simulated": True,
            "side": side,
            "qty": qty,
            "fill_price": fill,
            "cost": cost,
            "cash_after": cash_after,
            "notional": data.price * qty,
            "monitor": self.paper_engine.monitor(),
        }

    def _stage_pnl(self, context: dict[str, Any]) -> dict[str, Any]:
        data: SyntheticInput = context["input"]
        paper = context["stages"][Stage.PAPER_TRADING]
        gross = real_time_pnl(mark=data.price, entry=paper["fill_price"], qty=paper["qty"])
        fees = paper["cost"] * self.policy.fee
        tax = max(0.0, gross) * self.policy.tax
        equity = paper["cash_after"] + paper["notional"]
        return {
            "engine": "MonitoringEngine",
            "position": paper["qty"],
            "mark": data.price,
            "gross_pnl": gross,
            "fees": fees,
            "tax": tax,
            "net_pnl": net_return(gross=gross, fees=fees, tax=tax),
            "equity": equity,
            "drawdown": drawdown(peak=_EQUITY_PEAK, value=equity),
            "capital_ok": capital_level_ok(data.virtual_capital, 0.0),
            "alert": "breached"
            if anomaly_detected(gross, self.policy.max_drawdown * _EQUITY_PEAK)
            else "normal",
            "benchmark_outperformed": benchmark_comparison(gross, 0.0),
            "status": self.monitoring_engine.status(),
        }

    # -- finalisation -------------------------------------------------------

    def _finalise(
        self,
        result: ExecutionResult,
        state: TaskStateMachine,
        stages: list[StageRecord],
        order: list[str],
        audit_events: list[AuditEvent],
        failure: dict[str, Any] | None,
    ) -> ExecutionResult:
        result.state = state.state
        if failure is not None:
            if not state.is_terminal():
                state.transition(TaskState.FAILED)
                result.state = state.state
            result.status = RunStatus.FAILED
            result.failure = failure
        elif state.state == TaskState.REJECTED:
            result.status = RunStatus.REJECTED
        else:
            result.status = RunStatus.COMPLETED

        result.audit = self._build_audit(result, audit_events)
        stages.append(StageRecord(stage=Stage.AUDIT, status="ok"))
        order.append(Stage.AUDIT.value)
        result.stages = stages
        result.stage_order = order
        return result

    def _build_audit(
        self, result: ExecutionResult, audit_events: list[AuditEvent]
    ) -> dict[str, Any]:
        return {
            "engine": "AuditEngine",
            "trace_id": result.trace_id,
            "health": self.audit_engine.health(),
            "trace_id_generated": trace_id_generated(result.trace_id),
            "captured": all(
                capture_event(
                    event.event_type, event_required_or_optional(event.event_type) == "required"
                )
                for event in audit_events
            ),
            "retained": retention_allowed(0.0, self.policy.audit_retention_days),
            "events": [
                {
                    "channel": event.channel,
                    "event_type": event.event_type,
                    "trace_id": event.trace_id,
                }
                for event in audit_events
            ],
        }


_ATTRIBUTE_FOR: dict[Stage, str] = {
    Stage.VALIDATION: "validation",
    Stage.DISCOVERY: "discovery",
    Stage.MARKET_ANALYSIS: "market",
    Stage.SCORING: "scoring",
    Stage.STRATEGY: "strategy",
    Stage.RISK: "risk",
    Stage.DECISION: "decision",
    Stage.PAPER_TRADING: "paper",
    Stage.PNL: "pnl",
}

_SIGNAL_SCORES: dict[str, float] = {"buy": 1.0, "sell": -1.0, "hold": 0.0}

#: The ordered pipeline stages, re-exported for callers/tests.
__all__ = ["RuntimeOrchestrator", "STAGE_ORDER"]
