from typing import Optional, Dict, List, Tuple, BinaryIO, Any
from pydantic import Field, field_validator, ConfigDict
from ..shared.base import CustomBaseModel
from ..shared.enums import HTTPMethod

class HTTPRequest(CustomBaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    method: str  # Change to str for initial validation
    endpoint: str
    params: Optional[Dict] = None
    data: Optional[Dict] = None
    json_payload: Optional[Dict] = Field(default=None, alias="json")
    files: Optional[List[Tuple[str, Tuple[str, BinaryIO, str]]]] = None
    stream: bool = False

    @field_validator('method')
    def validate_method(cls, value):
        if value not in HTTPMethod.__members__:
            raise ValueError(f"Invalid HTTP method: {value}. Must be one of: {[m.value for m in HTTPMethod]}")
        return HTTPMethod[value]  # Convert to HTTPMethod enum member

    @property
    def json(self) -> Optional[Dict]:
        return self.json_payload

    @json.setter
    def json(self, value: Optional[Dict]) -> None:
        self.json_payload = value

    def model_dump_json(self, *args: Any, **kwargs: Any) -> str:
        """Override to avoid conflict with json field"""
        return super().model_dump_json(*args, **kwargs)