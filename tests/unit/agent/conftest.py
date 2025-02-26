import pytest
from ailibrary.types.shared.enums import AgentType, ResourcePath
from ailibrary.types.agent.requests import AgentCreateRequest, AgentUpdateRequest, AgentDeleteRequest
from ailibrary.types.agent.responses import AgentCreateResponse, AgentUpdateResponse, AgentDeleteResponse, AgentGetResponse, AgentListResponse


@pytest.fixture
def res_path():
    return ResourcePath.AGENT

# @pytest.fixture
# def create_request():
#     """Default agent creation payload"""
#     return AgentCreateRequest(
#         title="Test Agent",
#         instructions="Test instructions",
#         description="Test description"
#     )

@pytest.fixture
def agent_create_response():
    """Default agent response payload"""
    return AgentCreateResponse(namespace="test-agent", title="placeholder")
