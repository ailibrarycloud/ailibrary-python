import _setup_tests

def test_agent_kb(client):
    """ 
    Test that if kb is added to an agent, then agent.get() will include that knowledgeId (for both create and update)
    Test this when:
        - knowledge_search not specified
        - knowledge_search == False
        - knowledge_search == True 
    """

    def _create_agent_with_kb(client, agent_title, kb_id, kb_search):
        if kb_search is None:
            response = client.agent.create(title=agent_title, knowledgeId=kb_id)
        else:
            response = client.agent.create(title=agent_title, knowledgeId=kb_id, knowledge_search=kb_search)
        agent_namespace = response["namespace"]
        agent_info = client.agent.get(agent_namespace)
        client.agent.delete(namespace=agent_namespace, delete_connected_resources=False)
        return agent_info

    def _create_agent_update_with_kb(client, agent_title, kb_id, kb_search):
        response = client.agent.create(title=agent_title)
        agent_namespace = response["namespace"]
        if kb_search is None:
            client.agent.update(namespace=agent_namespace, knowledgeId=kb_id)
        else:
            client.agent.update(namespace=agent_namespace, knowledgeId=kb_id, knowledge_search=kb_search)
        agent_info = client.agent.get(agent_namespace)
        client.agent.delete(namespace=agent_namespace, delete_connected_resources=False)
        return agent_info

    def _get_result(info, kb_id):
        return "knowledgeId" in info and info["knowledgeId"] == knowledgeId

    kb_response = client.knowledge_base.create("kb_test")
    knowledgeId = kb_response["knowledgeId"]
    
    i = 1
    print("Running test_agent_kb:")
    for knowledge_search in [None, False, True]:
        a_info = _create_agent_with_kb(client, "test_agent", knowledgeId, knowledge_search)
        print(f"Case {i}: Initialize agent with kb, knowledge_search={knowledge_search}")
        print(f"knowledgeId found in response of agent.get() ?\n{_get_result(a_info, knowledgeId)}")
        i += 1
        
        b_info = _create_agent_update_with_kb(client, "test_agent", knowledgeId, knowledge_search)
        print(f"Case {i}: Update agent with kb, knowledge_search={knowledge_search}")
        print(f"knowledgeId found in response of agent.get() ?\n{_get_result(b_info, knowledgeId)}")
        i += 1
    
    client.knowledge_base.delete(knowledgeId)
    print("Finished running test_agent_kb:\n")


def test_agent_forms(client):
    """ 
    Test that if form is added to an agent, then agent.get() will include that form_id (for both create and update)
    Test this when:
        - form_filling not specified
        - form_filling == False
        - form_filling == True 
    """
    def _create_agent_with_form(client, agent_title, f_id, filling):
        if filling is None:
            response = client.agent.create(title=agent_title, form_id=f_id)
        else:
            response = client.agent.create(title=agent_title, form_id=f_id, form_filling=filling)
        agent_namespace = response["namespace"]
        agent_info = client.agent.get(agent_namespace)
        client.agent.delete(namespace=agent_namespace, delete_connected_resources=False)
        return agent_info

    def _create_agent_update_with_form(client, agent_title, f_id, filling):
        response = client.agent.create(title=agent_title)
        agent_namespace = response["namespace"]
        if filling is None:
            client.agent.update(namespace=agent_namespace, form_id=f_id)
        else:
            client.agent.update(namespace=agent_namespace, form_id=f_id, form_filling=filling)
        agent_info = client.agent.get(agent_namespace)
        client.agent.delete(namespace=agent_namespace, delete_connected_resources=False)
        return agent_info
    
    def _get_result(info, f_id):
        print(info)
        return "form_id" in info and info["form_id"] == f_id

    schema = {
        "name": { "type": "string" },
        "email": { "type": "string" },
        "years_of_experience": { "type": "number" },
        "years_experience_with_nextjs": { "type": "number" },
        "AI_experience": { "type": "boolean" }
    }

    forms = client.forms
    form_response = forms.create("test_form", schema)
    form_id = form_response["form_id"]

    i = 1
    print("Running test_agent_forms:")
    for form_filling in [None, False, True]:
        a_info = _create_agent_with_form(client, "test_agent", form_id, form_filling)
        print(f"Case {i}: Initialize agent with form, form_filling={form_filling}")
        print(f"form_id found in response of agent.get() ?\n{_get_result(a_info, form_id)}")
        i += 1
        
        b_info = _create_agent_update_with_form(client, "test_agent", form_id, form_filling)
        print(f"Case {i}: Update agent with form, form_filling={form_filling}")
        print(f"form_id found in response of agent.get() ?\n{_get_result(b_info, form_id)}")
        i += 1
    
    client.forms.delete(form_id)
    print("Finished running test_agent_forms:\n")
    


def test_files_kb(client):
    """ Test that when uploading a file and specifying a knowledge_base, the contents of the file can be retrieved after"""
    agent_response = client.agent.create(title="test_agent", knowledge_search=True)
    kb_id = agent_response["knowledgeId"]
    uploaded_files = client.files.upload(
        files=["old_tests/file_for_testing.txt, old_tests/file_for_testing2.txt"],
        knowledgeId=kb_id
    )

    #### Need a way to access the file in that kb
    client.agent.delete(agent_response["namespace"], delete_connected_resources=True)


if __name__ == "__main__":
    # This testing file will test how the entities integrate together
    client = _setup_tests.__setup()  # set up client
    # test_agent_kb(client)
    test_agent_forms(client)
    # test_files_kb(client)
