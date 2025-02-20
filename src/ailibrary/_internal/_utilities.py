from .__http_client import _HTTPClient
from ..types.utilities.requests import WebSearchRequest, WebParserRequest
from ..types.utilities.responses import (
    WebSearchResponse,
    WebParserResponse,
)
# from ..types.utilities.responses import SearchResultData, ParsedContentData

class _Utilities:
    """Utility functions to support AI agents."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def web_search(self, search_terms: list[str]) -> WebSearchResponse:
        """Search the web for terms."""
        request = WebSearchRequest(search_terms=search_terms)
        response = self._http_client._request(
            "POST",
            "/v1/utilities/websearch",
            json=request.model_dump()
        )
        return WebSearchResponse(**response)

    def web_parser(self, urls: list[str]) -> WebParserResponse:
        """Parse web pages for content."""
        request = WebParserRequest(urls=urls)
        response = self._http_client._request(
            "POST",
            "/v1/utilities/webparser",
            json=request.model_dump()
        )
        return WebParserResponse(**response)
