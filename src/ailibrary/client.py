from typing import Optional
from .utils.http import HTTPClient
from .resources.agent import Agent
from .resources.knowledge_base import KnowledgeBase
from .resources.files import Files
from .resources.utilities import Utilities
from .resources.notes import Notes

class AILibrary:
    """
    Flexible client for AI Library API that handles authentication and resource creation.
    Does not automatically instantiate resources unless requested.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.ailibrary.ai/v1"):
        """Initialize the client with authentication."""
        self._http = HTTPClient(api_key, base_url)
    
    def create_agent(self) -> Agent:
        """Create a new Agent instance using the authenticated HTTP client."""
        return Agent(http=self._http)
    
    def create_knowledge_base(self) -> KnowledgeBase:
        """Create a new KnowledgeBase instance using the authenticated HTTP client."""
        return KnowledgeBase(http=self._http)
    
    def create_files(self) -> Files:
        """Create a new Files instance using the authenticated HTTP client."""
        return Files(http=self._http)
    
    def create_utilities(self) -> Utilities:
        """Create a new Utilities instance using the authenticated HTTP client."""
        return Utilities(http=self._http)
    
    def create_notes(self) -> Notes:
        """Create a new Notes instance using the authenticated HTTP client."""
        return Notes(http=self._http)