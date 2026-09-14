"""Tests for Topic 23 registry — Audit Trail and Observability."""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_23_IDS = {
    "23.1",
    "23.2",
    "23.3",
    "23.4",
    "23.5",
    "23.6",
    "23.7",
    "23.8",
    "23.9",
    "23.10",
    "23.11",
    "23.12",
    "23.13",
    "23.14",
    "23.15",
    "23.15.1",
    "23.15.2",
    "23.16",
    "23.17",
    "23.17.1",
    "23.18",
    "23.18.1",
    "23.18.2",
    "23.19",
    "23.19.1",
    "23.19.2",
    "23.20",
    "23.20.1",
    "23.20.2",
    "23.21",
    "23.22",
    "23.23",
    "23.24",
    "23.25",
    "23.26",
    "23.27",
    "23.28",
    "23.29",
    "23.30",
}


def test_all_topic_23_items_are_registered():
    assert set(REQ_REGISTRY["23"]) == EXPECTED_TOPIC_23_IDS
