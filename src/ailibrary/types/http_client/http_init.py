from typing import Optional, Tuple, BinaryIO, Any
from pydantic import Field, field_validator, ConfigDict, ValidationError
from ..shared.base import CustomBaseModel
from ..shared.enums import HTTPMethod
from ..files.file_schema import FileSchema


class HTTPInit(CustomBaseModel):
    api_key: str = Field(..., description="The API key for the AI Library", min_length=1)
    base_url: str = Field(..., description="The base URL for the AI Library", min_length=1)
