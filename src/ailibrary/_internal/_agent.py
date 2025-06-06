from typing import Optional, Generator
from .__http_client import _HTTPClient
from ..types.agent.requests import AgentCreateRequest, AgentUpdateRequest, AgentDeleteRequest, AgentChatRequest
from ..types.agent.responses import AgentCreateResponse, AgentGetResponse, AgentListResponse, AgentUpdateResponse, AgentDeleteResponse
from ..types.shared.enums import ResourcePath
from pydantic import ValidationError
import requests
import json

class _Agent:
    """Client for interacting with the AI Library Agent API."""

    _RESOURCE_PATH = ResourcePath.AGENT.value

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
        response = self._http_client._request("POST", f"{self._RESOURCE_PATH}/create", json=payload)
        return self._validate_response(response, AgentCreateResponse)


    def get(self, namespace: str) -> dict:
        """Retrieve information about an agent."""
        if not isinstance(namespace, str) or not namespace:
            raise ValueError("Namespace must be a non-empty string")
        response = self._http_client._request("GET", f"{self._RESOURCE_PATH}/{namespace}")
        if "status" in response and response["status"] == "failure":
            return response
        return self._validate_response(response, AgentGetResponse)


    def list_agents(self) -> dict:
        """List all agents."""
        response = self._http_client._request("GET", self._RESOURCE_PATH)
        return self._validate_response(response, AgentListResponse)


    def update(self, namespace: str, **kwargs) -> dict:
        """Update an existing agent."""
        payload = AgentUpdateRequest(namespace=namespace, **kwargs).model_dump()
        response = self._http_client._request("PUT", f"{self._RESOURCE_PATH}/{namespace}", json=payload)
        return self._validate_response(response, AgentUpdateResponse)


    def delete(self, namespace: str, delete_connected_resources: bool) -> dict:
        """Delete an agent."""
        payload = AgentDeleteRequest(namespace=namespace, 
                                     delete_connected_resources=delete_connected_resources).model_dump()
        response = self._http_client._request("DELETE", f"{self._RESOURCE_PATH}/{namespace}", json=payload)
        return self._validate_response(response, AgentDeleteResponse)



    def chat_stream(self, namespace: str, messages: list[dict], **kwargs):
        """ Stream a chat with an agent with text data"""
        payload = AgentChatRequest(namespace=namespace, messages=messages, **kwargs).model_dump()
        headers = {
            'Content-Type': 'application/json',
            'X-Library-Key': self._http_client.headers["X-Library-Key"]
        }
        url = f"{self._http_client.base_url}/{self._RESOURCE_PATH}/{namespace}/chat"
        try:
            with requests.request("POST", url, headers=headers, json=payload, stream=True) as response:
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=8192):
                    try:
                        if chunk:
                            json_strings = chunk.decode('utf-8')
                            json_objects = [json.loads(json_string) for json_string in json_strings.splitlines()]
                            for obj in json_objects:
                                yield obj
                    except Exception as e:
                        print(f"Error processing chunk: {str(e)}\nMoving on to next chunk...")
        except Exception as e:
            print(f"Chat error: {str(e)}")


    def chat(self, namespace: str, messages: list[dict], **kwargs):
        """Chat with an agent."""
        payload = AgentChatRequest(namespace=namespace, messages=messages, **kwargs).model_dump()
        url = f"{self._RESOURCE_PATH}/{namespace}/chat"
        if payload["response_format"] == "json":
            result = self._http_client._request("POST", url, json=payload)
        else:
            result = ""
            for json_object in self.chat_stream(namespace=namespace, messages=messages, **kwargs):
                if json_object["object"] == "chat.completion.chunk":
                    result += json_object["content"]
        return result
