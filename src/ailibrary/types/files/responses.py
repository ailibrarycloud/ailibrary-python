from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..shared.responses import APIResponse, ListResponse
from ..shared.base import MetaModel

class FileData(MetaModel):
    id: int
    name: str
    mime_type: str
    size: int
    created_timestamp: datetime
    knowledgeId: Optional[str] = None

class FileResponse(APIResponse[FileData]):
    pass

class FileListResponse(ListResponse[FileData]):
    pass
