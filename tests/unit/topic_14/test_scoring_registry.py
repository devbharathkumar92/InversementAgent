"""Tests for Topic 14 registry — Opportunity Scoring traceability coverage."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_14_IDS = {
    "14.1",
    "14.2",
    "14.2.1",
    "14.2.2",
    "14.3",
    "14.4",
    "14.5",
    "14.6",
    "14.7",
    "14.8",
    "14.9",
    "14.10",
    "14.11",
    "14.12",
    "14.13",
    "14.14",
    "14.15",
    "14.16",
    "14.16.1",
    "14.16.2",
    "14.17",
    "14.17.1",
    "14.17.2",
    "14.18",
    "14.18.1",
    "14.18.2",
    "14.19",
    "14.20",
    "14.21",
    "14.21.1",
    "14.22",
    "14.22.1",
    "14.22.2",
    "14.23",
    "14.24",
    "14.25",
    "14.26",
    "14.27",
    "14.28",
    "14.29",
    "14.30",
}


def test_all_topic_14_items_are_registered():
    assert set(REQ_REGISTRY["14"]) == EXPECTED_TOPIC_14_IDS
