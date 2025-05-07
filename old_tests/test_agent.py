import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    if len(sys.argv) != 3:
        print("Error: provide correct amount of arguments \n" +
              "Usage: python test_agent.py <title> <update_title>")
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

    agent_data = agent.create(title, instructions="This is a test agent.")  # test create()
    print(f"agent.create() response:\n{agent_data}\n")

    namespace = agent_data["namespace"]
    agent_info = agent.get(namespace)  # Get information about the agent
    print(f"agent.get() response:\n{agent_info}\n")

    agents = agent.list_agents()  # List all agents
    print(f"agent.list_agents() response:\n{agents}\n")

    updated_agent = agent.update(namespace, title=update_title)  # Update the agent
    print(f"agent.update() response:\n{updated_agent}\n")
    ### Bug
    # print(f"agent.update() response with invalid agent name:\n{agent.update('invalid_agent_name', title=update_title)}\n")

    # # # #### ERROR: the response is not valid JSON
    # # print("Testing agent.chat():\n")
    # # test_agent_chat(agent, namespace)

    deleted_agent = agent.delete(namespace, True)  # Delete the agent
    print(f"agent.delete() response:\n{deleted_agent}\n")

    try:
        agent.get(namespace)
        print(f"Verified that get() does not crash when the given namespace is not found\n")
    except:
        print(f"Failed test case: get() crashes when namespace not found\n")
    
    try:
        agent.delete(namespace, True)
        print(f"Verified that delete() doesnt crash when the given namespace is not found\n")
    except:
        print(f"Failed test case: delete() doesnt work when namespace not found\n")


def test_agent_chat(agent, namespace):
    messages = [{"role": "user", "content": "Hello there! Who are you?"}]
    try:
        print("Starting chat test...")
        full_response = ""
        for chunk in agent.chat(namespace, messages):
            try:
                print(f"Raw chunk: {chunk}")
                full_response += chunk
            except Exception as e:
                print(f"Error processing chunk: {str(e)}")
        print(f"\nFull response: {full_response}")
    except Exception as e:
        print(f"Chat error: {str(e)}")



if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()

    # run test
    print("Running test_agent:\n")
    test_agent(client, args)
    # test_agent_chat(client.agent, "gricare_demo")
    print("Finished running test_agent\n")
