"""Tests for Topic 31 registry — Dependency and Execution Plan."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_31_IDS = {
    "31.1",
    "31.2",
    "31.3",
    "31.3.1",
    "31.3.2",
    "31.4",
    "31.5",
    "31.6",
    "31.7",
    "31.8",
    "31.9",
    "31.10",
    "31.11",
    "31.11.1",
    "31.11.2",
    "31.12",
    "31.12.1",
    "31.12.2",
    "31.13",
    "31.14",
    "31.15",
    "31.16",
    "31.17",
    "31.18",
    "31.19",
    "31.20",
    "31.21",
    "31.22",
    "31.23",
    "31.24",
    "31.24.1",
    "31.24.2",
    "31.25",
    "31.26",
    "31.27",
    "31.28",
    "31.29",
    "31.30",
}


def test_all_topic_31_items_are_registered():
    assert set(REQ_REGISTRY["31"]) == EXPECTED_TOPIC_31_IDS
