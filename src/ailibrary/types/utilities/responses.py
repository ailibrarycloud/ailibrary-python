from pydantic import BaseModel
from ..shared.responses import APIResponse
from ..shared.base import CustomBaseModel
from typing import Optional, Any


class WebSearchSource(CustomBaseModel):
    title: str
    description: str
    url: str
    isFamilyFriendly: bool
    language: str
    full_text: str

class NewsSearchSource(CustomBaseModel):
    title: str
    description: str
    url: str
    datePublished: str
    provider: str
    full_text: str

class RelatedUrl(CustomBaseModel):
    url: str
    title: str
    description: str
    type: str

class NewsArticle(CustomBaseModel):
    title: str
    description: str
    url: str
    source: str
    published_date: str
    content: str


class WebSearchResponse(CustomBaseModel):
    term: str
    prompt_context: str
    sources: list[WebSearchSource]


class WebParserResponse(CustomBaseModel):
    url: str
    title: str
    domain: str
    body: str
    related_urls: list[RelatedUrl]


class NewsSearchResponse(CustomBaseModel):
    articles: list[NewsArticle]
    total_results: int


class DocumentParserResponse(CustomBaseModel):
    url: str
    title: str
    body: str

class DocumentThumbnailResponse(CustomBaseModel):
    url: str
    thumbnail: str

class JSONSchemaGeneratorResponse(CustomBaseModel):
    name: dict
    email: dict
    phone: dict
    experience_in_years: dict
    ai_experience_in_years: dict
    highest_educational_qualification: dict
