from typing import List, Dict
from pydantic import 
from ..shared.responses import APIResponse

class SearchResult():
    title: str
    url: str
    snippet: str

class ParseResult():
    url: str
    content: str
    metadata: Dict

class WebSearchResponse(APIResponse[List[SearchResult]]):
    pass

class WebParserResponse(APIResponse[List[ParseResult]]):
    pass
