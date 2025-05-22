# general test, files list with one item (without knowledgeId)
# empty files list
# files list with multiple items
# none of the file paths can be opened
# only some of the file paths can be opened
# invalid file path formats altogether
# file paths that don't exist
# file paths to hidden files / files with restricted permissions
# file paths to weird niche file types (which file types are allowed anyway?)
# file paths where the path is too long for the database
# file paths with special characters
# file paths on windows vs unix-like systems?
# file sizes / paths to files that are just too big


# knowledgeId that exists
# knowledgeId that doesnt exist
# query knowledgeId thats too big for table?
# different kinds of characters in the query string for knowledgeId that exists
# different kinds of characters in actual knowledgeId


import pytest
import mimetypes
import os
from ailibrary._internal._files import _Files
from unittest.mock import ANY


class TestFilesUpload:
    
    @pytest.mark.parametrize("upload_payload", [
        {
            "files": ["tests/_sample_files/test.txt"],
            "knowledgeId": "test-knowledge"
        }
    ])
    def test_general(self, res_path, mock_http_client, upload_payload):
        """Test successful file upload with various valid payloads"""

        file_path = upload_payload["files"][0]
        file_name = os.path.basename(file_path)
        mime_type = mimetypes.guess_type(file_path)[0]

        files = _Files(mock_http_client)

        mock_response = {
            "url": "https://example.com/test.txt",
            "id": 1,
            "bytes": 1024,
            "name": file_name,
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
            files=[('files', (file_name, ANY, mime_type))]
        )
