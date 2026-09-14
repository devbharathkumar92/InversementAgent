"""Tests for Topic 19 registry — Decision Engine traceability."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_19_IDS = {
    "19.1",
    "19.2",
    "19.2.1",
    "19.2.2",
    "19.3",
    "19.3.1",
    "19.3.2",
    "19.4",
    "19.5",
    "19.6",
    "19.7",
    "19.8",
    "19.8.1",
    "19.8.2",
    "19.9",
    "19.10",
    "19.11",
    "19.12",
    "19.12.1",
    "19.12.2",
    "19.13",
    "19.14",
    "19.15",
    "19.16",
    "19.17",
    "19.18",
    "19.19",
    "19.19.1",
    "19.19.2",
    "19.20",
    "19.20.1",
    "19.20.2",
    "19.20.3",
    "19.21",
    "19.22",
    "19.23",
    "19.24",
    "19.25",
    "19.26",
    "19.27",
    "19.28",
    "19.29",
    "19.30",
}


def test_all_topic_19_items_are_registered():
    assert set(REQ_REGISTRY["19"]) == EXPECTED_TOPIC_19_IDS
