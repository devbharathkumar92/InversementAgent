"""Tests for the runtime orchestration layer (Topics 9/12-20/23/31).

These tests are the executable proof that the existing deterministic
engines are actually wired into one bounded runtime path:

    INPUT -> VALIDATION -> DISCOVERY -> MARKET ANALYSIS -> SCORING
          -> STRATEGY -> RISK -> DECISION -> PAPER TRADING -> P&L
          -> AUDIT/EVIDENCE

They are written against the repository's real engine contracts and do
not use live market data, brokers, network state, wall-clock time, or
randomness.
"""

import pytest

from src.common.market.engine import sentiment_from, trend_direction
from src.common.monitoring.engine import (
    drawdown,
    net_return,
    real_time_pnl,
)
from src.common.paper.engine import fee_applied, slippage_fill
from src.common.scoring.engine import composite_score
from src.common.strategy.engine import position_size
from src.task_runtime.orchestration import (
    STAGE_ORDER,
    RunStatus,
    RuntimeOrchestrator,
    RuntimePolicy,
    Stage,
    StageRecord,
    SyntheticInput,
)
from src.task_runtime.state_machine.engine import TaskState


def canonical_input(**overrides):
    """Return a fully-populated deterministic synthetic input."""
    data = {
        "asset": "NSE:TESTCO",
        "price": 110.0,
        "prior_price": 100.0,
        "volume": 1_000_000.0,
        "avg_volume": 100_000.0,
        "volatility": 0.40,
        "normal_volatility": 0.20,
        "liquidity": 0.90,
        "regime_ok": True,
        "projected_return": 0.10,
        "risk": 0.15,
        "reward": 4.0,
        "risk_amount": 1.5,
        "signal": "buy",
        "fetched_at": "2026-09-14T09:30:00Z",
        "as_of": "2026-09-14T09:35:00Z",
        "capital": 100_000.0,
        "virtual_capital": 100_000.0,
    }
    data.update(overrides)
    return SyntheticInput(**data)


def orchestrator(**policy_overrides):
    return RuntimeOrchestrator(
        name="runtime",
        policy=RuntimePolicy(**policy_overrides) if policy_overrides else RuntimePolicy(),
    )


class TestRuntimeImport:
    """A — a concrete runtime/orchestrator is importable and executable."""

    def test_orchestrator_exposes_run(self):
        assert callable(RuntimeOrchestrator(name="runtime").run)

    def test_stage_order_is_the_declared_pipeline(self):
        assert [stage.value for stage in STAGE_ORDER] == [
            "INPUT",
            "VALIDATION",
            "DISCOVERY",
            "MARKET_ANALYSIS",
            "SCORING",
            "STRATEGY",
            "RISK",
            "DECISION",
            "PAPER_TRADING",
            "PNL",
            "AUDIT",
        ]


class TestDeterministicSyntheticExecution:
    """B — a deterministic synthetic input runs with no external systems."""

    def test_run_completes_without_external_systems(self):
        result = orchestrator().run(canonical_input())
        assert result.status == RunStatus.COMPLETED
        assert result.state == TaskState.COMPLETED

    def test_existing_engines_are_actually_invoked(self):
        result = orchestrator().run(canonical_input())
        assert result.discovery["engine"] == "DiscoveryEngine"
        assert result.market["engine"] == "MarketAnalysisEngine"
        assert result.scoring["engine"] == "ScoringEngine"
        assert result.strategy["engine"] == "StrategyEngine"
        assert result.risk["engine"] == "RiskEngine"
        assert result.decision["engine"] == "DecisionEngine"
        assert result.paper["engine"] == "PaperEngine"
        assert result.pnl["engine"] == "MonitoringEngine"
        assert result.audit["engine"] == "AuditEngine"


class TestStageOrdering:
    """C — the pipeline executes in the declared order."""

    def test_input_stage_carries_synthetic_provenance(self):
        result = orchestrator().run(canonical_input())
        assert result.input["source"] == "synthetic"
        assert result.input["asset"] == "NSE:TESTCO"
        assert result.input["provenance"]["fetched_at"] == "2026-09-14T09:30:00Z"

    def test_stages_executed_in_declared_order(self):
        result = orchestrator().run(canonical_input())
        assert result.stage_order == [stage.value for stage in STAGE_ORDER]

    def test_every_stage_records_a_status(self):
        result = orchestrator().run(canonical_input())
        assert all(isinstance(record, StageRecord) for record in result.stages)
        assert all(record.status == "ok" for record in result.stages)
        assert result.stages[0].stage == Stage.INPUT
        assert result.stages[-1].stage == Stage.AUDIT


class TestRiskRejection:
    """D — a risk rejection stops paper execution and everything after it."""

    def test_risk_rejection_blocks_paper_execution(self):
        result = orchestrator(max_exposure_fraction=0.001).run(canonical_input())
        assert result.risk["approved"] is False
        assert result.status == RunStatus.REJECTED
        assert result.state == TaskState.REJECTED
        assert result.paper == {}
        assert "PAPER_TRADING" not in result.stage_order
        assert "PNL" not in result.stage_order

    def test_kill_switch_also_blocks(self):
        result = orchestrator(max_drawdown=-1.0).run(canonical_input())
        assert result.risk["approved"] is False
        assert result.paper == {}


class TestDecisionRejection:
    """E — a no-action/rejected decision stops paper execution."""

    def test_no_action_blocks_paper_execution(self):
        result = orchestrator(min_score=99.0).run(canonical_input())
        assert result.decision["approved"] is False
        assert result.decision["action"] == "no_action"
        assert result.status == RunStatus.REJECTED
        assert result.paper == {}
        assert "PAPER_TRADING" not in result.stage_order


class TestPaperExecution:
    """F — an approved decision reaches the paper layer only."""

    def test_approved_decision_reaches_paper_layer(self):
        result = orchestrator().run(canonical_input())
        assert result.decision["approved"] is True
        assert result.decision["action"] == "entry"
        assert result.paper["engine"] == "PaperEngine"
        assert result.paper["side"] == "buy"
        assert result.paper["simulated"] is True
        assert result.paper_only is True

    def test_no_live_broker_artifacts(self):
        result = orchestrator().run(canonical_input())
        assert "broker" not in result.paper
        assert "order_id" not in result.paper


class TestPnl:
    """G — paper execution produces deterministic P&L output."""

    def test_pnl_uses_monitoring_engine_contracts(self):
        result = orchestrator().run(canonical_input())
        policy = RuntimePolicy()
        fill = fee_applied(slippage_fill(110.0, policy.slippage), policy.fee)
        qty = result.paper["qty"]
        expected_gross = real_time_pnl(mark=110.0, entry=fill, qty=qty)
        assert result.pnl["gross_pnl"] == pytest.approx(expected_gross)
        assert result.pnl["net_pnl"] == pytest.approx(
            net_return(gross=expected_gross, fees=result.pnl["fees"], tax=result.pnl["tax"])
        )
        assert result.pnl["tax"] == pytest.approx(max(0.0, expected_gross) * policy.tax)
        assert result.pnl["equity"] == pytest.approx(
            result.paper["cash_after"] + result.paper["notional"]
        )
        assert result.pnl["drawdown"] == pytest.approx(
            drawdown(peak=100_000.0, value=result.pnl["equity"])
        )


class TestAudit:
    """H — execution produces audit/evidence output keyed by a trace id."""

    def test_audit_records_trace_and_events(self):
        result = orchestrator().run(canonical_input())
        assert result.audit["trace_id"] == result.trace_id
        assert result.audit["health"] == "ok"
        assert result.audit["retained"] is True
        assert result.audit["events"][0]["event_type"] == "input"
        assert result.audit["events"][-1]["channel"] == "runtime"

    def test_audit_events_share_the_run_trace(self):
        result = orchestrator().run(canonical_input())
        assert {event["trace_id"] for event in result.audit["events"]} == {result.trace_id}


class TestFailurePropagation:
    """I — an upstream failure stops downstream stages deterministically."""

    def test_validation_failure_stops_downstream(self):
        result = orchestrator().run(canonical_input(fetched_at="2026-09-01T00:00:00Z"))
        assert result.status == RunStatus.REJECTED
        assert result.state == TaskState.REJECTED
        assert result.validation["ok"] is False
        assert result.discovery == {}
        assert "DISCOVERY" not in result.stage_order
        assert result.paper == {}

    def test_discovery_failure_stops_downstream(self):
        def boom(_discovery_engine, _context):
            raise RuntimeError("discovery unavailable")

        orch = orchestrator()
        orch.stage_hooks = {Stage.DISCOVERY: boom}
        result = orch.run(canonical_input())
        assert result.status == RunStatus.FAILED
        assert result.state == TaskState.FAILED
        assert result.failure["stage"] == "DISCOVERY"
        assert result.paper == {}
        assert "PAPER_TRADING" not in result.stage_order

    def test_failure_cannot_bypass_safety(self):
        result = orchestrator(max_exposure_fraction=0.001).run(canonical_input())
        assert result.paper == {}
        assert result.pnl == {}


class TestDeterminism:
    """J — the same synthetic input twice yields equivalent output."""

    def test_repeat_run_is_equivalent(self):
        first = orchestrator().run(canonical_input())
        second = orchestrator().run(canonical_input())
        assert first.to_dict() == second.to_dict()

    def test_trace_id_is_derived_not_random(self):
        result = orchestrator().run(canonical_input())
        assert result.trace_id == "run-NSE:TESTCO-2026-09-14T09:35:00Z"


class TestMarketAndScoringWiring:
    """The market/scoring/strategy stages use the real engine contracts."""

    def test_market_stage_matches_engine_functions(self):
        result = orchestrator().run(canonical_input())
        assert result.market["trend"] == trend_direction([100.0, 110.0])
        assert result.market["regime"] == "bull"
        assert result.market["sentiment"] == sentiment_from(1.0, 1.0)

    def test_scoring_stage_matches_composite_engine(self):
        result = orchestrator().run(canonical_input())
        policy = RuntimePolicy()
        assert result.scoring["score"] == pytest.approx(
            composite_score(result.scoring["components"], policy.score_weights)
        )
        assert result.scoring["acceptable"] is True

    def test_strategy_stage_sizes_position_within_cap(self):
        result = orchestrator().run(canonical_input())
        policy = RuntimePolicy()
        assert result.strategy["size"] == pytest.approx(
            position_size(
                100_000.0, policy.position_fraction, 100_000.0 * policy.max_exposure_fraction
            )
        )
        assert result.strategy["entry_met"] is True


pytestmark = pytest.mark.unit
