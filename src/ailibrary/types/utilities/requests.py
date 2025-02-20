from pydantic import BaseModel, Field

class WebSearchRequest(BaseModel):
    search_terms: list[str] = Field(..., min_items=1)

class WebParserRequest(BaseModel):
    urls: list[str] = Field(..., min_items=1)
