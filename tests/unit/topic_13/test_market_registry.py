"""Tests for Topic 13 registry — Market Analysis traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_13_IDS = {
    "13.1",
    "13.2",
    "13.3",
    "13.4",
    "13.5",
    "13.6",
    "13.7",
    "13.8",
    "13.8.1",
    "13.8.2",
    "13.9",
    "13.10",
    "13.10.1",
    "13.10.2",
    "13.11",
    "13.11.1",
    "13.11.2",
    "13.12",
    "13.13",
    "13.14",
    "13.15",
    "13.16",
    "13.17",
    "13.17.1",
    "13.17.2",
    "13.18",
    "13.18.1",
    "13.18.2",
    "13.19",
    "13.19.1",
    "13.19.2",
    "13.20",
    "13.21",
    "13.21.1",
    "13.21.2",
    "13.22",
    "13.23",
    "13.24",
    "13.25",
    "13.26",
    "13.27",
    "13.28",
    "13.29",
    "13.30",
}


def test_all_topic_13_items_are_registered():
    assert set(REQ_REGISTRY["13"]) == EXPECTED_TOPIC_13_IDS
