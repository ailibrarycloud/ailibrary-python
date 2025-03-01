# general test for namespace that exists (delete_connected_resource not specified)
# delete_connected_resource=True
# delete_connected_resource=False
# namespace that doesnt exist
# different kinds of characters in the query string for namespace that exists
# different kinds of characters in actual namespace

import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.agent.responses import AgentDeleteResponse

class TestAgentDelete:
    @pytest.mark.parametrize("delete_params", [
        {
            "namespace": "test-agent",
            "delete_connected_resources": True
        },
        {
            "namespace": "test-agent",
            "delete_connected_resources": False
        }
    ])
    def test_general(self, res_path, mock_http_client, delete_params):
        """Test successful agent deletion with various valid payloads"""
        agent = _Agent(mock_http_client)
        
        # Set up mock response
        mock_response = {
            "statusCode": 200,
            "message": "Agent deleted successfully"
        }
        mock_http_client._request.return_value = mock_response
        
        response = agent.delete(**delete_params)

        assert isinstance(response, dict)
        assert response["statusCode"] == 200
        assert "message" in response

        delete_payload = delete_params.copy()
        delete_payload.pop("namespace")
        mock_http_client._request.assert_called_once_with(
            "DELETE",
            f"{res_path}/{delete_params['namespace']}",
            json=delete_payload
        )