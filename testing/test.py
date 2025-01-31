import _setup_tests
import test_agent, test_files, test_notes, test_utilities, test_knowledge_base

### This is the main test script that runs all the tests

if __name__ == "__main__":
    client = _setup_tests.__setup()    
    test_functions = [test_agent.test_agent, test_files.test_files, test_notes.test_notes, test_utilities.test_utilities, test_knowledge_base.test_knowledge_base]

    for test in test_functions:
        test_name = test.__name__
        try:
            print(f"Running test: {test_name}")
            test(client)
            print(f"Finished test: {test_name}")
        except Exception as e:
            print(f"Error in test: {test_name}\n See traceback below:")
            print(e)
