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
            agent_info = client.agent.update(namespace=agent_namespace, knowledgeId=kb_id)
        else:
            agent_info = client.agent.update(namespace=agent_namespace, knowledgeId=kb_id, knowledge_search=kb_search)
        client.agent.delete(namespace=agent_namespace, delete_connected_resources=False)
        return agent_info

    def _get_result(info, kb_id):
        return "knowledgeId" in a_info and a_info["knowledgeId"] == knowledgeId

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


if __name__ == "__main__":
    # This testing file will test how the entities integrate together
    client = _setup_tests.__setup()  # set up client
    test_agent_kb(client)
