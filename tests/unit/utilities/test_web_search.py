import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import WebSearchResponse

class TestUtilitiesWebSearch:
    @pytest.mark.parametrize("search_payload", [
        {
            "search_terms": ["AI technology", "machine learning"]
        }
    ])
    def test_general(self, res_path, mock_http_client, search_payload):
        """Test successful web search"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = {
            "term": "AI technology",
            "prompt_context": "AI technology refers to...",
            "sources": [
                {
                    "url": "https://example.com/ai",
                    "title": "AI Overview"
                }
            ]
        }
        mock_http_client._request.return_value = mock_response
        
        response = utilities.web_search(**search_payload)

        assert isinstance(response, dict)
        assert "term" in response
        assert "prompt_context" in response
        assert "sources" in response
        assert isinstance(response["sources"], list)

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/websearch",
            json=search_payload
        )
