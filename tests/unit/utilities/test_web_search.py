# general case
# empty search terms
# search terms with one empty string
# search terms where all strings are empty
# search terms where only some strings are empty
# search terms where string has length 1 (what is the minimum allowed length of the search string?)
# search terms where string is way too large and wont fit in database
# search terms where string has different kinds of characters
# search terms with inappropriate strings / banned topics?
# search terms where the strings are website urls


import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import WebSearchResponse

class TestUtilitiesWebSearch:
    @pytest.mark.parametrize("search_payload", [
        {
            "search_terms": ["AI technology"]
        }
    ])
    def test_general(self, res_path, mock_http_client, search_payload):
        """Test successful web search"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = [
            {
                "term": "AI technology",
                "prompt_context": "AI technology refers to...",
                "sources": [
                    {
                        "url": "https://example.com/ai",
                        "title": "AI Overview",
                        "description": "AI technology refers to...",
                        "isFamilyFriendly": True,
                        "language": "en",
                        "full_text": "Full article content..."
                    }
                ]
            }
        ]
        mock_http_client._request.return_value = mock_response
        
        response = utilities.web_search(**search_payload)
        assert isinstance(response, list)
        assert len(response) == 1
        response_0 = response[0]
        assert isinstance(response_0, dict)
        assert "term" in response_0
        assert "prompt_context" in response_0
        assert isinstance(response_0["sources"], list)
        sources_0 = response_0["sources"][0]
        assert isinstance(sources_0, dict)
        assert "url" in sources_0
        assert "title" in sources_0
        assert "description" in sources_0
        assert "isFamilyFriendly" in sources_0
        assert "language" in sources_0
        assert "full_text" in sources_0


        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/websearch",
            json=search_payload
        )
