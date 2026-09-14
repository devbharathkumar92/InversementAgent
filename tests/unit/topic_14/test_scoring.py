"""Tests for Topic 14 — Opportunity Scoring Engine.

Covers the scoring framework (14.2), component scores (14.3-14.15),
composite score (14.16), weighting definition/validation (14.17),
score thresholds (14.18), ranking (14.19), recalculation (14.21),
score decay (14.22), and score validation (14.23).
"""

import pytest

from src.common.scoring.engine import (
    ScoringEngine,
    composite_score,
    decayed_score,
    weights_valid,
)


class TestComponentScores:
    """REQ 14.3-14.9 — component scores map to a 0-100 scale."""

    def test_high_return_potential(self):
        eng = ScoringEngine(name="s")
        assert eng.return_potential_score(projected_return=0.35) >= 80

    def test_low_return_potential(self):
        eng = ScoringEngine(name="s")
        assert eng.return_potential_score(projected_return=0.02) <= 40

    def test_risk_score_is_bounded(self):
        eng = ScoringEngine(name="s")
        assert 0 <= eng.risk_score(risk=0.6) <= 100

    def test_risk_reward_component(self):
        eng = ScoringEngine(name="s")
        assert eng.risk_reward_score(reward=30.0, risk=10.0) > 50


class TestCompositeScore:
    """REQ 14.16/14.16.1/14.16.2 — weighted composite of components."""

    def test_all_components_equal(self):
        components = {"return": 80, "risk": 40, "prob": 60}
        weights = {"return": 0.4, "risk": 0.3, "prob": 0.3}
        assert composite_score(components, weights) == pytest.approx(62.0)

    def test_ignores_unknown_components(self):
        assert composite_score({"return": 100, "extra": 0}, {"return": 1.0}) == 100.0


class TestWeightValidation:
    """REQ 14.17.1/14.17.2 — weights must be non-negative and sum to 1."""

    def test_valid_weights(self):
        assert weights_valid({"return": 0.5, "risk": 0.5}) is True

    def test_sum_not_one(self):
        assert weights_valid({"a": 0.5, "b": 0.2}) is False

    def test_negative_weight(self):
        assert weights_valid({"a": 1.5}) is False

    def test_unknown_weight(self):
        assert weights_valid({"zzz": 1.0}) is False


class TestThresholds:
    """REQ 14.18/14.18.1 — scores below minimum are rejected."""

    def test_score_meets_minimum(self):
        eng = ScoringEngine(name="s")
        assert eng.acceptable(score=75, minimum=60) is True

    def test_score_rejected(self):
        eng = ScoringEngine(name="s")
        assert eng.acceptable(score=40, minimum=60) is False


class TestRanking:
    """REQ 14.19 — scored opportunities ranked best-to-worst."""

    def test_ranking_order(self):
        ranked = ScoringEngine.rank([{"score": 30}, {"score": 90}])
        assert ranked[0]["score"] == 90


class TestRecalculationAndDecay:
    """REQ 14.21/14.22/14.22.1 — scores can be refreshed and decay."""

    def test_recalculation_returns_new_score(self):
        eng = ScoringEngine(name="s")
        assert eng.recalculate(base=70, new_input=90) == 90

    def test_decay_reduces_score(self):
        assert decayed_score(base=100, decay=0.1) == 90.0

    def test_scores_below_expiry_get_zeroed(self):
        assert decayed_score(base=10, decay=0.5, expiry=5.0) == 0.0


pytestmark = pytest.mark.unit
