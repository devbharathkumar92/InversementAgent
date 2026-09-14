"""Tests for Topic 39 registry — Future Expansion Framework."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_39_IDS = {
    "39.1",
    "39.2",
    "39.3",
    "39.3.1",
    "39.3.2",
    "39.4",
    "39.4.1",
    "39.4.2",
    "39.5",
    "39.5.1",
    "39.5.2",
    "39.6",
    "39.7",
    "39.7.1",
    "39.7.2",
    "39.8",
    "39.9",
    "39.10",
    "39.11",
    "39.12",
    "39.13",
    "39.14",
    "39.15",
    "39.15.1",
    "39.15.2",
    "39.16",
    "39.17",
    "39.18",
    "39.19",
    "39.20",
    "39.21",
    "39.22",
    "39.23",
    "39.24",
    "39.25",
    "39.25.1",
    "39.25.2",
    "39.26",
    "39.26.1",
    "39.26.2",
    "39.27",
    "39.28",
    "39.29",
    "39.30",
}


def test_all_topic_39_items_are_registered():
    assert set(REQ_REGISTRY["39"]) == EXPECTED_TOPIC_39_IDS
