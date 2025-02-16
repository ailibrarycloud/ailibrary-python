from enum import Enum
from typing import Optional, Dict
from pydantic import BaseModel

class ResourceType(str, Enum):
    AGENT = "agent"
    KNOWLEDGE_BASE = "knowledgebase"
    FILE = "file"

class RoleType(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class AgentType(str, Enum):
    NOTEBOOK = "notebook"
    CHAT = "chat"
    VOICE = "voice"

class MetaModel(BaseModel):
    meta: Optional[Dict] = None
