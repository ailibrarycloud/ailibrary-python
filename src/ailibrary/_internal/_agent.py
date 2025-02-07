from typing import Dict, List, Optional, Literal
from .__http_client import _HTTPClient
import json
import requests


class _Agent:
    """Client for interacting with the AI Library Agent API."""

    def __init__(self, http_client: _HTTPClient):
        self._http_client = http_client

    def create(
        self,
        title: str,
        instructions: Optional[str] = "You are a helpful assistant.",
        description: Optional[str] = None,
        coverimage: Optional[str] = None,
        intromessage: Optional[str] = None,
        knowledge_search: Optional[bool] = None,
        knowledge_id: Optional[str] = None
    ) -> Dict:
        """Create a new agent with the specified parameters."""

        if not title:
            raise ValueError("Title cannot be empty")
        payload = {"title": title}
        optional_params = {"instructions": instructions, "description": description,
                           "coverimage": coverimage, "intromessage": intromessage,
                           "knowledge_search": knowledge_search, "knowledge_id": knowledge_id}
        for param in optional_params:
            param_value = optional_params[param]
            if param_value is not None:
                payload[param] = param_value
        return self._http_client._request("POST", "/v1/agent/create", json=payload)

    def get(self, namespace: str) -> Dict:
        """Retrieve information about an agent."""
        return self._http_client._request("GET", f"/v1/agent/{namespace}")

    def list_agents(self) -> Dict:
        """List all agents."""
        return self._http_client._request("GET", "/v1/agent")

    def update(
        self,
        namespace: str,
        title: Optional[str] = None,
        type: Optional[Literal["notebook", "chat", "voice"]] = None,
        instructions: Optional[str] = "You are a helpful assistant.",
        description: Optional[str] = None,
        coverimage: Optional[str] = None,
        intromessage: Optional[str] = None,
        knowledge_search: Optional[bool] = None,
        knowledge_id: Optional[str] = None
    ) -> Dict:
        """Update an existing agent."""

        payload = {"namespace": namespace}
        valid_types = ["notebook", "chat", "voice"]

        optional_params = {"title": title, "type": type, "instructions": instructions,
                           "description": description, "coverimage": coverimage,
                           "intromessage": intromessage, "knowledge_search": knowledge_search,
                           "knowledge_id": knowledge_id}
        for param in optional_params:
            param_value = optional_params[param]
            if param == "type" and param_value and param_value not in valid_types:
                raise ValueError(f"Invalid agent type. If specified, must be one of: {
                                 self._http_client._stringify(valid_types)} .")
            elif param_value is not None:
                payload[param] = param_value
        return self._http_client._request("PUT", f"/v1/agent/{namespace}", json=payload)

    def delete(self, namespace: str) -> Dict:
        """Delete an agent."""
        return self._http_client._request("DELETE", f"/v1/agent/{namespace}")

    def chat(self, namespace: str, messages: List[Dict[str, str]], session_id: Optional[str] = None) -> Dict:
        """Chat with an agent.

        Args:
            namespace: The agent namespace
            messages: List of message dictionaries (at least one).
                Requirements:
                    - At least one message
                    - Required key: 'role' 
                        - Possible values: 'assistant', 'user', 'system'
                    - Required key: 'content'
                        - Possible values: any string
            session_id: Optional session identifier
        """
        if not namespace:
            raise ValueError("Namespace cannot be empty")
        if not messages:
            raise ValueError("Messages list cannot be empty")

        valid_roles = {"assistant", "user", "system"}
        for msg in messages:
            if not isinstance(msg, dict):
                raise ValueError("Each message must be a dictionary")
            if "role" not in msg or "content" not in msg:
                raise ValueError(
                    "Each message must contain 'role' and 'content' keys")
            if msg["role"] not in valid_roles:
                raise ValueError(f"Message role must be one of {valid_roles}")
            if not isinstance(msg["content"], str):
                raise ValueError("Message content must be a string")

        domain = self._http_client.base_url
        url = f"{domain}/v1/agent/{namespace}/chat"
        payload = json.dumps({
            "messages": messages,
            "session_id": session_id if session_id else "test-session",
        })
        headers = {
            'Content-Type': 'application/json',
            'X-Library-Key': self._http_client.headers["X-Library-Key"]
        }
        # response = requests.request("POST", url, headers=headers, data=payload)
        with requests.request("POST", url, headers=headers, data=payload, stream=True) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    decoded_chunk = chunk.decode('utf-8')
                    yield decoded_chunk
        
