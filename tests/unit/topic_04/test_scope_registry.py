"""Tests for Topic 4 registry — System Scope item traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_4_IDS = {
    "4.1",
    "4.2",
    "4.2.1",
    "4.2.2",
    "4.3",
    "4.3.1",
    "4.4",
    "4.5",
    "4.6",
    "4.7",
    "4.7.1",
    "4.7.2",
    "4.7.3",
    "4.8",
    "4.9",
    "4.10",
    "4.10.1",
    "4.10.2",
    "4.11",
    "4.12",
    "4.13",
    "4.14",
    "4.15",
    "4.15.1",
    "4.15.2",
    "4.16",
    "4.17",
    "4.18",
    "4.19",
    "4.20",
    "4.21",
    "4.21.1",
    "4.21.2",
    "4.22",
    "4.23",
    "4.24",
    "4.25",
    "4.25.1",
    "4.25.2",
}


def test_all_topic_4_items_are_registered():
    assert set(REQ_REGISTRY["4"]) == EXPECTED_TOPIC_4_IDS
