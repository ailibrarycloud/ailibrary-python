from typing import Optional
from pydantic import Field
from ..shared.models import CustomBaseModel
from .forms_base_class import FormsBaseClass

class FormsCreateRequest(FormsBaseClass):
    title: str = Field(..., min_length=1)
    schema_data: dict = Field(..., alias="schema")


class FormsUpdateRequest(FormsBaseClass):
    form_id: str = Field(..., exclude=True, min_length=1)
    title: Optional[str] = None
    schema_data: Optional[dict] = Field(default=None, alias="schema")


class FormsDeleteRequest(CustomBaseModel):
    form_id: str = Field(..., min_length=1)
