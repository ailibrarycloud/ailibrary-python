import pytest
from ailibrary.types.shared.enums import ResourceType
from ..test_config import TestConstants, TestData

class TestAgentFlows:
    @pytest.mark.integration
    def test_create_and_chat_flow(self, api_client):
        """Test complete agent creation and chat workflow"""
        # Create agent
        agent = api_client.agent.create(**TestData.AGENT_CREATE_PAYLOAD)
        namespace = agent["namespace"]
        
        try:
            # Verify agent creation
            retrieved_agent = api_client.agent.get(namespace)
            assert retrieved_agent["title"] == TestData.AGENT_CREATE_PAYLOAD["title"]
            
            # Add a note to agent
            note = api_client.notes.add(
                content="Test note",
                role="user",
                resource=ResourceType.AGENT,
                resource_id=namespace
            )
            
            # Verify note was added
            agent_notes = api_client.notes.get_resource_notes(
                resource=ResourceType.AGENT,
                resource_id=namespace
            )
            assert len(agent_notes["notes"]) > 0
            
        finally:
            # Cleanup
            api_client.agent.delete(
                namespace=namespace,
                delete_connected_resources=True
            )

    @pytest.mark.integration
    def test_agent_with_knowledge_base_flow(self, api_client, test_file_path):
        """Test agent integration with knowledge base"""
        # Create knowledge base
        kb = api_client.knowledge_base.create(**TestData.KNOWLEDGE_BASE_CREATE_PAYLOAD)
        kb_id = kb["knowledgeId"]
        
        try:
            # Upload file to knowledge base
            uploaded_file = api_client.files.upload(
                files=[test_file_path],
                knowledgeId=kb_id
            )
            
            # Create agent with knowledge base
            agent_payload = {
                **TestData.AGENT_CREATE_PAYLOAD,
                "knowledge_id": kb_id
            }
            agent = api_client.agent.create(**agent_payload)
            
            # Verify knowledge base integration
            retrieved_agent = api_client.agent.get(agent["namespace"])
            assert retrieved_agent["knowledge_id"] == kb_id
            
        finally:
            # Cleanup
            api_client.agent.delete(
                namespace=agent["namespace"],
                delete_connected_resources=True
            )
