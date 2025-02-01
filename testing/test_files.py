import _setup_tests
import sys
from fastapi import UploadFile
from typing import List

def get_args():
    """ Get arguments from command line """
    num_args = len(sys.argv)

    if num_args < 2:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_knowledge_base.py <path_to_file_1> ...")
        sys.exit(1)

    file_paths = []
    for i in range(1, num_args):
        file_paths.append(sys.argv[i])
    args = {"files": file_paths}
    return args


def create_file_list(file_paths: str) -> List[UploadFile]:
    """ Create a list of UploadFiles """
    files = [
        ('files', (file_path.split("/")[-1], open(file_path, 'rb'), 'application/octet-stream'))
        for file_path in file_paths
    ]
    return files


def test_files(client, args):
    files = client.files
    file_paths = args.get("files", ["test_file.txt"])
    upload_file_list = create_file_list(file_paths)

    upload_response = files.upload(upload_file_list)  # Upload a file
    print(f"files.upload() response: {upload_response}")

    file_id = upload_response[0]["id"]

    all_files = files.list_files()  # List all files
    print(f"files.list_files() response: {all_files}")

    file_info = files.get(file_id)  # Get a file by ID
    print(f"files.get() response: {file_info}")

    delete_response = files.delete(file_id)  # Delete a file
    print(f"files.delete() response: {delete_response}")


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()  

    # run test
    print("Running test_files:\n")
    test_files(client)
    print("Finished running test_files\n")
