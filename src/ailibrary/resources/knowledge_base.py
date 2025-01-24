from typing import Dict, List, Optional
from ..utils.http import HTTPClient

class KnowledgeBase:
    def __init__(self, http: HTTPClient):
        self._http = http

    def create(self, name: str, meta: Optional[Dict] = None) -> Dict:
        payload = {"name": name}
        if meta:
            payload["meta"] = meta
        return self._http.request("POST", "/knowledgebase", json=payload)

    def list(self) -> Dict:
        return self._http.request("GET", "/knowledgebase")

    def get(self, knowledge_id: str) -> Dict:
        return self._http.request("GET", f"/knowledgebase/{knowledge_id}")

    def add_source(
        self,
        knowledge_id: str,
        source_type: str,
        urls: List[str],
        meta: Optional[Dict] = None,
    ) -> Dict:
        payload = {
            "type": source_type,
            "options": {"urls": urls}
        }
        if meta:
            payload["meta"] = meta
        return self._http.request("PUT", f"/knowledgebase/{knowledge_id}", json=payload)

    def get_status(self, knowledge_id: str) -> Dict:
        return self._http.request("GET", f"/knowledgebase/{knowledge_id}/status")

    def get_source(self, knowledge_id: str, source_id: str) -> Dict:
        return self._http.request("GET", f"/knowledgebase/{knowledge_id}/{source_id}")

    def list_sources(self, knowledge_id: str) -> List[Dict]:
        return self._http.request("GET", f"/knowledgebase/{knowledge_id}/sources")

    def delete_sources(
        self,
        knowledge_id: str,
        values: Optional[List[str]] = None,
        delete_all: bool = False
    ) -> Dict:
        payload = {"delete_all": delete_all}
        if values:
            payload["values"] = values
        return self._http.request("DELETE", f"/knowledgebase/{knowledge_id}/source", json=payload)