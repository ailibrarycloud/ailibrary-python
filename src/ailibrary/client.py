from typing import Optional
from .resources.agent import Agent
from .resources.knowledge_base import KnowledgeBase
from .resources.files import Files
from .resources.utilities import Utilities
from .resources.notes import Notes
from .utils.http_client import _HTTPClient


class AILibraryClient:
    """Main client for interacting with the AI Library API."""

    def __init__(self, api_key: str, base_url: str = "https://api.ailibrary.ai/v1"):
        self._http_client = _HTTPClient(api_key, base_url)

        # Initialize resources
        self.agent = Agent(self._http_client)
        self.knowledge_base = KnowledgeBase(self._http_client)
        self.files = Files(self._http_client)
        self.utilities = Utilities(self._http_client)
        self.notes = Notes(self._http_client)
