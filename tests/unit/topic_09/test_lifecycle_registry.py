"""Tests for Topic 9 registry — Lifecycle item traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_9_IDS = {
    "9.1",
    "9.2",
    "9.2.1",
    "9.2.2",
    "9.3",
    "9.4",
    "9.5",
    "9.6",
    "9.7",
    "9.8",
    "9.9",
    "9.10",
    "9.11",
    "9.12",
    "9.13",
    "9.14",
    "9.14.1",
    "9.14.2",
    "9.15",
    "9.15.1",
    "9.15.2",
    "9.16",
    "9.17",
    "9.17.1",
    "9.17.2",
    "9.18",
    "9.19",
    "9.20",
    "9.21",
    "9.22",
    "9.22.1",
    "9.22.2",
    "9.23",
    "9.24",
    "9.25",
    "9.26",
    "9.27",
    "9.27.1",
    "9.27.2",
    "9.28",
    "9.29",
    "9.30",
    "9.31",
    "9.32",
    "9.33",
    "9.34",
}


def test_all_topic_9_items_are_registered():
    assert set(REQ_REGISTRY["9"]) == EXPECTED_TOPIC_9_IDS
