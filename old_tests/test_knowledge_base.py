import _setup_tests
import sys
import time

def get_args():
    """ Get arguments from command line """
    if len(sys.argv) != 2:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_knowledge_base.py <name>")
        sys.exit(1)
    name = sys.argv[1]
    args = {"name": name}
    return args


def test_invalid_knowledgeId(kb_function, knowledgeId, **kwargs):
    function_name = kb_function.__name__
    try:
        kb_function(knowledgeId, **kwargs)
        print(f"Verified that {function_name}() does not crash when the given knowledgeId is not found\n")
    except:
        print(f"Failed test case: {function_name}() crashes when knowledgeId not found\n")


def test_knowledge_base(client, args):
    knowledge_base = client.knowledge_base
    name = args.get("name", "Test_Knowledge_Base")

    kb_data = knowledge_base.create(name)  # Create a knowledge base
    print(f"knowledge_base.create() response:\n{kb_data}\n")

    knowledgeId = kb_data["knowledgeId"]

    kbs = knowledge_base.list_knowledge_bases()  # List all knowledge bases
    print(f"knowledge_base.list_knowledge_bases() response:\n{kbs}\n")

    kb_info = knowledge_base.get(knowledgeId)  # Get a knowledge base by ID
    print(f"knowledge_base.get() response:\n{kb_info}\n")
    
    kb_status = knowledge_base.get_status(knowledgeId)  # Get the status of the knowledge base
    print(f"knowledge_base.get_status() response:\n{kb_status}\n")
    

    # MAJOR BUGS / UNFINISHED
    urls = ["https://example-files.online-convert.com/document/txt/example.txt"]
    options = {"urls": urls}
    source_data = knowledge_base.add_source(knowledgeId, type="docs", options=options)  # Add a source to the knowledge base
    print(f"knowledge_base.add_source() response:\n{source_data}\n")

    sources = knowledge_base.list_sources(knowledgeId)  # List all sources in the knowledge base
    print(f"knowledge_base.list_sources() response:\n{sources}\n")

    source_name = sources[0]["source"]
    time.sleep(5)
    source_info = knowledge_base.get_source(knowledgeId, source_name)
    print(f"knowledge_base.get_source() response:\n{source_info}\n")

    delete_sources_response = knowledge_base.delete_sources(knowledgeId, values=[source_name])  # Delete sources from the knowledge base
    print(f"knowledge_base.delete_sources() response:\n{delete_sources_response}\n")


    kb_delete_response = knowledge_base.delete(knowledgeId)  # delete knowledge base
    print(f"knowledge_base.delete() response:\n{kb_delete_response}\n")

    test_invalid_knowledgeId(knowledge_base.get, knowledgeId)
    test_invalid_knowledgeId(knowledge_base.delete, knowledgeId)


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()  
    
    # run test
    print("Running test_knowledge_base:\n")
    test_knowledge_base(client, args)
    print("Finished running test_knowledge_base\n")
