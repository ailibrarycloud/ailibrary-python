from typing import Optional
from .__http_client import _HTTPClient
from ..types.notes.requests import (
    NoteCreateRequest,
    NoteUpdateRequest,
    NoteDeleteRequest
)
from ..types.notes.responses import (
    NoteResponse,
    NoteListResponse,
    NoteData
)
from ..types.shared.enums import ResourceType, RoleType

class _Notes:
    """Notes resource for managing notes on resources."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def add(
        self,
        content: str,
        role: RoleType,
        resource: ResourceType,
        resource_id: str,
        meta: Optional[dict] = None
    ) -> NoteResponse:
        """Add a note to a resource.
            Args:
                content: The content of the note
                role: RoleType enum value
                resource: ResourceType enum value
                resource_id:
                    if resource == ResourceType.AGENT:
                        resource_id is namespace
                    if resource == ResourceType.KNOWLEDGE_BASE:
                        resource_id is knowledgeId
                    if resource == ResourceType.FILE:
                        resource_id is id
                meta: Optional metadata
        """
        request = NoteCreateRequest(
            content=content,
            role=role,
            resource=resource,
            resource_id=resource_id,
            meta=meta
        )
        response = self._http_client._request(
            "POST",
            "/v1/notes",
            json=request.model_dump()
        )
        return NoteResponse(**response)

    def get_resource_notes(self, resource: ResourceType, resource_id: str) -> NoteListResponse:
        """Get notes for a resource."""
        response = self._http_client._request(
            "GET",
            f"/v1/notes/{resource}/{resource_id}"
        )
        return NoteListResponse(**response)

    def get(self, note_id: str) -> NoteResponse:
        """Get a note by ID."""
        response = self._http_client._request(
            "GET",
            f"/v1/notes/{note_id}"
        )
        return NoteResponse(**response)

    def update(
        self,
        note_id: str,
        content: str,
        role: RoleType,
        meta: Optional[dict] = None
    ) -> NoteResponse:
        """Update a note."""
        request = NoteUpdateRequest(
            content=content,
            role=role,
            meta=meta
        )
        response = self._http_client._request(
            "PUT",
            f"/v1/notes/{note_id}",
            json=request.model_dump()
        )
        return NoteResponse(**response)

    def delete_notes(
        self,
        resource: ResourceType,
        resource_id: str,
        values: Optional[list[str]] = None,
        delete_all: Optional[bool] = None
    ) -> NoteResponse:
        """Delete notes for a resource."""
        request = NoteDeleteRequest(
            resource=resource,
            resource_id=resource_id,
            values=values,
            delete_all=delete_all
        )
        response = self._http_client._request(
            "DELETE",
            f"/v1/notes/{resource}/{resource_id}",
            json=request.model_dump()
        )
        return NoteResponse(**response)
