import _setup_tests
import sys


def get_args():
    """ Get arguments from command line """
    if len(sys.argv) != 4:
        print("Error: provide correct amount of arguments \n" +
              "Usage: python test_agent.py <title> <update_title> <chat_agent_title>")
        sys.exit(1)
    title = sys.argv[1]
    update_title = sys.argv[2]
    chat_agent_title = sys.argv[3]
    args = {"title": title, "update_title": update_title, "chat_agent_title": chat_agent_title}
    return args


def test_invalid_namespace(agent_function, namespace, **kwargs):
    function_name = agent_function.__name__
    try:
        agent_function(namespace, **kwargs)
        print(f"Verified that {function_name}() does not crash when the given namespace is not found\n")
    except:
        print(f"Failed test case: {function_name}() crashes when namespace not found\n")


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
    
    deleted_agent = agent.delete(namespace, True)  # Delete the agent
    print(f"agent.delete() response:\n{deleted_agent}\n")

    test_invalid_namespace(agent.update, namespace, title=update_title)
    test_invalid_namespace(agent.get, namespace)
    test_invalid_namespace(agent.delete, namespace)


def test_agent_chat(client):
    # messages = [{"role": "user", "content": "Hello there! Who are you?"}]
    # try:
    #     print("Starting chat test...")
    #     full_response = ""
    #     for chunk in agent.chat(namespace, messages):
    #         try:
    #             print(f"Raw chunk: {chunk}")
    #             full_response += chunk
    #         except Exception as e:
    #             print(f"Error processing chunk: {str(e)}")
    #     print(f"\nFull response: {full_response}")
    # except Exception as e:
    #     print(f"Chat error: {str(e)}")

    # ============================
    agent = client.agent
    chat_agent_title = args.get("chat_agent_title", "Test_Chat_Agent")

    print("Here is how we will test agent.chat():\n \
          First, we generate a schema using client.utilities.json_schema_generator()\n \
          then we use that schema to generate a form using client.form.create()\n \
          Then we create a chat agent and specify the form id\n \
          And then we finally call agent.chat().\n")
    
    print("Calling client.utilities.json_schema_generator()...\n")
    instructions = "Please generate a form with the following fields: \n name (string), email(string), phone(number), experience in years (number), ai experience in years (number), highest educational qualification (phd, bachelor's degree, high school, not mentioned)"
    schema = client.utilities.json_schema_generator(content=instructions)

    print(f"Here is the schema:\n{schema}\n\n\n Now calling client.forms.create():\n")
    form = client.forms.create(title="my agent form", schema=schema)
    form_id = form["form_id"]

    print(f"The form id is: {form_id}\nNow we will create a chat agent with this form attached.\n")
    agent_data = agent.create(chat_agent_title, instructions="This is a chat agent.")
    namespace = agent_data["namespace"]
    agent.update(namespace=namespace, type="voice", form_id=form_id)

    messages = [
        {
            "role": "user",
            "content": "My name is John Doe. Who are you?"
        }
    ]
    print(f"The namespace of the new chat agent is: {namespace}\n Here are the messages we will use:\n{messages}\n")

    format = "json"
    print(f"Calling client.agent.chat() using agent {namespace} (arguments passed are the messages above and response_format '{format}'):\n")
    response = agent.chat(namespace=namespace, messages=messages, response_format=format)
    print(f"client.agent.chat() response:\n\n{response}\n\n")


if __name__ == "__main__":
    args = get_args() # get arguments from command line
    client = _setup_tests.__setup() # set up client
    # run test
    print("Running test_agent (except for agent.chat()):\n")
    test_agent(client, args)
    # print("Finished running test_agent.\nNow running test_agent_chat\n")
    # test_agent_chat(client)
    print("Finished running all agent tests.\n")
