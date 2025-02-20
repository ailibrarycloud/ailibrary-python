from pydantic import BaseModel
from ..shared.responses import APIResponse

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

class ParseResult(BaseModel):
    url: str
    content: str
    metadata: dict

class WebSearchResponse(APIResponse[list[SearchResult]]):
    pass

class WebParserResponse(APIResponse[list[ParseResult]]):
    pass
