import pytest
from ailibrary._internal._knowledge_base import _KnowledgeBase
from ailibrary.types.knowledge_base.responses import KnowledgeBaseCreateResponse

class TestKnowledgeBaseCreate:
    @pytest.mark.parametrize("create_payload", [
        {
            "name": "Test Knowledge Base",
            "meta": {"category": "test"}
        }
    ])
    def test_general(self, res_path, mock_http_client, create_payload):
        """Test successful knowledge base creation with valid payload"""
        kb = _KnowledgeBase(mock_http_client)
        
        mock_response = {
            "knowledgeId": "kb_123",
            "status": "active",
            "meta": create_payload["meta"]
        }
        mock_http_client._request.return_value = mock_response
        
        response = kb.create(**create_payload)

        assert isinstance(response, dict)
        assert "knowledgeId" in response
        assert "status" in response
        assert response["meta"] == create_payload["meta"]

        mock_http_client._request.assert_called_once_with(
            "POST",
            res_path,
            json=create_payload
        )
