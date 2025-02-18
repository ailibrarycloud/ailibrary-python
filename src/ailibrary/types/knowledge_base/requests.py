from typing import Optional, Dict, List
from pydantic import BaseModel, Field
from ..shared.base import CustomBaseModel


class KnowledgeBaseCreateRequest(CustomBaseModel):
    name: str = Field(..., description="The name of the knowledge base")
    meta: Optional[Dict] = None

# class SourceOptions(BaseModel):
#     urls: Optional[Dict[str, str]] = None

# class AddSourceRequest(CustomBaseModel):
#     type: str = Field(..., pattern="^(docs|web|youtube)$")
#     options: SourceOptions
#     meta: Optional[Dict] = None
    
# class DeleteSourcesRequest(CustomBaseModel):
#     values: Optional[List[str]] = None
#     delete_all: Optional[bool] = None
#     knowledgeId: str = Field(..., 
#         description="The unique identifier for the knowledge base",
#         exclude=True
#     )
