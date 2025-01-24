from typing import Optional
from .resources.agent import Agent
from .resources.knowledge_base import KnowledgeBase
from .resources.files import Files
from .resources.utilities import Utilities
from .resources.notes import Notes
from .utils.http import HTTPClient

class AILibraryClient:
    """Main client for interacting with the AI Library API."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.ailibrary.ai/v1"):
        self.http = HTTPClient(api_key, base_url)
        
        # Initialize resources
        self.agent = Agent(self.http)
        self.knowledge_base = KnowledgeBase(self.http)
        self.files = Files(self.http)
        self.utilities = Utilities(self.http)
        self.notes = Notes(self.http)