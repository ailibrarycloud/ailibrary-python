import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    if len(sys.argv) != 2:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_knowledge_base.py <name>")
        sys.exit(1)
    name = sys.argv[1]
    args = {"name": name}
    return args


def test_knowledge_base(client, args):
    knowledge_base = client.knowledge_base
    name = args.get("name", "Test_Knowledge_Base")

    kb_data = knowledge_base.create(name)  # Create a knowledge base
    print(f"knowledge_base.create() response:\n{kb_data}\n")

    knowledge_id = kb_data["knowledgeId"]

    kbs = knowledge_base.list_knowledge_bases()  # List all knowledge bases
    print(f"knowledge_base.list_knowledge_bases() response:\n{kbs}\n")

    kb_info = knowledge_base.get(knowledge_id)  # Get a knowledge base by ID
    print(f"knowledge_base.get() response:\n{kb_info}\n")
    
    data_url = "https://example-files.online-convert.com/document/txt/example.txt"
    source_data = knowledge_base.add_source(knowledge_id, urls=[data_url], meta={"folder": "home"}, type="docs")  # Add a source to the knowledge base
    print(f"knowledge_base.add_source() response:\n{source_data}\n")

    kb_status = knowledge_base.get_status(knowledge_id)  # Get the status of the knowledge base
    print(f"knowledge_base.get_status() response:\n{kb_status}\n")

    source_info = knowledge_base.get_source(knowledge_id, source_data["id"])  # Get a source by ID
    print(f"knowledge_base.get_source() response:\n{source_info}\n")

    sources = knowledge_base.list_sources(knowledge_id)  # List all sources in the knowledge base
    print(f"knowledge_base.list_sources() response:\n{sources}\n")

    delete_sources_response = knowledge_base.delete_sources(knowledge_id, values=[source_data["id"]])  # Delete sources from the knowledge base
    print(f"knowledge_base.delete_sources() response:\n{delete_sources_response}\n")

    try:
        knowledge_base.get(knowledge_id)
    except:
        print(f"Verified that deleted knowledge base with id '{knowledge_id}' is not found\n")

if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()  
    
    # run test
    print("Running test_knowledge_base:\n")
    test_knowledge_base(client, args)
    print("Finished running test_knowledge_base\n")
