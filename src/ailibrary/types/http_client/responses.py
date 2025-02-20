from typing import Optional, Any
from pydantic import BaseModel

class HTTPResponse(BaseModel):
    status_code: int
    data: Any

class ErrorResponse(Exception):
    def __init__(
        self,
        status_code: int,
        message: str,
        error: Optional[dict] = None
    ):
        self.status_code = status_code
        self.message = message
        self.error = error
        super().__init__(message)
