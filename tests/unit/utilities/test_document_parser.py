import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import DocumentParserResponse

class TestUtilitiesDocumentParser:
    @pytest.mark.parametrize("parser_payload", [
        {
            "urls": ["https://example.com/document.pdf"]
        }
    ])
    def test_general(self, res_path, mock_http_client, parser_payload):
        """Test successful document parsing"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = {
            "url": "https://example.com/document.pdf",
            "title": "Test Document",
            "body": "Document content..."
        }
        mock_http_client._request.return_value = mock_response
        
        response = utilities.document_parser(**parser_payload)

        assert isinstance(response, dict)
        assert "url" in response
        assert "title" in response
        assert "body" in response

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/docparser",
            json=parser_payload
        )
