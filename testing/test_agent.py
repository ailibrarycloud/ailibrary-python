import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    if len(sys.argv) != 3:
        print("Error: provide correct amount of arguments \n" + "Usage: python test_agent.py <title> <update_title>")
        sys.exit(1)
    title = sys.argv[1]
    update_title = sys.argv[2]    
    args = {"title": title, "update_title": update_title}
    return args


def test_agent(client, args):
    """ Test basic functionality of agent.py 
    Args: title, update_title
    """
    agent = client.agent
    title = args.get("title", "Test_Agent")
    update_title = args.get("update_title", "Updated_Agent")

    agent_data = agent.create(title, description="This is a test agent.") # test create()
    print(f"agent.create() response:\n{agent_data}\n")

    namespace = agent_data["namespace"]

    agent_info = agent.get(namespace)  # Get information about the agent
    print(f"agent.get() response:\n{agent_info}\n")
    
    # agents = agent.list_agents()  # List all agents
    # print(f"agent.list_agents() response:\n{agents}\n")
    
    # updated_agent = agent.update(namespace, update_title)  # Update the agent
    # print(f"agent.update() response:\n{updated_agent}\n")

    # deleted_agent = agent.delete(namespace)  # Delete the agent
    # print(f"agent.delete() response:\n{deleted_agent}\n")

    # try:
    #     agent.get(namespace)
    # except:
    #     print(f"Verified that deleted agent with name '{namespace}' is not found\n")


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()  
    
    # run test
    print("Running test_agent:\n")
    test_agent(client, args)
    print("Finished running test_agent\n")
