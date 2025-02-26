# namespace that exists
# namespace that doesnt exist
# different kinds of characters in the query string for namespace that exists
# different kinds of characters in actual namespace

import pytest
from ailibrary._internal._agent import _Agent

class TestAgentGet:
    def test_get_agent_success(self, mock_http_client, agent_response_payload):
        """Test successful agent retrieval"""
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = agent_response_payload
        
        response = agent.get("test-agent")
        
        assert response["namespace"] == "test-agent"
        mock_http_client._request.assert_called_once_with(
            "GET",
            "/v1/agent/test-agent"
        )

    def test_get_agent_not_found(self, mock_http_client):
        """Test getting non-existent agent"""
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = {
            "status": "failure",
            "message": "Agent not found"
        }
        
        response = agent.get("non-existent")
        assert response["status"] == "failure"

    @pytest.mark.parametrize("namespace", [
        "test@agent",
        "test-agent_123",
        "特殊文字"
    ])
    def test_get_agent_special_chars(self, mock_http_client, namespace, agent_response_payload):
        """Test getting agent with special characters in namespace"""
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = {
            **agent_response_payload,
            "namespace": namespace
        }
        
        response = agent.get(namespace)
        assert response["namespace"] == namespace
