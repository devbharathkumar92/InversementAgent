"""Topic 1.8 — document integrity via content hashing."""

from __future__ import annotations

import hashlib


def content_hash(content: bytes) -> str:
    """Return a SHA-256 hex digest for the given byte content.

    Any change in ``content`` produces a different digest, enabling
    detection of unauthorized modification.
    """
    return hashlib.sha256(content).hexdigest()
