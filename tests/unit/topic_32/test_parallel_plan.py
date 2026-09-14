"""Tests for Topic 32 — Parallel Development Plan.

Covers parallelization eligibility (32.2), branch/repository
strategy (32.6/32.7/32.8), workspace isolation (32.9), shared
interface contracts (32.5/32.13/32.14), conflict detection and
merge handling (32.15/32.16/32.20), and final integration
readiness (32.29).
"""

import pytest

from src.common.parallelplan.engine import (
    ParallelPlanEngine,
    branch_naming_convention,
    conflict_detected,
    contract_valid,
    eligible_for_parallel,
    final_readiness_gate,
    interface_compatibility,
    isolation_respected,
    merge_preconditions_met,
    parallel_acceptance,
    resource_contention_handled,
    shared_resources_identified,
    workspaces_isolated,
)


class TestParallelization:
    """REQ 32.2.1/32.2.2/32.3/32.4."""

    def test_eligible_for_parallel(self):
        assert eligible_for_parallel(independent=True, exclusive=True) is True

    def test_prohibited_when_shared(self):
        assert eligible_for_parallel(independent=False, exclusive=True) is False

    def test_shared_resources_identified(self):
        assert shared_resources_identified(known=True) is True


class TestWorkspaces:
    """REQ 32.5.1/32.6/32.8/32.9.1/32.9.2."""

    def test_contract_valid(self):
        assert contract_valid(defined=True, owned=True) is True

    def test_contract_undefined(self):
        assert contract_valid(defined=False, owned=True) is False

    def test_branch_naming(self):
        assert branch_naming_convention(respects=True) is True

    def test_workspace_isolation(self):
        assert workspaces_isolated(separate=True) is True

    def test_isolation_respected(self):
        assert isolation_respected(isolated=True, shared_rules=True) is True

    def test_isolation_violated(self):
        assert isolation_respected(isolated=True, shared_rules=False) is False


class TestCoordination:
    """REQ 32.11/32.13/32.15.1/32.16/32.20.1."""

    def test_conflict_detected(self):
        assert conflict_detected(identified=True) is True

    def test_merge_preconditions_met(self):
        assert merge_preconditions_met(tested=True, reviewed=True) is True

    def test_merge_blocked(self):
        assert merge_preconditions_met(tested=True, reviewed=False) is False

    def test_interfaces_compatible(self):
        assert interface_compatibility(compatible=True) is True

    def test_resource_contention_handled(self):
        assert resource_contention_handled(managed=True) is True


class TestIntegration:
    """REQ 32.28/32.29.1/32.29.2."""

    def test_acceptance_met(self):
        assert parallel_acceptance(planned=True, validated=True) is True

    def test_final_readiness_gate(self):
        assert final_readiness_gate(checklist=False, gates=True) is False

    def test_readiness_open(self):
        assert final_readiness_gate(checklist=True, gates=True) is True


class TestEngine:
    """REQ 32.1 — parallel development lifecycle."""

    def test_requires_name(self):
        with pytest.raises(ValueError):
            ParallelPlanEngine(name=" ")

    def test_engine_status(self):
        assert ParallelPlanEngine(name="p").status() == "scheduled"


pytestmark = pytest.mark.unit
