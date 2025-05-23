import pytest
import os
from dotenv import load_dotenv
from ailibrary import AILibrary

# Load test environment variables
load_dotenv('.env.test')

@pytest.fixture(scope="session")
def e2e_client():
    """E2E test client with extended timeout"""
    return AILibrary(
        api_key=os.getenv("E2E_API_KEY"),
        domain=os.getenv("E2E_DOMAIN")
    )

@pytest.fixture(scope="session")
def e2e_config():
    """E2E test configuration"""
    return {
        "api_key": os.getenv("E2E_API_KEY"),
        "domain": os.getenv("E2E_DOMAIN")
    }

@pytest.fixture(scope="session")
def cleanup_registry(e2e_client):
    """Registry to track resources that need cleanup"""
    registry = {
        "agents": [],
        "knowledge_bases": [],
        "files": [],
        "notes": [],
        "forms": []
    }
    yield registry
    
    # Cleanup all registered resources
    for agent in registry["agents"]:
        try:
            e2e_client.agent.delete(namespace=agent)
        except Exception as e:
            print(f"Failed to cleanup agent {agent}: {e}")
            
    for form_id in registry["forms"]:
        try:
            e2e_client.forms.delete(form_id)
        except Exception as e:
            print(f"Failed to cleanup form {form_id}: {e}")