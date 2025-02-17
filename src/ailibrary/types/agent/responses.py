from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from ..shared.responses import APIResponse, ListResponse
from ..shared.base import MetaModel

class AgentData(MetaModel):
    namespace: str
    title: str
    created_timestamp: datetime
    type: str
    description: Optional[str] = None
    status: Optional[str] = None
    knowledge_search: Optional[bool] = None
    knowledgeId: Optional[str] = None

class AgentResponse(APIResponse[AgentData]):
    pass

class AgentListResponse(ListResponse[AgentData]):
    pass
