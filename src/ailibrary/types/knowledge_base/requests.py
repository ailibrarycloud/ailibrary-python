from typing import Optional
from pydantic import Field
from ..shared.models import CustomBaseModel
from ..shared.enums import SourceType

class KnowledgeBaseCreateRequest(CustomBaseModel):
    name: str = Field(..., description="The name of the knowledge base", min_length=1)
    meta: Optional[dict] = None

class SourceOptions(CustomBaseModel):
    urls: Optional[list[str]] = None

class AddSourceRequest(CustomBaseModel):
    type: SourceType
    options: Optional[SourceOptions] = None
    meta: Optional[dict] = None
    
class DeleteSourcesRequest(CustomBaseModel):
    values: Optional[list[str]] = None
    delete_all: Optional[bool] = None
    knowledgeId: str = Field(..., 
        description="The unique identifier for the knowledge base",
        exclude=True
    )
