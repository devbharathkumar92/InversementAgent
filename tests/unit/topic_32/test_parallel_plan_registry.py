"""Tests for Topic 32 registry — Parallel Development Plan."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_32_IDS = {
    "32.1",
    "32.2",
    "32.2.1",
    "32.2.2",
    "32.3",
    "32.4",
    "32.5",
    "32.5.1",
    "32.5.2",
    "32.6",
    "32.7",
    "32.8",
    "32.9",
    "32.9.1",
    "32.9.2",
    "32.10",
    "32.11",
    "32.12",
    "32.13",
    "32.14",
    "32.15",
    "32.15.1",
    "32.15.2",
    "32.16",
    "32.17",
    "32.18",
    "32.19",
    "32.20",
    "32.20.1",
    "32.20.2",
    "32.21",
    "32.22",
    "32.23",
    "32.24",
    "32.25",
    "32.26",
    "32.27",
    "32.28",
    "32.29",
    "32.29.1",
    "32.29.2",
    "32.30",
}


def test_all_topic_32_items_are_registered():
    assert set(REQ_REGISTRY["32"]) == EXPECTED_TOPIC_32_IDS
