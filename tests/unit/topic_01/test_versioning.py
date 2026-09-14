"""Tests for Topic 1.3/1.3.1/1.3.2/1.4 — Versioning and Version Status."""

import pytest

from src.common.document_control.versioning import (
    Version,
    can_transition_status,
    initial_status,
    next_version,
    parse_version,
)


class TestVersionFormat:
    """REQ 1.3.1 — version numbering rules."""

    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("1.0.0", (1, 0, 0)),
            ("2.1.7", (2, 1, 7)),
            ("0.0.1", (0, 0, 1)),
        ],
    )
    def test_parse_valid_versions(self, raw, expected):
        assert parse_version(raw) == expected

    @pytest.mark.parametrize("raw", ["1.2", "1", "1.2.3.4", "a.b.c", "1.2.x", ""])
    def test_parse_rejects_malformed(self, raw):
        with pytest.raises(ValueError):
            parse_version(raw)

    def test_version_comparable_and_sortable(self):
        assert Version("1.10.0") > Version("1.9.9")
        assert Version("2.0.0") > Version("1.99.99")
        assert sorted(["1.1.0", "1.0.2", "2.0.0", "1.0.10"], key=Version) == [
            "1.0.2",
            "1.0.10",
            "1.1.0",
            "2.0.0",
        ]


class TestVersionIncrementRules:
    """REQ 1.3.2 — change class to version increment mapping."""

    @pytest.mark.parametrize(
        "change_class,current,expected",
        [
            ("major", "1.2.3", "2.0.0"),
            ("minor", "1.2.3", "1.3.0"),
            ("patch", "1.2.3", "1.2.4"),
        ],
    )
    def test_increment_by_change_class(self, change_class, current, expected):
        assert next_version(current, change_class) == expected

    def test_no_increment_without_approval(self):
        with pytest.raises(ValueError):
            next_version("1.2.3", "minor", approved=False)

    def test_unknown_change_class_rejected(self):
        with pytest.raises(ValueError):
            next_version("1.2.3", "unknown")


class TestVersionStatus:
    """REQ 1.4 — exactly one authoritative status; valid transitions only."""

    def test_initial_status_is_draft(self):
        assert initial_status() == "DRAFT"

    @pytest.mark.parametrize(
        "current,target,expected",
        [
            ("DRAFT", "IN_REVIEW", True),
            ("IN_REVIEW", "APPROVED", True),
            ("APPROVED", "BASELINED", True),
            ("BASELINED", "SUPERSEDED", True),
            ("DRAFT", "BASELINED", False),
            ("APPROVED", "IN_REVIEW", False),
            ("BASELINED", "REJECTED", False),
        ],
    )
    def test_status_transitions(self, current, target, expected):
        assert can_transition_status(current, target) == expected

    def test_unknown_status_rejected(self):
        with pytest.raises(ValueError):
            can_transition_status("DRAFT", "UNKNOWN")


pytestmark = pytest.mark.unit
