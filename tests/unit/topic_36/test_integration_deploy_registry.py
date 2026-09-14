"""Tests for Topic 36 registry — Integration and Deployment."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_36_IDS = {
    "36.1",
    "36.2",
    "36.3",
    "36.4",
    "36.5",
    "36.6",
    "36.7",
    "36.8",
    "36.9",
    "36.10",
    "36.11",
    "36.12",
    "36.13",
    "36.13.1",
    "36.13.2",
    "36.14",
    "36.14.1",
    "36.14.2",
    "36.15",
    "36.16",
    "36.16.1",
    "36.16.2",
    "36.17",
    "36.18",
    "36.19",
    "36.20",
    "36.21",
    "36.21.1",
    "36.21.2",
    "36.22",
    "36.23",
    "36.24",
    "36.24.1",
    "36.24.2",
    "36.25",
    "36.25.1",
    "36.25.2",
    "36.26",
    "36.27",
    "36.28",
    "36.29",
    "36.30",
}


def test_all_topic_36_items_are_registered():
    assert set(REQ_REGISTRY["36"]) == EXPECTED_TOPIC_36_IDS
