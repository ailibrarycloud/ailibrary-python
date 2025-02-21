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
    note_id: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    role: RoleType
    meta: Optional[dict] = None


class NoteDeleteRequest(BaseModel):
    resource: ResourceType
    resource_id: str
    values: Optional[list[str]] = None
    delete_all: Optional[bool] = None


    @field_validator("values", "delete_all")
    def validate_values_and_delete_all(cls, v, info):
        # this validator is run once each for values and delete_all
        # so in one iteration, v == values, and in the other v == delete_all
        # info.data is dictionary of all fields and 
        # info.field_name is the name of the current field

        all_fields = info.data
        values, delete_all = all_fields.get("values"), all_fields.get("delete_all")

        if values is None and (delete_all is None or delete_all is False):
            raise ValueError("Either values or delete_all=True must be provided")
        
        return v
