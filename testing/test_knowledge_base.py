import _setup_tests


def test_knowledge_base(client):
    knowledge_base = client.knowledge_base

    kb_data = knowledge_base.create("test_kb")  # Create a knowledge base
    print(f"knowledge_base.create() response: {kb_data}")

    knowledge_id = kb_data["id"]

    kbs = knowledge_base.list_knowledge_bases()  # List all knowledge bases
    print(f"knowledge_base.list_knowledge_bases() response: {kbs}")

    kb_info = knowledge_base.get(knowledge_id)  # Get a knowledge base by ID
    print(f"knowledge_base.get() response: {kb_info}")

    source_data = knowledge_base.add_source(knowledge_id, type="docs")  # Add a source to the knowledge base
    print(f"knowledge_base.add_source() response: {source_data}")

    kb_status = knowledge_base.get_status(knowledge_id)  # Get the status of the knowledge base
    print(f"knowledge_base.get_status() response: {kb_status}")

    sources = knowledge_base.list_sources(knowledge_id)  # List all sources in the knowledge base
    print(f"knowledge_base.list_sources() response: {sources}")

    delete_sources_response = knowledge_base.delete_sources(knowledge_id, values=[source_data["id"]])  # Delete sources from the knowledge base
    print(f"knowledge_base.delete_sources() response: {delete_sources_response}")


if __name__ == "__main__":
    client = _setup_tests.__setup()
    print("Running test_knowledge_base:")
    test_knowledge_base(client)
    print("Finished running test_knowledge_base")
