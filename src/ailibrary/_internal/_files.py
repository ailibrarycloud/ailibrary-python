from typing import Dict, List, Tuple, Optional, BinaryIO
from .__http_client import _HTTPClient
import mimetypes
import os


class _Files:
    """Files resource for managing file uploads and operations."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def upload(self, files: List[str], knowledge_id: Optional[str] = None) -> List[Dict]:
        """Upload files to AI Library.
        files is a list where each element contains a path to the file.
        """

        payload = {}
        if knowledge_id:
            payload['knowledgeId'] = knowledge_id
        for file in files:
            file_name = os.path.basename(file)
            mime_type = mimetypes.guess_type(file)[0]
            files = [
                ('files', (file_name, open(file, 'rb'), mime_type))
            ]

        return self._http_client._request("POST", "/v1/files", data=payload, files=files)



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
