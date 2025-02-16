from typing import Optional, Dict, List, Tuple, BinaryIO
from pydantic import 
from ..shared.enums import HTTPMethod

class HTTPRequest():
    method: HTTPMethod
    endpoint: str
    params: Optional[Dict] = None
    data: Optional[Dict] = None
    json: Optional[Dict] = None
    files: Optional[List[Tuple[str, Tuple[str, BinaryIO, str]]]] = None
    stream: bool = False