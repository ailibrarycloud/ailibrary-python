# import pytest
# from ailibrary._internal._agent import _Agent
# from ailibrary.types.agent.responses import AgentChatResponse


# class TestAgentChat:
#     @pytest.mark.parametrize("chat_payload", [{
#         "namespace": "test-agent",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "My name is John Doe. Who are you?"
#             }
#         ],
#         "response_format": "json",
#         "session_id": "test-session-123"
#     }])
#     def test_chat_json(self, res_path, mock_http_client, chat_payload):
#         """Test successful agent chat with JSON response format"""
#         agent = _Agent(mock_http_client)

#         # Set up mock response
#         mock_response = {
#             "response": {
#                 "name": "John Doe",
#                 "greeting": "Hello! I am an AI assistant."
#             },
#             "session_id": chat_payload["session_id"],
#             "conversation_id": "conv_abc123",
#             "meta": {"type": "greeting"}
#         }
#         mock_http_client._request.return_value = mock_response

#         namespace = chat_payload.pop("namespace")
#         response = agent.chat(namespace, **chat_payload)

#         assert isinstance(response, dict)
#         assert "response" in response
#         assert "session_id" in response
#         assert "conversation_id" in response
#         assert "meta" in response
        
#         # Verify response contains expected fields
#         assert response["session_id"] == chat_payload["session_id"]
#         assert isinstance(response["response"], dict)
#         assert "name" in response["response"]
#         assert "greeting" in response["response"]

#         mock_http_client._request.assert_called_once_with(
#             "POST",
#             f"{res_path}/{namespace}/chat",
#             json=chat_payload
#         )


    # @pytest.mark.parametrize("chat_payload", [{
    #     "namespace": "test-agent",
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": "My name is John, I like apples"
    #         },
    #         {
    #             "role": "user",
    #             "content": "My name is James, I am a professor and I like bananas"
    #         },
    #         {
    #             "role": "user",
    #             "content": "My name is Mark, I like apples"
    #         },
    #         {
    #             "role": "user",
    #             "content": "I am John, I work as a developer"
    #         }
    #     ],
    #     "response_format": "text",
    #     "session_id": "test-session-456"
    # }])
    # def test_chat_text(self, res_path, mock_http_client, chat_payload):
    #     """Test successful agent chat with text response format"""
    #     agent = _Agent(mock_http_client)
        
    #     # Set up mock response
    #     mock_response = {
    #         "response": "Based on the conversation, here are the developers who like apples: John and Mark.",
    #         "session_id": chat_payload["session_id"],
    #         "conversation_id": "conv_def456",
    #         "meta": {"type": "summary"}
    #     }
    #     mock_http_client._request.return_value = mock_response
        
    #     namespace = chat_payload.pop("namespace")
    #     response = agent.chat(namespace, **chat_payload)

    #     assert isinstance(response, dict)
    #     assert "response" in response
    #     assert "session_id" in response
    #     assert "conversation_id" in response
    #     assert "meta" in response
        
    #     # Verify response contains expected fields
    #     assert response["session_id"] == chat_payload["session_id"]
    #     assert isinstance(response["response"], str)
    #     assert len(response["response"]) > 0

    #     mock_http_client._request.assert_called_once_with(
    #         "POST",
    #         f"{res_path}/{namespace}/chat",
    #         json=chat_payload
    #     )
