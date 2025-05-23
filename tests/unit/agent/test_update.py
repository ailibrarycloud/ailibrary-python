# general test for namespace that exists
# namespace that doesnt exist
# different kinds of characters in the query string for namespace that exists
# different kinds of characters in actual namespace
# every other test as create()

# update with non-empty title when original title is empty
# update with empty title when original title is non-empty
# update with different non-empty title when original title is non-empty
# update with exactly same title as original title

# repeat w other parameters


import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.agent.responses import AgentUpdateResponse

class TestAgentUpdate:
    @pytest.mark.parametrize("update_payload", [
        {
            "namespace": "test-agent",
            "title": "Updated Test Agent",
            "instructions": "Updated test instructions",
            "description": "Updated test description"
        }
    ])


    def test_general(self, res_path, mock_http_client, update_payload):
        """Test successful agent update with various valid payloads"""
        agent = _Agent(mock_http_client)
        
        # Set up mock response
        mock_response = {
            "response": "success"
        }
        mock_http_client._request.return_value = mock_response
        
        namespace = update_payload.pop("namespace")
        response = agent.update(namespace, **update_payload)

        assert isinstance(response, dict)
        assert response["response"] == "success"

        mock_http_client._request.assert_called_once_with(
            "PUT",
            f"{res_path}/{namespace}",
            json=update_payload
        )