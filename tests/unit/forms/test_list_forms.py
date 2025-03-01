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
                    "form_id": "form_123",
                    "title": "Test Form 1",
                    "userName": "dev1",
                    "created_timestamp": "2024-03-14T12:00:00Z",
                    "updated_timestamp": "2024-03-14T12:10:00Z"
                },
                {
                    "form_id": "form_456",
                    "title": "Test Form 2",
                    "userName": "dev2",
                    "created_timestamp": "2024-03-14T12:00:00Z",
                    "updated_timestamp": "2024-03-14T12:10:00Z"
                }
            ],
            "meta": {"total_items": 2, "total_pages": 1, "current_page": 1, "limit": 10, "next_page": "", "prev_page": ""}
        }
        mock_http_client._request.return_value = mock_response
        
        response = forms.list_forms()
        assert isinstance(response, dict)
        assert isinstance(response["forms"], list)
        assert isinstance(response["meta"], dict)


        mock_http_client._request.assert_called_once_with(
            "GET",
            res_path
        )