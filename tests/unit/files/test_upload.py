import pytest
from ailibrary._internal._files import _Files
from ailibrary.types.files.responses import FileUploadResponse


class TestFilesUpload:
    @pytest.mark.parametrize("upload_payload", [
        {
            "files": ["test.txt"],
            "knowledgeId": "test-knowledge"
        }
    ])
    def test_general(self, res_path, mock_http_client, upload_payload):
        """Test successful file upload with various valid payloads"""
        files = _Files(mock_http_client)
        
        mock_response = {
            "url": "https://example.com/test.txt",
            "id": 1,
            "bytes": 1024,
            "name": "test.txt",
            "meta": {"type": "text"}
        }
        mock_http_client._request.return_value = mock_response
        
        response = files.upload(**upload_payload)

        assert isinstance(response, dict)
        assert "url" in response
        assert "id" in response
        assert "bytes" in response
        assert "name" in response

        mock_http_client._request.assert_called_once_with(
            "POST",
            res_path,
            data={"knowledgeId": upload_payload["knowledgeId"]},
            files=[('files', ('test.txt', mock.ANY, mock.ANY))]
        )
