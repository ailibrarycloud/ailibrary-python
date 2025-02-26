from pydantic import BaseModel, Field
from ..shared.base import CustomBaseModel

class WebSearchRequest(CustomBaseModel):
    search_terms: list[str] = Field(..., min_length=1)

class WebParserRequest(CustomBaseModel):
    urls: list[str] = Field(..., min_length=1)
