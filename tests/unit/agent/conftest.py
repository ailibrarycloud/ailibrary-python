import pytest
from ailibrary.types.shared.enums import AgentType, ResourcePath
from ailibrary.types.agent.requests import AgentCreateRequest, AgentUpdateRequest, AgentDeleteRequest
from ailibrary.types.agent.responses import AgentCreateResponse, AgentUpdateResponse, AgentDeleteResponse, AgentGetResponse, AgentListResponse


@pytest.fixture
def res_path():
    return "/agent"

# @pytest.fixture
# def create_request():
#     """Default agent creation payload"""
#     return AgentCreateRequest(
#         title="Test Agent",
#         instructions="Test instructions",
#         description="Test description"
#     )

@pytest.fixture
def validated_agent_response():
    def _create_validated_response(create_payload: dict, namespace: str = "test-namespace") -> dict:
        """Helper to create and validate agent response data
        
        Args:
            create_payload: The payload used to create the agent
            namespace: The namespace to use in response (defaults to "test-namespace")
            
        Returns:
            dict: Validated response data
        """
        response_data = {
            **create_payload,
            "namespace": namespace
        }
        # Validate using Pydantic model
        validated_response = AgentCreateResponse(**response_data)
        return validated_response.model_dump()
    
    return _create_validated_response

