# general case
# form_id is empty
# form_id is too long
# form_id does not exist

import pytest
from ailibrary._internal._forms import _Forms

class TestFormsGet:
    @pytest.mark.parametrize("form_id", ["form_123"])
    def test_general(self, res_path, mock_http_client, form_id):
        """Test successful form retrieval"""
        forms = _Forms(mock_http_client)
        
        mock_response = {
            "form_id": form_id,
            "title": "Test Form",
            "schema": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "years_of_experience": {"type": "number"},
                "years_experience_with_nextjs": {"type": "number"},
                "AI_experience": {"type": "boolean"}
            }
        }
        mock_http_client._request.return_value = mock_response
        response = forms.get(form_id)

        assert isinstance(response, dict)
        assert response["form_id"] == form_id
        assert "schema" in response
        assert "title" in response

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{form_id}"
        )