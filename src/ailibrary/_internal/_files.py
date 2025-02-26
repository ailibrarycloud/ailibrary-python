from typing import Optional, BinaryIO, IO, Union
from .__http_client import _HTTPClient
import mimetypes
import os
from ..types.files.requests import FileUploadRequest, FileListRequest
from ..types.files.responses import FileUploadResponse, FileGetResponse, FileListResponse, FileDeleteResponse
from ..types.shared.base import PaginationParams
from pydantic import ValidationError


class _Files:
    """Files resource for managing file uploads and operations."""

    _RESOURCE_PATH = "/files"

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def _validate_response(self, response: Union[list[dict], dict], validation_class) -> Union[list[dict], dict]:
        try:
            if isinstance(response, list):
                for item in response:
                    validation_class(**item)
            else:
                validation_class(**response)
            return response
        except ValidationError as e:
            raise e


    def upload(self, files: list[str], knowledgeId: Optional[str] = None) -> dict:
        """Upload files to AI Library.
        Args:
            files: List of paths to files to upload
            knowledgeId: Optional knowledge base ID to associate files with
        """
        request = FileUploadRequest(files=files, knowledgeId=knowledgeId)
        file_objs = []
        payload = {}
        
        if request.knowledgeId:
            payload['knowledgeId'] = request.knowledgeId
            
        for file_path in request.files:
            # if not os.path.exists(file_path):
            #     raise ValueError(f"File not found: {file_path}")
            file_name = os.path.basename(file_path)
            mime_type = mimetypes.guess_type(file_path)[0]
            file_objs.append(
                ('files', (file_name, open(file_path, 'rb'), mime_type))
            )
        response = self._http_client._request("POST", self._RESOURCE_PATH, data=payload, files=file_objs)
        return self._validate_response(response, FileUploadResponse)


    def list_files(self, page: Optional[int] = None, limit: Optional[int] = None) -> dict:
        """List all files."""
        pagination = FileListRequest(page=page, limit=limit)
        response = self._http_client._request("GET", self._RESOURCE_PATH, params=pagination.model_dump())
        return self._validate_response(response, FileListResponse)


    def get(self, file_id: int) -> dict:
        """Retrieve a file by ID."""
        if not isinstance(file_id, int):
            raise ValueError("file_id must be an integer")
        response = self._http_client._request("GET", f"{self._RESOURCE_PATH}/{file_id}")
        return self._validate_response(response, FileGetResponse)


    def delete(self, file_id: int) -> dict:
        """Delete a file."""
        response = self._http_client._request("DELETE", f"{self._RESOURCE_PATH}/{file_id}")
        return self._validate_response(response, FileDeleteResponse)
