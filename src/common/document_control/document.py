"""Topic 1.1/1.2 — document identity and mandatory metadata."""

from __future__ import annotations

from dataclasses import dataclass

_REQUIRED_FIELDS = frozenset(
    {
        "document_id",
        "project_name",
        "title",
        "version",
        "status",
        "owner",
        "authoring_agent",
        "approval_authority",
        "creation_date",
        "last_modified_date",
        # baseline_state is populated by the baseline workflow.
    }
)


class MetadataError(ValueError):
    """Raised when document metadata is missing or invalid."""


class DuplicateIdentityError(ValueError):
    """Raised when two documents claim the same ``(document_id, version)``."""


@dataclass
class SRSDocument:
    """A controlled SRS document with unique composite identity.

    REQ 1.1: the ``document_id`` stays stable across ordinary version
    changes; the composite identity ``(document_id, version)`` is unique.
    """

    document_id: str | None = None
    project_name: str | None = None
    title: str | None = None
    version: str | None = None
    status: str | None = None
    owner: str | None = None
    authoring_agent: str | None = None
    approval_authority: str | None = None
    creation_date: str | None = None
    last_modified_date: str | None = None
    baseline_state: str | None = "NONE"

    def __post_init__(self) -> None:
        self._validate()
        self._register_identity()

    def _validate(self) -> None:
        for field_name in _REQUIRED_FIELDS:
            value = getattr(self, field_name)
            if not value or not str(value).strip():
                raise MetadataError(f"Missing required metadata field: {field_name}")

    def _register_identity(self) -> None:
        doc_id = self.document_id
        version = self.version
        if not doc_id or not version:
            raise MetadataError("document_id and version are required for identity")
        composite = (doc_id, version)
        if composite in _IDENTITY_REGISTRY:
            raise DuplicateIdentityError(
                f"Duplicate document composite identity: (document_id={self.document_id!r}, "
                f"version={self.version!r})"
            )
        _IDENTITY_REGISTRY.add(composite)

    def __repr__(self) -> str:
        return (
            f"SRSDocument(document_id={self.document_id!r}, version={self.version!r}, "
            f"status={self.status!r})"
        )


def reset_identity_registry() -> None:
    """Clear the process-wide identity registry.

    Intended for test isolation; production code should not call this.
    """
    _IDENTITY_REGISTRY.clear()


# Process-wide registry of created composite identities (document_id, version).
_IDENTITY_REGISTRY: set[tuple[str, str]] = set()
