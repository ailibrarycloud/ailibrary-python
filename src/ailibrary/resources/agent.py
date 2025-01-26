from typing import Dict, List, Optional, Literal
from ..utils.http_client import _HTTPClient

###### WHAT IF USER PROVIDES THE WRONG TYPES OF VARIABLES? eg user passes a list instead of a string?
###### rather than use a million if statements in each function, how can we validate the data?

class Agent:
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

        ### What if title is None or an empty string?
        payload = {"title": title}
        optional_params = [instructions, description, coverimage, intromessage, knowledge_search, knowledge_id]
        for param in optional_params:
            if param:
                payload[param] = param
        return self._http_client._request("POST", "/agent/create", json=payload)


    def get(self, namespace: str) -> Dict:
        """Retrieve information about an agent."""
        return self._http_client._request("GET", f"/agent/{namespace}")


    def list_agents(self) -> Dict:
        """List all agents."""
        return self._http_client._request("GET", "/agent")


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
        acceptable_types = ["notebook", "chat", "voice"]
        optional_params = [title, type, instructions, description, coverimage, intromessage, knowledge_search, knowledge_id]
        for param in optional_params:
            ### What if title is specified but its an empty string? or the title is not found?
            if param == "type" and param and param not in acceptable_types:
                raise ValueError(f"Invalid agent type. If specified, must be one of: {self._http_client._stringify(acceptable_types)} .")
            elif param:   
                payload[param] = param
        return self._http_client._request("PUT", f"/agent/{namespace}", json=payload)


    def delete(self, namespace: str) -> Dict:
        """Delete an agent."""
        return self._http_client._request("DELETE", f"/agent/{namespace}")


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
            'session_id: Optional session identifier
        """
        if not messages:
            raise ValueError("Messages list cannot be empty")
        
        valid_roles = {"assistant", "user", "system"}
        for msg in messages:
            if not isinstance(msg, dict):
                raise ValueError("Each message must be a dictionary")
            if "role" not in msg or "content" not in msg:
                raise ValueError("Each message must contain 'role' and 'content' keys")
            if msg["role"] not in valid_roles:
                raise ValueError(f"Message role must be one of {valid_roles}")
            if not isinstance(msg["content"], str):
                raise ValueError("Message content must be a string")

        ### What if namespace is None or empty?
        payload = {
            "namespace": namespace,
            "messages": messages
        }
        if session_id:
            payload["session_id"] = session_id

        return self._http_client._request("POST", f"/agent/{namespace}/chat", json=payload)
