from typing import Dict, List, Optional
from ..utils.http import HTTPClient

class Notes:
    def __init__(self, http: HTTPClient):
        self._http = http

    def add(
        self,
        content: str,
        role: str,
        resource: str,
        resource_id: str,
        meta: Optional[Dict] = None
    ) -> Dict:
        payload = {
            "content": content,
            "role": role,
            "resource": resource,
            "resource_id": resource_id
        }
        if meta:
            payload["meta"] = meta
        return self._http.request("POST", "/notes", json=payload)

    def get_for_resource(self, resource: str, resource_id: str) -> List[Dict]:
        return self._http.request("GET", f"/notes/{resource}/{resource_id}")

    def update(
        self,
        note_id: str,
        content: str,
        role: str,
        meta: Optional[Dict] = None
    ) -> Dict:
        payload = {
            "content": content,
            "role": role
        }
        if meta:
            payload["meta"] = meta
        return self._http.request("PUT", f"/notes/{note_id}", json=payload)

    def get(self, note_id: str) -> Dict:
        return self._http.request("GET", f"/notes/{note_id}")

    def delete_for_resource(
        self,
        resource: str,
        resource_id: str,
        values: Optional[List[str]] = None,
        delete_all: bool = False
    ) -> Dict:
        payload = {"delete_all": delete_all}
        if values:
            payload["values"] = values
        return self._http.request("DELETE", f"/notes/{resource}/{resource_id}", json=payload)

    def delete(self, note_id: str) -> Dict:
        return self._http.request("DELETE", f"/notes/{note_id}")