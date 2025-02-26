from .__http_client import _HTTPClient
from ..types.utilities.requests import WebSearchRequest, WebParserRequest
from ..types.utilities.responses import (
    WebSearchResponse,
    WebParserResponse,
)
from pydantic import ValidationError
from typing import Union
from ..types.shared.enums import ResourcePath
# from ..types.utilities.responses import SearchResultData, ParsedContentData

class _Utilities:
    """Utility functions to support AI agents."""

    _RESOURCE_PATH = ResourcePath.UTILITIES

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def _validate_response(self, response: Union[dict, list[dict]], validation_class) -> Union[dict, list[dict]]    :
        try:
            if isinstance(response, list):
                for item in response:
                    validation_class(**item)
            else:
                validation_class(**response)
            return response
        except ValidationError as e:
            raise e


    def web_search(self, search_terms: list[str]) -> dict:
        """Search the web for terms."""
        payload = WebSearchRequest(search_terms=search_terms).model_dump()
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/websearch",
            json=payload
        )
        return self._validate_response(response, WebSearchResponse)


    def web_parser(self, urls: list[str]) -> dict:
        """Parse web pages for content."""
        payload = WebParserRequest(urls=urls).model_dump()
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/webparser",
            json=payload
        )
        return self._validate_response(response, WebParserResponse)
