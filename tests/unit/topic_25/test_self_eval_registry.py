"""Tests for Topic 25 registry — Self-Evaluation."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_25_IDS = {
    "25.1",
    "25.2",
    "25.2.1",
    "25.2.2",
    "25.3",
    "25.3.1",
    "25.3.2",
    "25.4",
    "25.5",
    "25.6",
    "25.7",
    "25.8",
    "25.9",
    "25.10",
    "25.11",
    "25.12",
    "25.13",
    "25.14",
    "25.15",
    "25.16",
    "25.17",
    "25.18",
    "25.19",
    "25.20",
    "25.20.1",
    "25.20.2",
    "25.21",
    "25.21.1",
    "25.21.2",
    "25.22",
    "25.23",
    "25.24",
    "25.24.1",
    "25.24.2",
    "25.25",
    "25.26",
    "25.26.1",
    "25.26.2",
    "25.27",
    "25.28",
    "25.29",
    "25.30",
}


def test_all_topic_25_items_are_registered():
    assert set(REQ_REGISTRY["25"]) == EXPECTED_TOPIC_25_IDS
