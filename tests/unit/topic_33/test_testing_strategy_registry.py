"""Tests for Topic 33 registry — Testing Strategy."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_33_IDS = {
    "33.1",
    "33.2",
    "33.3",
    "33.4",
    "33.4.1",
    "33.4.2",
    "33.5",
    "33.6",
    "33.6.1",
    "33.6.2",
    "33.7",
    "33.8",
    "33.9",
    "33.10",
    "33.11",
    "33.11.1",
    "33.11.2",
    "33.12",
    "33.13",
    "33.14",
    "33.15",
    "33.16",
    "33.17",
    "33.18",
    "33.19",
    "33.20",
    "33.21",
    "33.22",
    "33.23",
    "33.24",
    "33.25",
    "33.26",
    "33.26.1",
    "33.26.2",
    "33.27",
    "33.28",
    "33.29",
    "33.30",
}


def test_all_topic_33_items_are_registered():
    assert set(REQ_REGISTRY["33"]) == EXPECTED_TOPIC_33_IDS
