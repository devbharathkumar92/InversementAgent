"""Tests for Topic 16 registry — Risk & Safety traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_16_IDS = {
    "16.1",
    "16.2",
    "16.3",
    "16.3.1",
    "16.3.2",
    "16.4",
    "16.5",
    "16.5.1",
    "16.5.2",
    "16.6",
    "16.7",
    "16.7.1",
    "16.7.2",
    "16.8",
    "16.9",
    "16.10",
    "16.11",
    "16.12",
    "16.13",
    "16.14",
    "16.15",
    "16.16",
    "16.17",
    "16.18",
    "16.18.1",
    "16.18.2",
    "16.18.3",
    "16.19",
    "16.19.1",
    "16.19.2",
    "16.20",
    "16.20.1",
    "16.20.2",
    "16.21",
    "16.21.1",
    "16.21.2",
    "16.22",
    "16.23",
    "16.24",
    "16.25",
    "16.26",
    "16.27",
    "16.28",
    "16.29",
    "16.30",
}


def test_all_topic_16_items_are_registered():
    assert set(REQ_REGISTRY["16"]) == EXPECTED_TOPIC_16_IDS
