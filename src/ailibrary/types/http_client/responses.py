from typing import Optional, Dict, Any, Generic, TypeVar
from pydantic import BaseModel

class HTTPResponse(BaseModel):
    status_code: int
    headers: Dict[str, str]
    body: Any
    error: Optional[str] = None
