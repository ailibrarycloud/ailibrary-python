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

    # agent_data = agent.create(title, description="This is a test agent.")  # test create()
    agent_data = agent.create(title, description="This is a test agent.", knowledge_id="testkbkush_1738821332107373")  # test create()
    print(f"agent.create() response:\n{agent_data}\n")

    namespace = agent_data["namespace"]

    agent_info = agent.get(namespace)  # Get information about the agent
    print(f"agent.get() response:\n{agent_info}\n")

    agents = agent.list_agents()  # List all agents
    print(f"agent.list_agents() response:\n{agents}\n")

    updated_agent = agent.update(namespace, update_title)  # Update the agent
    print(f"agent.update() response:\n{updated_agent}\n")

    # #### ERROR: the response is not valid JSON
    # chat_response = agent.chat(namespace, [{"role": "user", "content": "Hello there! Who are you?"}])  # Chat with the agent
    # print(f"agent.chat() response:\n{chat_response}\n")

    # print("Testing agent.chat():\n")
    # test_agent_chat(client, {})

    deleted_agent = agent.delete(namespace)  # Delete the agent
    print(f"agent.delete() response:\n{deleted_agent}\n")

    try:
        agent.get(namespace)
        print(f"Verified that delete() doesnt crash when the given namespace is not found\n")
    except:
        # print(f"Verified that deleted agent with name '{namespace}' is not found\n")
        print(f"Failed test case: delete() doesnt work when namespace not found\n")


async def test_agent_chat(client, args):
    response = await client.agent.chat(
        "gricare_demo", [{"role": "user", "content": "Hello there! Who are you?"}])
    async def text_iterator():
        async for chunk in response:
            print(chunk)
    await text_iterator()
                  


if __name__ == "__main__":
    # get arguments from command line
    args = get_args()

    # set up client
    client = _setup_tests.__setup()

    # run test
    print("Running test_agent:\n")
    print(client.agent.delete("test_agent_kushagra-20250207012326"))
    # test_agent(client, args)
    # test_agent_chat(client, args)
    print("Finished running test_agent\n")
