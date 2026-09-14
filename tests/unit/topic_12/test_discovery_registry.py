"""Tests for Topic 12 registry — Opportunity Discovery traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_12_IDS = {
    "12.1",
    "12.2",
    "12.3",
    "12.4",
    "12.5",
    "12.5.1",
    "12.5.2",
    "12.6",
    "12.6.1",
    "12.6.2",
    "12.7",
    "12.8",
    "12.9",
    "12.10",
    "12.11",
    "12.12",
    "12.13",
    "12.14",
    "12.14.1",
    "12.14.2",
    "12.15",
    "12.16",
    "12.17",
    "12.17.1",
    "12.17.2",
    "12.18",
    "12.18.1",
    "12.18.2",
    "12.19",
    "12.19.1",
    "12.19.2",
    "12.20",
    "12.21",
    "12.21.1",
    "12.21.2",
    "12.22",
    "12.23",
    "12.24",
    "12.25",
    "12.26",
    "12.27",
    "12.28",
    "12.29",
    "12.30",
}


def test_all_topic_12_items_are_registered():
    assert set(REQ_REGISTRY["12"]) == EXPECTED_TOPIC_12_IDS
