from typing import Optional, Dict, List
from pydantic import , Field
from ..shared.base import MetaModel

class KnowledgeBaseCreateRequest(MetaModel):
    name: str = Field(..., min_length=1)

class SourceOptions():
    urls: Optional[Dict[str, str]] = None

class AddSourceRequest(MetaModel):
    type: str = Field(..., pattern="^(docs|web|youtube)$")
    options: SourceOptions
    
class DeleteSourcesRequest():
    values: Optional[List[str]] = None
    delete_all: Optional[bool] = None
