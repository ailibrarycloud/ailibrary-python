from typing import List
from pydantic import BaseModel, Field

class WebSearchRequest(BaseModel):
    search_terms: List[str] = Field(..., min_items=1)

class WebParserRequest(BaseModel):
    urls: List[str] = Field(..., min_items=1)
