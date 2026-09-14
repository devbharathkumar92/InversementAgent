"""Tests for Topic 5 registry — System Principles item traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_5_IDS = {
    "5.1",
    "5.2",
    "5.3",
    "5.3.1",
    "5.3.2",
    "5.4",
    "5.5",
    "5.6",
    "5.7",
    "5.8",
    "5.8.1",
    "5.8.2",
    "5.9",
    "5.10",
    "5.11",
    "5.12",
    "5.13",
    "5.14",
    "5.15",
    "5.16",
    "5.17",
    "5.18",
    "5.19",
    "5.20",
    "5.21",
    "5.22",
    "5.23",
    "5.24",
    "5.25",
    "5.26",
    "5.26.1",
    "5.26.2",
    "5.27",
    "5.27.1",
    "5.27.2",
    "5.27.3",
    "5.27.4",
    "5.28",
    "5.29",
    "5.30",
    "5.31",
    "5.31.1",
    "5.31.2",
    "5.32",
    "5.33",
    "5.33.1",
    "5.33.2",
    "5.34",
}


def test_all_topic_5_items_are_registered():
    assert set(REQ_REGISTRY["5"]) == EXPECTED_TOPIC_5_IDS
