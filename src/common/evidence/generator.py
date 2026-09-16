"""Deterministic topic evidence generator.

Answers the MASTER.md §24 traceability questions for every topic:

    Which SRS requirement was implemented?   -> requirement_ids
    Which files implement it?                -> source_modules
    Which tests verify it?                   -> test_files
    Which validation commands passed?        -> validation (recorded separately)
    Which commit contains it?                -> commit
    Which agent performed the work?          -> agent
    Which configuration/version was used?    -> python / registry size

Evidence is derived from the repository itself, never fabricated.
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path, PurePath
from typing import Any

from src.common.requirements.registry import REQ_REGISTRY

_IMPORT_RE = re.compile(r"^\s*(?:from|import)\s+(src\.[A-Za-z0-9_.]+)", re.MULTILINE)


def _topic_dir_name(topic: str) -> str:
    return f"topic_{int(topic):02d}"


def _repo_relative_posix(repo: PurePath, path: PurePath) -> str:
    """Render a repository-relative path with `/` separators on every OS.

    `PurePath.relative_to()` yields the host's native separator, so on Windows
    it emits backslashes. Evidence paths are a platform-independent contract,
    so they are always normalized to POSIX form.
    """
    return path.relative_to(repo).as_posix()


@dataclass
class EvidenceRecord:
    topic: str
    requirement_ids: list[str]
    requirement_count: int
    source_modules: list[str]
    test_files: list[str]
    doc: str
    spec: str
    commit: str = ""
    agent: str = "openhands"
    validation: str = "pytest -m unit; ruff check; ruff format --check; mypy src"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def collect_source_modules(repo: Path, topic: str) -> list[str]:
    """Return deduped `src.common.*` packages imported by the topic's tests."""
    test_dir = repo / "tests" / "unit" / _topic_dir_name(topic)
    modules: set[str] = set()
    if test_dir.is_dir():
        for path in sorted(test_dir.glob("*.py")):
            for match in _IMPORT_RE.findall(path.read_text(encoding="utf-8")):
                # collapse to the owning package (drop symbols/leaf module)
                parts = match.split(".")
                if len(parts) >= 3 and parts[:2] == ["src", "common"]:
                    modules.add(".".join(parts[:3]))
                else:
                    modules.add(match)
    return sorted(modules)


def collect_test_files(repo: Path, topic: str) -> list[str]:
    test_dir = repo / "tests" / "unit" / _topic_dir_name(topic)
    if not test_dir.is_dir():
        return []
    return sorted(_repo_relative_posix(repo, p) for p in test_dir.glob("test_*.py"))


def _current_commit(repo: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def build_record(topic: str, repo: Path) -> EvidenceRecord:
    reqs = sorted(REQ_REGISTRY[topic], key=lambda r: [int(p) for p in r.split(".")])
    return EvidenceRecord(
        topic=topic,
        requirement_ids=reqs,
        requirement_count=len(reqs),
        source_modules=collect_source_modules(repo, topic),
        test_files=collect_test_files(repo, topic),
        doc=f"docs/topics/TOPIC_{int(topic):02d}.md",
        spec=f"srs/topics/TOPIC_{int(topic):02d}.md",
        commit=_current_commit(repo),
    )


def build_topic_evidence(repo: Path) -> dict[str, EvidenceRecord]:
    return {t: build_record(t, repo) for t in sorted(REQ_REGISTRY, key=int)}


def write_evidence(
    records: list[EvidenceRecord], out_dir: Path, filename: str = "evidence.json"
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "inversement.evidence/v1",
        "topic_count": len(records),
        "total_requirements": sum(r.requirement_count for r in records),
        "topics": [r.to_dict() for r in records],
    }
    out = out_dir / filename
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out
