import pytest
from ailibrary._internal._utilities import _Utilities
from ailibrary.types.utilities.responses import JSONSchemaGeneratorResponse

class TestUtilitiesJSONSchemaGenerator:
    @pytest.mark.parametrize("schema_payload", [
        {
            "content": "Create a schema for a user profile with name, email, and experience"
        }
    ])
    def test_general(self, res_path, mock_http_client, schema_payload):
        """Test successful JSON schema generation"""
        utilities = _Utilities(mock_http_client)
        
        mock_response = {
            "name": {"type": "string", "description": "User's full name"},
            "email": {"type": "string", "format": "email"},
            "phone": {"type": "string", "pattern": "^\\+?[1-9]\\d{1,14}$"},
            "experience_in_years": {"type": "integer", "minimum": 0},
            "ai_experience_in_years": {"type": "integer", "minimum": 0},
            "highest_educational_qualification": {"type": "string", "enum": ["BS", "MS", "PhD"]}
        }
        mock_http_client._request.return_value = mock_response
        
        response = utilities.json_schema_generator(**schema_payload)

        assert isinstance(response, dict)
        assert "name" in response
        assert "email" in response
        assert "phone" in response
        assert "experience_in_years" in response
        assert "ai_experience_in_years" in response
        assert "highest_educational_qualification" in response

        mock_http_client._request.assert_called_once_with(
            "POST",
            f"{res_path}/schema_generator",
            json=schema_payload
        )
