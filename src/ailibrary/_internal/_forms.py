from typing import Optional
from .__http_client import _HTTPClient
from ..types.forms.requests import (
    FormCreateRequest,
    FormUpdateRequest,
    FormDeleteRequest
)
from ..types.forms.responses import (
    FormCreateResponse,
    FormGetResponse,
    FormListResponse,
    FormUpdateResponse,
    FormDeleteResponse
)
from pydantic import ValidationError


class _Forms:
    """Forms resource for managing form templates and submissions."""

    _RESOURCE_PATH = "/form"

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def _validate_response(self, response: dict, validation_class) -> dict:
        try:
            validation_class(**response)
            return response
        except ValidationError as e:
            raise e


    def create(self, title: str, schema: dict) -> dict:
        """Create a new form template.
        
        Args:
            title: The title of the form
            schema: List of field definitions
        """
        payload = FormCreateRequest(title=title, schema=schema).model_dump()
        response = self._http_client._request(
            "POST",
            # f"{self._RESOURCE_PATH}/create",
            f"{self._RESOURCE_PATH}",
            json=payload
        )
        return self._validate_response(response, FormCreateResponse)


    def get(self, form_id: str) -> dict:
        """Retrieve a form template by ID."""
        if not isinstance(form_id, str) or not form_id:
            raise ValueError("form_id must be a non-empty string")
        response = self._http_client._request(
            "GET",
            f"{self._RESOURCE_PATH}/{form_id}"
        )
        return self._validate_response(response, FormGetResponse)


    def list_forms(self) -> dict:
        """List all form templates."""
        response = self._http_client._request("GET", self._RESOURCE_PATH)
        return self._validate_response(response, FormListResponse)


    def update(self, form_id: str, **kwargs) -> dict:
        """Update an existing form template."""
        payload = FormUpdateRequest(form_id=form_id, **kwargs).model_dump()
        response = self._http_client._request(
            "PUT",
            f"{self._RESOURCE_PATH}/{form_id}",
            json=payload
        )
        return self._validate_response(response, FormUpdateResponse)


    def delete(self, form_id: str) -> dict:
        """Delete a form template."""
        if not isinstance(form_id, str) or not form_id:
            raise ValueError("form_id must be a non-empty string")
        response = self._http_client._request(
            "DELETE",
            f"{self._RESOURCE_PATH}/{form_id}",
        )
        return self._validate_response(response, FormDeleteResponse)
