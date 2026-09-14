"""Tests for Topic 24 registry — Error Detection and Recovery."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_24_IDS = {
    "24.1",
    "24.2",
    "24.2.1",
    "24.2.2",
    "24.3",
    "24.4",
    "24.5",
    "24.6",
    "24.7",
    "24.8",
    "24.9",
    "24.10",
    "24.11",
    "24.12",
    "24.13",
    "24.14",
    "24.15",
    "24.15.1",
    "24.15.2",
    "24.16",
    "24.16.1",
    "24.16.2",
    "24.17",
    "24.17.1",
    "24.17.2",
    "24.18",
    "24.18.1",
    "24.18.2",
    "24.19",
    "24.19.1",
    "24.19.2",
    "24.20",
    "24.21",
    "24.22",
    "24.23",
    "24.24",
    "24.25",
    "24.25.1",
    "24.25.2",
    "24.26",
    "24.27",
    "24.28",
    "24.29",
    "24.30",
}


def test_all_topic_24_items_are_registered():
    assert set(REQ_REGISTRY["24"]) == EXPECTED_TOPIC_24_IDS
