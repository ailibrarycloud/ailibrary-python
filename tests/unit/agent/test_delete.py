# general test for namespace that exists (delete_connected_resource not specified)
# delete_connected_resource=True
# delete_connected_resource=False
# namespace that doesnt exist
# different kinds of characters in the query string for namespace that exists
# different kinds of characters in actual namespace

import pytest
from ailibrary._internal._agent import _Agent

class TestAgentDelete:
    @pytest.mark.parametrize("delete_connected", [True, False, None])
    def test_delete_agent_success(self, mock_http_client, delete_connected):
        """Test successful agent deletion with different delete_connected_resources values"""
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = {
            "statusCode": 200,
            "message": "Agent deleted successfully"
        }
        
        kwargs = {}
        if delete_connected is not None:
            kwargs["delete_connected_resources"] = delete_connected
            
        response = agent.delete("test-agent", **kwargs)
        
        assert response["statusCode"] == 200
        mock_http_client._request.assert_called_once()

    def test_delete_nonexistent_agent(self, mock_http_client):
        """Test deleting non-existent agent"""
        agent = _Agent(mock_http_client)
        mock_http_client._request.return_value = {
            "statusCode": 404,
            "message": "Agent not found"
        }
        
        response = agent.delete("non-existent", delete_connected_resources=True)
        assert response["statusCode"] == 404
