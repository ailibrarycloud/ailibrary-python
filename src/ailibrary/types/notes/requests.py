from typing import Optional, List
from pydantic import , Field
from ..shared.base import MetaModel
from ..shared.enums import ResourceType, RoleType

class NoteCreateRequest(MetaModel):
    content: str = Field(..., min_length=1)
    role: RoleType
    resource: ResourceType
    resource_id: str = Field(..., min_length=1)

class NoteUpdateRequest(MetaModel):
    content: str = Field(..., min_length=1)
    role: RoleType

class NoteDeleteRequest():
    resource: ResourceType
    resource_id: str
    values: Optional[List[str]] = None
    delete_all: Optional[bool] = None
