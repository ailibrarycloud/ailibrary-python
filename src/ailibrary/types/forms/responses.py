from typing import Optional
from datetime import datetime
from ..shared.base import CustomBaseModel

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

class FormCreateResponse(CustomBaseModel):
    form_id: str
    title: str
    schema: str


class FormGetResponse(CustomBaseModel):
    form_id: str
    title: str
    schema: dict


class FormListResponse(CustomBaseModel):
    forms: list[FormListItems]
    meta: FormMeta


class FormUpdateResponse(CustomBaseModel):
    form_id: str
    title: str
    schema: dict


class FormDeleteResponse(CustomBaseModel):
    status: str
    message: str
