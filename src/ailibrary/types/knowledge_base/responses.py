from datetime import datetime
from typing import Optional
from ..shared.responses import APIResponse, ListResponse
from .requests import KnowledgeBaseCreateRequest
from ..shared.base import CustomBaseModel


class KnowledgeBaseCreateResponse(CustomBaseModel):
    knowledgeId: str
    status: str
    meta: Optional[dict] = None


class KnowledgeBaseGetResponse(KnowledgeBaseCreateResponse):
    title: str
    sources: int
    generations: int
    addhistory: int
    visibility: str
    default_prompts: Optional[str] = None
    default_model: Optional[str] = None
    default_urls: Optional[dict] = None
    userName: str
    userEmail: str
    special_event: Optional[str] = None
    star: Optional[str] = None
    meta: Optional[dict] = None


class KnowledgeBaseListData(KnowledgeBaseCreateResponse):
    created_timestamp: str
    updated_timestamp: str
    title: str
    userName: str


class KnowledgeBaseListResponse(CustomBaseModel):
    knowledgebases: list[KnowledgeBaseListData]
    meta: dict



# class SourceData(CustomBaseModel):
#     id: str
#     type: str
#     status: str
#     created_timestamp: datetime
#     options: Optional[dict] = None
#     meta: Optional[dict] = None

# class SourceResponse(APIResponse[SourceData]):
#     pass

# class SourceListResponse(ListResponse[SourceData]):
#     pass
