"""Tests for Topic 8 registry — Determinism item traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_8_IDS = {
    "8.1",
    "8.2",
    "8.3",
    "8.4",
    "8.4.1",
    "8.4.2",
    "8.5",
    "8.5.1",
    "8.5.2",
    "8.6",
    "8.6.1",
    "8.6.2",
    "8.7",
    "8.7.1",
    "8.7.2",
    "8.8",
    "8.9",
    "8.10",
    "8.11",
    "8.12",
    "8.13",
    "8.14",
    "8.15",
    "8.16",
    "8.17",
    "8.17.1",
    "8.18",
    "8.18.1",
    "8.18.2",
    "8.19",
    "8.20",
    "8.20.1",
    "8.20.2",
    "8.21",
    "8.21.1",
    "8.21.2",
    "8.22",
    "8.23",
    "8.24",
    "8.25",
    "8.26",
    "8.27",
    "8.28",
    "8.29",
    "8.30",
    "8.31",
}


def test_all_topic_8_items_are_registered():
    assert set(REQ_REGISTRY["8"]) == EXPECTED_TOPIC_8_IDS
