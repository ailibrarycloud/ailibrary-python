from typing import Optional, Tuple, BinaryIO, Any
from pydantic import Field, field_validator, ConfigDict, ValidationError
from ..shared.base import CustomBaseModel
from ..shared.enums import HTTPMethod
from ..files.file_schema import FileSchema

class HTTPRequest(CustomBaseModel):
    method: str  # Change to str for initial validation
    endpoint: str
    params: Optional[dict] = None
    data: Optional[dict] = None
    json_payload: Optional[dict] = Field(default=None, alias="json")
    files: Optional[list] = None
    stream: bool = False


    @field_validator('method')
    def validate_method(cls, value):
        if value not in HTTPMethod.__members__:
            raise ValueError(f"Invalid HTTP method: {value}. Must be one of: {[m.value for m in HTTPMethod]}")
        return HTTPMethod[value]  # Convert to HTTPMethod enum member


    @field_validator("files")
    def validate_files(cls, file_list):
        # print(file_list)
        if file_list is not None:
            try:
                # validate <files> parameter using the FileSchema validator
                for item in file_list:
                    FileSchema(file_tuple=item)
            except ValidationError as e:
                raise e
        return file_list
    

    @property
    def json(self) -> Optional[dict]:
        return self.json_payload


    @json.setter
    def json(self, value: Optional[dict]) -> None:
        self.json_payload = value


    def model_dump_json(self, *args: Any, **kwargs: Any) -> str:
        """Override to avoid conflict with json field"""
        return super().model_dump_json(*args, **kwargs)