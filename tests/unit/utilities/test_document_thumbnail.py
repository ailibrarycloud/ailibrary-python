import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import DocumentThumbnailResponse

class TestUtilitiesDocumentThumbnail:
    @pytest.mark.parametrize("thumbnail_payload", [
        {
            "urls": ["https://example.com/document.pdf"]
        }
    ])
    def test_general(self, res_path, mock_http_client, thumbnail_payload):
        """Test successful thumbnail generation"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = {
            "url": "https://example.com/document.pdf",
            "thumbnail": "base64_encoded_image_data"
        }
        mock_http_client._request.return_value = mock_response
        
        response = utilities.document_thumbnail(**thumbnail_payload)

        assert isinstance(response, dict)
        assert "url" in response
        assert "thumbnail" in response

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/thumbnail",
            json=thumbnail_payload
        )
