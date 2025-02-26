import pytest
from ailibrary._internal._knowledge_base import _KnowledgeBase
from ailibrary.types.knowledge_base.responses import KnowledgeBaseGetResponse

class TestKnowledgeBaseGet:
    @pytest.mark.parametrize("knowledge_id", ["kb_123"])
    def test_general(self, res_path, mock_http_client, knowledge_id):
        """Test successful knowledge base retrieval"""
        kb = _KnowledgeBase(mock_http_client)
        
        mock_response = {
            "knowledgeId": knowledge_id,
            "status": "active",
            "title": "Test KB",
            "sources": 5,
            "generations": 10,
            "addhistory": 2,
            "visibility": "private",
            "userName": "testuser",
            "userEmail": "test@example.com"
        }
        mock_http_client._request.return_value = mock_response
        
        response = kb.get(knowledge_id)

        assert isinstance(response, dict)
        assert response["knowledgeId"] == knowledge_id
        
        for key in mock_response:
            assert key in response
            assert response[key] == mock_response[key]

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{knowledge_id}"
        )
