import pytest
from ailibrary._internal._forms import _Forms
from ailibrary.types.forms.responses import FormGetResponse

class TestFormsGet:
    @pytest.mark.parametrize("form_id", ["form_123"])
    def test_general(self, res_path, mock_http_client, form_id):
        """Test successful form retrieval"""
        forms = _Forms(mock_http_client)
        
        mock_response = {
            "formId": form_id,
            "status": "active",
            "title": "Test Form",
            "description": "A test form",
            "fields": [
                {
                    "name": "email",
                    "type": "email",
                    "required": True
                }
            ],
            "created_timestamp": "2024-03-14T12:00:00Z"
        }
        mock_http_client._request.return_value = mock_response
        
        response = forms.get(form_id)

        assert isinstance(response, dict)
        assert response["formId"] == form_id
        
        for key in mock_response:
            assert key in response
            assert response[key] == mock_response[key]

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{form_id}"
        )