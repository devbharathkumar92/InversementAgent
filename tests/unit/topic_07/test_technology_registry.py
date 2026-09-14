"""Tests for Topic 7 registry — Technology item traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_7_IDS = {
    "7.1",
    "7.1.1",
    "7.1.2",
    "7.2",
    "7.3",
    "7.4",
    "7.5",
    "7.6",
    "7.7",
    "7.7.1",
    "7.7.2",
    "7.8",
    "7.9",
    "7.9.1",
    "7.9.2",
    "7.10",
    "7.12",
    "7.13",
    "7.14",
    "7.15",
    "7.16",
    "7.17",
    "7.18",
    "7.18.1",
    "7.18.2",
    "7.19",
    "7.20",
    "7.21",
    "7.22",
    "7.23",
    "7.24",
    "7.25",
    "7.26",
    "7.26.1",
    "7.26.2",
    "7.28",
    "7.28.1",
    "7.28.2",
    "7.29",
    "7.29.1",
    "7.29.2",
    "7.30",
    "7.31",
}


def test_all_topic_7_items_are_registered():
    assert set(REQ_REGISTRY["7"]) == EXPECTED_TOPIC_7_IDS
