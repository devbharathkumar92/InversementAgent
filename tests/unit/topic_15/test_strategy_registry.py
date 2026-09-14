"""Tests for Topic 15 registry — Strategy Engine traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_15_IDS = {
    "15.1",
    "15.2",
    "15.2.1",
    "15.2.2",
    "15.3",
    "15.4",
    "15.4.1",
    "15.4.2",
    "15.5",
    "15.5.1",
    "15.5.2",
    "15.6",
    "15.6.1",
    "15.6.2",
    "15.7",
    "15.7.1",
    "15.7.2",
    "15.8",
    "15.9",
    "15.9.1",
    "15.9.2",
    "15.10",
    "15.10.1",
    "15.10.2",
    "15.11",
    "15.12",
    "15.13",
    "15.14",
    "15.15",
    "15.16",
    "15.17",
    "15.18",
    "15.18.1",
    "15.18.2",
    "15.19",
    "15.20",
    "15.21",
    "15.22",
    "15.23",
    "15.24",
    "15.25",
    "15.26",
    "15.27",
    "15.28",
    "15.29",
    "15.30",
}


def test_all_topic_15_items_are_registered():
    assert set(REQ_REGISTRY["15"]) == EXPECTED_TOPIC_15_IDS
