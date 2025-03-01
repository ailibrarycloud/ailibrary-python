# general test
# table with 0 items
# table with exactly one item

import pytest
from ailibrary._internal._agent import _Agent
from ailibrary.types.agent.responses import AgentListResponse

class TestAgentList:
    def test_general(self, res_path, mock_http_client):
        """Test successful agent listing"""
        agent = _Agent(mock_http_client)
        
        # Set up mock response
        mock_response = {
            "agents": [
                {
                    "namespace": "test-agent-1",
                    "title": "Test Agent 1",
                    "description": "Test description 1"
                },
                {
                    "namespace": "test-agent-2",
                    "title": "Test Agent 2",
                    "description": "Test description 2"
                }
            ],
            "meta": {"page": 1}
        }
        mock_http_client._request.return_value = mock_response
        
        response = agent.list_agents()

        assert isinstance(response, dict)
        assert "agents" in response
        assert isinstance(response["agents"], list)
        assert "meta" in response
        
        # Verify each agent in the list has required fields
        for agent_data in response["agents"]:
            assert "namespace" in agent_data
            assert "title" in agent_data

        mock_http_client._request.assert_called_once_with(
            "GET",
            res_path
        )