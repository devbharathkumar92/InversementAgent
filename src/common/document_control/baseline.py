"""Topic 1.11/1.11.1/1.11.2/1.11.3 — baseline creation, lock, and modification.

A locked baseline cannot be edited in place. The only permitted path to
change it is the controlled change workflow, which produces a new version
and a new baseline while preserving the predecessor baseline (rollback and
historical traceability).
"""

from __future__ import annotations

from dataclasses import dataclass

from .change_control import APPROVAL_AUTHORITIES
from .integrity import content_hash
from .versioning import Version


class BaselineError(Exception):
    """Base error for baseline operations."""


class InvalidBaselineError(BaselineError):
    """Raised when a baseline cannot be created from the provided inputs."""


class BaselineLockError(BaselineError):
    """Raised when an unauthorized/write attempt targets a locked baseline."""


@dataclass
class Baseline:
    """An immutable, locked reference snapshot of a controlled version."""

    version: str
    integrity_hash: str
    approved_by: str
    locked: bool = True

    @classmethod
    def create(
        cls,
        version: str,
        integrity_hash: str,
        approved_by: str,
    ) -> Baseline:
        if not integrity_hash:
            raise InvalidBaselineError("A baseline requires an integrity hash")
        if approved_by not in APPROVAL_AUTHORITIES:
            raise InvalidBaselineError(f"{approved_by!r} is not an approved baseline authority")
        # Versions must be parseable to be baseline-eligible.
        Version(version)
        return cls(version=version, integrity_hash=integrity_hash, approved_by=approved_by)

    def modify(self, new_content: bytes) -> Baseline:
        """Reject any direct write/tamper against a locked baseline.

        Raises:
            BaselineLockError: always — direct modification is prohibited.
        """
        raise BaselineLockError(
            "Locked baseline cannot be modified in place; use the controlled "
            "change workflow (create_controlled_replacement)"
        )

    def create_controlled_replacement(
        self,
        new_content: bytes,
        approved_by: str,
    ) -> Baseline:
        """Produce a new controlled version and baseline via the approved workflow.

        The predecessor baseline is preserved untouched so history remains
        recoverable.
        """
        if approved_by not in APPROVAL_AUTHORITIES:
            raise InvalidBaselineError(f"{approved_by!r} is not an approved baseline authority")
        new_version = str(Version(self.version).bump("minor"))
        return Baseline.create(
            version=new_version,
            integrity_hash=content_hash(new_content),
            approved_by=approved_by,
        )
