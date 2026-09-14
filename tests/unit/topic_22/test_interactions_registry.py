"""Tests for Topic 22 registry — Human Interaction and Notifications."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_22_IDS = {
    "22.1",
    "22.2",
    "22.3",
    "22.3.1",
    "22.3.2",
    "22.3.3",
    "22.4",
    "22.4.1",
    "22.4.2",
    "22.5",
    "22.5.1",
    "22.5.2",
    "22.6",
    "22.7",
    "22.8",
    "22.9",
    "22.10",
    "22.11",
    "22.12",
    "22.13",
    "22.14",
    "22.15",
    "22.16",
    "22.16.1",
    "22.16.2",
    "22.17",
    "22.18",
    "22.19",
    "22.20",
    "22.21",
    "22.22",
    "22.23",
    "22.23.1",
    "22.23.2",
    "22.24",
    "22.25",
    "22.26",
    "22.27",
    "22.28",
    "22.29",
    "22.30",
}


def test_all_topic_22_items_are_registered():
    assert set(REQ_REGISTRY["22"]) == EXPECTED_TOPIC_22_IDS
