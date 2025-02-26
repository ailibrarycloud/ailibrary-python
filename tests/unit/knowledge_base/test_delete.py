import pytest
from ailibrary._internal._knowledge_base import _KnowledgeBase
from ailibrary.types.knowledge_base.responses import KnowledgeBaseDeleteResponse

class TestKnowledgeBaseDelete:
    @pytest.mark.parametrize("knowledge_id", ["kb_123"])
    def test_general(self, res_path, mock_http_client, knowledge_id):
        """Test successful knowledge base deletion"""
        kb = _KnowledgeBase(mock_http_client)
        
        mock_response = {
            "status": "success",
            "message": "Knowledge base deleted successfully"
        }
        mock_http_client._request.return_value = mock_response
        
        response = kb.delete(knowledge_id)

        assert isinstance(response, dict)
        assert response["status"] == "success"
        assert "message" in response

        mock_http_client._request.assert_called_once_with(
            "DELETE",
            f"{res_path}/{knowledge_id}"
        )
