"""Tests for Topic 21 registry — Dashboard and User Visibility."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_21_IDS = {
    "21.1",
    "21.2",
    "21.3",
    "21.3.1",
    "21.3.2",
    "21.4",
    "21.4.1",
    "21.4.2",
    "21.5",
    "21.6",
    "21.6.1",
    "21.6.2",
    "21.7",
    "21.8",
    "21.9",
    "21.9.1",
    "21.9.2",
    "21.10",
    "21.11",
    "21.12",
    "21.13",
    "21.14",
    "21.15",
    "21.16",
    "21.17",
    "21.18",
    "21.19",
    "21.20",
    "21.21",
    "21.21.1",
    "21.21.2",
    "21.22",
    "21.23",
    "21.24",
    "21.25",
    "21.26",
    "21.27",
    "21.27.1",
    "21.27.2",
    "21.28",
    "21.29",
    "21.30",
}


def test_all_topic_21_items_are_registered():
    assert set(REQ_REGISTRY["21"]) == EXPECTED_TOPIC_21_IDS
