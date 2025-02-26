import pytest
from ailibrary._internal._knowledge_base import _KnowledgeBase

class TestKnowledgeBaseGetStatus:
    @pytest.mark.parametrize("knowledge_id", ["kb_123"])
    def test_general(self, res_path, mock_http_client, knowledge_id):
        """Test successful knowledge base status retrieval"""
        kb = _KnowledgeBase(mock_http_client)
        
        mock_response = "processing"
        mock_http_client._request.return_value = mock_response
        
        response = kb.get_status(knowledge_id)

        assert isinstance(response, str)
        assert response == mock_response

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{knowledge_id}/status"
        )
