from typing import Dict, List, Optional, Generator
from .__http_client import _HTTPClient
import requests
from ..types.agent.requests import AgentCreateRequest, AgentUpdateRequest
# from ..types.agent.requests import ChatRequest
from ..types.agent.responses import AgentCreateResponse, AgentGetResponse, AgentListResponse, AgentUpdateResponse, AgentDeleteResponse
# from ..types.chat.responses import ChatResponse
from pydantic import ValidationError


class _Agent:
    """Client for interacting with the AI Library Agent API."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client


    def _validate_response(self, response: dict, validation_class) -> dict:
        try:
            validation_class(**response)
            return response
        except ValidationError as e:
            raise e


    def create(self, title: str, **kwargs) -> dict:
        """Create a new agent with the specified parameters."""
        payload = AgentCreateRequest(title=title, **kwargs).model_dump()
        response = self._http_client._request("POST", "/v1/agent/create", json=payload)
        return self._validate_response(response, AgentCreateResponse)


    def get(self, namespace: str) -> dict:
        """Retrieve information about an agent."""
        response = self._http_client._request("GET", f"/v1/agent/{namespace}")
        return self._validate_response(response, AgentGetResponse)


    def list_agents(self) -> dict:
        """List all agents."""
        response = self._http_client._request("GET", "/v1/agent")
        # agent_obj = response["agents"][0]
        # for item in agent_obj:
        #     print(f"{item}\n")
        #     print(f"{response[item]}\n")
        # return response
        return self._validate_response(response, AgentListResponse)


    def update(self, namespace: str, **kwargs) -> dict:
        """Update an existing agent."""
        payload = AgentUpdateRequest(namespace=namespace, **kwargs).model_dump()
        response = self._http_client._request("PUT", f"/v1/agent/{namespace}", json=payload)
        print(response)
        print(type(response))
        return self._validate_response(response, AgentUpdateResponse)


    def delete(self, namespace: str) -> dict:
        """Delete an agent."""
        response = self._http_client._request("DELETE", f"/v1/agent/{namespace}")
        print(response)
        print(type(response))
        return self._validate_response(response, AgentDeleteResponse)

    # ### WORK IN PROGRESS ###
    # def chat(self, namespace: str, messages: List[Dict], stream: bool = False) -> Generator[str, None, None]:
    #     """Chat with an agent."""
    #     request = ChatRequest(messages=messages)
    #     url = f"{self._http_client.base_url}/v1/agent/{namespace}/chat"
    #     payload = request.model_dump_json()
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'X-Library-Key': self._http_client.headers["X-Library-Key"]
    #     }

    #     with requests.request("POST", url, headers=headers, data=payload, stream=True) as response:
    #         response.raise_for_status()
    #         for chunk in response.iter_content(chunk_size=8192):
    #             if chunk:
    #                 yield chunk.decode('utf-8')
        
