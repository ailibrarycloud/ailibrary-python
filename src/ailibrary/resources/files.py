from typing import Dict, List, Optional, BinaryIO
from ..utils.http_client import _HTTPClient

###### WHAT IF USER PROVIDES THE WRONG TYPES OF VARIABLES? eg user passes a list instead of a string?
###### rather than use a million if statements in each function, how can we validate the data?

class Files:
    """Files resource for managing file uploads and operations."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def upload(self, files: List[BinaryIO], knowledge_id: Optional[str] = None) -> List[Dict]:
        """Upload files to AI Library."""

        ### verify files is correct here
        ### where/how is the knowledge_id passed to the client? 
        files_data = [('files', file) for file in files]
        # params = {}
        # if knowledge_id:
        #     params['knowledgeId'] = knowledge_id
        return self._http_client._request("POST", "/files", files=files_data)


    def list_files(self, page: Optional[int] = None, limit: Optional[int] = None) -> Dict:
        """List all files."""
        params_dict = {}
        optional_params = [page, limit]
        for param in optional_params
        if param:
            params_dict['page'] = page
        if limit:
            params['limit'] = limit
        return self._http_client._request("GET", "/files", params=params)


    def get(self, file_id: str) -> Dict:
        """Retrieve a file by ID."""
        return self._http_client._request("GET", f"/files/{file_id}")


    def delete(self, file_id: str) -> Dict:
        """Delete a file."""
        return self._http_client._request("DELETE", f"/files/{file_id}")
