from typing import Dict, List, Optional
from ..utils.http import HTTPClient

class KnowledgeBase:
    """Knowledge Base resource for managing vector databases."""
    
    def __init__(self, http: HTTPClient):
        self.http = http
    
    def create(self, name: str, meta: Optional[Dict] = None) -> Dict:
        """Create a new knowledge base."""
        payload = {"name": name}
        if meta:
            payload["meta"] = meta
        return self.http.request("POST", "/knowledgebase", json=payload)
    
    def list(self) -> Dict:
        """List all knowledge bases."""
        return self.http.request("GET", "/knowledgebase")
    
    def get(self, knowledge_id: str) -> Dict:
        """Retrieve a knowledge base by ID."""
        return self.http.request("GET", f"/knowledgebase/{knowledge_id}")
    
    def add_source(
        self,
        knowledge_id: str,
        source_type: str,
        urls: List[str],
        meta: Optional[Dict] = None,
    ) -> Dict:
        """Add sources to a knowledge base."""
        payload = {
            "type": source_type,
            "options": {"urls": urls}
        }
        if meta:
            payload["meta"] = meta
        return self.http.request("PUT", f"/knowledgebase/{knowledge_id}", json=payload)
    
    def get_status(self, knowledge_id: str) -> Dict:
        """Get knowledge base processing status."""
        return self.http.request("GET", f"/knowledgebase/{knowledge_id}/status")
    
    def get_source(self, knowledge_id: str, source_id: str) -> Dict:
        """Retrieve source details."""
        return self.http.request("GET", f"/knowledgebase/{knowledge_id}/{source_id}")
    
    def list_sources(self, knowledge_id: str) -> List[Dict]:
        """List all sources in a knowledge base."""
        return self.http.request("GET", f"/knowledgebase/{knowledge_id}/sources")
    
    def delete_sources(
        self,
        knowledge_id: str,
        values: Optional[List[str]] = None,
        delete_all: bool = False
    ) -> Dict:
        """Delete sources from a knowledge base."""
        payload = {"delete_all": delete_all}
        if values:
            payload["values"] = values
        return self.http.request("DELETE", f"/knowledgebase/{knowledge_id}/source", json=payload)