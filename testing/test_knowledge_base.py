import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    num_args = len(sys.argv)

    if num_args < 2:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_knowledge_base.py <path_to_file_1> ...")
        sys.exit(1)

    file_paths = []
    for i in range(1, num_args):
        file_paths.append(sys.argv[i])
    args = {"name": name}
    return args


def test_knowledge_base(client, args):
    knowledge_base = client.knowledge_base
    name = args.get("name", "Test_Knowledge_Base")

    kb_data = knowledge_base.create(name)  # Create a knowledge base
    print(f"knowledge_base.create() response:{kb_data}\n")

    knowledge_id = kb_data["knowledgeId"]

    kbs = knowledge_base.list_knowledge_bases()  # List all knowledge bases
    print(f"knowledge_base.list_knowledge_bases() response:{kbs}\n")

    kb_info = knowledge_base.get(knowledge_id)  # Get a knowledge base by ID
    print(f"knowledge_base.get() response:{kb_info}\n")

    # source_data = knowledge_base.add_source(knowledge_id, type="docs")  # Add a source to the knowledge base
    # print(f"knowledge_base.add_source() response:{source_data}\n")

    kb_status = knowledge_base.get_status(knowledge_id)  # Get the status of the knowledge base
    print(f"knowledge_base.get_status() response:{kb_status}\n")

    # sources = knowledge_base.list_sources(knowledge_id)  # List all sources in the knowledge base
    # print(f"knowledge_base.list_sources() response:{sources}\n")

    # delete_sources_response = knowledge_base.delete_sources(knowledge_id, values=[source_data["id"]])  # Delete sources from the knowledge base
    # print(f"knowledge_base.delete_sources() response:{delete_sources_response}\n")


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()  
    
    # run test
    print("Running test_knowledge_base:\n")
    test_knowledge_base(client, args)
    print("Finished running test_knowledge_base\n")
