# general test (without meta)
# note_id that exists
# note_id that doesn't exist
# negative note_id?
# note_id is a string?
# empty content
# invalid role
# each type of valid role

# with meta (json-friendly string)
# with meta (non-json-friendly string)
import pytest
from ailibrary._internal._notes import _Notes
from ailibrary.types.shared.enums import RoleType
from ailibrary.types.notes.responses import NoteUpdateResponse

class TestNotesUpdate:
    @pytest.mark.parametrize("update_payload", [
        {
            "note_id": "note_123",
            "content": "Updated note content",
            "role": RoleType.USER,
            "meta": {"category": "updated"}
        }
    ])
    def test_general(self, res_path, mock_http_client, update_payload):
        """Test successful note update"""
        notes = _Notes(mock_http_client)
        
        mock_response = {
            "status": "success",
            "message": "Note updated successfully",
            "meta": {"updated": True}
        }
        mock_http_client._request.return_value = mock_response
        
        note_id = update_payload.pop("note_id")
        response = notes.update(note_id, **update_payload)

        assert isinstance(response, dict)
        assert response["status"] == "success"
        assert "message" in response
        assert "meta" in response

        mock_http_client._request.assert_called_once_with(
            "PUT",
            f"{res_path}/{note_id}",
            json=update_payload
        )
