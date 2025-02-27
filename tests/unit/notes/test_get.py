# general test
# note_id that exists
# note_id that doesn't exist
# negative note_id?
# note_id is a string?

import pytest
from ailibrary._internal._notes import _Notes
from ailibrary.types.shared.enums import ResourceType, RoleType
from ailibrary.types.notes.responses import NoteGetResponse

class TestNotesGet:
    @pytest.mark.parametrize("note_id", ["note_123"])
    def test_general(self, res_path, mock_http_client, note_id):
        """Test successful note retrieval"""
        notes = _Notes(mock_http_client)
        
        mock_response = {
            "noteId": note_id,
            "content": "Test note",
            "role": RoleType.USER,
            "resource": ResourceType.AGENT,
            "resourceId": "test-agent",
            "meta": {"category": "test"},
            "created_timestamp": "2024-03-14T12:00:00Z",
            "updated_timestamp": "2024-03-14T12:00:00Z",
            "userEmail": "test@example.com",
            "userName": "Test User"
        }
        mock_http_client._request.return_value = mock_response
        
        response = notes.get(note_id)

        assert isinstance(response, dict)
        assert response["noteId"] == note_id
        
        for key in mock_response:
            assert key in response
            assert response[key] == mock_response[key]

        mock_http_client._request.assert_called_once_with(
            "GET",
            f"{res_path}/{note_id}"
        )
