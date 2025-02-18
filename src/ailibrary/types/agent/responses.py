from typing import Optional, List
from ..shared.responses import APIResponse, ListResponse
from .requests import AgentCreateRequest
from datetime import datetime


class AgentData(AgentCreateRequest):
    namespace: str
    created_timestamp: datetime
    status: Optional[str] = None


class AgentResponse(APIResponse[AgentData]):
    pass


class AgentListResponse(ListResponse[AgentData]):
    pass
