import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.agent.requests import AgentCreateRequest
from ailibrary.types.agent.responses import AgentCreateResponse
from ..test_config import TestConstants, TestData

class TestAgentUnit:
    def test_create_agent_validation(self, mock_http_client):
        """Test agent creation with valid data"""
        agent = _Agent(mock_http_client)
        
        # Mock the HTTP response
        mock_http_client._request.return_value = {
            "namespace": "test-agent",
            **TestData.AGENT_CREATE_PAYLOAD
        }
        
        # Test the create method
        response = agent.create(**TestData.AGENT_CREATE_PAYLOAD)
        
        # Verify the response
        assert isinstance(response, dict)
        assert response["namespace"] == "test-agent"
        assert response["title"] == TestData.AGENT_CREATE_PAYLOAD["title"]
        
        # Verify the HTTP request was made correctly
        mock_http_client._request.assert_called_once_with(
            "POST",
            "/v1/agent/create",
            json=TestData.AGENT_CREATE_PAYLOAD
        )

    def test_create_agent_invalid_data(self, mock_http_client):
        """Test agent creation with invalid data"""
        agent = _Agent(mock_http_client)
        
        with pytest.raises(ValueError):
            agent.create(title="")  # Empty title should raise error

    @pytest.mark.parametrize("method,endpoint,params", [
        ("get", "test-agent", {}),
        ("delete", "test-agent", {"delete_connected_resources": True}),
        ("update", "test-agent", {"title": "Updated Title"})
    ])
    def test_agent_operations(self, mock_http_client, method, endpoint, params):
        """Test various agent operations"""
        agent = _Agent(mock_http_client)
        operation = getattr(agent, method)
        operation(endpoint, **params)
