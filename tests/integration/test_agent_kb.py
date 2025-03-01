import pytest
from ailibrary._internal._agent import _Agent
from ailibrary._internal._knowledge_base import _KnowledgeBase

class TestAgentKBIntegration:
    @pytest.mark.parametrize("knowledge_search", [None, False, True])
    def test_agent_with_kb_create(self, mock_http_client, knowledge_search):
        """Test that when creating an agent with a knowledge base, the knowledgeId is properly set"""
        # Create knowledge base first
        kb = _KnowledgeBase(mock_http_client)
        kb_response = {
            "knowledgeId": "kb_123",
            "status": "active",
            "title": "Test KB"
        }
        mock_http_client._request.return_value = kb_response
        
        kb_id = kb.create("Test KB")["knowledgeId"]
        
        # Now create agent with this knowledge base
        agent = _Agent(mock_http_client)
        create_payload = {
            "title": "Test Agent",
            "knowledgeId": kb_id
        }
        if knowledge_search is not None:
            create_payload["knowledge_search"] = knowledge_search
            
        agent_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "knowledgeId": kb_id,
            "knowledge_search": knowledge_search if knowledge_search is not None else False
        }
        mock_http_client._request.return_value = agent_response
        
        response = agent.create(**create_payload)
        
        assert isinstance(response, dict)
        assert response["knowledgeId"] == kb_id
        assert response["knowledge_search"] == (knowledge_search if knowledge_search is not None else False)
        
        # Verify agent.get() includes the knowledge base info
        get_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "knowledgeId": kb_id,
            "knowledge_search": knowledge_search if knowledge_search is not None else False
        }
        mock_http_client._request.return_value = get_response
        
        agent_info = agent.get("test-agent")
        assert agent_info["knowledgeId"] == kb_id
        assert agent_info["knowledge_search"] == (knowledge_search if knowledge_search is not None else False)

    @pytest.mark.parametrize("knowledge_search", [None, False, True])
    def test_agent_with_kb_update(self, mock_http_client, knowledge_search):
        """Test that when updating an agent with a knowledge base, the knowledgeId is properly set"""
        # Create knowledge base first
        kb = _KnowledgeBase(mock_http_client)
        kb_response = {
            "knowledgeId": "kb_123",
            "status": "active",
            "title": "Test KB"
        }
        mock_http_client._request.return_value = kb_response
        
        kb_id = kb.create("Test KB")["knowledgeId"]
        
        # Create agent without knowledge base
        agent = _Agent(mock_http_client)
        create_response = {
            "namespace": "test-agent",
            "title": "Test Agent"
        }
        mock_http_client._request.return_value = create_response
        
        agent.create(title="Test Agent")
        
        # Update agent with knowledge base
        update_payload = {
            "namespace": "test-agent",
            "knowledgeId": kb_id
        }
        if knowledge_search is not None:
            update_payload["knowledge_search"] = knowledge_search
            
        update_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "knowledgeId": kb_id,
            "knowledge_search": knowledge_search if knowledge_search is not None else False
        }
        mock_http_client._request.return_value = update_response
        
        response = agent.update(**update_payload)
        
        assert isinstance(response, dict)
        assert response["knowledgeId"] == kb_id
        assert response["knowledge_search"] == (knowledge_search if knowledge_search is not None else False)
        
        # Verify agent.get() includes the knowledge base info
        get_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "knowledgeId": kb_id,
            "knowledge_search": knowledge_search if knowledge_search is not None else False
        }
        mock_http_client._request.return_value = get_response
        
        agent_info = agent.get("test-agent")
        assert agent_info["knowledgeId"] == kb_id
        assert agent_info["knowledge_search"] == (knowledge_search if knowledge_search is not None else False) 