from typing import List, Optional, Dict
from .__http_client import _HTTPClient
from ..types.knowledge_base.requests import (
    KnowledgeBaseCreateRequest,
    AddSourceRequest,
    DeleteSourcesRequest
)
from ..types.knowledge_base.responses import (
    KnowledgeBaseResponse,
    KnowledgeBaseListResponse,
    SourceListResponse,
    KnowledgeBaseData,
    SourceData
)


class _KnowledgeBase:
    """Knowledge Base resource for managing vector databases."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def create(self, name: str, meta: Optional[Dict] = None) -> KnowledgeBaseResponse:
        """Create a new knowledge base."""
        request = KnowledgeBaseCreateRequest(name=name, meta=meta)
        response = self._http_client._request(
            "POST",
            "/v1/knowledgebase",
            json=request.model_dump()
        )
        return KnowledgeBaseResponse(**response)


    def list_knowledge_bases(self) -> KnowledgeBaseListResponse:
        """List all knowledge bases."""
        response = self._http_client._request("GET", "/v1/knowledgebase")
        return KnowledgeBaseListResponse(**response)


    def get(self, knowledgeId: str) -> KnowledgeBaseResponse:
        """Retrieve a knowledge base by ID."""
        if not knowledgeId:
            raise ValueError("Knowledge ID cannot be empty")
        response = self._http_client._request("GET", f"/v1/knowledgebase/{knowledgeId}")
        return KnowledgeBaseResponse(**response)


    def get_status(self, knowledgeId: str) -> KnowledgeBaseResponse:
        """Get knowledge base processing status."""
        response = self._http_client._request("GET", f"/v1/knowledgebase/{knowledgeId}/status")
        return KnowledgeBaseResponse(**response)


    # ### WORK IN PROGRESS, error in internal implementation ###
    # def add_source(
    #     self,
    #     knowledgeId: str,
    #     type: str,
    #     meta: Optional[Dict] = None,
    #     urls: Optional[Dict] = None
    # ) -> KnowledgeBaseResponse:
    #     """Add sources to a knowledge base."""
    #     request = AddSourceRequest(
    #         type=type,
    #         urls=urls,
    #         meta=meta
    #     )
    #     response = self._http_client._request(
    #         "PUT",
    #         f"/v1/knowledgebase/{knowledgeId}",
    #         json=request.model_dump()
    #     )
    #     return KnowledgeBaseResponse(**response)


    # ### WORK IN PROGRESS, error in internal implementation ###
    # def get_source(self, knowledgeId: str, source_id: str) -> SourceData:
    #     """Retrieve source details."""
    #     response = self._http_client._request(
    #         "GET",
    #         f"/v1/knowledgebase/{knowledgeId}/{source_id}"
    #     )
    #     return SourceData(**response)


    # ### WORK IN PROGRESS, error in internal implementation ###
    # def list_sources(self, knowledgeId: str) -> SourceListResponse:
    #     """List all sources in a knowledge base."""
    #     response = self._http_client._request(
    #         "GET",
    #         f"/v1/knowledgebase/{knowledgeId}/sources"
    #     )
    #     return SourceListResponse(**response)


    # ### WORK IN PROGRESS, error in internal implementation ###
    # def delete_sources(
    #     self,
    #     knowledgeId: str,
    #     values: List[str],
    #     delete_all: Optional[bool] = False
    # ) -> KnowledgeBaseResponse:
    #     """Delete sources from a knowledge base."""
    #     request = DeleteSourcesRequest(values=values, delete_all=delete_all)
    #     response = self._http_client._request(
    #         "DELETE",
    #         f"/v1/knowledgebase/{knowledgeId}/source",
    #         json=request.model_dump()
    #     )
    #     return KnowledgeBaseResponse(**response)
