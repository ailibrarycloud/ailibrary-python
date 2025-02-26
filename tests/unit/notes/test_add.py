import pytest
from ailibrary._internal._notes import _Notes
from ailibrary.types.shared.enums import ResourceType, RoleType
from ailibrary.types.notes.responses import NoteAddResponse

class TestNotesAdd:
    @pytest.mark.parametrize("add_payload", [
        {
            "content": "Test note content",
            "role": RoleType.USER,
            "resource": ResourceType.AGENT,
            "resource_id": "test-agent",
            "meta": {"category": "test"}
        }
    ])
    def test_general(self, res_path, mock_http_client, add_payload):
        """Test successful note addition"""
        notes = _Notes(mock_http_client)
        
        mock_response = {
            "status": "success",
            "noteId": "note_123"
        }
        mock_http_client._request.return_value = mock_response
        
        response = notes.add(**add_payload)

        assert isinstance(response, dict)
        assert response["status"] == "success"
        assert "noteId" in response

        mock_http_client._request.assert_called_once_with(
            "POST",
            res_path,
            json=add_payload
        )
