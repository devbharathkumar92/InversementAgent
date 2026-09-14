"""Tests for Topic 29 registry — Sub-Agent Architecture."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_29_IDS = {
    "29.1",
    "29.2",
    "29.2.1",
    "29.2.2",
    "29.3",
    "29.3.1",
    "29.3.2",
    "29.4",
    "29.4.1",
    "29.4.2",
    "29.5",
    "29.6",
    "29.7",
    "29.8",
    "29.9",
    "29.10",
    "29.11",
    "29.12",
    "29.13",
    "29.14",
    "29.15",
    "29.15.1",
    "29.15.2",
    "29.16",
    "29.17",
    "29.18",
    "29.19",
    "29.19.1",
    "29.19.2",
    "29.20",
    "29.20.1",
    "29.20.2",
    "29.21",
    "29.21.1",
    "29.21.2",
    "29.22",
    "29.23",
    "29.24",
    "29.25",
    "29.26",
    "29.27",
    "29.28",
    "29.29",
    "29.30",
}


def test_all_topic_29_items_are_registered():
    assert set(REQ_REGISTRY["29"]) == EXPECTED_TOPIC_29_IDS
