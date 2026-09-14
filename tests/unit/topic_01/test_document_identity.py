"""Tests for Topic 1.1/1.2 — Document Identity and Metadata."""

import pytest

from src.common.document_control.document import (
    DuplicateIdentityError,
    MetadataError,
    SRSDocument,
    reset_identity_registry,
)


def make_document(**overrides):
    defaults = {
        "document_id": "SRST1BL001",
        "project_name": "AI Investment Opportunity Agent",
        "title": "SRS Topic 1",
        "version": "1.0.0",
        "owner": "SRS Governance Owner",
        "authoring_agent": "SRS Writer Agent",
        "approval_authority": "Project Governance",
        "creation_date": "2026-01-01",
        "last_modified_date": "2026-01-01",
        "baseline_state": "NONE",
        "status": "DRAFT",
    }
    defaults.update(overrides)
    return defaults


@pytest.fixture(autouse=True)
def _reset_identity_registry():
    reset_identity_registry()
    yield
    reset_identity_registry()


class TestDocumentIdentity:
    """REQ 1.1 — unique, authoritative, stable identity."""

    def test_document_created_with_unique_id(self):
        doc = SRSDocument(**make_document())
        assert doc.document_id == "SRST1BL001"

    def test_two_documents_same_id_different_version_are_distinct(self):
        # REQ 1.1: the Document ID stays stable across ordinary version
        # changes; the composite identity is (document_id, version).
        doc1 = SRSDocument(**make_document(version="1.0.0"))
        doc2 = SRSDocument(**make_document(version="1.1.0"))
        assert doc1.document_id == doc2.document_id
        assert doc1.version != doc2.version

    def test_two_documents_same_id_and_version_conflict(self):
        kwargs = make_document(version="1.0.0")
        SRSDocument(**kwargs)
        with pytest.raises(DuplicateIdentityError):
            SRSDocument(**kwargs)


class TestDocumentMetadata:
    """REQ 1.2 — mandatory metadata, schema-validated."""

    @pytest.mark.parametrize(
        "missing",
        [
            "document_id",
            "project_name",
            "version",
            "owner",
            "approval_authority",
            "creation_date",
        ],
    )
    def test_metadata_requires_mandatory_fields(self, missing):
        kwargs = make_document()
        del kwargs[missing]
        with pytest.raises(MetadataError):
            SRSDocument(**kwargs)

    def test_metadata_validates_required_fields_present(self):
        doc = SRSDocument(**make_document())
        assert doc.project_name == "AI Investment Opportunity Agent"
        assert doc.version == "1.0.0"
        assert doc.approval_authority == "Project Governance"


pytestmark = pytest.mark.unit
