from typing import Dict, List, Optional, BinaryIO
from ..utils.http import HTTPClient

class Files:
    """Files resource for managing file uploads and operations."""
    
    def __init__(self, http: HTTPClient):
        self.http = http
    
    def upload(self, files: List[BinaryIO], knowledge_id: Optional[str] = None) -> List[Dict]:
        """Upload files to AI Library."""
        files_data = [('files', file) for file in files]
        params = {}
        if knowledge_id:
            params['knowledgeId'] = knowledge_id
        return self.http.request("POST", "/files", files=files_data)
    
    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> Dict:
        """List all files."""
        params = {}
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return self.http.request("GET", "/files", params=params)
    
    def get(self, file_id: str) -> Dict:
        """Retrieve a file by ID."""
        return self.http.request("GET", f"/files/{file_id}")
    
    def delete(self, file_id: str) -> Dict:
        """Delete a file."""
        return self.http.request("DELETE", f"/files/{file_id}")