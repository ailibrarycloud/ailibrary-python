from pydantic import BaseModel, Field
from ..shared.base import CustomBaseModel
from typing import Optional

class WebSearchRequest(CustomBaseModel):
    search_terms: list[str] = Field(..., min_length=1)

class WebParserRequest(CustomBaseModel):
    urls: list[str] = Field(..., min_length=1)

class NewsSearchRequest(CustomBaseModel):
    search_terms: list[str] = Field(..., min_length=1)

class DocumentParserRequest(CustomBaseModel):
    urls: list[str] = Field(..., min_length=1)

class DocumentThumbnailRequest(CustomBaseModel):
    urls: list[str] = Field(..., min_length=1)

class JSONSchemaGeneratorRequest(CustomBaseModel):
    content: str = Field(..., min_length=1)
