"""Tests for Topic 7 — Technology Stack and Technical Feasibility.

Covers deterministic responsibilities (7.7.2), technology selection /
rejection criteria (7.1.1/7.1.2), branch strategy (7.18.2), dependency
pinning (7.26.1), and exact version compatibility (7.26).
"""

import pytest

from src.common.technology.selection import (
    BranchStrategy,
    TechSelection,
    validate_dependency_pinning,
    validate_pinned_dependency,
)


@pytest.fixture
def selection_dict():
    return {
        "name": "TechStack",
        "deterministic_responsibilities": [
            "validate-input-schema",
            "calculate-scoring-metrics",
        ],
        "llm_responsibilities": [
            "generate-narrative",
            "classify-opportunity",
        ],
        "selected_technologies": ["python=3.12", "pandas=2.2.0"],
        "branch_prefixes": ["feature/", "fix/", "release/"],
    }


class TestNonLLMDeterministic:
    """REQ 7.7.2 — deterministic responsibilities stay non-LLM."""

    def test_deterministic_responsibilities_registered(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert "validate-input-schema" in sel.deterministic_responsibilities

    def test_metric_calculation_is_deterministic(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert sel.is_deterministic("calculate-scoring-metrics") is True

    def test_llm_responsibility_not_deterministic(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert sel.is_deterministic("generate-narrative") is False

    def test_responsibility_requires_one_owner(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert sel.owner_of("validate-input-schema") == "deterministic"


class TestTechFeasibility:
    """REQ 7.1.1/7.1.2 — selection and rejection are governed."""

    def test_technology_not_selected(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert sel.is_selected("python") is False

    def test_technology_selected_with_version(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert sel.is_selected("python=3.12") is True

    def test_unsupported_technology_rejected(self, selection_dict):
        sel = TechSelection(**selection_dict)
        assert sel.reject_if_unsupported("hardware-trading-engine") is True


class TestBranchStrategy:
    """REQ 7.18.2 — branch naming and protection rules."""

    def test_branch_with_valid_prefix(self, selection_dict):
        br = BranchStrategy.from_deps(**selection_dict)
        assert br.is_conformant("feature/topic-07-tech") is True

    def test_branch_with_invalid_prefix(self, selection_dict):
        br = BranchStrategy.from_deps(**selection_dict)
        assert br.is_conformant("random/branch") is False

    def test_main_branch_protected(self, selection_dict):
        br = BranchStrategy.from_deps(**selection_dict)
        assert br.is_protected("main") is True


class TestDependencyPinning:
    """REQ 7.26.1/7.26 — dependencies are fully pinned (reproducible)."""

    def test_pinned_dependency_ok(self):
        assert validate_pinned_dependency("pandas==2.2.0") is True

    def test_unpinned_dependency_fails(self):
        assert validate_pinned_dependency("pandas>=2.2") is False

    def test_spec_set_validation_ok(self, selection_dict):
        assert validate_dependency_pinning(selection_dict["selected_technologies"]) is True

    def test_spec_set_with_unpinned_fails(self):
        deps = ["python==3.12", "numpy"]  # numpy unpinned
        assert validate_dependency_pinning(deps) is False


pytestmark = pytest.mark.unit
