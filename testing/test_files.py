import _setup_tests


def test_files(client):
    files = client.files

    with open("test_file.txt", "rb") as f:
        upload_response = files.upload([f])  # Upload a file
    print(f"files.upload() response: {upload_response}")

    file_id = upload_response[0]["id"]

    all_files = files.list_files()  # List all files
    print(f"files.list_files() response: {all_files}")

    file_info = files.get(file_id)  # Get a file by ID
    print(f"files.get() response: {file_info}")

    delete_response = files.delete(file_id)  # Delete a file
    print(f"files.delete() response: {delete_response}")


if __name__ == "__main__":
    client = _setup_tests.__setup()
    print("Running test_files:")
    test_files(client)
    print("Finished running test_files")
