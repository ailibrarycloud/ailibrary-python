from typing import Dict, List, Optional
from ..utils.http_client import _HTTPClient


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
        payload = {
            "title": title,
            "instructions": instructions
        }
        if description:
            payload["description"] = description
        if coverimage:
            payload["coverimage"] = coverimage
        if intromessage:
            payload["intromessage"] = intromessage
        if knowledge_search is not None:
            payload["knowledge_search"] = knowledge_search
        if knowledge_id:
            payload["knowledge_id"] = knowledge_id

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
        agent_type: Optional[str] = None,
        instructions: Optional[str] = None,
        description: Optional[str] = None,
        coverimage: Optional[str] = None,
        intromessage: Optional[str] = None,
        knowledge_search: Optional[bool] = None,
        knowledge_id: Optional[str] = None
    ) -> Dict:
        """Update an existing agent."""
        payload = {}
        if title:
            payload["title"] = title
        if agent_type:
            payload["type"] = agent_type
        if instructions:
            payload["instructions"] = instructions
        if description:
            payload["description"] = description
        if coverimage:
            payload["coverimage"] = coverimage
        if intromessage:
            payload["intromessage"] = intromessage
        if knowledge_search is not None:
            payload["knowledge_search"] = knowledge_search
        if knowledge_id:
            payload["knowledge_id"] = knowledge_id

        return self._http_client._request("PUT", f"/agent/{namespace}", json=payload)

    def delete(self, namespace: str) -> Dict:
        """Delete an agent."""
        return self._http_client._request("DELETE", f"/agent/{namespace}")

    def chat(self, namespace: str, messages: List[Dict[str, str]], session_id: Optional[str] = None) -> Dict:
        """Chat with an agent."""
        payload = {"messages": messages}
        if session_id:
            payload["session_id"] = session_id

        return self._http_client._request("POST", f"/agent/{namespace}/chat", json=payload)
