import pytest
from ailibrary._internal._files import _Files
from ailibrary._internal._knowledge_base import _KnowledgeBase
from ailibrary._internal._agent import _Agent

class TestFilesKBIntegration:
    def test_files_with_kb_upload(self, mock_http_client, test_file_name, test_file_path):
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
        upload_response = [
            {
                "url": f"https://example.com/{test_file_name}",
                "id": 1,
                "bytes": 1024,
                "name": test_file_name,
                "meta": {"type": "text"}
            }
        ]
        mock_http_client._request.return_value = upload_response
        
        response = files.upload(
            files=[test_file_path],
            knowledgeId=kb_id
        )
        
        assert isinstance(response, list)
        # assert "files" in response
        assert len(response) == 1
        assert response[0]["id"] == 1
        assert response[0]["name"] == test_file_name
        
        # Verify the files are associated with the knowledge base
        kb_list_sources_response = [
            {
                "created_timestamp": "2025-05-23 00:33:28",
                "id": 4177,
                "knowledgeId": kb_id,
                "source": test_file_name,
                "source_type": "docs",
                "updated_timestamp": "2025-05-23 00:33:28",
                "url": f"https://base/corbett/user@ailibrary.ai/{test_file_name}",
                "userEmail": "user@ailibrary.ai",
                "userName": "user"
            }
        ]
        mock_http_client._request.return_value = kb_list_sources_response
        sources_info = kb.list_sources(kb_id)
        assert isinstance(sources_info, list)
        assert len(sources_info) == 1
        
        source_info = sources_info[0]
        assert "knowledgeId" in source_info and source_info["knowledgeId"] == kb_id
        assert "source" in source_info and source_info["source"] == test_file_name
        assert "url" in source_info and source_info["url"].split("/")[-1] == test_file_name
        assert "source_type" in source_info
