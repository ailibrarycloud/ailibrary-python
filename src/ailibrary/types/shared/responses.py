from typing import Optional, Dict, Any, Generic, TypeVar, List
from pydantic import BaseModel
from .base import MetaModel
from .base import CustomBaseModel

T = TypeVar('T')

class APIResponse(CustomBaseModel, Generic[T]):
    # status_code: int
    # message: Optional[str] = None
    # data: Optional[T] = None
    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(key)

class ErrorResponse(CustomBaseModel):
    status_code: int
    message: str
    error: Optional[Dict[str, Any]] = None

class ListResponse(CustomBaseModel, Generic[T]):
    items: List[T]
    total: int
    page: Optional[int] = None
    limit: Optional[int] = None
