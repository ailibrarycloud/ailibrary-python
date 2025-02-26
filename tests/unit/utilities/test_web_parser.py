import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import WebParserResponse

class TestUtilitiesWebParser:
    @pytest.mark.parametrize("parser_payload", [
        {
            "urls": ["https://example.com/article"]
        }
    ])
    def test_general(self, res_path, mock_http_client, parser_payload):
        """Test successful web parsing"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = {
            "url": "https://example.com/article",
            "title": "Test Article",
            "domain": "example.com",
            "body": "Article content...",
            "related_urls": [
                {
                    "url": "https://example.com/related",
                    "title": "Related Article",
                    "description": "A related article",
                    "type": "article"
                }
            ]
        }
        mock_http_client._request.return_value = mock_response
        
        response = utilities.web_parser(**parser_payload)

        assert isinstance(response, dict)
        assert "url" in response
        assert "title" in response
        assert "domain" in response
        assert "body" in response
        assert "related_urls" in response
        assert isinstance(response["related_urls"], list)

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/webparser",
            json=parser_payload
        )
