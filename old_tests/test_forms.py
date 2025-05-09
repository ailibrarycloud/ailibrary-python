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


def test_invalid_form_id(forms_function, form_id, **kwargs):
    function_name = forms_function.__name__
    try:
        forms_function(form_id, **kwargs)
        print(f"Verified that {function_name}() does not crash when the given form_id is not found\n")
    except:
        print(f"Failed test case: {function_name}() crashes when form_id not found\n")


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

    form_id = create_response["form_id"]
    form_info = forms.get(form_id)  # Get information about the form
    print(f"form.get() response:\n{form_info}\n")

    forms_list = forms.list_forms()  # List all forms
    print(f"form.list_forms() response:\n{forms_list}\n")

    updated_form = forms.update(form_id, title=update_title)  # Update the form
    print(f"form.update() response:\n{updated_form}\n")

    deleted_form = forms.delete(form_id)  # Delete the form
    print(f"form.delete() response:\n{deleted_form}\n")

    test_invalid_form_id(forms.update, form_id, title=update_title)
    test_invalid_form_id(forms.get, form_id)
    test_invalid_form_id(forms.delete, form_id)


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()
    # set up client
    client = _setup_tests.__setup()
    # run test
    print("Running test_forms:\n")
    test_forms(client, args)
    print("Finished running test_forms\n")
