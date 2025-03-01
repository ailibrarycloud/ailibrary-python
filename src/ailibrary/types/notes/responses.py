from datetime import datetime
from typing import Optional
# from ..shared.responses import APIResponse, ListResponse
from ..shared.enums import ResourceType, RoleType
from ..shared.models import CustomBaseModel


class NoteAddResponse(CustomBaseModel):
    status: str
    noteId: str

class NoteUpdateResponse(CustomBaseModel):
    status: str
    message: str
    meta: Optional[dict] = None

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
    resourceId: Optional[str] = None
    updated_timestamp: str
    userEmail: str
    userName: str