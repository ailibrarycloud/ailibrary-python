from pydantic import BaseModel
from ..shared.responses import APIResponse
from ..shared.base import CustomBaseModel


class WebSearchResponse(CustomBaseModel):
    term: str
    prompt_context: str
    sources: list[dict]

class RelatedUrl(CustomBaseModel):
    url: str
    title: str
    description: str
    type: str

class WebParserResponse(CustomBaseModel):
    url: str
    title: str
    domain: str
    body: str
    related_urls: list[RelatedUrl]
