from typing import Optional
from .__http_client import _HTTPClient
from ..types.knowledge_base.requests import (
    KnowledgeBaseCreateRequest,
    AddSourceRequest,
    DeleteSourcesRequest
)
from ..types.knowledge_base.responses import (
    KnowledgeBaseListResponse,
    KnowledgeBaseGetResponse,
    KnowledgeBaseCreateResponse,
    KnowledgeBaseDeleteResponse,
    SourceAddResponse
)
from pydantic import ValidationError


class _KnowledgeBase:
    """Knowledge Base resource for managing vector databases."""

    _RESOURCE_PATH = "/knowledgebase"

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def _validate_non_empty_string(self, value: str, param_name: str) -> None:
        if not isinstance(value, str) or not value:
            raise ValueError(f"{param_name} must be a non-empty string")

    def _validate_response(self, response: dict, validation_class) -> dict:
        try:
            validation_class(**response)
            return response
        except ValidationError as e:
            raise e


    def create(self, name: str, meta: Optional[dict] = None) -> dict:
        """Create a new knowledge base."""
        payload = KnowledgeBaseCreateRequest(name=name, meta=meta).model_dump()
        response = self._http_client._request(
            "POST",
            self._RESOURCE_PATH,
            json=payload
        )
        return self._validate_response(response, KnowledgeBaseCreateResponse)


    def list_knowledge_bases(self) -> dict:
        """List all knowledge bases."""
        response = self._http_client._request("GET", self._RESOURCE_PATH)
        return self._validate_response(response, KnowledgeBaseListResponse)


    def get(self, knowledgeId: str) -> dict:
        """Retrieve a knowledge base by ID."""
        self._validate_non_empty_string(knowledgeId, "knowledgeId")
        response = self._http_client._request("GET", f"{self._RESOURCE_PATH}/{knowledgeId}")
        return self._validate_response(response, KnowledgeBaseGetResponse)


    def get_status(self, knowledgeId: str) -> str:
        """Get knowledge base processing status."""
        self._validate_non_empty_string(knowledgeId, "knowledgeId")
        response = self._http_client._request("GET", f"{self._RESOURCE_PATH}/{knowledgeId}/status")
        if not isinstance(response, str):
            raise ValueError("knowledge_base.get_status() response is not a string")
        return response


    def delete(self, knowledgeId: str) -> str:
        """Delete knowledge base."""
        self._validate_non_empty_string(knowledgeId, "knowledgeId")
        response = self._http_client._request("DELETE", f"{self._RESOURCE_PATH}/{knowledgeId}")
        return self._validate_response(response, KnowledgeBaseDeleteResponse)


    def add_source(
        self,
        knowledgeId: str,
        type: str,
        options: Optional[dict] = None,
        meta: Optional[dict] = None,
    ) -> dict:
        """Add sources to a knowledge base."""
        payload = AddSourceRequest(type=type, options=options, meta=meta).model_dump()
        response = self._http_client._request(
            "PUT",
            f"{self._RESOURCE_PATH}/{knowledgeId}",
            json=payload
        )
        # return response
        return self._validate_response(response, SourceAddResponse)


    def list_sources(self, knowledgeId: str) -> dict:
        """List all sources in a knowledge base."""
        response = self._http_client._request(
            "GET",
            f"{self._RESOURCE_PATH}/{knowledgeId}/sources"
        )
        return response


    def get_source(self, knowledgeId: str, source: str) -> dict:
        """Retrieve source details."""
        response = self._http_client._request(
            "GET",
            f"{self._RESOURCE_PATH}/{knowledgeId}/{source}"
        )
        return response
    

    def delete_sources(
        self,
        knowledgeId: str,
        values: list[str],
        delete_all: Optional[bool] = None
    ) -> dict:
        """Delete sources from a knowledge base."""
        payload = DeleteSourcesRequest(knowledgeId=knowledgeId, values=values, delete_all=delete_all).model_dump()
        response = self._http_client._request(
            "DELETE",
            f"{self._RESOURCE_PATH}/{knowledgeId}/source",
            json=payload
        )
        return response
