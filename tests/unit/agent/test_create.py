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
from pydantic import ValidationError


class TestAgentCreate:

    # =================== HELPERS ============================================================================
    def _run_create_test(self, res_path, mock_http_client, create_payload, validated_agent_response):
        agent = _Agent(mock_http_client)
        response_data = validated_agent_response(create_payload) # Use the fixture to create validated response
        mock_http_client._request.return_value = response_data # Set the mock to return the validated data

        response = agent.create(**create_payload)
        assert isinstance(response, dict)
        assert isinstance(response["namespace"], str)
        
        for key in create_payload: # Verify response contains expected fields
            assert key in response
            assert response[key] == create_payload[key]
        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/create",
            json=create_payload
        )
    
    def _run_invalid_payload_test(self, mock_http_client, invalid_payload, validated_agent_response):
        agent = _Agent(mock_http_client)
        with pytest.raises(ValidationError) as excinfo:
            response_data = validated_agent_response(invalid_payload)


    # =================== TEST CASES ============================================================================
    @pytest.mark.parametrize("create_payload",
        [{
            "title": "Test Agent",
            "instructions": "Test instructions",
            "description": "Test description"
        }]
    )
    def test_general(self, res_path, mock_http_client, create_payload, validated_agent_response):
        """Test successful agent creation with various valid payloads"""
        self._run_create_test(res_path, mock_http_client, create_payload, validated_agent_response)


    # Empty title test
    @pytest.mark.parametrize("invalid_payload", [{"title": ""}])
    def test_empty_title(self, mock_http_client, invalid_payload, validated_agent_response):
        """Test agent creation with invalid data"""
        self._run_invalid_payload_test(mock_http_client, invalid_payload, validated_agent_response)



# [
#         
#         {"title": "Test", "type": "invalid"},  # Invalid agent type
#         {"title": "Test", "instructions": 123},  # Wrong type for instructions
#     ]

    # # Title too long test
    # @pytest.mark.parametrize("invalid_payload", [{"title": "x" * 256}])
    # def test_title_too_long(self, mock_http_client, invalid_payload, validated_agent_response):
    #     """Test agent creation with invalid data"""
    #     response_data = validated_agent_response(invalid_payload)
    #     # self._run_invalid_payload_test(mock_http_client, invalid_payload, validated_agent_response)


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
