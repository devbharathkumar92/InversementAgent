"""Tests for Topic 27 registry — SRS Version Control and Governance."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_27_IDS = {
    "27.1",
    "27.2",
    "27.3",
    "27.4",
    "27.5",
    "27.5.1",
    "27.5.2",
    "27.6",
    "27.7",
    "27.8",
    "27.8.1",
    "27.9",
    "27.9.1",
    "27.9.2",
    "27.10",
    "27.10.1",
    "27.10.2",
    "27.11",
    "27.11.1",
    "27.11.2",
    "27.12",
    "27.13",
    "27.13.1",
    "27.13.2",
    "27.14",
    "27.15",
    "27.16",
    "27.17",
    "27.18",
    "27.19",
    "27.20",
    "27.21",
    "27.22",
    "27.23",
    "27.24",
    "27.25",
    "27.26",
    "27.26.1",
    "27.26.2",
    "27.27",
    "27.28",
    "27.28.1",
    "27.28.2",
    "27.29",
    "27.30",
}


def test_all_topic_27_items_are_registered():
    assert set(REQ_REGISTRY["27"]) == EXPECTED_TOPIC_27_IDS
