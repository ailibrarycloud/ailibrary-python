from enum import Enum
import pytest
import os
from ailibrary import AILibrary

class TestConstants:
    TEST_API_KEY = "test-key"
    TEST_DOMAIN = "https://test-api.ailibrary.ai/"
    
    # Test data constants
    AGENT_NAMESPACE = "test-agent"
    KNOWLEDGE_BASE_ID = "test-kb"
    FILE_ID = "test-file"
    NOTE_ID = "test-note"
    
    # Test file paths
    TEST_FILE_PATH = "tests/data/test.pdf"

class TestData:
    AGENT_CREATE_PAYLOAD = {
        "title": "Test Agent",
        "instructions": "Test instructions",
        "description": "Test description"
    }
    
    KNOWLEDGE_BASE_CREATE_PAYLOAD = {
        "name": "Test Knowledge Base",
        "meta": {"type": "test"}
    }

# Add E2E specific fixtures
@pytest.fixture(scope="session")
def e2e_config():
    """E2E test configuration"""
    return {
        "api_key": os.getenv("E2E_API_KEY", "test-key"),
        "domain": os.getenv("E2E_DOMAIN", "https://staging-api.ailibrary.ai/"),
        "timeout": int(os.getenv("E2E_TIMEOUT", "300"))
    }

@pytest.fixture(scope="session")
def e2e_client(e2e_config):
    """Dedicated client for E2E tests"""
    return AILibrary(
        api_key=e2e_config["api_key"],
        domain=e2e_config["domain"]
    )
