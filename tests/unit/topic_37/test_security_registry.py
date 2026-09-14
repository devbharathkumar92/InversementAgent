"""Tests for Topic 37 registry — Security and Secrets Management."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_37_IDS = {
    "37.1",
    "37.2",
    "37.3",
    "37.3.1",
    "37.3.2",
    "37.4",
    "37.4.1",
    "37.4.2",
    "37.5",
    "37.6",
    "37.6.1",
    "37.6.2",
    "37.7",
    "37.8",
    "37.8.1",
    "37.8.2",
    "37.9",
    "37.9.1",
    "37.9.2",
    "37.10",
    "37.10.1",
    "37.10.2",
    "37.11",
    "37.12",
    "37.13",
    "37.14",
    "37.15",
    "37.16",
    "37.17",
    "37.18",
    "37.19",
    "37.20",
    "37.21",
    "37.22",
    "37.23",
    "37.23.1",
    "37.23.2",
    "37.24",
    "37.25",
    "37.25.1",
    "37.25.2",
    "37.26",
    "37.27",
    "37.28",
    "37.29",
    "37.30",
}


def test_all_topic_37_items_are_registered():
    assert set(REQ_REGISTRY["37"]) == EXPECTED_TOPIC_37_IDS
