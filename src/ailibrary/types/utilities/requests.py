from typing import List
from pydantic import , Field

class WebSearchRequest():
    search_terms: List[str] = Field(..., min_items=1)

class WebParserRequest():
    urls: List[str] = Field(..., min_items=1)
