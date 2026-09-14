"""Tests for registry completeness — regression-fix gaps.

The authoritative SRS exposes heading IDs that earlier extraction
patterns skipped (numbered with `---` separators, semicolons inside
headings, or page-break wrappers). These tests lock the required
headings into the registry.
"""

import pytest

from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

GAPS = {
    "7": {
        "7.11": "Real-Time Data Processing Technologies",
        "7.27": "Performance and Resource Requirements",
    },
    "8": {"8.6.2": "Processing Constraints"},
    "19": {"19.15.1": "No-Action Conditions"},
    "20": {"20.9.1": "P&L Inputs", "20.9.2": "P&L Calculation", "20.9.3": "P&L Update"},
    "26": {"26.25.2": "Unauthorized Change Prevention"},
}


@pytest.mark.parametrize("topic", sorted(GAPS))
def test_registry_contains_gap_requirement(topic):
    for req_id, title in GAPS[topic].items():
        assert req_id in REQ_REGISTRY[topic], f"{req_id} missing from registry"
        assert REQ_REGISTRY[topic][req_id] == title


def test_registry_completeness_against_srs():
    # every registry id must either exist in the SRS doc text or be a
    # known project artifact id (baseline/checklist), never invented.
    import re

    for topic, table in REQ_REGISTRY.items():
        src = open(f"srs/topics/TOPIC_{int(topic):02d}.md", encoding="utf-8").read()
        for req_id in table:
            assert re.search(rf"\b{re.escape(req_id)}\b", src), (
                f"{req_id} not found in SRS topic {topic}"
            )
