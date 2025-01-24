import requests
from typing import Dict, Optional, Any, BinaryIO

class HTTPClient:
    """Handles HTTP requests to the AI Library API."""
    
    def __init__(self, api_key: str, base_url: str):
        self.base_url = base_url
        self.headers = {
            "X-Library-Key": api_key,
            "Content-Type": "application/json"
        }
    
    def request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict] = None,
        json: Optional[Dict] = None,
        files: Optional[Dict[str, BinaryIO]] = None,
        stream: bool = False
    ) -> Any:
        """Make an HTTP request to the API."""
        url = f"{self.base_url}{endpoint}"
        
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            json=json,
            files=files,
            stream=stream
        )
        
        response.raise_for_status()
        return response.json()
