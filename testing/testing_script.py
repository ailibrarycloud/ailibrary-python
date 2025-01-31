import ailibrary as ai
from dotenv import load_dotenv
import os


def test_agent(client):
    """ Test basic functionality of agent.py """
    agent = client.agent

    title = "test_agent_kushagra_1"  # Create an agent
    agent_data = agent.create(title, description="This is a test agent.")

    print(f"agent.create() response: {agent_data}")
    
    namespace = agent_data["namespace"]

    agent_info = agent.get(namespace)  # Get information about the agent
    print(f"agent.get() response: {agent_info}")
    
    agents = agent.list_agents()  # List all agents
    print(f"agent.list_agents() response: {agents}")
    
    updated_agent = agent.update(namespace, title="Updated Agent")  # Update the agent
    print(f"agent.update() response: {updated_agent}")

    deleted_agent = agent.delete(namespace)  # Delete the agent
    print(f"agent.delete() response: {deleted_agent}")

    try:
        agent.get(namespace)
    except:
        print(f"Accessing agent with namespace {namespace}: Not successful")


def test_knowledge_base(client):
    knowledge_base = client.knowledge_base
    name = "test_kb"

    kb_data = knowledge_base.create(name)  # Create a knowledge base
    print(f"knowledge_base.create() response: {kb_data}")

    k_id = kb_data["knowledgeId"]

    kbs = knowledge_base.list_knowledge_bases()  # List all knowledge bases
    print(f"knowledge_base.list_knowledge_bases() response: {kbs}")

    kb_info = knowledge_base.get(k_id)  # Get a knowledge base by ID
    print(f"knowledge_base.get() response: {kb_info}")

    source_data = knowledge_base.add_source(k_id, type="docs")  # Add a source to the knowledge base
    print(f"knowledge_base.add_source() response: {source_data}")

    kb_status = knowledge_base.get_status(k_id)  # Get the status of the knowledge base
    print(f"knowledge_base.get_status() response: {kb_status}")

    sources = knowledge_base.list_sources(k_id)  # List all sources in the knowledge base
    print(f"knowledge_base.list_sources() response: {sources}")

    delete_sources_response = knowledge_base.delete_sources(k_id, values=[source_data["id"]])  # Delete sources from the knowledge base
    print(f"knowledge_base.delete_sources() response: {delete_sources_response}")


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


def test_utilities(client):
    utilities = client.utilities

    search_response = utilities.web_search(["AI", "Library"])  # Perform a web search
    print(f"utilities.web_search() response: {search_response}")

    parser_response = utilities.web_parser(["https://example.com"])  # Parse web pages
    print(f"utilities.web_parser() response: {parser_response}")


def test_notes(client):
    notes = client.notes

    note_data = notes.add("This is a test note", "user", "agent", "test_namespace")  # Add a note
    print(f"notes.add() response: {note_data}")

    note_id = note_data["id"]

    resource_notes = notes.get_for_resource("agent", "test_namespace")  # Get notes for a resource
    print(f"notes.get_for_resource() response: {resource_notes}")

    update_response = notes.update(note_id, "Updated note content", "user")  # Update a note
    print(f"notes.update() response: {update_response}")

    note_info = notes.get(note_id)  # Get a note by ID
    print(f"notes.get() response: {note_info}")

    delete_response = notes.delete(note_id)  # Delete a note
    print(f"notes.delete() response: {delete_response}")


if __name__ == "__main__":
    # api_key = "Please let me in"
    load_dotenv()
    api_key = os.environ["DEV_KEY"]

    client = ai.AILibraryClient(api_key)
    tests = [test_agent, test_knowledge_base, test_files, test_utilities, test_notes]
    for test in tests:
        test_name = test.__name__
        try:
            test(client)
            print(f"Finished test: {test_name}")
        except Exception as e:
            print(f"Error in test: {test_name}\n See traceback below:")
            print(e)
