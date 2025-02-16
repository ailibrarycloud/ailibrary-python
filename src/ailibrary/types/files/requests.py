from typing import Optional, List
from pydantic import , Field
from ..shared.base import MetaModel, PaginationParams

class FileUploadRequest(MetaModel):
    file_paths: List[str] = Field(..., min_items=1)
    knowledgeId: Optional[str] = None

class FileListRequest(PaginationParams):
    pass
