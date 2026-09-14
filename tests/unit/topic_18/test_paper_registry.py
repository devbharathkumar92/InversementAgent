"""Tests for Topic 18 registry — Paper Trading Engine traceability."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_18_IDS = {
    "18.1",
    "18.2",
    "18.2.1",
    "18.2.2",
    "18.3",
    "18.4",
    "18.4.1",
    "18.4.2",
    "18.5",
    "18.5.1",
    "18.5.2",
    "18.6",
    "18.7",
    "18.8",
    "18.9",
    "18.10",
    "18.11",
    "18.11.1",
    "18.11.2",
    "18.12",
    "18.13",
    "18.14",
    "18.15",
    "18.16",
    "18.17",
    "18.18",
    "18.19",
    "18.20",
    "18.21",
    "18.22",
    "18.22.1",
    "18.22.2",
    "18.23",
    "18.24",
    "18.25",
    "18.26",
    "18.27",
    "18.28",
    "18.28.1",
    "18.28.2",
    "18.29",
    "18.30",
}


def test_all_topic_18_items_are_registered():
    assert set(REQ_REGISTRY["18"]) == EXPECTED_TOPIC_18_IDS
