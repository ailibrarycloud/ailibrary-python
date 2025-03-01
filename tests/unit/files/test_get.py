# file_id that exists
# file_id that doesnt exist
# string file_id
# negative file_id ??


import pytest
from ailibrary._internal._files import _Files
from ailibrary.types.files.responses import FileGetResponse

class TestFilesGet:
    @pytest.mark.parametrize("file_id", [1])
    def test_general(self, res_path, mock_http_client, file_id):
        """Test successful file retrieval"""
        files = _Files(mock_http_client)
        
        mock_response = {
            "url": "https://example.com/test.txt",
            "id": file_id,
            "bytes": 1024,
            "name": "test.txt",
            "created_timestamp": "2024-03-14T12:00:00Z"
        }
        mock_http_client._request.return_value = mock_response
        
        response = files.get(file_id)

        assert isinstance(response, dict)
        assert response["id"] == file_id
        
        for key in mock_response:
            assert key in response
            assert response[key] == mock_response[key]

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{file_id}"
        )
