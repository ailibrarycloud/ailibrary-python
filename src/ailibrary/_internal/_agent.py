from typing import Dict, List, Optional, Generator
from .__http_client import _HTTPClient
import requests
from ..types.agent.requests import AgentCreateRequest, AgentUpdateRequest, ChatRequest
from ..types.agent.responses import AgentResponse, AgentListResponse, AgentData
from ..types.chat.responses import ChatResponse
# from ..types.shared.enums import HTTPMethod


class _Agent:
    """Client for interacting with the AI Library Agent API."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def create(self, **kwargs) -> AgentResponse:
        """Create a new agent with the specified parameters."""
        payload = AgentCreateRequest(**kwargs).model_dump()
        response = self._http_client._request("POST", "/v1/agent/create", json=payload)
        return AgentResponse(**response)


    def get(self, namespace: str) -> AgentResponse:
        """Retrieve information about an agent."""
        response = self._http_client._request("GET", f"/v1/agent/{namespace}")
        return AgentResponse(**response)


    def list_agents(self) -> AgentListResponse:
        """List all agents."""
        response = self._http_client._request("GET", "/v1/agent")
        return AgentListResponse(**response)


    def update(self, namespace: str, **kwargs) -> AgentResponse:
        """Update an existing agent."""
        payload = AgentUpdateRequest(namespace=namespace, **kwargs).model_dump()
        response = self._http_client._request("PUT", f"/v1/agent/{namespace}", json=payload)
        return AgentResponse(**response)


    def delete(self, namespace: str) -> AgentResponse:
        """Delete an agent."""
        response = self._http_client._request("DELETE", f"/v1/agent/{namespace}")
        return AgentResponse(**response)


    ### WORK IN PROGRESS ###
    def chat(self, namespace: str, messages: List[Dict], stream: bool = False) -> Generator[str, None, None]:
        """Chat with an agent."""
        request = ChatRequest(messages=messages)
        url = f"{self._http_client.base_url}/v1/agent/{namespace}/chat"
        payload = request.model_dump_json()
        headers = {
            'Content-Type': 'application/json',
            'X-Library-Key': self._http_client.headers["X-Library-Key"]
        }

        with requests.request("POST", url, headers=headers, data=payload, stream=True) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk.decode('utf-8')
        
