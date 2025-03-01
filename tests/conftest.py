import pytest
from unittest.mock import Mock
from dotenv import load_dotenv
import os
from ailibrary import AILibrary
from ailibrary._internal.__http_client import _HTTPClient

# Load test environment variables
load_dotenv('.env.test')

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
