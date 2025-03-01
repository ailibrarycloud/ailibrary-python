from typing import Optional
from datetime import datetime
from ..shared.base import CustomBaseModel
from .forms_base_class import FormsBaseClass
from pydantic import Field

class FormListItems(CustomBaseModel):
    form_id: str
    title: str
    userName: str
    created_timestamp: str
    updated_timestamp: str

class FormMeta(CustomBaseModel):
    total_items: int
    total_pages: int
    current_page: int
    limit: int
    next_page: str
    previous_page: str

class FormCreateResponse(FormsBaseClass):
    form_id: str
    title: str
    schema_data: dict = Field(default=..., alias="schema")


class FormGetResponse(FormsBaseClass):
    form_id: str
    title: str
    schema_data: dict = Field(default=..., alias="schema")


class FormListResponse(CustomBaseModel):
    forms: list[FormListItems]
    meta: FormMeta


class FormUpdateResponse(FormsBaseClass):
    form_id: str
    title: str
    schema_data: dict = Field(default=..., alias="schema")


class FormDeleteResponse(CustomBaseModel):
    status: str
    message: str
