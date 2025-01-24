import requests
from typing import Dict, List, Optional, Union

class AILibraryAgent:
    """Client for interacting with the AI Library Agent API."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.ailibrary.ai/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_agent(
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
        endpoint = f"{self.base_url}/agent/create"
        
        payload = {
            "title": title,
            "instructions": instructions
        }
        
        # Add optional parameters if provided
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

        response = requests.post(endpoint, headers=self.headers, json=payload)
        return response.json()

    def get_agent(self, namespace: str) -> Dict:
        """Retrieve information about an agent."""
        endpoint = f"{self.base_url}/agent/{namespace}"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def list_agents(self) -> Dict:
        """List all agents."""
        endpoint = f"{self.base_url}/agent"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def update_agent(
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
        endpoint = f"{self.base_url}/agent/{namespace}"
        
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

        response = requests.put(endpoint, headers=self.headers, json=payload)
        return response.json()

    def delete_agent(self, namespace: str) -> Dict:
        """Delete an agent."""
        endpoint = f"{self.base_url}/agent/{namespace}"
        response = requests.delete(endpoint, headers=self.headers)
        return response.json()

    def chat(self, namespace: str, messages: List[Dict[str, str]], session_id: Optional[str] = None) -> Dict:
        """Chat with an agent."""
        endpoint = f"{self.base_url}/agent/{namespace}/chat"
        
        payload = {
            "messages": messages
        }
        if session_id:
            payload["session_id"] = session_id

        response = requests.post(endpoint, headers=self.headers, json=payload, stream=True)
        return response.json()