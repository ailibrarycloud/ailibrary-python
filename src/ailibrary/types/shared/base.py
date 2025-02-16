from typing import Optional, Dict, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class MetaModel(BaseModel):
    meta: Optional[Dict] = None

class PaginationParams(BaseModel):
    page: Optional[int] = None
    limit: Optional[int] = None
