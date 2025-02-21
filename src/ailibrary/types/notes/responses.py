from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..shared.responses import APIResponse, ListResponse
from ..shared.base import MetaModel
from ..shared.enums import ResourceType, RoleType
from ..shared.base import CustomBaseModel


class NoteAddResponse(CustomBaseModel):
    status: str
    noteId: str

class NoteUpdateResponse(CustomBaseModel):
    status: str
    message: str
    meta: dict

class NoteDeleteResponse(CustomBaseModel):
    status: str
    message: str

class NoteData(CustomBaseModel):
    content: str
    role: RoleType
    meta: Optional[dict] = None
    created_timestamp: datetime

class NoteGetResourceNotesResponse(CustomBaseModel):
    notes: list[NoteData]
    meta: dict

class NoteGetResponse(NoteData):
    noteId: str
    resource: ResourceType
    resourceId: str
    updated_timestamp: str
    userEmail: str
    userName: str