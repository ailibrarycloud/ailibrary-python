import _setup_tests


def test_notes(client):
    notes = client.notes

    note_data = notes.add("This is a test note", "user", "agent", "test_namespace")  # Add a note
    print(f"notes.add() response: {note_data}")

    note_id = note_data["id"]

    resource_notes = notes.get_for_resource("agent", "test_namespace")  # Get notes for a resource
    print(f"notes.get_for_resource() response: {resource_notes}")

    update_response = notes.update(note_id, "Updated note content", "user")  # Update a note
    print(f"notes.update() response: {update_response}")

    note_info = notes.get(note_id)  # Get a note by ID
    print(f"notes.get() response: {note_info}")

    delete_response = notes.delete(note_id)  # Delete a note
    print(f"notes.delete() response: {delete_response}")


if __name__ == "__main__":
    client = _setup_tests.__setup()
    print("Running test_notes:")
    test_notes(client)
    print("Finished running test_notes")
