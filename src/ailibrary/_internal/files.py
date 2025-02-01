from typing import Dict, List, Optional, BinaryIO
from ..utils.http_client import _HTTPClient


class _Files:
    """Files resource for managing file uploads and operations."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def upload(self, files: list, knowledge_id: Optional[str] = None) -> List[Dict]:
        """Upload files to AI Library.
        files is a list where each element contains a path to the file.
        """

        files_data = [('files', file) for file in files]
        payload = {}
        if knowledge_id:
            payload['knowledgeId'] = knowledge_id
        return self._http_client._request("POST", "/v1/files", files=files_data, json=payload)


    def list_files(self, page: Optional[int] = None, limit: Optional[int] = None) -> Dict:
        """List all files."""
        params_dict = {}
        optional_params = {"page": page, "limit": limit}
        for param in optional_params:
            param_value = optional_params[param]
            if param_value is not None:
                params_dict[param] = param_value

        return self._http_client._request("GET", "/v1/files", params=params_dict)


    def get(self, file_id: str) -> Dict:
        """Retrieve a file by ID."""
        return self._http_client._request("GET", f"/v1/files/{file_id}")


    def delete(self, file_id: str) -> Dict:
        """Delete a file."""
        return self._http_client._request("DELETE", f"/v1/files/{file_id}")
