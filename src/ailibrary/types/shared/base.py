from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')

class CustomBaseModel(BaseModel):
    model_config = ConfigDict(
        loc_by_alias=False,  # Shows full path in validation errors
        exclude_none=True,  # Moves this from model_dump to config
        # validate_assignment=True,  # Ensures validation on attribute assignment
        extra='ignore'  # Provides backward compatibility with older Pydantic behavior
    )
    
    # def dict(self, *args, **kwargs):
    #     # Set exclude_none to True by default
    #     kwargs['exclude_none'] = True
    #     return super().dict(*args, **kwargs)

    def model_dump(self, *args, **kwargs):
        return super().model_dump(*args, **kwargs)


class MetaModel(CustomBaseModel):
    meta: Optional[dict] = None

class PaginationParams(CustomBaseModel):
    page: Optional[int] = None
    limit: Optional[int] = None

