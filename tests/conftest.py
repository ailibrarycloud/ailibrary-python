import pytest
from unittest.mock import Mock
from dotenv import load_dotenv
import os
from ailibrary import AILibrary
from ailibrary._internal.__http_client import _HTTPClient

# Load test environment variables
load_dotenv('.env.test')

def pytest_collection_modifyitems(session, config, items):
    # Define test directory priority (lower index = runs first)
    ORDER = {
        "http_client": 0,
        "unit": 1,
        "integration": 2,
        "e2e": 3
    }
    
    # Sort test items based on their directory
    def get_test_priority(item):
        path = str(item.fspath)
        for key, priority in ORDER.items():
            if f"/{key}/" in path:
                return priority
        return 99  # Default for unclassified tests
    
    items.sort(key=lambda item: get_test_priority(item))


@pytest.fixture
def mock_http_client():
    """Fixture for mocked HTTP client"""
    return Mock(spec=_HTTPClient)

@pytest.fixture
def mock_response():
    """Fixture for mocked API responses"""
    def _create_response(data):
        return data
    return _create_response

@pytest.fixture
def api_client():
    """Fixture for real API client (for integration tests)"""
    return AILibrary(
        api_key=os.getenv('TEST_API_KEY'),
        domain=os.getenv('TEST_DOMAIN')
    )

@pytest.fixture
def test_file_path(tmp_path):
    """Fixture to create a temporary test file"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")
    return str(test_file)
