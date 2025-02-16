from typing import Dict, List, Optional, Literal
from .__http_client import _HTTPClient
import json
import requests
from ..types.agent.requests import AgentCreateRequest, AgentUpdateRequest
from ..types.chat.requests import ChatRequest, Message


class _Agent:
    """Client for interacting with the AI Library Agent API."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def create(self, **kwargs) -> Dict:
        """Create a new agent with the specified parameters."""
        request = AgentCreateRequest(**kwargs)
        return self._http_client._request(
            "POST", 
            "/v1/agent/create", 
            json=request.model_dump(exclude_none=True)
        )


    def get(self, namespace: str) -> Dict:
        """Retrieve information about an agent."""
        return self._http_client._request("GET", f"/v1/agent/{namespace}")

    def list_agents(self) -> Dict:
        """List all agents."""
        return self._http_client._request("GET", "/v1/agent")

    def update(self, namespace: str, **kwargs) -> Dict:
        """Update an existing agent."""
        request = AgentUpdateRequest(namespace=namespace, **kwargs)
        return self._http_client._request(
            "PUT",
            f"/v1/agent/{namespace}",
            json=request.model_dump(exclude_none=True)
        )

    def delete(self, namespace: str) -> Dict:
        """Delete an agent."""
        return self._http_client._request("DELETE", f"/v1/agent/{namespace}")

    def chat(self, namespace: str, messages: List[Dict], session_id: Optional[str] = None) -> Generator[str, None, None]:
        """Chat with an agent."""
        request = ChatRequest(
            namespace=namespace,
            messages=[Message(**msg) for msg in messages],
            session_id=session_id
        )
        
        domain = self._http_client.base_url
        url = f"{domain}/v1/agent/{namespace}/chat"
        payload = request.model_dump_json()
        headers = {
            'Content-Type': 'application/json',
            'X-Library-Key': self._http_client.headers["X-Library-Key"]
        }

        with requests.request("POST", url, headers=headers, data=payload, stream=True) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    decoded_chunk = chunk.decode('utf-8')
                    yield decoded_chunk
        
