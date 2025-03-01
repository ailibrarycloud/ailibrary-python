# general test
# empty content
# content has one char (what should be the min length?)
# content only comprised of whitespace characters
# content max length (for database)?
# special characters? Unicode characters only?
# what if I don't even ask to generate a schema? what if i just 
#        ask to manually edit database with erroneous values? 
# what if the content string is completely nonsensical?
#      - content string is fully made of digits
#      - real worlds in a completely jibberish order
#      - literal jibberish


import pytest
from ailibrary._internal._utilities import _Utilities


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
