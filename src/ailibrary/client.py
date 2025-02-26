from ._internal._agent import _Agent
from ._internal._knowledge_base import _KnowledgeBase
from ._internal._files import _Files
from ._internal._utilities import _Utilities
from ._internal._notes import _Notes
from ._internal.__http_client import _HTTPClient


class AILibrary:
    """Main client for interacting with the AI Library API."""

    def __init__(self, api_key: str, domain: str = "https://api.ailibrary.ai/", version: str = "v1/"):
        self._http_client = _HTTPClient(api_key, domain, version)

        # Initialize resources
        self.agent = _Agent(self._http_client)
        self.knowledge_base = _KnowledgeBase(self._http_client)
        self.files = _Files(self._http_client)
        self.utilities = _Utilities(self._http_client)
        self.notes = _Notes(self._http_client)
