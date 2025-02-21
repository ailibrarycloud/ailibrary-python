from typing import Optional
from pydantic import BaseModel, Field, field_validator
from ..shared.base import MetaModel
from ..shared.enums import ResourceType, RoleType
from ..files.file_schema import FileSchema
from pydantic import ValidationError

class NoteAddRequest(MetaModel):
    content: str = Field(..., min_length=1)
    role: RoleType
    resource: ResourceType
    resource_id: str = Field(..., min_length=1)
    meta: Optional[dict] = None

class NoteUpdateRequest(MetaModel):
    note_id: str = Field(..., min_length=1, exclude=True)
    content: str = Field(..., min_length=1)
    role: RoleType
    meta: Optional[dict] = None


class NoteDeleteRequest(BaseModel):
    resource: ResourceType
    resource_id: str
    values: Optional[list[str]] = None
    delete_all: Optional[bool] = None


    @field_validator("delete_all")
    def validate_values_and_delete_all(cls, v, info):
        # If delete_all is True, values is ignored so we can return early
        if v:
            return v
        # If we get here, delete_all is either False or None
        # So we need valid values
        other_fields = info.data
        values = other_fields.get("values")
        if not values:
            raise ValueError(
                "Either provide a list of note IDs in 'values' or set delete_all=True. "
                "At least one must be specified."
            )
        return v
