from typing import Optional, Any
from pydantic import Field
from ..shared.base import CustomBaseModel


class FormField(CustomBaseModel):
    name: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)
    required: bool = False
    options: Optional[list[str]] = None
    description: Optional[str] = None


class FormCreateRequest(CustomBaseModel):
    title: str = Field(..., min_length=1)
    schema: dict


class FormUpdateRequest(CustomBaseModel):
    form_id: str = Field(..., min_length=1)
    title: Optional[str] = None
    fields: Optional[list[FormField]] = None
    description: Optional[str] = None
    meta: Optional[dict] = None


class FormDeleteRequest(CustomBaseModel):
    form_id: str = Field(..., min_length=1)


class FormSubmitRequest(CustomBaseModel):
    form_id: str = Field(..., min_length=1)
    values: dict[str, Any]
