import pytest
from ailibrary._internal._forms import _Forms
from ailibrary.types.forms.responses import FormListResponse

class TestFormsList:
    def test_general(self, res_path, mock_http_client):
        """Test successful form listing"""
        forms = _Forms(mock_http_client)
        
        mock_response = {
            "forms": [
                {
                    "formId": "form_123",
                    "title": "Test Form 1",
                    "status": "active",
                    "created_timestamp": "2024-03-14T12:00:00Z"
                },
                {
                    "formId": "form_456",
                    "title": "Test Form 2",
                    "status": "active",
                    "created_timestamp": "2024-03-14T12:00:00Z"
                }
            ],
            "meta": {"total": 2}
        }
        mock_http_client._request.return_value = mock_response
        
        response = forms.list_forms()

        assert isinstance(response, dict)
        assert "forms" in response
        assert isinstance(response["forms"], list)
        assert "meta" in response
        
        for form in response["forms"]:
            assert "formId" in form
            assert "title" in form
            assert "status" in form

        mock_http_client._request.assert_called_once_with(
            "GET",
            res_path
        )