from datetime import datetime
from typing import Optional
from pydantic import 
from ..shared.responses import APIResponse, ListResponse
from ..shared.base import MetaModel
from ..shared.enums import ResourceType, RoleType

class NoteData(MetaModel):
    id: str
    content: str
    role: RoleType
    resource: ResourceType
    resource_id: str
    created_timestamp: datetime
    updated_timestamp: Optional[datetime] = None

class NoteResponse(APIResponse[NoteData]):
    pass

class NoteListResponse(ListResponse[NoteData]):
    pass
