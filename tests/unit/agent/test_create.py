# general valid params
# general invalid params
# empty title
# way too large title that wont fit in database
# different kinds of characters in the title
# different kinds of characters in the other string parameters
# each and every kind of parameter

import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.shared.enums import AgentType
from ailibrary.types.agent.responses import AgentCreateResponse


class TestAgentCreate:
    @pytest.mark.parametrize("create_payload",
        [{
            "title": "Test Agent",
            "instructions": "Test instructions",
            "description": "Test description"
        }]
    )
    def test_general(self, res_path, mock_http_client, create_payload, validated_agent_response):
        """Test successful agent creation with various valid payloads"""
        agent = _Agent(mock_http_client)
        
        # Use the fixture to create validated response
        response_data = validated_agent_response(create_payload)
        
        # Set the mock to return the validated data
        mock_http_client._request.return_value = response_data
        
        response = agent.create(**create_payload)

        assert isinstance(response, dict)
        assert isinstance(response["namespace"], str)

        # Verify response contains expected fields
        for key in create_payload:
            assert key in response
            assert response[key] == create_payload[key]

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/create",
            json=create_payload
        )



    # @pytest.mark.parametrize("invalid_payload", [
    #     {"title": ""},  # Empty title
    #     {"title": "x" * 256},  # Title too long
    #     {"title": "Test", "type": "invalid"},  # Invalid agent type
    #     {"title": "Test", "instructions": 123},  # Wrong type for instructions
    # ])
    # def test_create_agent_validation_error(self, mock_http_client, invalid_payload):
    #     """Test agent creation with invalid data"""
    #     agent = _Agent(mock_http_client)
    #     with pytest.raises(ValueError):
    #         agent.create(**invalid_payload)

    # def test_create_agent_special_chars(self, mock_http_client, agent_response_payload):
    #     """Test agent creation with special characters"""
    #     special_payload = {
    #         "title": "Test@#$%^&*()_+",
    #         "instructions": "Special chars: éèêë",
    #         "description": "More ßpecial chars"
    #     }
    #     agent = _Agent(mock_http_client)
    #     mock_http_client._request.return_value = {**agent_response_payload, **special_payload}
        
    #     response = agent.create(**special_payload)
    #     assert response["title"] == special_payload["title"]
