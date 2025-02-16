from typing import Optional, Dict, List
from pydantic import BaseModel, Field
from ..shared.base import MetaModel

class KnowledgeBaseCreateRequest(MetaModel):
    name: str = Field(..., min_length=1)

class SourceOptions(BaseModel):
    urls: Optional[Dict[str, str]] = None

class AddSourceRequest(MetaModel):
    type: str = Field(..., pattern="^(docs|web|youtube)$")
    options: SourceOptions
    
class DeleteSourcesRequest(BaseModel):
    values: Optional[List[str]] = None
    delete_all: Optional[bool] = None
