from typing import Optional
from .__http_client import _HTTPClient
from ..types.notes.requests import (
    NoteAddRequest,
    NoteUpdateRequest,
    NoteDeleteRequest
)
from ..types.notes.responses import (NoteAddResponse, NoteGetResourceNotesResponse, NoteUpdateResponse, NoteGetResponse, NoteDeleteResponse)
from ..types.shared.enums import ResourceType, RoleType
from pydantic import ValidationError


class _Notes:
    """Notes resource for managing notes on resources."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def _validate_response(self, response: dict, validation_class) -> dict:
        try:
            # if isinstance(response, list):
            #     for item in response:
            #         validation_class(**item)
            # else:
            validation_class(**response)
            return response
        except ValidationError as e:
            raise e


    def add(
        self,
        content: str,
        role: RoleType,
        resource: ResourceType,
        resource_id: str,
        meta: Optional[dict] = None
    ) -> dict:
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
        payload = NoteAddRequest(
            content=content,
            role=role,
            resource=resource,
            resource_id=resource_id,
            meta=meta
        ).model_dump()
        
        response = self._http_client._request(
            "POST",
            "/v1/notes",
            json=payload
        )
        return self._validate_response(response, NoteAddResponse)


    def get_resource_notes(self, resource: ResourceType, resource_id: str) -> dict:
        """Get notes for a resource."""
        response = self._http_client._request(
            "GET",
            f"/v1/notes/{resource}/{resource_id}"
        )
        return self._validate_response(response, NoteGetResourceNotesResponse)


    def get(self, note_id: str) -> dict:
        """Get a note by ID."""
        response = self._http_client._request(
            "GET",
            f"/v1/notes/{note_id}"
        )
        return self._validate_response(response, NoteGetResponse)


    def update(
        self,
        note_id: str,
        content: str,
        role: RoleType,
        meta: Optional[dict] = None
    ) -> dict:
        """Update a note."""
        payload = NoteUpdateRequest(
            note_id=note_id,
            content=content,
            role=role,
            meta=meta
        ).model_dump()

        response = self._http_client._request(
            "PUT",
            f"/v1/notes/{note_id}",
            json=payload
        )
        return self._validate_response(response, NoteUpdateResponse)


    def delete_notes(
        self,
        resource: ResourceType,
        resource_id: str,
        values: Optional[list[str]] = None,
        delete_all: Optional[bool] = None
    ) -> dict:
        """Delete notes for a resource."""
        payload = NoteDeleteRequest(
            resource=resource,
            resource_id=resource_id,
            values=values,
            delete_all=delete_all
        ).model_dump()
        
        response = self._http_client._request(
            "DELETE",
            f"/v1/notes/{resource}/{resource_id}",
            json=payload
        )
        return self._validate_response(response, NoteDeleteResponse)
