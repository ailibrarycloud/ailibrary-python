from typing import Optional
from .utils.http_client import _HTTPClient
from .resources.agent import Agent
from .resources.knowledge_base import KnowledgeBase
from .resources.files import Files
from .resources.utilities import Utilities
from .resources.notes import Notes


class AILibrary:
    """
    Flexible client for AI Library API that handles authentication and resource creation.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.ailibrary.ai/v1"):
        """Initialize the client with authentication."""
        self._http_client = _HTTPClient(api_key, base_url)

    def create_agent(self) -> Agent:
        """Create a new Agent instance using authenticated client."""
        return Agent(http_client=self._http_client)

    def create_knowledge_base(self) -> KnowledgeBase:
        """Create a new Knowledge Base instance using authenticated client."""
        return KnowledgeBase(http_client=self._http_client)

    def create_files(self) -> Files:
        """Create a new Files instance using authenticated client."""
        return Files(http_client=self._http_client)

    def create_utilities(self) -> Utilities:
        """Create a new Utilities instance using authenticated client."""
        return Utilities(http_client=self._http_client)

    def create_notes(self) -> Notes:
        """Create a new Notes instance using authenticated client."""
        return Notes(http_client=self._http_client)
