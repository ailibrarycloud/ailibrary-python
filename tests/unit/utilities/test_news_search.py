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
        
        # mock_response = {
        #     "articles": [
        #         {
        #             "title": "Latest AI Developments",
        #             "description": "Recent advances in AI...",
        #             "url": "https://example.com/news/ai",
        #             "source": "Tech News",
        #             "published_date": "2024-03-14T12:00:00Z",
        #             "content": "Full article content..."
        #         }
        #     ],
        #     "total_results": 1
        # }
        mock_response = [
            {
                "search_term": "AI news",
                "prompt_context": "AI news refers to...",
                "sources": [
                    {
                        "title": "Latest AI Developments",
                        "description": "Recent advances in AI...",
                        "url": "https://example.com/news/ai",
                        "datePublished": "2024-03-14T12:00:00Z",
                        "provider": "Tech News",
                        "full_text": "Full article content..."
                    }
                ]
            }
        ]
        mock_http_client._request.return_value = mock_response
        
        response = utilities.news_search(**search_payload)

        assert isinstance(response, list)
        assert len(response) == 1
        response_0 = response[0]
        assert isinstance(response_0, dict)
        assert "search_term" in response_0
        assert "prompt_context" in response_0
        assert isinstance(response_0["sources"], list)
        sources_0 = response_0["sources"][0]
        assert isinstance(sources_0, dict)
        assert "title" in sources_0
        assert "description" in sources_0
        assert "url" in sources_0
        assert "datePublished" in sources_0
        assert "provider" in sources_0
        assert "full_text" in sources_0


        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/news",
            json=search_payload
        )
