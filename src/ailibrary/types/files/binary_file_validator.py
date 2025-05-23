from pydantic import BaseModel, ConfigDict, field_validator
from io import BufferedReader
from typing import Any


class BinaryFileValidator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, 
                              loc_by_alias=False, 
                              use_enum_values=True, 
                              extra="allow") # for now
    file_obj: Any
    
    @field_validator('file_obj')
    def validate_file_object(cls, v):
        ### TWO POSSIBLE APPROACHES
        ## 1. Directly check the type of the object
        if not isinstance(v, BufferedReader):
            raise ValueError("File object must be a io.BufferedReader")

        ## 2. Check if object has required binary file methods and other properties

        # required_attrs = ['read', 'write', 'seek', 'tell', 'close', 'fileno', 'mode']
        # for attr in required_attrs:
        #     if not hasattr(v, attr):
        #         raise ValueError(f"File object missing required attribute: {attr}")
        
        # Verify it's opened in binary mode
        if 'b' not in v.mode:
            raise ValueError("File must be opened in binary mode")
            
        # Check if file is readable
        if not v.readable():
            raise ValueError("File object must be readable")
            
        return v