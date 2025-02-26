import pytest
from ailibrary._internal._notes import _Notes
from ailibrary.types.shared.enums import ResourceType, RoleType
from ailibrary.types.notes.responses import NoteGetResourceNotesResponse

class TestNotesGetResourceNotes:
    @pytest.mark.parametrize("get_params", [
        {
            "resource": ResourceType.AGENT,
            "resource_id": "test-agent"
        }
    ])
    def test_general(self, res_path, mock_http_client, get_params):
        """Test successful resource notes retrieval"""
        notes = _Notes(mock_http_client)
        
        mock_response = {
            "notes": [
                {
                    "content": "Test note 1",
                    "role": RoleType.USER,
                    "meta": {"category": "test"},
                    "created_timestamp": "2024-03-14T12:00:00Z"
                }
            ],
            "meta": {"total": 1}
        }
        mock_http_client._request.return_value = mock_response
        
        response = notes.get_resource_notes(**get_params)

        assert isinstance(response, dict)
        assert "notes" in response
        assert isinstance(response["notes"], list)
        assert "meta" in response

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{get_params['resource']}/{get_params['resource_id']}"
        )
