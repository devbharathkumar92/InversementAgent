# Prompt Repository

Autonomous development prompts for the AI Investment Opportunity Agent.

```text
prompts/
├── README.md
├── PROMPT_00_PROJECT_BOOTSTRAP.md            # Official bootstrap prompt (from the SRS package; see MASTER.md §18)
├── TOPICS/
│   ├── TOPIC_01.md
│   ├── TOPIC_02.md
│   └── ... TOPIC_40.md
└── templates/
    └── TOPIC_PROMPT_TEMPLATE.md
```

> The detailed bootstrap prompt (the original project upload) is preserved at
> the repository root as `PROMPT_00_PROJECT_BOOTSTRAP.md` (referenced by
> `MASTER.md` §25).

## How prompts are used

1. Each **topic prompt** (`TOPICS/TOPIC_NN.md`) drives one autonomous agent to
   implement exactly one SRS topic on its own feature branch.
2. The **topic prompt template** (`templates/TOPIC_PROMPT_TEMPLATE.md`) is the
   canonical shape that topics follow.
3. Topic prompts are **generated** from `scripts/gen_topic_prompts.py` so the
   set stays consistent and regenerable.
4. The authoritative requirements for a topic live in
   `srs/topics/TOPIC_NN.md`; prompts reference but never replace them.

## Regenerating topic prompts

```bash
python scripts/gen_topic_prompts.py
```

## Bootstrap prompts

- `PROMPT_00_PROJECT_BOOTSTRAP.md` — the official bootstrap prompt shipped with
  the SRS package (concise, authoritative).
- `<repo root>/PROMPT_00_PROJECT_BOOTSTRAP.md` — the extended bootstrap prompt
  received as the original project upload; kept for reference (per MASTER.md §25).

## Governance

- Prompts must never override `SRS.md` or `MASTER.md`.
- Material changes to prompts themselves follow the project change-control
  workflow (`MASTER.md` §21, Topic 27).