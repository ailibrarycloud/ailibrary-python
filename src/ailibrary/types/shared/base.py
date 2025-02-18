from typing import Optional, Dict, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class CustomBaseModel(BaseModel):
    # def dict(self, *args, **kwargs):
    #     # Set exclude_none to True by default
    #     kwargs['exclude_none'] = True
    #     return super().dict(*args, **kwargs)

    def model_dump(self, *args, **kwargs):
        # Set exclude_none to True by default
        kwargs['exclude_none'] = True
        return super().model_dump(*args, **kwargs)


class MetaModel(CustomBaseModel):
    meta: Optional[Dict] = None

class PaginationParams(CustomBaseModel):
    page: Optional[int] = None
    limit: Optional[int] = None

