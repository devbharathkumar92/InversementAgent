"""Tests for Topic 6 registry — System Architecture item traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_6_IDS = {
    "6.1",
    "6.2",
    "6.3",
    "6.3.1",
    "6.3.2",
    "6.4",
    "6.5",
    "6.6",
    "6.7",
    "6.8",
    "6.9",
    "6.10",
    "6.11",
    "6.12",
    "6.13",
    "6.14",
    "6.15",
    "6.16",
    "6.17",
    "6.17.1",
    "6.17.2",
    "6.18",
    "6.18.1",
    "6.18.2",
    "6.19",
    "6.19.1",
    "6.19.2",
    "6.20",
    "6.21",
    "6.21.1",
    "6.21.2",
    "6.22",
    "6.22.1",
    "6.22.2",
    "6.23",
    "6.23.1",
    "6.23.2",
    "6.24",
    "6.25",
    "6.26",
    "6.27",
    "6.28",
    "6.29",
    "6.30",
}


def test_all_topic_6_items_are_registered():
    assert set(REQ_REGISTRY["6"]) == EXPECTED_TOPIC_6_IDS
