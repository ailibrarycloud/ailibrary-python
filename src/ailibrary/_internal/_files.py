from typing import List, Optional
from .__http_client import _HTTPClient
import mimetypes
import os
from ..types.files.requests import FileUploadRequest
from ..types.files.responses import FileResponse, FileListResponse, FileData
from ..types.shared.base import PaginationParams
from ..types.shared.enums import HTTPMethod


class _Files:
    """Files resource for managing file uploads and operations."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def upload(self, file_paths: List[str], knowledgeId: Optional[str] = None) -> FileResponse:
        """Upload files to AI Library.
        files is a list where each element contains a path to the file.
        """
        request = FileUploadRequest(file_paths=file_paths, knowledgeId=knowledgeId)
        files = []
        payload = {}
        
        if request.knowledgeId:
            payload['knowledgeId'] = request.knowledgeId
            
        for file_path in request.file_paths:
            file_name = os.path.basename(file_path)
            mime_type = mimetypes.guess_type(file_path)[0]
            files.append(
                ('files', (file_name, open(file_path, 'rb'), mime_type))
            )

        response = self._http_client._request(
            HTTPMethod.POST,
            "/v1/files",
            data=payload,
            files=files
        )
        return FileResponse(**response)

    def list_files(self, page: Optional[int] = None, limit: Optional[int] = None) -> FileListResponse:
        """List all files."""
        pagination = PaginationParams(page=page, limit=limit)
        response = self._http_client._request(
            HTTPMethod.GET,
            "/v1/files",
            params=pagination.model_dump()
        )
        return FileListResponse(**response)

    def get(self, file_id: int) -> FileResponse:
        """Retrieve a file by ID."""
        response = self._http_client._request(
            HTTPMethod.GET,
            f"/v1/files/{file_id}"
        )
        return FileResponse(**response)

    def delete(self, file_id: int) -> FileResponse:
        """Delete a file."""
        response = self._http_client._request(
            HTTPMethod.DELETE,
            f"/v1/files/{file_id}"
        )
        return FileResponse(**response)
