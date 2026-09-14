"""Tests for Topic 26 registry — Self-Improvement and Change Management."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_26_IDS = {
    "26.1",
    "26.2",
    "26.3",
    "26.3.1",
    "26.3.2",
    "26.4",
    "26.5",
    "26.5.1",
    "26.5.2",
    "26.6",
    "26.6.1",
    "26.6.2",
    "26.7",
    "26.8",
    "26.8.1",
    "26.8.2",
    "26.9",
    "26.10",
    "26.11",
    "26.12",
    "26.13",
    "26.13.1",
    "26.13.2",
    "26.14",
    "26.14.1",
    "26.14.2",
    "26.15",
    "26.16",
    "26.17",
    "26.18",
    "26.18.1",
    "26.18.2",
    "26.19",
    "26.20",
    "26.21",
    "26.22",
    "26.23",
    "26.24",
    "26.25",
    "26.25.1",
    "26.25.2",
    "26.26",
    "26.26.1",
    "26.27",
    "26.27.1",
    "26.28",
    "26.29",
    "26.30",
}


def test_all_topic_26_items_are_registered():
    assert set(REQ_REGISTRY["26"]) == EXPECTED_TOPIC_26_IDS
