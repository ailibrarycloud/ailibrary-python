from typing import Optional, Any, Generic, TypeVar
from pydantic import BaseModel
from .base import MetaModel
from .base import CustomBaseModel

T = TypeVar('T')

class APIResponse(CustomBaseModel, Generic[T]):
    data: T
    
    def __init__(self, **data):
        # Move all data into a nested 'data' structure if it's not already there
        if 'data' not in data:
            data = {'data': data}
        super().__init__(**data)
    
    def __getitem__(self, key):
        try:
            return getattr(self.data, key)
        except AttributeError:
            raise KeyError(key)

class ErrorResponse(CustomBaseModel):
    status_code: int
    message: str
    error: Optional[dict[str, Any]] = None

class ListResponse(CustomBaseModel, Generic[T]):
    items: list[T]
    total: int
    page: Optional[int] = None
    limit: Optional[int] = None
