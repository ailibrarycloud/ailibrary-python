from typing import Dict, List, Optional, BinaryIO
from ..utils.http_client import HTTPClient


class Files:
    """Files resource for managing file uploads and operations."""

    def __init__(self, http_client: HTTPClient):
        self._http_client = http_client

    def upload(self, files: List[BinaryIO], knowledge_id: Optional[str] = None) -> List[Dict]:
        """Upload files to AI Library."""
        files_data = [('files', file) for file in files]
        params = {}
        if knowledge_id:
            params['knowledgeId'] = knowledge_id
        return self._http_client._request("POST", "/files", files=files_data, params=params)

    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> Dict:
        """List all files."""
        params = {}
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return self._http_client._request("GET", "/files", params=params)

    def get(self, file_id: str) -> Dict:
        """Retrieve a file by ID."""
        return self._http_client._request("GET", f"/files/{file_id}")

    def delete(self, file_id: str) -> Dict:
        """Delete a file."""
        return self._http_client._request("DELETE", f"/files/{file_id}")
