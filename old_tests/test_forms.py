import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    if len(sys.argv) != 3:
        print("Error: provide correct amount of arguments \n" +
              "Usage: python test_forms.py <title> <update_title>")
        sys.exit(1)
    title = sys.argv[1]
    update_title = sys.argv[2]
    args = {"title": title, "update_title": update_title}
    return args


def test_forms(client, args):
    """ Test basic functionality of form.py 
    Args: title, update_title
    """
    forms = client.forms
    title = args.get("title", "Test_Forms")
    update_title = args.get("update_title", "Updated_Form")
    schema = {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "years_of_experience": {"type": "number"},
        "years_experience_with_nextjs": {"type": "number"},
        "AI_experience": {"type": "boolean"}
    }

    create_response = forms.create(title, schema)  # test create()
    print(f"form.create() response:\n{create_response}\n")

    # namespace = form_data["namespace"]
    # form_info = form.get(namespace)  # Get information about the form
    # print(f"form.get() response:\n{form_info}\n")

    # forms = form.list_forms()  # List all forms
    # print(f"form.list_forms() response:\n{forms}\n")

    # updated_form = form.update(namespace, title=update_title)  # Update the form
    # print(f"form.update() response:\n{updated_form}\n")


    # deleted_form = form.delete(namespace, True)  # Delete the form
    # print(f"form.delete() response:\n{deleted_form}\n")


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()
    # set up client
    client = _setup_tests.__setup()
    # run test
    print("Running test_forms:\n")
    test_forms(client, args)
    print("Finished running test_forms\n")
