from typing import Optional, Dict, List, Tuple, BinaryIO
from pydantic import BaseModel
from ..shared.enums import HTTPMethod

class HTTPRequest(BaseModel):
    method: HTTPMethod
    endpoint: str
    params: Optional[Dict] = None
    data: Optional[Dict] = None
    json: Optional[Dict] = None
    files: Optional[List[Tuple[str, Tuple[str, BinaryIO, str]]]] = None
    stream: bool = False