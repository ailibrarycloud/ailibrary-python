import pytest
from ailibrary._internal._forms import _Forms
from ailibrary.types.forms.responses import FormUpdateResponse

class TestFormsUpdate:
    @pytest.mark.parametrize("update_payload", [
        {
            "form_id": "form_123",
            "title": "Updated Test Form",
            "schema": {
                "fields": [
                    {
                        "name": "email",
                        "type": "email",
                        "required": True
                    }
                ]
            }
        }
    ])
    def test_general(self, res_path, mock_http_client, update_payload):
        """Test successful form update"""
        forms = _Forms(mock_http_client)
        
        mock_response = {
            "form_id": update_payload["form_id"],
            "title": update_payload["title"],
            "schema": update_payload["schema"]
        }
        mock_http_client._request.return_value = mock_response
        
        form_id = update_payload.pop("form_id")
        response = forms.update(form_id, **update_payload)

        assert isinstance(response, dict)
        assert "form_id" in response
        assert "title" in response
        assert "schema" in response

        mock_http_client._request.assert_called_once_with(
            "PUT",
            f"{res_path}/{form_id}",
            json=update_payload
        )