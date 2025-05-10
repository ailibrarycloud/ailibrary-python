from typing import Optional
from datetime import datetime
from ..shared.base import CustomBaseModel
from .forms_base_class import FormsBaseClass
from pydantic import Field


class FormsMeta(CustomBaseModel):
    total_items: int
    total_pages: int
    current_page: int
    limit: int
    next_page: str
    prev_page: str


class FormsListItems(FormsBaseClass):
    form_id: str
    title: str
    userName: str
    created_timestamp: str
    updated_timestamp: str


class FormsCreateResponse(FormsBaseClass):
    form_id: str
    title: str
    schema_data: dict = Field(default=..., alias="schema")


class FormsGetResponse(FormsBaseClass):
    form_id: str
    title: str
    schema_data: dict = Field(default=..., alias="schema")


class FormsListResponse(CustomBaseModel):
    forms: list[FormsListItems]
    meta: FormsMeta


class FormsUpdateResponse(FormsBaseClass):
    form_id: str
    title: str
    schema_data: dict = Field(default=..., alias="schema")


class FormsDeleteResponse(CustomBaseModel):
    status: str
    message: str
