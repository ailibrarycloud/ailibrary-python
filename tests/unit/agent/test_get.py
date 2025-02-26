# namespace that exists
# namespace that doesnt exist
# different kinds of characters in the query string for namespace that exists
# different kinds of characters in actual namespace
import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.agent.responses import AgentGetResponse


class TestAgentGet:
    @pytest.mark.parametrize("namespace", ["test-agent"])
    def test_general(self, res_path, mock_http_client, namespace, validated_agent_response):
        """Test successful agent retrieval with various valid namespaces"""
        agent = _Agent(mock_http_client)
        
        # Create base response data
        base_response = {
            "title": "Test Agent",
            "instructions": "Test instructions",
            "description": "Test description",
            "namespace": namespace,
            "created_timestamp": "2024-03-14T12:00:00Z",
            "status": "active"
        }
        
        # Set the mock to return the response
        mock_http_client._request.return_value = base_response
        
        response = agent.get(namespace)

        assert isinstance(response, dict)
        assert response["namespace"] == namespace
        
        # Verify all expected fields are present
        for key in base_response:
            assert key in response
            assert response[key] == base_response[key]

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{namespace}"
        )