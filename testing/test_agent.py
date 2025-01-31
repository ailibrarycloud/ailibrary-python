import _setup_tests


def test_agent(client, title, update_title="Updated Agent"):
    """ Test basic functionality of agent.py """
    agent = client.agent

    agent_data = agent.create(title, description="This is a test agent.") # test create()
    print(f"agent.create() response:\n {agent_data}")

    namespace = agent_data["namespace"]

    agent_info = agent.get(namespace)  # Get information about the agent
    print(f"agent.get() response:\n {agent_info}")
    
    agents = agent.list_agents()  # List all agents
    print(f"agent.list_agents() response:\n {agents}")
    
    updated_agent = agent.update(namespace, update_title)  # Update the agent
    print(f"agent.update() response:\n {updated_agent}")

    deleted_agent = agent.delete(namespace)  # Delete the agent
    print(f"agent.delete() response:\n {deleted_agent}")

    try:
        agent.get(namespace)
    except:
        print(f"Accessing agent with namespace {namespace}: Not successful")


if __name__ == "__main__":
    client = _setup_tests.__setup()  
    print("Running test_agent:")
    title = ""
    test_agent(client, title)
    print("Finished running test_agent")
