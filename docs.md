# AI Library Python API Documentation

## Table of Contents
- [AI Library Python API Documentation](#ai-library-python-api-documentation)
  - [Table of Contents](#table-of-contents)
  - [Authentication](#authentication)
  - [Agents](#agents)
    - [Create agent](#create-agent)
    - [Get agent](#get-agent)
    - [List agents](#list-agents)
    - [Update agent](#update-agent)
    - [Delete agent](#delete-agent)
    - [Chat with agent](#chat-with-agent)
  - [Knowledge Bases](#knowledge-bases)
    - [Create knowledge base](#create-knowledge-base)
    - [List knowledge bases](#list-knowledge-bases)
    - [Get knowledge base](#get-knowledge-base)
    - [Add source to knowledge base](#add-source-to-knowledge-base)
    - [Get knowledge base status](#get-knowledge-base-status)
    - [Get source](#get-source)
    - [List sources](#list-sources)
    - [Delete sources](#delete-sources)
  - [Files](#files)
    - [Upload files](#upload-files)
    - [List files](#list-files)
    - [Get file](#get-file)
    - [Delete file](#delete-file)
  - [Notes](#notes)
    - [Add note](#add-note)
    - [Get note](#get-note)
    - [Get notes for resource](#get-notes-for-resource)
    - [Update note](#update-note)
    - [Delete notes](#delete-notes)
  - [Utilities](#utilities)
    - [Web search](#web-search)
    - [Web parser](#web-parser)

## Authentication

The AI Library API uses API keys for authentication. You can obtain your API key from your AI Library dashboard.

```python
import os
import ailibrary as ai

client = ai.AILibrary(
    api_key="your-api-key",  # Defaults to os.environ["AI_LIBRARY_KEY"]
    domain="https://api.ailibrary.ai/"  # Optional: only for self-hosted instances
)
```

## Agents

The Agents API enables you to create, manage, and interact with AI assistants. These agents can be customized with specific instructions, knowledge bases, and conversation settings. Use this API to build intelligent conversational interfaces for your applications.

### Create agent

```python
agent = client.agent.create(
    title="Sales Assistant",
    instructions="You are a helpful sales assistant...",
    description="An AI assistant for sales inquiries"
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Required | The name of your agent |
| `instructions` | string | Optional | System instructions for the agent. Defaults to "You are a helpful assistant." |
| `description` | string | Optional | A description of the agent's purpose |
| `coverimage` | string | Optional | URL to the agent's avatar image |
| `intromessage` | string | Optional | Initial message the agent sends |
| `knowledge_search` | boolean | Optional | Enable knowledge base search |
| `knowledge_id` | string | Optional | ID of an associated knowledge base |

**Returns**

Returns the JSON response containing information about the new agent object.

```python
{
    'coverimage': 'https://www.ailibrary.ai/ailibrary.svg', 
    'description': 'An AI assistant for sales inquiries', 
    'intromessage': 'How can I help you today?', 
    'namespace': 'Sales Assistant', 
    'title': 'test_agent_kushagra', 
    'type': 'chat', 
    'instructions': 'You are a helpful assistant. Answer the questions based on the information you are given. If answer is not available in the context, try to navigate the conversation smartly. Answer in English only.'
}
```

### Get agent

```python
agent = client.agent.get(namespace="sales-assistant-abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `namespace` | string | Required | The agent's unique identifier |

**Returns**

Returns the JSON response containing information about the matching agent, if found.

```python
# {
#     "namespace": "sales-assistant-abc123",
#     "title": "Sales Assistant",
#     "description": "An AI assistant for sales inquiries",
#     "instructions": "You are a helpful sales assistant...",
#     "knowledge_id": "kb_123abc"
# }
{
    'coverimage': 'https://www.ailibrary.ai/ailibrary.svg',
    'created_timestamp': '2025-02-07 01:11:16', 
    'description': 'An AI assistant for sales inquiries', 
    'intromessage': 'How can I help you today?', 
    'namespace': 'Sales Assistant',
    'response_schema': None,
    'showcase': None, 
    'status': None, 
    'title': 'test_agent_kushagra', 
    'type': 'chat', 
    'instructions': 'You are a helpful assistant. Answer the questions based on the information you are given. If answer is not available in the context, try to navigate the conversation smartly. Answer in English only.'
}
```

### List agents

```python
agents = client.agent.list_agents()
```

**Parameters**

No parameters required.

**Returns**

Returns the JSON response containing list of agents and meta info.

```python
{
    "agents": [
        {
            "namespace": "agent-abc123",
            "title": "Sales Assistant",
            "description": "Sales inquiry assistant"
            # ... other agent info
        },
        # ... more agents
    ],

    "meta": {...}
}
```

### Update agent

```python
updated_agent = client.agent.update(
    namespace="sales-assistant-abc123",
    title="Updated Sales Assistant",
    instructions="New instructions..."
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `namespace` | string | Required | The agent's unique identifier |
| `title` | string | Optional | New name for the agent |
| `type` | string | Optional | One of: "notebook", "chat", "voice" |
| `instructions` | string | Optional | New system instructions |
| `description` | string | Optional | New description |
| `coverimage` | string | Optional | New avatar URL |
| `intromessage` | string | Optional | New initial message |
| `knowledge_search` | boolean | Optional | Enable/disable knowledge search |
| `knowledge_id` | string | Optional | New knowledge base ID |

**Returns**

Returns a confirmation for the update operation.

```python
{'response': 'success'}
```

### Delete agent

```python
response = client.agent.delete(namespace="sales-assistant-abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `namespace` | string | Required | The agent's unique identifier |

**Returns**

Returns a deletion confirmation.

```python
{
    'statusCode': 200,
    'message': 'Agent deleted successfully'
}
```

### Chat with agent

```python
response = client.agent.chat(
    namespace="sales-assistant-abc123",
    messages=[
        {"role": "system", "content": "You are a helpful sales assistant."},
        {"role": "user", "content": "Hello, can you help me?"},
        {"role": "assistant", "content": "Of course! How can I assist you?"},
        {"role": "user", "content": "I'm looking for pricing information."}
    ],
    session_id="session_xyz789"  # Optional
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `namespace` | string | Required | The agent's unique identifier |
| `messages` | list | Required | List of message objects representing the conversation history. Must contain at least one message. |
| `session_id` | string | Optional | Session identifier for conversation continuity |

**Message Object Schema**

Each object in the `messages` list must have the following structure:

| Field | Type | Required | Allowed Values | Description |
|-------|------|----------|----------------|-------------|
| `role` | string | Required | "system", "user", or "assistant" | Identifies who sent the message |
| `content` | string | Required | Any non-empty string | The content of the message |

**Example Messages List**
```python
messages=[
    # System message setting the context
    {
        "role": "system",
        "content": "You are a helpful sales assistant."
    },
    # User message
    {
        "role": "user",
        "content": "What are your prices?"
    },
    # Assistant's previous response
    {
        "role": "assistant",
        "content": "I'd be happy to help you with pricing information."
    }
]
```

**Returns**

Returns a chat completion object.

```python
{
    "response": "Our pricing starts at $10/month for the basic plan...",
    "session_id": "session_xyz789",
    "conversation_id": "conv_abc123"
}
```

## Knowledge Bases

The Knowledge Bases API enables you to create and manage vector databases that store and process documents. These knowledge bases can be associated with agents to provide them with specific information and context for their responses.

### Create knowledge base

```python
kb = client.knowledge_base.create(
    name="Product Documentation",
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Required | Name of the knowledge base |
| `meta` | dict | Optional | Additional metadata for the knowledge base |

**Returns**

Returns a JSON response for the new knowledge base object.

```python
# {
#     "knowledgeId": "kb_abc123",
#     "name": "Product Documentation",
#     "meta": {
#         "category": "technical"
#     }
# }
{'status': 'success', 'knowledgeId': 'kb_abc123'}
```

### List knowledge bases

```python
knowledge_bases = client.knowledge_base.list_knowledge_bases()
```

**Parameters**

No parameters required.

**Returns**

Returns the JSON response containing list of knolwedge bases and meta info.

```python
{
    "knowledgebases": [
        {
            "knowledgeId": "kb_abc123",
            # ... other knolwedge base info
        },
        # ... more knowledge bases
    ],
    "meta": {...}
}
```

### Get knowledge base

```python
kb = client.knowledge_base.get(knowledge_id="kb_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |

**Returns**

Returns a JSON response containing info about the knowledge base object, if found.

```python
{
    'title': 'Title of Knowledge Base',
    'knowledgeId': 'kb_abc123',
    'status': 'processing',
    'sources': 0,
    'generations': 0,
    'addhistory': 1,
    'visibility': 'private',
    'default_prompts': None,
    'default_model': None,
    'default_urls': None,
    'userName': 'Kushagra Agrawal',
    'userEmail': 'kush.agr02@gmail.com',
    'special_event': None,
    'star': None,
    'meta': None
}
```

### Add source to knowledge base

```python
source = client.knowledge_base.add_source(
    knowledge_id="kb_abc123",
    type="docs",
    urls=["https://example.com/docs.pdf"],
    meta={"category": "documentation"}
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |
| `type` | string | Required | Type of source: "docs", "web", or "youtube" |
| `urls` | list | Optional | List of URLs to process |
| `meta` | object | Optional | Additional metadata for the source |

**Returns**

Returns a source object.

```python
{
    "sourceId": "src_xyz789",
    "status": "processing",
    "type": "docs",
    "meta": {"category": "documentation"}
}
```

### Get knowledge base status

```python
status = client.knowledge_base.get_status(knowledge_id="kb_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |

**Returns**

Returns the processing status of the knowledge base as a string.

```python
"available"
```

### Get source

```python
source = client.knowledge_base.get_source(
    knowledge_id="kb_abc123",
    source_id="src_xyz789"
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |
| `source_id` | string | Required | The source identifier |

**Returns**

Returns a source object.

```python
{
    "sourceId": "src_xyz789",
    "type": "docs",
    "status": "processed",
    "meta": {"category": "documentation"},
    "url": "https://example.com/docs.pdf"
}
```

### List sources

```python
sources = client.knowledge_base.list_sources(knowledge_id="kb_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |

**Returns**

Returns a list of source objects or an empty string if there are no sources for the specified knowledge base.

```python
[
    {
        # ... source info
    },
    # ... more sources
]
```

### Delete sources

```python
response = client.knowledge_base.delete_sources(
    knowledge_id="kb_abc123",
    values=["src_xyz789", "src_abc123"],  # or use delete_all=True
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |
| `values` | list | Optional | List of source IDs to delete |
| `delete_all` | boolean | Optional | If true, deletes all sources |

Note: Either `values` or `delete_all` must be specified.

**Returns**

Returns a deletion confirmation.

```python
{
    "status": "success",
    "message": "Sources deleted successfully"
}
```

## Files

The Files API allows you to upload and manage files that can be processed by knowledge bases.

### Upload files

```python
uploaded_files = client.files.upload(
    files=["/path/to/document.pdf"],
    knowledge_id="kb_abc123"  # Optional
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `files` | list | Required | List of file paths to upload |
| `knowledge_id` | string | Optional | Knowledge base to associate files with |

**Returns**

Returns an list of file objects.

```python
# knowledge_id?
[
    {
        'url': 'https://domain/corbett/email/file_name.txt',
        'id': 1232,
        'bytes': 17,
        'name': 'file_name.txt'
    },
    
    # ... other files
]
```

### List files

```python
files = client.files.list_files(
    page=1,
    limit=10
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | Optional | Page number for pagination |
| `limit` | integer | Optional | Number of files per page |

**Returns**

Returns the JSON response containing list of files and meta info.

```python
{
    'files': [
        {
            'bytes': 17,
            'created_timestamp': 'YYYY-MM-DD hh:mm:ss',
            'id': 1232,
            'name': 'file_name.txt'
            'url': 'https://domain/corbett/email/file_name.txt',
        },
        # ... other files
    ],
    
    'meta': {'limit': 10, 'next_page': 2, 'prev_page': '', 'total_items': 2}
}
```

### Get file

```python
file = client.files.get(file_id="file_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_id` | string | Required | The file identifier |

**Returns**

Returns a file object.

```python
{
    'bytes': 17,
    'created_timestamp': 'YYYY-MM-DD hh:mm:ss',
    'id': 1232,
    'name': 'file_name.txt'
    'url': 'https://domain/corbett/email/file_name.txt'
}
```

### Delete file

```python
response = client.files.delete(file_id="file_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_id` | string | Required | The file identifier |

**Returns**

Returns a deletion confirmation.

```python
{'response': 'Record successfully deleted'}
```

## Notes

The Notes API allows you to add annotations and comments to various resources within the AI Library. Notes can be attached to agents, knowledge bases, and files to provide additional context or documentation.

Here are some common parameters required for multiple functions and their restrictions.

**Common Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `role` | string | One of: "assistant", "user", "system" |
| `resource` | string | One of: "agent", "knowledgebase", "file" |
| `resource_id` | string | Identifier of the resource. The expected value depends on the resource type:<br>- For `resource="agent"`: use the agent's namespace<br>- For `resource="knowledgebase"`: use the knowledgeId<br>- For `resource="file"`: use the file id |

### Add note

```python
note = client.notes.add(
    content="Important information about this agent",
    role="user",
    resource="agent",
    resource_id="agent_abc123",
    meta={"priority": "high"}
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `content` | string | Required | The note content |
| `role` | string | Required | See "Common Parameters" at the start of section |
| `resource` | string | Required | See "Common Parameters" at the start of section |
| `resource_id` | string | Required | See "Common Parameters" at the start of section |
| `meta` | object | Optional | Additional metadata for the note |

**Returns**

Returns a JSON response confirming a new note was created, as well as the id of the note.

```python
{'status': 'success', 'noteId': 'note_xyz789'}
```

### Get note

```python
note = client.notes.get(note_id="note_xyz789")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `note_id` | string | Required | The note identifier |

**Returns**

Returns a JSON response containing information about the note object, if found.

```python
{
    'content': 'note content',
    'created_timestamp': 'YYYY-MM-DD hh:mm:ss',
    'noteId': 'note_xyz789',
    'resource': 'agent',
    'resource_id': 'agent_name',
    'role': 'user',
    'updated_timestamp': 'YYYY-MM-DD hh:mm:ss',
    'userEmail': 'username@email.com',
    'userName': 'FirstName LastName'
}
```

### Get notes for resource

```python
notes = client.notes.get_resource_notes(
    resource="agent",
    resource_id="agent_abc123"
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resource` | string | Required | See "Common Parameters" at the start of section |
| `resource_id` | string | Required | See "Common Parameters" at the start of section |

**Returns**

Returns the JSON response containing list of notes and meta info.

```python
{
    'meta': {'current_page': 1, 'limit': 50, 'next_page': '', 'prev_page': '', 'total_items': 1, 'total_pages': 1}, 
    'notes': 
    [
        {
            'content': 'note content',
            'created_timestamp': 'YYYY-MM-DD hh:mm:ss',
            'noteId': 'note_xyz789',
            'resource': 'agent',
            'resource_id': 'agent_name',
            'role': 'user',
            'updated_timestamp': 'YYYY-MM-DD hh:mm:ss',
            'userEmail': 'username@gmail.com',
            'userName': 'FirstName LastName'
        },
        # ... other notes
    ]
}
```

### Update note

```python
updated_note = client.notes.update(
    note_id="note_xyz789",
    content="Updated information",
    role="user",
    meta={"priority": "low"}
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `note_id` | string | Required | The note identifier |
| `content` | string | Required | New note content |
| `role` | string | Required | See "Common Parameters" at the start of section |
| `meta` | object | Optional | Updated metadata |

**Returns**

Returns an update confirmation.

```python
{
    'status': 'success',
    'message': 'Note updated successfully'
}
```

### Delete notes

```python
response = client.notes.delete_notes(
    resource="agent",
    resource_id="agent_abc123",
    values=["note_xyz789"],  # or use delete_all=True
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resource` | string | Required | See "Common Parameters" at the start of section |
| `resource_id` | string | Required | See "Common Parameters" at the start of section |
| `values` | list | Optional | List of note IDs to delete |
| `delete_all` | boolean | Optional | If true, deletes all notes for the resource |

Note: Either `values` or `delete_all=True` must be specified. If both are specified then `delete_all` takes precedence.

**Returns**

Returns a deletion confirmation.

```python
{
    "status": "success",
    "message": "Notes deleted successfully"
}
```

## Utilities

The Utilities API provides additional functionality to enhance agent capabilities, including web search and content parsing features.

### Web search

```python
results = client.utilities.web_search(
    search_terms=["AI Library", "documentation"]
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `search_terms` | list | Required | List of search terms |

**Returns**

Returns an list of search result objects.

```python
[
    {
        "term": "humans",
        "prompt_context": "Human - WikipediaCarl Linnaeus coined the name Homo sapiens. All modern humans ...",
        "sources": [
            {
                "title": "Human - Wikipedia",
                "description": "Carl Linnaeus coined the name Homo sapiens. All modern humans are classified into the species Homo sapiens, coined by ...",
                "url": "https://en.wikipedia.org/wiki/Human",
                "isFamilyFriendly": True,
                "language": "en",
                "full_text": "Human - WikipediaCarl Linnaeus coined the name Homo sapiens. All modern humans are classified into the species Homo sapiens...",
            },
            # ... other sources objects
        ],
    },
    # ... other term objects
]

```

### Web parser

```python
parsed_content = client.utilities.web_parser(
    urls=["https://example.com/article"]
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `urls` | list | Required | List of URLs to parse |

**Returns**

Returns an list of parsed page objects.

```python
[
    {
        "url": "https://www.ailibrary.ai",
        "title": "AI Library Agent Builder Platform",
        "domain": "https://www.ailibrary.ai",
        "body": "AI LibraryAI LibraryOpen main menuAgentsUse CasesPricingBUILD YOUR AGENTLog in →Generative AI Platform to rapidly build ...",
        "relatedurls": [
            {
                "url": "https://www.ailibrary.ai/blog",
                "title": "AI Library Status",
                "description": "Welcome to AI Library's home for real-time and historical data on system performance.",
                "type": "web",
            },
            {
                "url": "https://www.ailibrary.ai/about",
                "title": "AI Library · GitHub",
                "description": "AI Library enables faster generative AI adoption in enterprises - AI Library",
                "type": "web",
            },
            # ... more related urls
        ],
    },
    # ... more parsed page objects
]

```
