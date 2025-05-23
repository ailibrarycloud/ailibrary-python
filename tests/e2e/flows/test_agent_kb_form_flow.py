import pytest
from datetime import datetime
from ailibrary.types.shared.enums import ResourceType

class TestAgentKBFormFlow:
    """Test suite for agent, knowledge base, and form integration workflows"""
    
    @pytest.fixture(scope="class")
    def form_id(self, e2e_client, cleanup_registry):
        """Create and register form for the test suite"""
        form_schema = {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "experience": {"type": "number"}
        }
        form = e2e_client.forms.create("Test Form", form_schema)
        form_id = form["form_id"]
        cleanup_registry["forms"].append(form_id)
        return form_id

    @pytest.fixture(scope="class")
    def initial_kb(self, e2e_client, cleanup_registry):
        """Create and register initial knowledge base"""
        kb = e2e_client.knowledge_base.create(
            name="Initial KB",
            meta={"type": "documentation", "version": "1.0"}
        )
        kb_id = kb["knowledgeId"]
        cleanup_registry["knowledge_bases"].append(kb_id)
        return kb

    @pytest.fixture(scope="class")
    @pytest.mark.e2e
    def create_agent_with_form_and_kb(self, e2e_client, cleanup_registry, form_id, initial_kb):
        """Fixture to create and verify agent with form and knowledge base"""
        agent = e2e_client.agent.create(
            title="Test Agent",
            instructions="Test instructions",
            knowledge_search=True,
            knowledge_id=initial_kb["knowledgeId"],
            form_id=form_id
        )
        namespace = agent["namespace"]
        cleanup_registry["agents"].append(namespace)

        # Verify creation
        agent_details = e2e_client.agent.get(namespace)
        assert agent_details["formId"] == form_id
        assert agent_details["knowledge_id"] == initial_kb["knowledgeId"]
        return namespace

    @pytest.mark.e2e
    def test_update_agent_name(self, e2e_client, create_agent_with_form_and_kb):
        """Test updating agent name with current date"""
        namespace = create_agent_with_form_and_kb
        current_date = datetime.now().strftime("%Y-%m-%d")
        updated_title = f"Test Agent {current_date}"
        
        e2e_client.agent.update(namespace, title=updated_title)
        
        # Verify update
        agent_details = e2e_client.agent.get(namespace)
        assert agent_details["title"] == updated_title

    @pytest.mark.e2e
    def test_agent_list_verification(self, e2e_client, create_agent_with_form_and_kb):
        """Test agent appears in list"""
        namespace = create_agent_with_form_and_kb
        agents_list = e2e_client.agent.list_agents()
        assert any(a["namespace"] == namespace for a in agents_list["agents"])

    @pytest.mark.e2e
    def test_knowledge_base_update_flow(self, e2e_client, cleanup_registry, 
                                      create_agent_with_form_and_kb, initial_kb):
        """Test knowledge base update and verification flow"""
        namespace = create_agent_with_form_and_kb
        
        # Create new KB
        new_kb = e2e_client.knowledge_base.create(
            name="New KB",
            meta={"type": "test", "version": "2.0"}
        )
        new_kb_id = new_kb["knowledgeId"]
        cleanup_registry["knowledge_bases"].append(new_kb_id)

        # Update agent with new KB
        e2e_client.agent.update(namespace, knowledge_id=new_kb_id)

        # Delete old KB
        e2e_client.knowledge_base.delete(initial_kb["knowledgeId"])
        cleanup_registry["knowledge_bases"].remove(initial_kb["knowledgeId"])

        # Update and verify KB meta
        updated_meta = {"type": "test", "version": "2.1", "updated": True}
        e2e_client.knowledge_base.update(new_kb_id, meta=updated_meta)
        
        kb_details = e2e_client.knowledge_base.get(new_kb_id)
        assert kb_details["meta"] == updated_meta

        # Verify KB in list
        kb_list = e2e_client.knowledge_base.list_knowledge_bases()
        assert any(kb["knowledgeId"] == new_kb_id for kb in kb_list["knowledge_bases"])
