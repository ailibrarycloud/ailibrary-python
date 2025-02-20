from typing import Optional
from pydantic import BaseModel, Field
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

class NoteDeleteRequest(BaseModel):
    resource: ResourceType
    resource_id: str
    values: Optional[list[str]] = None
    delete_all: Optional[bool] = None
