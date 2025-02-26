import pytest
from ailibrary._internal._knowledge_base import _KnowledgeBase
from ailibrary.types.knowledge_base.responses import KnowledgeBaseListResponse

class TestKnowledgeBaseList:
    def test_general(self, res_path, mock_http_client):
        """Test successful knowledge base listing"""
        kb = _KnowledgeBase(mock_http_client)
        
        mock_response = {
            "knowledgebases": [
                {
                    "knowledgeId": "kb_123",
                    "status": "active",
                    "title": "Test KB 1",
                    "userName": "testuser",
                    "created_timestamp": "2024-03-14T12:00:00Z",
                    "updated_timestamp": "2024-03-14T12:00:00Z"
                },
                {
                    "knowledgeId": "kb_456",
                    "status": "active",
                    "title": "Test KB 2",
                    "userName": "testuser",
                    "created_timestamp": "2024-03-14T12:00:00Z",
                    "updated_timestamp": "2024-03-14T12:00:00Z"
                }
            ],
            "meta": {"page": 1}
        }
        mock_http_client._request.return_value = mock_response
        
        response = kb.list_knowledge_bases()

        assert isinstance(response, dict)
        assert "knowledgebases" in response
        assert isinstance(response["knowledgebases"], list)
        assert "meta" in response
        
        for kb_data in response["knowledgebases"]:
            assert "knowledgeId" in kb_data
            assert "title" in kb_data
            assert "status" in kb_data

        mock_http_client._request.assert_called_once_with(
            "GET",
            res_path
        )
