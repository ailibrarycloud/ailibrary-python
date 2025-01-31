import ailibrary as ai
from dotenv import load_dotenv
import os


def test_agent(client):
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


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ["DEV_KEY"]

    client = ai.AILibraryClient(api_key)
    test_agent(client)

