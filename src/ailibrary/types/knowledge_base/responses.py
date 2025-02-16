from datetime import datetime
from typing import Optional, List, Dict
from pydantic import 
from ..shared.responses import APIResponse, ListResponse
from ..shared.base import MetaModel

class KnowledgeBaseData(MetaModel):
    id: str
    name: str
    created_timestamp: datetime
    status: str
    source_count: Optional[int] = None

class SourceData(MetaModel):
    id: str
    type: str
    status: str
    created_timestamp: datetime
    options: Optional[Dict] = None

class KnowledgeBaseResponse(APIResponse[KnowledgeBaseData]):
    pass

class KnowledgeBaseListResponse(ListResponse[KnowledgeBaseData]):
    pass

class SourceResponse(APIResponse[SourceData]):
    pass

class SourceListResponse(ListResponse[SourceData]):
    pass
