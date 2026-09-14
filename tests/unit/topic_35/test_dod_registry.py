"""Tests for Topic 35 registry — Definition of Done."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_35_IDS = {
    "35.1",
    "35.2",
    "35.2.1",
    "35.2.2",
    "35.3",
    "35.4",
    "35.5",
    "35.5.1",
    "35.5.2",
    "35.6",
    "35.6.1",
    "35.6.2",
    "35.7",
    "35.8",
    "35.9",
    "35.10",
    "35.11",
    "35.12",
    "35.13",
    "35.14",
    "35.15",
    "35.16",
    "35.17",
    "35.18",
    "35.19",
    "35.20",
    "35.21",
    "35.22",
    "35.23",
    "35.24",
    "35.24.1",
    "35.24.2",
    "35.25",
    "35.26",
    "35.27",
    "35.27.1",
    "35.27.2",
    "35.28",
    "35.29",
    "35.30",
}


def test_all_topic_35_items_are_registered():
    assert set(REQ_REGISTRY["35"]) == EXPECTED_TOPIC_35_IDS
