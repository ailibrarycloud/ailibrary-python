from .__http_client import _HTTPClient
from ..types.utilities.requests import (
    WebSearchRequest, 
    WebParserRequest,
    NewsSearchRequest,
    DocumentParserRequest,
    DocumentThumbnailRequest,
    JSONSchemaGeneratorRequest
)
from ..types.utilities.responses import (
    WebSearchResponse,
    WebParserResponse,
    NewsSearchResponse,
    DocumentParserResponse,
    DocumentThumbnailResponse
)
from ..types.shared.enums import ResourcePath
from pydantic import ValidationError
from typing import Union, Optional


# from ..types.utilities.responses import SearchResultData, ParsedContentData

class _Utilities:
    """Utility functions to support AI agents."""

    _RESOURCE_PATH = ResourcePath.UTILITIES.value

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def _validate_response(self, response: Union[dict, list[dict]], validation_class) -> Union[dict, list[dict]]:
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


    def news_search(self, search_terms: list[str]) -> dict:
        """Search news articles for terms."""
        payload = NewsSearchRequest(search_terms=search_terms).model_dump()
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/news",
            json=payload
        )
        return self._validate_response(response, NewsSearchResponse)


    def document_parser(self, urls: str) -> dict:
        """Parse document content and metadata."""
        payload = DocumentParserRequest(urls=urls).model_dump()
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/docparser",
            json=payload
        )
        return self._validate_response(response, DocumentParserResponse)


    def document_thumbnail(self, urls: str) -> dict:
        """Generate document page thumbnail."""
        payload = DocumentThumbnailRequest(urls=urls).model_dump()
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/thumbnail",
            json=payload
        )
        return self._validate_response(response, DocumentThumbnailResponse)


    def json_schema_generator(self, content: str) -> dict:
        """Generate JSON schema from text description."""
        payload = JSONSchemaGeneratorRequest(content=content).model_dump()
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/schema_generator",
            json=payload
        )
        return response


    def json_schema_validator(self, schema: dict) -> Union[bool, dict]:
        """Check if given JSON schema is valid."""
        if not isinstance(schema, dict):
            raise TypeError("Input schema be a dict.")
        payload = schema
        response = self._http_client._request(
            "POST",
            f"{self._RESOURCE_PATH}/schema_validator",
            json=payload
        )
        return response