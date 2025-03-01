from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')

class CustomBaseModel(BaseModel):
    model_config = ConfigDict(
        loc_by_alias=False,  # Shows full path in validation errors
        validate_assignment=True,  # Ensures re-validation everytime the a model attribute is reassigned
        extra='ignore'  # extra arguments to models are ignored...for now
    )


    def model_dump(self, *args, **kwargs):
        kwargs['exclude_none'] = True
        return super().model_dump(*args, **kwargs)


class MetaModel(CustomBaseModel):
    meta: Optional[dict] = None

class PaginationParams(CustomBaseModel):
    page: Optional[int] = None
    limit: Optional[int] = None

