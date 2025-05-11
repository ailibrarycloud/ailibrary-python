from typing import Optional
from pydantic import Field
from ..shared.models import CustomBaseModel


class FileUploadRequest(CustomBaseModel):
    files: list[str] = Field(..., description="List of file paths to upload", min_length=1)
    knowledgeId: Optional[str] = Field(None, description="Optional knowledge base ID to associate files with")


class FileListRequest(CustomBaseModel):
    page: Optional[int] = Field(None, description="Page number for pagination")
    limit: Optional[int] = Field(None, description="Number of items per page")
