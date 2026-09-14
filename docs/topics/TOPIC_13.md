# Topic 13 — Market Analysis Engine

> Status: ✅ **IMPLEMENTED** (TDD), branch `feature/topic-13-market-analysis`

## Decision

**Implementation required (core).** Topic 13 is the market analysis
layer that gives the agent its market context and regime awareness:

- **13.3**: market trend analysis — price-series trend classification.
- **13.8**: technical indicators (e.g., position vs moving average).
- **13.10 / 13.10.1 / 13.10.2**: news analysis — relevance tagging and
  impact (negative/positive/neutral).
- **13.11 / 13.11.1**: sentiment classification from a signed score.
- **13.17 / 13.17.1 / 13.17.2**: conflicting-signal detection and
  resolution.
- **13.18 / 13.18.1 / 13.18.2**: signal confidence assessment.
- **13.19 / 13.19.1 / 13.19.2**: market regime detection —
  classification (bull/bear/chop) and regime transitions.

## Requirement → Code/Test mapping

| REQ ID | Requirement | Delivered in | Tests |
|---|---|---|---|
| 13.3 | Market Trend Analysis | `engine.py` (`trend_direction`) | `test_market_analysis.py::TestTrendAnalysis` |
| 13.4 | Price Analysis / momentum | `engine.py` (`momentum_is_up`) | `test_market_analysis.py::TestTrendAnalysis` |
| 13.8 | Technical Analysis | `engine.py` (`MarketAnalysisEngine.above_sma`) | `test_market_analysis.py::TestTechnicalAnalysis` |
| 13.10.1 | News Relevance | `engine.py` (`news_relevant`) | `test_market_analysis.py::TestNewsImpact` |
| 13.10.2 | News Impact | `engine.py` (`analyze_news_impact`) | `test_market_analysis.py::TestNewsImpact` |
| 13.11 | Sentiment Analysis | `engine.py` (`sentiment_from`) | `test_market_analysis.py::TestSentiment` |
| 13.17/13.17.1/13.17.2 | Conflicting-Signal Detection | `engine.py` (`conflict_flagged`, `resolve_conflict`) | `test_market_analysis.py::TestConflictDetection` |
| 13.18.1/13.18.2 | Signal Confidence | `engine.py` (`confidence_assessed`) | `test_market_analysis.py::TestConfidenceAssessment` |
| 13.19/13.19.1/13.19.2 | Market Regime Detection | `engine.py` (`detect_regime`, `transition_to`) | `test_market_analysis.py::TestRegimeDetection` |
| — | Full Topic 13 contract | `registry.py` (+ traceability test) | `test_market_registry.py` |

## Registry addition

Topic 13 (absent before) added as the authoritative 44-item block
(including 13.1 — Market Analysis Objectives, found with single-space
separator in the SRS), exactly matching the SRS topic file.

## Validation

- `python -m pytest -m unit` → **308 passed** (23 from Topic 13)
- `python -m ruff check src tests` → clean
- `python -m ruff format --check src tests` → clean
- `python -m mypy src` → no issues (80 files)

## Notes / decisions

- Regime model: high volatility (≥ 0.5 normalized) → **chop**; otherwise
  momentum sign selects **bull** vs **bear**. A transition occurs when
  the classified regime differs from the current one.
- `confidence_assessed` returns the raw agreement ratio so the caller
  (REQ 13.18.2) applies the configured threshold externally.
- Sentiment thresholds use a ±0.2 dead-zone to avoid sign-flapping
  around neutral.
- The environment was reinstalled (`pip install -e ".[dev]"`) in this
  session after the interpreter lost pytest/ruff/mypy; the full suite
  was rerun and is green (308 passed).