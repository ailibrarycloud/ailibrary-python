from typing import Optional, Dict, Any, Generic, TypeVar, List
from pydantic import 
from .base import MetaModel

T = TypeVar('T')

class APIResponse(, Generic[T]):
    status_code: int
    message: Optional[str] = None
    data: Optional[T] = None

class ErrorResponse():
    status_code: int
    message: str
    error: Optional[Dict[str, Any]] = None

class ListResponse(, Generic[T]):
    items: List[T]
    total: int
    page: Optional[int] = None
    limit: Optional[int] = None
