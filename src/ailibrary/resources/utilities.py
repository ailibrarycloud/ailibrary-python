from typing import Dict, List
from ..utils.http_client import _HTTPClient


class Utilities:
    """Utility functions to support AI agents."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def web_search(self, search_terms: List[str]) -> List[Dict]:
        """Search the web for terms."""
        return self._http_client._request("POST", "/utilities/websearch", json={
            "search_terms": search_terms
        })


    def web_parser(self, urls: List[str]) -> List[Dict]:
        """Parse web pages for content."""
        return self._http_client._request("POST", "/utilities/webparser", json={
            "urls": urls
        })
