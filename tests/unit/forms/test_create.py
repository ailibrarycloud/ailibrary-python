# general case
# title is empty
# title is too long
# schema is empty


import pytest
from ailibrary._internal._forms import _Forms
from ailibrary.types.forms.responses import FormCreateResponse

class TestFormsCreate:
    @pytest.mark.parametrize("create_payload", [
        {
            "title": "Test Form",
            "schema": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "years_of_experience": {"type": "number"},
                "years_experience_with_nextjs": {"type": "number"},
                "AI_experience": {"type": "boolean"}
            }

        }
    ])
    def test_general(self, res_path, mock_http_client, create_payload):
        """Test successful form creation"""
        forms = _Forms(mock_http_client)

        mock_response = {
            "form_id": "form_123",
            "title": create_payload["title"],
            "schema": create_payload["schema"]
        }
        mock_http_client._request.return_value = mock_response

        response = forms.create(**create_payload)

        assert isinstance(response, dict)
        assert "form_id" in response
        assert "schema" in response
        assert response["title"] == create_payload["title"]

        mock_http_client._request.assert_called_once_with(
            "POST",
            res_path,
            json=create_payload
        )
