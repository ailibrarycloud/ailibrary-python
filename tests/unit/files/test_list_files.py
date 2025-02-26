import pytest
from ailibrary._internal._files import _Files
from ailibrary.types.files.responses import FileListResponse

class TestFilesList:
    def test_general(self, res_path, mock_http_client):
        """Test successful file listing"""
        files = _Files(mock_http_client)
        
        mock_response = {
            "files": [
                {
                    "url": "https://example.com/test1.txt",
                    "id": 1,
                    "bytes": 1024,
                    "name": "test1.txt"
                },
                {
                    "url": "https://example.com/test2.txt",
                    "id": 2,
                    "bytes": 2048,
                    "name": "test2.txt"
                }
            ],
            "meta": {"page": 1}
        }
        mock_http_client._request.return_value = mock_response
        
        response = files.list_files()

        assert isinstance(response, dict)
        assert "files" in response
        assert isinstance(response["files"], list)
        assert "meta" in response
        
        for file_data in response["files"]:
            assert "url" in file_data
            assert "id" in file_data
            assert "bytes" in file_data
            assert "name" in file_data

        mock_http_client._request.assert_called_once_with(
            "GET",
            res_path,
            params={"page": None, "limit": None}
        )
