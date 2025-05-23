import pytest
from ailibrary._internal._agent import _Agent
from ailibrary._internal._forms import _Forms

class TestAgentFormsIntegration:
    @pytest.mark.parametrize("form_filling", [None, False, True])
    def test_agent_with_form_create(self, mock_http_client, form_filling):
        """Test that when creating an agent with a form, the form_id is properly set"""
        # Create form first
        forms = _Forms(mock_http_client)
        schema = {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "years_of_experience": {"type": "number"},
            "years_experience_with_nextjs": {"type": "number"},
            "AI_experience": {"type": "boolean"}
        }
        
        form_response = {
            "form_id": "form_123",
            "title": "Test Form",
            "schema": schema
        }
        mock_http_client._request.return_value = form_response
        
        form_id = forms.create("Test Form", schema)["form_id"]
        
        # Now create agent with this form
        agent = _Agent(mock_http_client)
        create_payload = {
            "title": "Test Agent",
            "form_id": form_id
        }
        if form_filling is not None:
            create_payload["form_filling"] = form_filling
            
        agent_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "form_id": form_id,
            "form_filling": form_filling if form_filling is not None else False
        }
        mock_http_client._request.return_value = agent_response
        
        response = agent.create(**create_payload)
        
        assert isinstance(response, dict)
        assert response["form_id"] == form_id
        assert response["form_filling"] == (form_filling if form_filling is not None else False)
        
        # Verify agent.get() includes the form info
        get_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "form_id": form_id,
            "form_filling": form_filling if form_filling is not None else False
        }
        mock_http_client._request.return_value = get_response
        
        agent_info = agent.get("test-agent")
        assert agent_info["form_id"] == form_id
        assert agent_info["form_filling"] == (form_filling if form_filling is not None else False)

    @pytest.mark.parametrize("form_filling", [None, False, True])
    def test_agent_with_form_update(self, mock_http_client, form_filling):
        """Test that when updating an agent with a form, the form_id is properly set"""
        # Create form first
        forms = _Forms(mock_http_client)
        schema = {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "years_of_experience": {"type": "number"},
            "years_experience_with_nextjs": {"type": "number"},
            "AI_experience": {"type": "boolean"}
        }
        
        form_response = {
            "form_id": "form_123",
            "title": "Test Form",
            "schema": schema
        }
        mock_http_client._request.return_value = form_response
        
        form_id = forms.create("Test Form", schema)["form_id"]
        
        # Create agent without form
        agent = _Agent(mock_http_client)
        create_response = {
            "namespace": "test-agent",
            "title": "Test Agent"
        }
        mock_http_client._request.return_value = create_response
        
        agent.create(title="Test Agent")
        
        # Update agent with form
        update_payload = {
            "namespace": "test-agent",
            "form_id": form_id
        }
        if form_filling is not None:
            update_payload["form_filling"] = form_filling
            
        update_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "form_id": form_id,
            "form_filling": form_filling if form_filling is not None else False
        }
        mock_http_client._request.return_value = update_response
        
        response = agent.update(**update_payload)
        
        assert isinstance(response, dict)
        assert response["form_id"] == form_id
        assert response["form_filling"] == (form_filling if form_filling is not None else False)
        
        # Verify agent.get() includes the form info
        get_response = {
            "namespace": "test-agent",
            "title": "Test Agent",
            "form_id": form_id,
            "form_filling": form_filling if form_filling is not None else False
        }
        mock_http_client._request.return_value = get_response
        
        agent_info = agent.get("test-agent")
        assert agent_info["form_id"] == form_id
        assert agent_info["form_filling"] == (form_filling if form_filling is not None else False) 