from pydantic import ConfigDict, field_validator, ValidationError
from typing import Tuple, BinaryIO, Any
from ..shared.models import CustomBaseModel
from .binary_file_validator import BinaryFileValidator


class FileSchema(CustomBaseModel):
    file_tuple: Tuple[str, Tuple[str, Any, str]]


    @field_validator("file_tuple")
    # validate the binary file located at file_tuple[1][1] using BinaryFileValidator
    def validate_file_tuple(cls, value):
        file_obj = value[1][1]
        try:
            BinaryFileValidator(file_obj=file_obj)
        except ValidationError as e:
            raise e
        
        return value