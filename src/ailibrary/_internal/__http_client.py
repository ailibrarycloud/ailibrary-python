import requests
import aiohttp
from typing import Dict, List, Tuple, Optional, Any, BinaryIO


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
    

    def _stringify(list_of_strings: str):
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
        """Make a synchronous HTTP request to the API."""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            data=data,
            json=json,
            files=files,
            stream=stream
        )
        # print(response.json())

        # if response_no_json:
        #     return response
        response.raise_for_status()
        return response.json()


    async def _async_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        stream: bool = False,
    ) -> Any:
        """Make an asynchronous HTTP request to the API."""
        url = f"{self.base_url}{endpoint}"
        
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                data=data,
                json=json
            ) as response:
                response.raise_for_status()
                
                if stream:
                    return response.content
                
                return await response.json()


    async def _async_stream(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
    ):
        """Make an asynchronous streaming HTTP request to the API."""
        response_content = await self._async_request(
            method=method,
            endpoint=endpoint,
            params=params,
            data=data,
            json=json,
            stream=True
        )
        
        async for chunk in response_content.iter_any():
            if chunk:
                yield chunk.decode('utf-8')
