# general case
# form_id is empty
# form_id is too long
# form_id does not exist


import pytest
from ailibrary._internal._forms import _Forms
from ailibrary.types.forms.responses import FormDeleteResponse

class TestFormsDelete:
    @pytest.mark.parametrize("form_id", ["form_123"])
    def test_general(self, res_path, mock_http_client, form_id):
        """Test successful form deletion"""
        forms = _Forms(mock_http_client)
        
        mock_response = {
            "response": "success",
        }
        mock_http_client._request.return_value = mock_response
        
        response = forms.delete(form_id)

        assert isinstance(response, dict)
        assert response["response"] == "success"

        mock_http_client._request.assert_called_once_with(
            "DELETE",
            f"{res_path}/{form_id}"
        )
