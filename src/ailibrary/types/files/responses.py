from datetime import datetime
from typing import Optional
# from ..shared.responses import APIResponse, ListResponse
# from .requests import FileUploadRequest
from ..shared.models import CustomBaseModel


class FileResponseData(CustomBaseModel):
    url: str
    id: int
    bytes: int
    name: str
    meta: Optional[dict] = None

class FileUploadResponse(FileResponseData):
    pass

class FileGetResponse(FileResponseData):
    created_timestamp: str

class FileListResponse(CustomBaseModel):
    files: list[FileResponseData]
    meta: dict

class FileDeleteResponse(CustomBaseModel):
    response: str
