from typing import Optional, List
from ..shared.responses import APIResponse, ListResponse
from .requests import AgentCreateRequest
from ..shared.base import CustomBaseModel


class AgentCreateResponse(AgentCreateRequest):
    namespace: str

class AgentGetResponse(AgentCreateResponse):
    created_timestamp: Optional[str] = None 
    status: Optional[str] = None
    showcase: Optional[str] = None

class AgentListResponse(CustomBaseModel):
    agents: List[AgentGetResponse]
    meta: dict

class AgentUpdateResponse(CustomBaseModel):
    response: str

class AgentDeleteResponse(CustomBaseModel):
    statusCode: int
    message: str
