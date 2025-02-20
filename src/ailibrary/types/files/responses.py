from datetime import datetime
from typing import Optional
from ..shared.responses import APIResponse, ListResponse
from .requests import FileUploadRequest
from ..shared.base import CustomBaseModel

class FileData(CustomBaseModel):
    id: int
    name: str
    mime_type: str
    size: int
    created_timestamp: datetime
    knowledgeId: Optional[str] = None

class FileUploadResponse(CustomBaseModel):
    files: list[FileData]
    meta: dict

class FileGetResponse(FileData):
    pass

class FileListResponse(CustomBaseModel):
    files: list[FileData]
    meta: dict
