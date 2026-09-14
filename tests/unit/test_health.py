"""Health endpoint smoke test (bootstrap infrastructure)."""

import pytest
from fastapi.testclient import TestClient

from src.api.v1.main import app

client = TestClient(app)


@pytest.mark.unit
def test_health_returns_ok() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
