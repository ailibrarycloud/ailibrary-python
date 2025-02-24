import pytest
import os
from ailibrary import AILibrary

@pytest.fixture(scope="session")
def e2e_client():
    """E2E test client with extended timeout"""
    return AILibrary(
        api_key=os.getenv("E2E_API_KEY", "test-key"),
        domain=os.getenv("E2E_DOMAIN", "https://staging-api.ailibrary.ai/")
    )

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