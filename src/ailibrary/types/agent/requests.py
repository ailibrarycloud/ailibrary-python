from typing import Optional
from enum import Enum
from pydantic import Field
from .chat_message_model import ChatMessageModel
from ..shared.base import CustomBaseModel
from ..shared.enums import AgentType


class ResponseFormatEnum(str, Enum):
    # TEXT = "text"
    JSON = "json"

class AgentChatRequest(CustomBaseModel):
    namespace: str = Field(..., 
        description="The unique identifier for the agent",
        exclude=True,
        min_length=1
    )
    messages: list[ChatMessageModel]
    response_format: Optional[ResponseFormatEnum] = "json"
    session_id: Optional[str] = None
    

class AgentDeleteRequest(CustomBaseModel):
    namespace: str = Field(..., 
        description="The unique identifier for the agent",
        exclude=True,
        min_length=1
    )
    delete_connected_resources: bool


class AgentCreateRequest(CustomBaseModel):
    title: str = Field(..., description="The name of your agent", min_length=1)
    instructions: Optional[str] = "You are a helpful assistant."
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
        exclude=True,
        min_length=1
    )
    title: Optional[str] = None
    type: Optional[AgentType] = None
