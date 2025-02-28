from typing import Optional
from pydantic import BaseModel, Field
from ..shared.base import CustomBaseModel


class KnowledgeBaseCreateRequest(CustomBaseModel):
    name: str = Field(..., description="The name of the knowledge base", min_length=1)
    meta: Optional[dict] = None

# class SourceOptions(BaseModel):
#     urls: Optional[dict[str, str]] = None

# class AddSourceRequest(CustomBaseModel):
#     type: str = Field(..., pattern="^(docs|web|youtube)$")
#     options: SourceOptions
#     meta: Optional[dict] = None
    
# class DeleteSourcesRequest(CustomBaseModel):
#     values: Optional[list[str]] = None
#     delete_all: Optional[bool] = None
#     knowledgeId: str = Field(..., 
#         description="The unique identifier for the knowledge base",
#         exclude=True
#     )
