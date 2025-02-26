from enum import Enum

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

class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class ResourcePath(str, Enum):
    AGENT = "/agent"
    KNOWLEDGE_BASE = "/knowledgebase"
    FILES = "/files"
    NOTES = "/notes"
    UTILITIES = "/utilities"
