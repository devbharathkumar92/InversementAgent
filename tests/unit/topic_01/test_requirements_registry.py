"""Tests for the requirements registry (traceability backbone).

Every implemented topic's numbered requirement IDs must be registered so
that tests and evidence can reference the authoritative SRS requirement.
"""

import pytest

from src.common.requirements import REQ_REGISTRY, get_requirement_title


def test_topic_1_registered_with_expected_items():
    assert {"1.1", "1.3.2", "1.11.2", "1.12"} <= set(REQ_REGISTRY["1"])


def test_topic_2_registered_with_expected_items():
    assert {"2.1", "2.7.1", "2.12.2", "2.15"} <= set(REQ_REGISTRY["2"])


def test_topics_3_4_5_registered():
    assert "3.17.2" in REQ_REGISTRY["3"]
    assert "4.15.2" in REQ_REGISTRY["4"]
    assert "5.8.1" in REQ_REGISTRY["5"]


def test_get_requirement_title_returns_title():
    assert get_requirement_title("1", "1.1") == "Document Identity"


def test_get_requirement_title_unknown_raises():
    with pytest.raises(KeyError):
        get_requirement_title("1", "1.99")
    with pytest.raises(KeyError):
        get_requirement_title("99", "1.1")


@pytest.mark.parametrize("topic", ["1", "2", "3", "4", "5"])
def test_topic_has_no_empty_titles(topic):
    for rid, title in REQ_REGISTRY[topic].items():
        assert title.strip(), f"{topic}.{rid} has empty title"
        assert not title.startswith("Purpose"), f"{topic}.{rid} title polluted"


pytestmark = pytest.mark.unit
