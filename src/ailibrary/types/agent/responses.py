from typing import Optional
from .requests import AgentCreateRequest
from ..shared.base import CustomBaseModel


class AgentCreateResponse(AgentCreateRequest):
    namespace: str

class AgentGetResponse(AgentCreateResponse):
    created_timestamp: Optional[str] = None 
    status: Optional[str] = None
    showcase: Optional[str] = None

class AgentListResponse(CustomBaseModel):
    agents: list[AgentGetResponse]
    meta: dict

class AgentUpdateResponse(CustomBaseModel):
    response: Optional[str] = None
    status: Optional[str] = None
    message: Optional[str] = None

class AgentDeleteResponse(CustomBaseModel):
    statusCode: int
    message: str
