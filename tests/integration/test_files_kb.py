import pytest
from ailibrary._internal._files import _Files
from ailibrary._internal._knowledge_base import _KnowledgeBase
from ailibrary._internal._agent import _Agent

class TestFilesKBIntegration:
    def test_files_with_kb_upload(self, mock_http_client, test_file_path):
        """Test that when uploading files to a knowledge base, they are properly associated"""
        # Create knowledge base first
        kb = _KnowledgeBase(mock_http_client)
        kb_response = {
            "knowledgeId": "kb_123",
            "status": "active",
            "title": "Test KB"
        }
        mock_http_client._request.return_value = kb_response
        
        kb_id = kb.create("Test KB")["knowledgeId"]
        
        # Create agent with this knowledge base
        agent = _Agent(mock_http_client)
        agent_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "knowledgeId": kb_id,
            "knowledge_search": True
        }
        mock_http_client._request.return_value = agent_response
        
        agent.create(title="Test Agent", knowledgeId=kb_id, knowledge_search=True)
        
        # Upload files to the knowledge base
        files = _Files(mock_http_client)
        upload_response = {
            "files": [
                {
                    "url": "https://example.com/test.txt",
                    "id": 1,
                    "bytes": 1024,
                    "name": "test.txt",
                    "meta": {"type": "text"}
                }
            ]
        }
        mock_http_client._request.return_value = upload_response
        
        response = files.upload(
            files=[test_file_path],
            knowledgeId=kb_id
        )
        
        assert isinstance(response, dict)
        assert "files" in response
        assert isinstance(response["files"], list)
        assert len(response["files"]) == 1
        assert response["files"][0]["id"] == 1
        assert response["files"][0]["name"] == "test.txt"
        
        # Verify the files are associated with the knowledge base
        kb_get_response = {
            "knowledgeId": kb_id,
            "status": "active",
            "title": "Test KB",
            "files": [
                {
                    "url": "https://example.com/test.txt",
                    "id": 1,
                    "bytes": 1024,
                    "name": "test.txt",
                    "meta": {"type": "text"}
                }
            ]
        }
        mock_http_client._request.return_value = kb_get_response
        
        kb_info = kb.get(kb_id)
        assert "files" in kb_info
        assert isinstance(kb_info["files"], list)
        assert len(kb_info["files"]) == 1
        assert kb_info["files"][0]["id"] == 1
        assert kb_info["files"][0]["name"] == "test.txt" 