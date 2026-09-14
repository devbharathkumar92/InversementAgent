"""Tests for Topic 20 registry — Monitoring and P&L Management."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_20_IDS = {
    "20.1",
    "20.2",
    "20.3",
    "20.4",
    "20.5",
    "20.6",
    "20.7",
    "20.8",
    "20.9",
    "20.10",
    "20.11",
    "20.12",
    "20.13",
    "20.14",
    "20.14.1",
    "20.14.2",
    "20.14.3",
    "20.15",
    "20.16",
    "20.17",
    "20.18",
    "20.18.1",
    "20.18.2",
    "20.19",
    "20.20",
    "20.21",
    "20.22",
    "20.22.1",
    "20.22.2",
    "20.23",
    "20.24",
    "20.25",
    "20.26",
    "20.27",
    "20.28",
    "20.29",
    "20.30",
}


def test_all_topic_20_items_are_registered():
    assert set(REQ_REGISTRY["20"]) == EXPECTED_TOPIC_20_IDS
