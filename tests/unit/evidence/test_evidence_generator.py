"""Unit tests for the topic evidence generator (MASTER.md §24, DoD item 5)."""

import json
from pathlib import Path

import pytest

from src.common.evidence.generator import (
    EvidenceRecord,
    build_record,
    build_topic_evidence,
    collect_source_modules,
    collect_test_files,
    write_evidence,
)
from src.common.requirements.registry import REQ_REGISTRY

pytestmark = pytest.mark.unit

REPO = Path(__file__).resolve().parents[3]


def test_collect_source_modules_finds_topic_modules():
    mods = collect_source_modules(REPO, "1")
    assert any(m.startswith("src.common.document_control") for m in mods)


def test_collect_test_files_finds_topic_tests():
    files = collect_test_files(REPO, "1")
    assert all(f.startswith("tests/unit/topic_01/") for f in files)
    assert files


def test_build_record_has_required_answers():
    rec = build_record("1", REPO)
    assert isinstance(rec, EvidenceRecord)
    assert rec.topic == "1"
    assert rec.requirement_ids == sorted(
        REQ_REGISTRY["1"], key=lambda r: [int(p) for p in r.split(".")]
    )
    d = rec.to_dict()
    for key in (
        "topic",
        "requirement_ids",
        "requirement_count",
        "source_modules",
        "test_files",
        "doc",
        "spec",
        "commit",
    ):
        assert key in d
    # every required governance answer is answerable
    assert d["requirement_count"] == len(REQ_REGISTRY["1"])
    assert d["doc"] == "docs/topics/TOPIC_01.md"
    assert d["spec"] == "srs/topics/TOPIC_01.md"


def test_build_topic_evidence_covers_all_registry_topics():
    recs = build_topic_evidence(REPO)
    assert set(recs) == set(REQ_REGISTRY)
    assert recs["40"].requirement_count == len(REQ_REGISTRY["40"])


def test_write_evidence_round_trips_json(tmp_path):
    rec = build_record("1", REPO)
    out = write_evidence([rec], tmp_path)
    assert out.exists()
    payload = json.loads(out.read_text())
    assert payload["topics"][0]["topic"] == "1"
    assert payload["total_requirements"] == len(REQ_REGISTRY["1"])
    assert payload["topic_count"] == 1


def test_evidence_is_deterministic():
    a = build_record("1", REPO).to_dict()
    b = build_record("1", REPO).to_dict()
    a.pop("commit", None)
    b.pop("commit", None)
    assert a == b
