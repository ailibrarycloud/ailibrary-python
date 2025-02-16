from typing import List, Dict
from pydantic import BaseModel
from ..shared.responses import APIResponse

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

class ParseResult(BaseModel):
    url: str
    content: str
    metadata: Dict

class WebSearchResponse(APIResponse[List[SearchResult]]):
    pass

class WebParserResponse(APIResponse[List[ParseResult]]):
    pass
