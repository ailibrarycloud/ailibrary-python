import requests
from typing import Dict, List, Tuple, Optional, Any, BinaryIO
from ..types.http_client.requests import HTTPRequest
from ..types.http_client.responses import HTTPResponse, ErrorResponse
from ..types.shared.enums import HTTPMethod


class _HTTPClient:
    """Handles HTTP requests to the AI Library API."""
    
    def __init__(self, api_key: str, base_url: str):
        if base_url[-1] == "/":
            self.base_url = base_url[:-1]
        else:
            self.base_url = base_url

        self.headers = {
            "X-Library-Key": api_key,
            # "Content-Type": "application/json"
        }
    

    @staticmethod
    def _stringify(list_of_strings: List[str]) -> str:
        """ 
        input example: ["A", "list", "of", "words"]
        return value example: "'A', 'list', 'of', 'words'"
        """
        return "'" + "', '".join(list_of_strings) + "'"


    def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        files: Optional[List[Tuple[str, Tuple[str, BinaryIO, str]]]] = None,
        stream: bool = False,
        # response_no_json: bool = False
    ) -> Any:
        """Make an HTTP request to the API."""
        if method not in HTTPMethod.__members__:
            raise ValueError(f"Invalid HTTP method: {method}. Must be one of: {[m.value for m in HTTPMethod]}")

        request = HTTPRequest(
            method=method,
            endpoint=endpoint,
            params=params,
            data=data,
            json=json,
            files=files,
            stream=stream
        )

        url = f"{self.base_url}{request.endpoint}"
        try:
            response = requests.request(
                method=request.method.value,
                url=url,
                headers=self.headers,
                params=request.params,
                data=request.data,
                json=request.json,
                files=request.files,
                stream=request.stream
            )
            # print(response.json())

            # if response_no_json:
            #     return response
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ErrorResponse(
                status_code=e.response.status_code if e.response else 500,
                message=str(e),
                error=e.response.json() if e.response else None
            )
