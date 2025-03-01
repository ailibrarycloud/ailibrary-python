import requests
from typing import Tuple, Optional, Any, BinaryIO
from ..types.http_client.http_request import HTTPRequest
from ..types.http_client.http_init import HTTPInit
from ..types.http_client.responses import HTTPResponse, ErrorResponse
from ..types.shared.enums import HTTPMethod


class _HTTPClient:
    """Handles HTTP requests to the AI Library API."""
    
    def __init__(self, api_key: str, base_url: str, version: str):
        init_params = HTTPInit(api_key=api_key, base_url=base_url, version=version)
        api_key, base_url, version = init_params.api_key, init_params.base_url, init_params.version
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        if version[-1] == "/":
            version = version[:-1]
            
        self.base_url = f"{base_url}/{version}"
        self.headers = {
            "X-Library-Key": api_key,
        }


    # @staticmethod
    # def _stringify(list_of_strings: list[str]) -> str:
    #     """ 
    #     input example: ["A", "list", "of", "words"]
    #     return value example: "'A', 'list', 'of', 'words'"
    #     """
    #     return "'" + "', '".join(list_of_strings) + "'"


    def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        files: Optional[list] = None,
        stream: bool = False,
        # response_no_json: bool = False
    ) -> Any:
        """Make an HTTP request to the API."""

        # verify the the fields are valid
        valid_params = HTTPRequest(
            method=method,
            endpoint=endpoint,
            params=params,
            data=data,
            json=json,
            files=files,
            stream=stream
        )
        url = f"{self.base_url}{valid_params.endpoint}"
        try:
            response = requests.request(
                method=valid_params.method,
                url=url,
                headers=self.headers,
                params=valid_params.params,
                data=valid_params.data,
                json=valid_params.json,
                files=valid_params.files,
                stream=valid_params.stream
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
