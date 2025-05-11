from pydantic import BaseModel
# from ..shared.responses import APIResponse
from ..shared.models import CustomBaseModel
from typing import Optional, Any


class WebSearchSources(CustomBaseModel):
    title: str
    url: str
    description: str
    isFamilyFriendly: bool
    language: str
    full_text: str

class NewsSearchSources(CustomBaseModel):
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
    sources: list[WebSearchSources]


class WebParserResponse(CustomBaseModel):
    url: str
    title: str
    domain: str
    body: str
    related_urls: Optional[list[RelatedUrl]] = None


class NewsSearchResponse(CustomBaseModel):
    search_term: str
    prompt_context: str
    sources: list[NewsSearchSources]


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
