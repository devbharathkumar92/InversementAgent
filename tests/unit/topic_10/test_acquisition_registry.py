"""Tests for Topic 10 registry — Data Acquisition traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_10_IDS = {
    "10.1",
    "10.2",
    "10.3",
    "10.3.1",
    "10.3.2",
    "10.3.3",
    "10.3.4",
    "10.3.5",
    "10.4",
    "10.5",
    "10.6",
    "10.7",
    "10.8",
    "10.9",
    "10.9.1",
    "10.9.2",
    "10.10",
    "10.11",
    "10.12",
    "10.13",
    "10.14",
    "10.15",
    "10.15.1",
    "10.15.2",
    "10.16",
    "10.17",
    "10.18",
    "10.18.1",
    "10.18.2",
    "10.18.3",
    "10.19",
    "10.19.1",
    "10.19.2",
    "10.20",
    "10.21",
    "10.21.1",
    "10.21.2",
    "10.22",
    "10.23",
    "10.24",
    "10.25",
    "10.26",
    "10.27",
    "10.28",
    "10.29",
    "10.30",
}


def test_all_topic_10_items_are_registered():
    assert set(REQ_REGISTRY["10"]) == EXPECTED_TOPIC_10_IDS
