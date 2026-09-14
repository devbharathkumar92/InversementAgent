#!/usr/bin/env python3
"""Generate topic evidence artifacts (MASTER.md §24, DoD item 5).

Usage:
    python scripts/gen_evidence.py [--out data/evidences]

Writes `data/evidences/evidence.json` answering, for every topic: which
SRS requirements were implemented, which source modules and tests deliver
them, the spec/doc paths, and the current commit.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from src.common.evidence.generator import (  # noqa: E402
    build_topic_evidence,
    write_evidence,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="data/evidences", help="output directory")
    args = parser.parse_args()

    records = list(build_topic_evidence(REPO).values())
    out = write_evidence(records, (REPO / args.out).resolve())
    total = sum(r.requirement_count for r in records)
    print(f"wrote {out} ({len(records)} topics, {total} requirement IDs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
