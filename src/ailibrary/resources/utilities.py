from typing import Dict, List
from ..utils.http import HTTPClient

class Utilities:
    """Utility functions to support AI agents."""
    
    def __init__(self, http: HTTPClient):
        self.http = http
    
    def web_search(self, search_terms: List[str]) -> List[Dict]:
        """Search the web for terms."""
        return self.http.request("POST", "/utilities/websearch", json={
            "search_terms": search_terms
        })
    
    def web_parser(self, urls: List[str]) -> List[Dict]:
        """Parse web pages for content."""
        return self.http.request("POST", "/utilities/webparser", json={
            "urls": urls
        })