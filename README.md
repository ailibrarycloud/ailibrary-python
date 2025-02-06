# AI Library Python API Library

The AI Library Python library provides convenient access to the AI Library REST API from any Python 3.8+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients.

## Installation

```
pip install ailibrary
```

## Usage

```
import os
import ailibrary as ai
client = ai.AILibrary(
    api_key=os.environ.get("AI_LIBRARY_KEY"),
    domain="https://api.ailibrary.ai/" // only required for self-hosted AI Library instances
)
```

## Creating your first agent

Initialise your agent
```
sales_agent = client.agent.create(
    title = "Sales Agent"
    instructions="You are a sales agent trying to qualify a lead. You are receiving this "
    )
```
Add training files
```
client.files.upload(
    files = ['/local/path/to/file.pdf'], //txt, pdf, pptx, docx, xlsx
    knowledge_id = sales_agent.knowledge_id
)
```
Check status of the agent knowledge
```
print(client.knowledge_base.get_status())
```

Chat with agent

```
completion = agent.chat(
    messages = [
        {
            "role": "assistant",
            "content": "Hey, are you looking to buy?"
        },
        {
            "role": "user",
            "content": "Yes, I want to know more first"
        }
    ]
)

```
