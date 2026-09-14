"""Topic evidence generation (MASTER.md §24, DoD item 5)."""

from src.common.evidence.generator import (
    EvidenceRecord,
    build_record,
    build_topic_evidence,
    collect_source_modules,
    collect_test_files,
    write_evidence,
)

__all__ = [
    "EvidenceRecord",
    "build_record",
    "build_topic_evidence",
    "collect_source_modules",
    "collect_test_files",
    "write_evidence",
]
