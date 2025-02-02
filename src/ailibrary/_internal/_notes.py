from typing import Dict, List, Optional
from .__http_client import __HTTPClient


class _Notes:
    """Notes resource for managing notes on resources."""

    def __init__(self, http_client: __HTTPClient):
        self.VALID_ROLES = ["assistant", "user", "system"]
        self.VALID_RESOURCES = ["agent", "knowledgebase", "file"]
        self._http_client = http_client


    def _check_role(self, role: str):
        if role not in self.VALID_ROLES:
            raise ValueError(f"Invalid role. Valid roles: {self._http_client._stringify(self.VALID_ROLES)} .")


    def _check_resource(self, resource: str):
        if resource not in self.VALID_RESOURCES:
            raise ValueError(f"Invalid resource. Valid resources: {self._http_client._stringify(self.VALID_RESOURCES)} .")


    def add(
        self,
        content: str,
        role: str,
        resource: str,
        resource_id: str,
        meta: Optional[Dict] = None
    ) -> Dict:
        """Add a note to a resource.
            Args:
                content: The content of the note
                role: Possible values: see self.VALID_ROLES
                resource: Possible values: see self.VALID_RESOURCES
                resource_id:
                    if resouce == 'agent':
                        resource_id is namespace
                    if resouce == 'knowledgebase'
                        resource_id is knowledgeId
                    if resouce == 'file'
                        resource_id is id

                meta: Optional arg
        """

        self._check_role(role)
        self._check_resource(resource)
        
        payload = {
            "content": content,
            "role": role,
            "resource": resource,
            "resource_id": resource_id
        }
        if meta:
            payload["meta"] = meta
        return self._http_client._request("POST", "/v1/notes", json=payload)


    def get_for_resource(self, resource: str, resource_id: str) -> List[Dict]:
        """Get notes for a resource."""
        self._check_resource(resource)
        return self._http_client._request("GET", f"/v1/notes/{resource}/{resource_id}")


    def update(
        self,
        note_id: str,
        content: str,
        role: str,
        meta: Optional[Dict] = None
    ) -> Dict:
        """Update a note."""
        self._check_role(role)
        payload = {
            "content": content,
            "role": role
        }
        if meta:
            payload["meta"] = meta
        return self._http_client._request("PUT", f"/v1/notes/{note_id}", json=payload)


    def get(self, note_id: str) -> Dict:
        """Get a note by ID."""
        return self._http_client._request("GET", f"/v1/notes/{note_id}")


    def delete_notes(
        self,
        resource: str,
        resource_id: str,
        values: List[str] = None,
        delete_all: bool = None
    ) -> Dict:
        """Delete notes for a resource.
        <resource> and <resource_id> are required, as well as 
        one of the following: <values> or <delete_all>.
        If <values> is not provided, <delete_all> must be true.
        """
        self._check_resource(resource)
        if (not values and not delete_all):
            raise ValueError("One of the following is required: values or delete_all=True.")
        
        payload = {"resource": resource, "resource_id": resource_id}
        if delete_all:
            payload["delete_all"] = delete_all  # doesn't matter what values are, delete all notes
        else:
            payload["values"] = values # only delete notes with these values
        return self._http_client._request("DELETE", f"/v1/notes/{resource}/{resource_id}", json=payload)
