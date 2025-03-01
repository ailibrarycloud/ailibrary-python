import pytest
from ailibrary.types.shared.enums import ResourcePath

@pytest.fixture
def res_path():
    return ResourcePath.UTILITIES
