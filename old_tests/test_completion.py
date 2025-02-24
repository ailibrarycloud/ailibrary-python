import json
import ailibrary as ai

client = ai.AILibrary("d4qgdcs2lgUBvwWDFjC6NeOIrLS87cpoDHlwPL5a", "https://bb27-2601-640-8a81-8330-2d05-1f7c-f006-af42.ngrok-free.app")

def collect_chunks(completion):
    result = ""
    buffer = ""
    for chunk in completion:
        buffer += chunk
        try:
            chunk_json = json.loads(buffer)
            result += chunk_json["content"]
            print(chunk_json["content"])
            buffer = ""
        except json.JSONDecodeError:
            continue
    return result

# Example usage
completion = client.agent.chat(
    namespace="sales-agent-20250206022633",
    session_id="sample-session",
    messages=[
        {
            "role": "assistant",
            "content": "Hey, are you looking to buy?"
        },
        {
            "role": "user",
            "content": "Tell me more about the product"
        }
    ]
)

result = collect_chunks(completion)
print(result)