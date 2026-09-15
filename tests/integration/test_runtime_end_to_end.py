"""End-to-end integration test for the runtime orchestration path.

Proves the real wiring through the public interface:

    HTTP request -> FastAPI endpoint -> RuntimeOrchestrator -> Input
      -> Validation -> Discovery -> Market Analysis -> Scoring
      -> Strategy -> Risk -> Decision -> Paper Trading -> P&L
      -> Audit/Evidence -> HTTP response

Nothing is mocked: the endpoint calls the real orchestrator, which calls
each existing engine. There is no live market data, broker, credential,
or network dependency in this path.
"""

import pytest
from fastapi.testclient import TestClient

from src.api.v1.main import app

client = TestClient(app)

PAYLOAD = {
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


def test_health_still_works():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


@pytest.mark.integration
def test_paper_run_reaches_completion_through_real_components():
    resp = client.post("/run/paper", json=PAYLOAD)
    assert resp.status_code == 200

    body = resp.json()
    assert body["status"] == "COMPLETED"
    assert body["state"] == "COMPLETED"
    assert body["paper_only"] is True

    assert [stage["stage"] for stage in body["stages"]] == [
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

    assert body["discovery"]["engine"] == "DiscoveryEngine"
    assert body["market"]["engine"] == "MarketAnalysisEngine"
    assert body["scoring"]["engine"] == "ScoringEngine"
    assert body["strategy"]["engine"] == "StrategyEngine"
    assert body["risk"]["approved"] is True
    assert body["decision"]["approved"] is True
    assert body["paper"]["engine"] == "PaperEngine"
    assert body["paper"]["simulated"] is True
    assert body["pnl"]["engine"] == "MonitoringEngine"
    assert body["audit"]["engine"] == "AuditEngine"
    assert body["audit"]["trace_id"] == body["trace_id"]
    assert body["pnl"]["equity"] > 0


@pytest.mark.integration
def test_paper_run_is_deterministic_across_requests():
    first = client.post("/run/paper", json=PAYLOAD).json()
    second = client.post("/run/paper", json=PAYLOAD).json()
    assert first == second


@pytest.mark.integration
def test_risk_rejection_never_reaches_paper_stage():
    resp = client.post("/run/paper", json={**PAYLOAD, "max_exposure_fraction": 0.001})
    assert resp.status_code == 200

    body = resp.json()
    assert body["status"] == "REJECTED"
    assert body["risk"]["approved"] is False
    assert body["paper"] == {}
    assert "PAPER_TRADING" not in [stage["stage"] for stage in body["stages"]]


@pytest.mark.integration
def test_no_action_decision_never_reaches_paper_stage():
    resp = client.post("/run/paper", json={**PAYLOAD, "min_score": 99.0})
    assert resp.status_code == 200

    body = resp.json()
    assert body["status"] == "REJECTED"
    assert body["decision"]["action"] == "no_action"
    assert body["paper"] == {}


@pytest.mark.integration
def test_validation_failure_stops_execution():
    stale = {**PAYLOAD, "fetched_at": "2026-09-01T00:00:00Z"}
    body = client.post("/run/paper", json=stale).json()
    assert body["status"] == "REJECTED"
    assert body["validation"]["ok"] is False
    assert body["discovery"] == {}


@pytest.mark.integration
def test_invalid_payload_is_rejected_before_execution():
    resp = client.post("/run/paper", json={**PAYLOAD, "price": -1})
    assert resp.status_code == 422
