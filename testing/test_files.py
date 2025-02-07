import _setup_tests
import sys
from typing import List, Tuple, BinaryIO
import ast

def get_args():
    """ Get arguments from command line """
    num_args = len(sys.argv)

    if num_args < 2:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_files.py <path_to_file_1> ...")
        sys.exit(1)

    file_paths = []
    for i in range(1, num_args):
        file_paths.append(sys.argv[i])
    args = {"files": file_paths}
    return args


def test_files(client, args):
    files = client.files
    file_paths = args.get("files", ["testing/test_file.txt"])

    upload_response = files.upload(file_paths)  # Upload a file
    print(f"files.upload() response:\n{upload_response}\n")

    file_id = upload_response[0]["id"]

    all_files = files.list_files()  # List all files
    print(f"files.list_files() response:\n{all_files}\n")

    file_info = files.get(file_id)  # Get a file by ID
    print(f"files.get() response:\n{file_info}\n")

    delete_response = files.delete(file_id)  # Delete a file
    print(f"files.delete() response:\n{delete_response}\n")

    try:
        files.delete(file_id)
        print(f"Verified that delete() doesnt crash when the file_id is not found\n")        
    except:
        print(f"Failed test case: delete() doesnt work when file_id not found\n")


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()  

    # run test
    print("Running test_files:\n")
    test_files(client, args)
    print("Finished running test_files\n")
