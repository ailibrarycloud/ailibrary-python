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
        "domain": os.getenv("E2E_DOMAIN"),
        "timeout": int(os.getenv("E2E_TIMEOUT", "300"))
    }

@pytest.fixture(scope="session")
def cleanup_registry():
    """Registry to track resources that need cleanup"""
    registry = {
        "agents": [],
        "knowledge_bases": [],
        "files": [],
        "notes": []
    }
    yield registry
    
    # Cleanup all registered resources
    client = e2e_client()
    for agent in registry["agents"]:
        try:
            client.agent.delete(namespace=agent)
        except Exception as e:
            print(f"Failed to cleanup agent {agent}: {e}")
    # Similar cleanup for other resources