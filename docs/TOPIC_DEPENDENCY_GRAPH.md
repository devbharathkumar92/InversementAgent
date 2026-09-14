# Topic Dependency Graph

Dependency-aware execution order for the 40 SRS topics.

**Rule:** A topic shall not start until its dependencies are complete
(`PROJECT_STATUS.md` must show `COMPLETED` for each dependency).

---

## Phase 1 — Foundation (Topics 1–5)

```text
TOPIC_01
   │
   ▼
TOPIC_02
   │
   ├──► TOPIC_03 ──► TOPIC_04
   │                      │
   └──────────────────────► TOPIC_05
```

- TOPIC_01 → TOPIC_02 → (TOPIC_03, TOPIC_04) → TOPIC_05
- TOPIC_04 also depends on TOPIC_02 directly.

## Phase 2 — Architecture & Technical Specification (Topics 6–9)

```text
TOPIC_05 → TOPIC_06 → TOPIC_07 → TOPIC_08
                      │            │
                      └────────────┴──► TOPIC_09
```

- 06 depends on 05; 07 on 06; 08 on 06+07; 09 on 06+07+08.

## Phase 3 — Data & Intelligence (Topics 10–15)

```text
TOPIC_09
   ▼
TOPIC_10 ──► TOPIC_11
                 │
                 ├──► TOPIC_12 ──► TOPIC_13 ──► TOPIC_14 ──► TOPIC_15
                 │        │
                 └────────┘
```

- 10 → 11 → (12 → 13 → 14 → 15). 12 also needs 10+11; 13 needs 11+12.

## Phase 4 — Trading / Investment Simulation & Safety (Topics 16–20)

```text
                 TOPIC_15
                    │
                    ▼
                 TOPIC_16
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
    TOPIC_17               (also needs 11)
        │
        ▼
    TOPIC_18
        │
        ▼
    TOPIC_19 (needs 15–18)
        │
        ▼
    TOPIC_20 (needs 18, 19)
```

## Phase 5 — User Visibility & Reliability (Topics 21–26)

```text
TOPIC_20 → TOPIC_21 → TOPIC_22
              │           │
              └───────────┴──► TOPIC_23 → TOPIC_24
                                            │
                                            ▼
                                      TOPIC_25 → TOPIC_26
```

## Phase 6 — Multi-Agent Development (Topics 27–32)

```text
TOPIC_27 (governance; needs 01–26)
   ▼
TOPIC_28
   ▼
TOPIC_29
   ▼
TOPIC_30 → TOPIC_31 → TOPIC_32
```

## Phase 7 — QA & Release (Topics 33–40)

```text
TOPIC_33 (needs 08, 09, 27–32)
   ▼
TOPIC_34
   ▼
TOPIC_35
   ▼
TOPIC_36 (needs 10–35)
   ▼
TOPIC_37
   ▼
TOPIC_38 ──► TOPIC_39 ──► TOPIC_40
```

---

## Summary Table

| Topic | Name | Depends on |
|---|---|---|
| 01 | Document Control and Versioning | — |
| 02 | Core Goal and Mission | 01 |
| 03 | Proof of Value Definition | 02 |
| 04 | System Scope and Boundaries | 02, 03 |
| 05 | System Principles and Non-Negotiable Rules | 04 |
| 06 | High-Level System Architecture | 05 |
| 07 | Technology Stack and Technical Feasibility | 06 |
| 08 | Agent Determinism and Specification Completeness | 06, 07 |
| 09 | System Execution Lifecycle | 06–08 |
| 10 | Data Acquisition Layer | 09 |
| 11 | Data Validation and Quality Layer | 10 |
| 12 | Opportunity Discovery Engine | 10, 11 |
| 13 | Market Analysis Engine | 11, 12 |
| 14 | Opportunity Scoring Engine | 12, 13 |
| 15 | Strategy Engine | 13, 14 |
| 16 | Risk and Safety Engine | 11, 15 |
| 17 | Backtesting and Simulation | 15, 16 |
| 18 | Paper Trading Engine | 16, 17 |
| 19 | Decision Engine | 15–18 |
| 20 | Monitoring and P&L Management | 18, 19 |
| 21 | Dashboard and User Visibility | 20 |
| 22 | Human Interaction and Notifications | 21 |
| 23 | Audit Trail and Observability | 20–22 |
| 24 | Error Detection and Recovery | 23 |
| 25 | Self-Evaluation | 23, 24 |
| 26 | Self-Improvement and Change Management | 25 |
| 27 | SRS Version Control and Governance | 01–26 |
| 28 | Requirement Traceability | 27 |
| 29 | Sub-Agent Architecture | 27, 28 |
| 30 | Sub-Agent Task Specification | 29 |
| 31 | Dependency and Execution Plan | 30 |
| 32 | Parallel Development Plan | 31 |
| 33 | Testing Strategy | 08, 09, 27–32 |
| 34 | SRS Self-Validation | 33 |
| 35 | Definition of Done | 33, 34 |
| 36 | Integration and Deployment | 10–35 |
| 37 | Security and Secrets Management | 36 |
| 38 | PoV Release Criteria | 36, 37 |
| 39 | Future Expansion Framework | 38 |
| 40 | Appendices | all |

---

## Parallelization Notes

- Topics 3 and 4 can run sequentially after 2; their child specs can be analysed
  in parallel once contracts are frozen (`MASTER.md` §12).
- Topics 17 and 18 depend on 16; only design/test-prep parallel work is allowed
  until 16 is validated.
- No parallel implementation may alter locked baselines or bypass approval gates.