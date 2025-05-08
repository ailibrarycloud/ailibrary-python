from pydantic import BaseModel, ConfigDict
from ..shared.enums import RoleType

# the format of each message when passing a list of messages to agent.chat()
class ChatMessageModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, loc_by_alias=False, extra='ignore') ### ignore this    
    # below are the required keys for each message dictionary
    role: RoleType
    content: str
