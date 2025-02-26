# general valid params
# general invalid params
# way too large title that wont fit in database
# different kinds of characters in the title
# different kinds of characters in the other string parameters
# each and every kind of parameter

import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.shared.enums import AgentType


class TestAgentCreate:
    
    def test_create_agent_success(self, mock_http_client, agent_create_payload, agent_response_payload):
        """Test successful agent creation with valid data"""
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = agent_response_payload
        
        response = agent.create(**agent_create_payload)
        
        assert response["namespace"] == "test-agent"
        assert response["title"] == agent_create_payload["title"]
        mock_http_client._request.assert_called_once_with(
            "POST",
            "/v1/agent/create",
            json=agent_create_payload
        )

    @pytest.mark.parametrize("invalid_payload", [
        {"title": ""},  # Empty title
        {"title": "x" * 256},  # Title too long
        {"title": "Test", "type": "invalid"},  # Invalid agent type
        {"title": "Test", "instructions": 123},  # Wrong type for instructions
    ])
    def test_create_agent_validation_error(self, mock_http_client, invalid_payload):
        """Test agent creation with invalid data"""
        agent = _Agent(mock_http_client)
        with pytest.raises(ValueError):
            agent.create(**invalid_payload)

    def test_create_agent_special_chars(self, mock_http_client, agent_response_payload):
        """Test agent creation with special characters"""
        special_payload = {
            "title": "Test@#$%^&*()_+",
            "instructions": "Special chars: éèêë",
            "description": "More ßpecial chars"
        }
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = {**agent_response_payload, **special_payload}
        
        response = agent.create(**special_payload)
        assert response["title"] == special_payload["title"]
