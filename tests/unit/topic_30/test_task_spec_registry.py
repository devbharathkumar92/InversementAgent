"""Tests for Topic 30 registry — Sub-Agent Task Specification."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_30_IDS = {
    "30.1",
    "30.2",
    "30.3",
    "30.3.1",
    "30.3.2",
    "30.4",
    "30.5",
    "30.5.1",
    "30.5.2",
    "30.6",
    "30.6.1",
    "30.6.2",
    "30.7",
    "30.8",
    "30.9",
    "30.10",
    "30.11",
    "30.12",
    "30.12.1",
    "30.12.2",
    "30.13",
    "30.14",
    "30.15",
    "30.16",
    "30.17",
    "30.18",
    "30.18.1",
    "30.18.2",
    "30.19",
    "30.19.1",
    "30.19.2",
    "30.20",
    "30.21",
    "30.21.1",
    "30.21.2",
    "30.22",
    "30.23",
    "30.24",
    "30.25",
    "30.26",
    "30.26.1",
    "30.26.2",
    "30.27",
    "30.28",
    "30.29",
    "30.30",
}


def test_all_topic_30_items_are_registered():
    assert set(REQ_REGISTRY["30"]) == EXPECTED_TOPIC_30_IDS
