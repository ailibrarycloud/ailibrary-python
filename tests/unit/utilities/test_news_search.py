import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import NewsSearchResponse

class TestUtilitiesNewsSearch:
    @pytest.mark.parametrize("search_payload", [
        {
            "search_terms": ["AI news", "machine learning developments"]
        }
    ])
    def test_general(self, res_path, mock_http_client, search_payload):
        """Test successful news search"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = {
            "articles": [
                {
                    "title": "Latest AI Developments",
                    "description": "Recent advances in AI...",
                    "url": "https://example.com/news/ai",
                    "source": "Tech News",
                    "published_date": "2024-03-14T12:00:00Z",
                    "content": "Full article content..."
                }
            ],
            "total_results": 1
        }
        mock_http_client._request.return_value = mock_response
        
        response = utilities.news_search(**search_payload)

        assert isinstance(response, dict)
        assert "articles" in response
        assert isinstance(response["articles"], list)
        assert "total_results" in response

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/news",
            json=search_payload
        )
