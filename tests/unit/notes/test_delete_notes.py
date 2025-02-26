import pytest
from ailibrary._internal._notes import _Notes
from ailibrary.types.shared.enums import ResourceType
from ailibrary.types.notes.responses import NoteDeleteResponse

class TestNotesDelete:
    @pytest.mark.parametrize("delete_payload", [
        {
            "resource": ResourceType.AGENT,
            "resource_id": "test-agent",
            "values": ["note_123", "note_456"],
            "delete_all": False
        }
    ])
    def test_general(self, res_path, mock_http_client, delete_payload):
        """Test successful notes deletion"""
        notes = _Notes(mock_http_client)
        
        mock_response = {
            "status": "success",
            "message": "Notes deleted successfully"
        }
        mock_http_client._request.return_value = mock_response
        
        response = notes.delete_notes(**delete_payload)

        assert isinstance(response, dict)
        assert response["status"] == "success"
        assert "message" in response

        mock_http_client._request.assert_called_once_with(
            "DELETE",
            f"{res_path}/{delete_payload['resource']}/{delete_payload['resource_id']}",
            json=delete_payload
        )
