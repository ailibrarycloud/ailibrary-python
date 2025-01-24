from typing import Dict, List, Optional, Union
from ..utils.http import HTTPClient

class Notes:
    """Notes resource for managing notes on resources."""
    
    def __init__(self, http: HTTPClient):
        self.http = http
    
    def add(
        self,
        content: str,
        role: str,
        resource: str,
        resource_id: str,
        meta: Optional[Dict] = None
    ) -> Dict:
        """Add a note to a resource."""
        payload = {
            "content": content,
            "role": role,
            "resource": resource,
            "resource_id": resource_id
        }
        if meta:
            payload["meta"] = meta
        return self.http.request("POST", "/notes", json=payload)
    
    def get_for_resource(self, resource: str, resource_id: str) -> List[Dict]:
        """Get notes for a resource."""
        return self.http.request("GET", f"/notes/{resource}/{resource_id}")
    
    def update(
        self,
        note_id: str,
        content: str,
        role: str,
        meta: Optional[Dict] = None
    ) -> Dict:
        """Update a note."""
        payload = {
            "content": content,
            "role": role
        }
        if meta:
            payload["meta"] = meta
        return self.http.request("PUT", f"/notes/{note_id}", json=payload)
    
    def get(self, note_id: str) -> Dict:
        """Get a note by ID."""
        return self.http.request("GET", f"/notes/{note_id}")
    
    def delete_for_resource(
        self,
        resource: str,
        resource_id: str,
        values: Optional[List[str]] = None,
        delete_all: bool = False
    ) -> Dict:
        """Delete notes for a resource."""
        payload = {"delete_all": delete_all}
        if values:
            payload["values"] = values
        return self.http.request("DELETE", f"/notes/{resource}/{resource_id}", json=payload)
    
    def delete(self, note_id: str) -> Dict:
        """Delete a note by ID."""
        return self.http.request("DELETE", f"/notes/{note_id}")