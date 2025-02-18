from datetime import datetime
from typing import Optional, List, Dict
from ..shared.responses import APIResponse, ListResponse
from .requests import KnowledgeBaseCreateRequest
from ..shared.base import CustomBaseModel


class KnowledgeBaseCreateResponse(CustomBaseModel):
    knowledgeId: str
    status: str
    meta: Optional[Dict] = None


class KnowledgeBaseGetResponse(KnowledgeBaseCreateResponse):
    title: str
    sources: int
    generations: int
    addhistory: int
    visibility: str
    default_prompts: Optional[str] = None
    default_model: Optional[str] = None
    default_urls: Optional[Dict] = None
    userName: str
    userEmail: str
    special_event: Optional[str] = None
    star: Optional[str] = None
    meta: Optional[Dict] = None


class KnowledgeBaseListData(KnowledgeBaseCreateResponse):
    created_timestamp: str
    updated_timestamp: str
    title: str
    userName: str


class KnowledgeBaseListResponse(CustomBaseModel):
    knowledgebases: List[KnowledgeBaseListData]
    meta: dict



# class SourceData(CustomBaseModel):
#     id: str
#     type: str
#     status: str
#     created_timestamp: datetime
#     options: Optional[Dict] = None
#     meta: Optional[Dict] = None

# class SourceResponse(APIResponse[SourceData]):
#     pass

# class SourceListResponse(ListResponse[SourceData]):
#     pass
