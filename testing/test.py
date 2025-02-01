import _setup_tests
from test_agent import test_agent
from test_knowledge_base import test_knowledge_base
# from test_files import test_files
from test_notes import test_notes
from test_utilities import test_utilities


### This is the main test script that runs all the tests
tests = {"test_agent": test_agent, 
         "test_knowledge_base": test_knowledge_base, 
        #  "test_files": test_files,
         "test_notes": test_notes,
         "test_utilities": test_utilities}

args = {"test_agent": {}, 
        "test_knowledge_base": {}, "test_files": {}, "test_notes": {}, "test_utilities": {}}

if __name__ == "__main__":
    client = _setup_tests.__setup()    

    for test_name in tests:
        test = tests[test_name]
        try:
            print(f"Running test: {test_name}")
            test(client, args)
            print(f"Finished test: {test_name}")
        except Exception as e:
            print(f"Error in test: {test_name}\n See traceback below:")
            print(e)
