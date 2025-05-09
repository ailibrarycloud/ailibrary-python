import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    if len(sys.argv) < 5:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_notes.py <content> <role> <resource> <resource_id>")
        sys.exit(1)
    content = sys.argv[1]
    role = sys.argv[2]
    resource = sys.argv[3]
    resource_id = sys.argv[4]

    args = {"content": content, "role": role, "resource": resource, "resource_id": resource_id}
    return args


def test_invalid_note_id(notes_function, note_id, **kwargs):
    function_name = notes_function.__name__
    try:
        if function_name == "delete_notes":
            resource, resource_id = kwargs.get("resource"), kwargs.get("resource_id")
            notes_function(resource=resource, resource_id=resource_id, values=[note_id], delete_all=False)
        else:
            notes_function(note_id, **kwargs)
        print(f"Verified that {function_name}() does not crash when the given note_id is not found\n")
    except:
        print(f"Failed test case: {function_name}() crashes when note_id not found\n")


def test_notes(client, args):
    notes = client.notes
    content = args.get("content", "This is a test note")
    role = args.get("role", "user")
    resource = args.get("resource", "agent")
    resource_id = args.get("resource_id", "test_agent_namespace")

    note_data = notes.add(content, role, resource, resource_id)  # Add a note
    print(f"notes.add() response:\n{note_data}\n")

    note_id = note_data["noteId"]

    resource_notes = notes.get_resource_notes(resource, resource_id)  # Get notes for a resource
    print(f"notes.get_resource_notes() response:\n{resource_notes}\n")

    update_response = notes.update(note_id, content="Updated note content", role="user")  # Update a note
    print(f"notes.update() response:\n{update_response}\n")

    note_info = notes.get(note_id)  # Get a note by ID
    print(f"notes.get() response:\n{note_info}\n")

    # delete_notes_response = notes.delete_notes(resource, resource_id, [note_id])  # Delete note
    delete_notes_response = notes.delete_notes(resource, resource_id, delete_all=True)  # Delete note
    print(f"notes.delete_notes() response:\n{delete_notes_response}\n") 


    test_invalid_note_id(notes.update, note_id, content="Updated note content", role="user")
    test_invalid_note_id(notes.get, note_id)
    # helper correctly will correctly call delete_notes with the specified note_id
    test_invalid_note_id(notes.delete_notes, note_id, resource=resource, resource_id=resource_id) 


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()
    client = _setup_tests.__setup()
    print("Running test_notes:\n")
    test_notes(client, args)
    print("Finished running test_notes\n")
