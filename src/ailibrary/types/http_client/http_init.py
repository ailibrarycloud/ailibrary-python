from pydantic import Field
from ..shared.models import CustomBaseModel


class HTTPInit(CustomBaseModel):
    api_key: str = Field(..., description="The API key for the AI Library", min_length=1)
    base_url: str = Field(..., description="The base URL for the AI Library", min_length=1)
