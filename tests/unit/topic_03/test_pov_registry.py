"""Tests for Topic 3 registry — PoV item traceability coverage.

Confirms every numbered Topic 3 item (3.1-3.24) is registered so it cannot
silently drift out of the controlled requirement set (REQ 1.0A).
"""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

EXPECTED_TOPIC_3_IDS = {
    "3.1",
    "3.2",
    "3.3",
    "3.3.1",
    "3.3.2",
    "3.3.3",
    "3.4",
    "3.5",
    "3.5.1",
    "3.5.2",
    "3.6",
    "3.7",
    "3.7.1",
    "3.7.2",
    "3.7.3",
    "3.8",
    "3.9",
    "3.10",
    "3.11",
    "3.12",
    "3.13",
    "3.14",
    "3.15",
    "3.15.1",
    "3.15.2",
    "3.16",
    "3.17",
    "3.17.1",
    "3.17.2",
    "3.18",
    "3.18.1",
    "3.18.2",
    "3.19",
    "3.20",
    "3.21",
    "3.21.1",
    "3.21.2",
    "3.22",
    "3.23",
    "3.24",
}


def test_all_topic_3_items_are_registered():
    assert set(REQ_REGISTRY["3"]) == EXPECTED_TOPIC_3_IDS


def test_no_topic_3_requirement_is_missing():
    for req_id in EXPECTED_TOPIC_3_IDS:
        assert req_id in REQ_REGISTRY["3"], f"missing {req_id}"
