# general test, urls list with one item
# empty urls list
# urls list with multiple items
# none of the urls can be opened
# only some of the urls can be opened
# invalid url formats altogether
# urls that don't exist
# restricted urls hidden behind a paywall?
# restricted urls hidden behind a login site?
# some urls with http, some with https, some with just the domain
# file links from anywhere in the world?
# what if some urls are not files but actually webpages 
# urls that are too long for the database
# urls with special characters
# localhost:3000/ when im hosting something on localhost
# url to a local file on computer ?
# restricted websites / inappropriate websites?
# domain safety? what if someone adds a url to a malicious website ???

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
