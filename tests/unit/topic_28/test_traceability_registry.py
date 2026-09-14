"""Tests for Topic 28 registry — Requirement Traceability."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_28_IDS = {
    "28.1",
    "28.2",
    "28.3",
    "28.3.1",
    "28.3.2",
    "28.4",
    "28.5",
    "28.6",
    "28.7",
    "28.8",
    "28.9",
    "28.10",
    "28.10.1",
    "28.10.2",
    "28.11",
    "28.11.1",
    "28.11.2",
    "28.12",
    "28.13",
    "28.14",
    "28.15",
    "28.16",
    "28.17",
    "28.18",
    "28.18.1",
    "28.18.2",
    "28.19",
    "28.19.1",
    "28.20",
    "28.20.1",
    "28.21",
    "28.22",
    "28.23",
    "28.24",
    "28.25",
}


def test_all_topic_28_items_are_registered():
    assert set(REQ_REGISTRY["28"]) == EXPECTED_TOPIC_28_IDS
