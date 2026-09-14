"""Tests for Topic 34 registry — SRS Self-Validation."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_34_IDS = {
    "34.1",
    "34.2",
    "34.3",
    "34.3.1",
    "34.3.2",
    "34.4",
    "34.4.1",
    "34.4.2",
    "34.5",
    "34.6",
    "34.7",
    "34.8",
    "34.9",
    "34.10",
    "34.11",
    "34.12",
    "34.13",
    "34.14",
    "34.15",
    "34.16",
    "34.17",
    "34.18",
    "34.19",
    "34.20",
    "34.20.1",
    "34.20.2",
    "34.21",
    "34.21.1",
    "34.21.2",
    "34.22",
    "34.23",
    "34.24",
    "34.25",
    "34.26",
    "34.27",
    "34.27.1",
    "34.27.2",
    "34.28",
    "34.29",
    "34.30",
}


def test_all_topic_34_items_are_registered():
    assert set(REQ_REGISTRY["34"]) == EXPECTED_TOPIC_34_IDS
