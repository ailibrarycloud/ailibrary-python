from typing import Optional, List
from pydantic import , Field
from ..shared import MetaModel, AgentType

class AgentCreateRequest(MetaModel):
    title: str = Field(..., description="The name of your agent")
    instructions: str = Field(
        default="You are a helpful assistant.",
        description="System instructions for the agent"
    )
    description: Optional[str] = None
    coverimage: Optional[str] = None
    intromessage: Optional[str] = None
    knowledge_search: Optional[bool] = None
    knowledgeId: Optional[str] = None
    form_filling: Optional[bool] = None
    form_id: Optional[str] = None
    form_schema: Optional[str] = None

class AgentUpdateRequest(MetaModel):
    namespace: str
    title: Optional[str] = None
    type: Optional[AgentType] = None
    instructions: Optional[str] = None
    description: Optional[str] = None
    coverimage: Optional[str] = None
    intromessage: Optional[str] = None
    knowledge_search: Optional[bool] = None
    knowledgeId: Optional[str] = None
