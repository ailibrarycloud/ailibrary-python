import pytest
from ailibrary.types.shared.enums import AgentType
from ailibrary.types.agent.requests import AgentCreateRequest, AgentUpdateRequest, AgentDeleteRequest

@pytest.fixture
def resource_path():
    return "/agent"

@pytest.fixture
def create_request():
    """Default agent creation payload"""
    return AgentCreateRequest(
        title="Test Agent",
        instructions="Test instructions",
        description="Test description"
    )

@pytest.fixture
def agent_response_payload():
    """Default agent response payload"""
    return {
        "namespace": "test-agent",
        **TestData.AGENT_CREATE_PAYLOAD
    }
