# file_id that exists
# file_id that doesnt exist
# string file_id
# negative file_id ??

import pytest
from ailibrary._internal._files import _Files
from ailibrary.types.files.responses import FileDeleteResponse

class TestFilesDelete:
    @pytest.mark.parametrize("file_id", [1])
    def test_general(self, res_path, mock_http_client, file_id):
        """Test successful file deletion"""
        files = _Files(mock_http_client)
        
        mock_response = {
            "response": "success"
        }
        mock_http_client._request.return_value = mock_response
        
        response = files.delete(file_id)

        assert isinstance(response, dict)
        assert response["response"] == "success"

        mock_http_client._request.assert_called_once_with(
            "DELETE",
            f"{res_path}/{file_id}"
        )
