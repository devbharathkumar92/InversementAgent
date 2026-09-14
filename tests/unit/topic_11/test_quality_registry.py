"""Tests for Topic 11 registry — Data Quality traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_11_IDS = {
    "11.1",
    "11.2",
    "11.2.1",
    "11.2.2",
    "11.3",
    "11.3.1",
    "11.3.2",
    "11.4",
    "11.5",
    "11.6",
    "11.7",
    "11.8",
    "11.9",
    "11.10",
    "11.10.1",
    "11.10.2",
    "11.11",
    "11.12",
    "11.12.1",
    "11.12.2",
    "11.13",
    "11.14",
    "11.15",
    "11.16",
    "11.17",
    "11.18",
    "11.19",
    "11.20",
    "11.20.1",
    "11.20.2",
    "11.21",
    "11.22",
    "11.22.1",
    "11.22.2",
    "11.22.3",
    "11.23",
    "11.24",
    "11.25",
    "11.26",
    "11.27",
    "11.28",
    "11.29",
    "11.30",
}


def test_all_topic_11_items_are_registered():
    assert set(REQ_REGISTRY["11"]) == EXPECTED_TOPIC_11_IDS
