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


def test_notes(client, args):
    notes = client.notes
    content = args.get("content", "This is a test note")
    role = args.get("role", "user")
    resource = args.get("resource", "agent")
    resource_id = args.get("resource_id", "test_agent_namespace")

    note_data = notes.add(content, role, resource, resource_id)  # Add a note
    print(f"notes.add() response:\n{note_data}\n")

    note_id = note_data["noteId"]

    resource_notes = notes.get_for_resource(resource, resource_id)  # Get notes for a resource
    print(f"notes.get_for_resource() response:\n{resource_notes}\n")

    update_response = notes.update(note_id, "Updated note content", "user")  # Update a note
    print(f"notes.update() response:\n{update_response}\n")

    note_info = notes.get(note_id)  # Get a note by ID
    print(f"notes.get() response:\n{note_info}\n")

    delete_resource_response = notes.delete_notes(resource, resource_id)  # Delete a resource
    print(f"notes.delete_notes_in_resource() response:\n{delete_resource_response}\n")



    try:
        notes.delete_notes_in_resource(resource, resource_id)
    except:
        print(f"Verified that deleted resource with id '{resource_id}' is not found\n")

    try:
        notes.delete(note_id)
    except:
        print(f"Verified that deleted note with id '{note_id}' is not found\n")


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()
    client = _setup_tests.__setup()
    print("Running test_notes:\n")
    test_notes(client, args)
    print("Finished running test_notes\n")
