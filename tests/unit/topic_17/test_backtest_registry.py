"""Tests for Topic 17 registry — Backtesting & Simulation traceability."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_17_IDS = {
    "17.1",
    "17.2",
    "17.2.1",
    "17.2.2",
    "17.3",
    "17.4",
    "17.4.1",
    "17.4.2",
    "17.5",
    "17.6",
    "17.7",
    "17.8",
    "17.9",
    "17.9.1",
    "17.9.2",
    "17.10",
    "17.11",
    "17.12",
    "17.12.1",
    "17.12.2",
    "17.13",
    "17.14",
    "17.15",
    "17.16",
    "17.17",
    "17.18",
    "17.19",
    "17.19.1",
    "17.19.2",
    "17.20",
    "17.20.1",
    "17.21",
    "17.21.1",
    "17.21.2",
    "17.22",
    "17.23",
    "17.24",
    "17.25",
    "17.26",
    "17.27",
    "17.28",
    "17.29",
    "17.30",
}


def test_all_topic_17_items_are_registered():
    assert set(REQ_REGISTRY["17"]) == EXPECTED_TOPIC_17_IDS
