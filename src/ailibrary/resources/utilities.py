from typing import Dict, List
from ..utils.http import HTTPClient

class Utilities:
    def __init__(self, http: HTTPClient):
        self._http = http

    def web_search(self, search_terms: List[str]) -> List[Dict]:
        return self._http.request("POST", "/utilities/websearch", json={
            "search_terms": search_terms
        })

    def web_parser(self, urls: List[str]) -> List[Dict]:
        return self._http.request("POST", "/utilities/webparser", json={
            "urls": urls
        })