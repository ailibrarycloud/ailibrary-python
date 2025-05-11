# from typing import Any
from ..shared.models import CustomBaseModel
from pydantic import Field, ConfigDict

class FormsBaseClass(CustomBaseModel):
    model_config = ConfigDict(validate_by_alias=True, 
                              validate_by_name=True, 
                              serialize_by_alias=True, 
                              use_enum_values=True,
                              extra="allow") # for now

    schema_data: dict = Field(default=None, alias="schema")

    # @property
    # def schema(self) -> Any:
    #     return self.schema_data

    # @schema.setter
    # def schema(self, value: Any) -> None:
    #     self.schema_data = value

    # def model_dump(self, *args, **kwargs):
    #     kwargs['exclude_none'] = True
    #     kwargs["by_alias"] = True
    #     return super().model_dump(*args, **kwargs)