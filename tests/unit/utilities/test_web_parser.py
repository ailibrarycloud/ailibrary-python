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
# websites from anywhere in the world?
# some urls are files, others are webpages 
# urls that are too long for the database
# urls with special characters
# localhost:3000/ when im hosting something on localhost
# url to a local file on computer ?
# restricted websites / inappropriate websites?
# domain safety? what if someone adds a url to a malicious website ???


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
