from typing import Optional
from pydantic import Field
from ..shared.base import CustomBaseModel
from ..shared.enums import AgentType


class AgentDeleteRequest(CustomBaseModel):
    namespace: str = Field(..., 
        description="The unique identifier for the agent",
        exclude=True
    )
    delete_connected_resources: bool


class AgentCreateRequest(CustomBaseModel):
    title: str = Field(..., description="The name of your agent")
    instructions: str = Field(
        default="You are a helpful assistant.",
        description="System instructions for the agent"
    )
    type: Optional[AgentType] = None
    description: Optional[str] = None
    coverimage: Optional[str] = None
    intromessage: Optional[str] = None
    knowledge_search: Optional[bool] = None
    knowledgeId: Optional[str] = None
    form_filling: Optional[bool] = None
    form_id: Optional[str] = None
    form_schema: Optional[str] = None
    

class AgentUpdateRequest(AgentCreateRequest):
    namespace: str = Field(..., 
        description="The unique identifier for the agent",
        exclude=True
    )
