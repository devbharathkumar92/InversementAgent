"""Topic 1 — Document Control and Versioning.

Implements the controlled-document lifecycle required by SRS Topic 1:
identity, metadata, versioning, status transitions, change control,
approval, integrity, storage, review, baseline locking, and audit.
"""

from .audit import AuditEvent, AuditLog
from .baseline import Baseline, BaselineLockError, InvalidBaselineError
from .change_control import ChangeRequest
from .document import SRSDocument, reset_identity_registry
from .integrity import content_hash
from .versioning import Version

__all__ = [
    "SRSDocument",
    "reset_identity_registry",
    "Version",
    "ChangeRequest",
    "AuditEvent",
    "AuditLog",
    "Baseline",
    "BaselineLockError",
    "InvalidBaselineError",
    "content_hash",
]
