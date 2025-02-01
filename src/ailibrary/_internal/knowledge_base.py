from ..utils.http_client import _HTTPClient
from typing import Dict, List, Optional


class _KnowledgeBase:
    """Knowledge Base resource for managing vector databases."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def create(self, name: str, meta: Optional[Dict] = None) -> Dict:
        """Create a new knowledge base."""
        if not name:
            raise ValueError("Name cannot be empty")
        payload = {"name": name}
        if meta:
            payload["meta"] = meta
        return self._http_client._request("POST", "/v1/knowledgebase", json=payload)


    def list_knowledge_bases(self) -> Dict:
        """List all knowledge bases."""
        return self._http_client._request("GET", "/v1/knowledgebase")


    def get(self, knowledge_id: str) -> Dict:
        """Retrieve a knowledge base by ID."""
        if not knowledge_id:
            raise ValueError("Knowledge ID cannot be empty")
        return self._http_client._request("GET", f"/v1/knowledgebase/{knowledge_id}")


    def add_source(
        self,
        knowledge_id: str,
        type: str,
        meta: Optional[Dict] = None,
        options: Optional[Dict] = None
    ) -> Dict:
        """Add sources to a knowledge base."""
        
        valid_types = ["docs"]
        if type not in valid_types:
            raise ValueError(f"Invalid type. Valid types: {self._http_client._stringify(valid_types)} .")

        payload = {
            "type": type
        }
        optional_params = {"meta": meta, "options": options}
        for param in optional_params:
            param_value = optional_params[param]
            if param_value is not None:
                payload[param] = param_value
        return self._http_client._request("PUT", f"/v1/knowledgebase/{knowledge_id}", json=payload)


    def get_status(self, knowledge_id: str) -> Dict:
        """Get knowledge base processing status."""
        return self._http_client._request("GET", f"/v1/knowledgebase/{knowledge_id}/status")


    def get_source(self, knowledge_id: str, source_id: str) -> Dict:
        """Retrieve source details."""
        return self._http_client._request("GET", f"/v1/knowledgebase/{knowledge_id}/{source_id}")


    def list_sources(self, knowledge_id: str) -> List[Dict]:
        """List all sources in a knowledge base."""
        return self._http_client._request("GET", f"/v1/knowledgebase/{knowledge_id}/sources")


    def delete_sources(
        self,
        knowledge_id: str,
        values: List[str],
        delete_all: Optional[bool] = False
    ) -> Dict:
        """Delete sources from a knowledge base."""
        payload = {"values": values}
        if delete_all:
            payload["delete_all"] = delete_all
        return self._http_client._request("DELETE", f"/v1/knowledgebase/{knowledge_id}/source", json=payload)
