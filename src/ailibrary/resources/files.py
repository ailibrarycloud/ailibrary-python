from typing import Dict, List, Optional, BinaryIO
from ..utils.http import HTTPClient

class Files:
    def __init__(self, http: HTTPClient):
        self._http = http

    def upload(self, files: List[BinaryIO], knowledge_id: Optional[str] = None) -> List[Dict]:
        files_data = [('files', file) for file in files]
        params = {}
        if knowledge_id:
            params['knowledgeId'] = knowledge_id
        return self._http.request("POST", "/files", files=files_data, params=params)

    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> Dict:
        params = {}
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return self._http.request("GET", "/files", params=params)

    def get(self, file_id: str) -> Dict:
        return self._http.request("GET", f"/files/{file_id}")

    def delete(self, file_id: str) -> Dict:
        return self._http.request("DELETE", f"/files/{file_id}")