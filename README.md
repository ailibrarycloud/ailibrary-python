# AI Library Python API Library

The AI Library Python library provides convenient access to the AI Library REST API from any Python 3.8+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients.  

## Installation
`pip install openai`

## Usage
```
import os
import ailibrary as ai
client = ai.AILibrary(
    api_key=os.environ.get("AI_LIBRARY_KEY"),  
    domain=os.environ.get("DOMAIN")
)
```

## Create an agent

`sales_agent = client.agent.create(title = "Sales Agent")`