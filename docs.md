# AI Library Python API Documentation

## Table of Contents
- [AI Library Python API Documentation](#ai-library-python-api-documentation)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [About](#about)
    - [Basic Usage](#basic-usage)
    - [Tutorials](#tutorials)
  - [2. Getting Started](#2-getting-started)
    - [Installation](#installation)
    - [Authentication](#authentication)
    - [Configuration?](#configuration)
  - [3. API Reference](#3-api-reference)
    - [Authentication](#authentication-1)
    - [3.1 Agents](#31-agents)
    - [3.2 Knowledge Bases](#32-knowledge-bases)
    - [3.3 Files](#33-files)
    - [3.4 Notes](#34-notes)
    - [3.5 Utilities](#35-utilities)
    - [Error Handling](#error-handling)
  - [4. Examples](#4-examples)
  - [5. Advanced Features](#5-advanced-features)
  - [6. Best Practices](#6-best-practices)
  - [7. Troubleshooting](#7-troubleshooting)
  - [8. FAQ](#8-faq)
  - [9. Contributing](#9-contributing)
  - [10. License](#10-license)
  - [11. Changelog](#11-changelog)
  - [12. Contact & Support](#12-contact--support)

## 1. Introduction
### About
- Overview of the package
- Key features
- Purpose and scope
### Basic Usage
- Simple examples to run the package
### Tutorials
- Step-by-step guides for various features and tasks


## 2. Getting Started
### Installation
- Installation methods (pip, npm, etc.)
- System requirements
### Authentication
- Explain how client works
- API keys
### Configuration?
- Configuration options
- Environment variables and file settings


## 3. API Reference

The AI Library API is organized around REST. The API accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes.

### Authentication

The AI Library API uses API keys for authentication. You can obtain your API key from your AI Library dashboard.

```python
import os
import ailibrary as ai

client = ai.AILibrary(
    api_key="your-api-key",  # Defaults to os.environ["AI_LIBRARY_KEY"]
    domain="https://api.ailibrary.ai/"  # Optional: only for self-hosted instances
)
```

### 3.1 Agents

Agents are AI assistants that can be customized with specific instructions and knowledge bases.

#### Create agent

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

Returns an agent object.

```python
{
    "namespace": "sales-assistant-abc123",
    "title": "Sales Assistant",
    "description": "An AI assistant for sales inquiries",
    "knowledge_id": "kb_123abc"
}
```

#### Get agent

```python
agent = client.agent.get(namespace="sales-assistant-abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `namespace` | string | Required | The agent's unique identifier |

**Returns**

Returns the agent object.

```python
{
    "namespace": "sales-assistant-abc123",
    "title": "Sales Assistant",
    "description": "An AI assistant for sales inquiries",
    "instructions": "You are a helpful sales assistant...",
    "knowledge_id": "kb_123abc"
}
```

#### List agents

```python
agents = client.agent.list_agents()
```

**Parameters**

No parameters required.

**Returns**

Returns a list of agent objects.

```python
{
    "agents": [
        {
            "namespace": "agent-abc123",
            "title": "Sales Assistant",
            "description": "Sales inquiry assistant"
        },
        # ... more agents
    ]
}
```

#### Update agent

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

Returns the updated agent object.

```python
{
    "namespace": "sales-assistant-abc123",
    "title": "Updated Sales Assistant",
    "instructions": "New instructions...",
    # ... other updated properties
}
```

#### Delete agent

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
    "status": "success",
    "message": "Agent deleted successfully"
}
```

#### Chat with agent

```python
response = client.agent.chat(
    namespace="sales-assistant-abc123",
    messages=[
        {"role": "user", "content": "Hello, can you help me?"}
    ],
    session_id="session_xyz789"  # Optional
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `namespace` | string | Required | The agent's unique identifier |
| `messages` | array | Required | Array of message objects with `role` and `content` |
| `session_id` | string | Optional | Session identifier for conversation continuity |

**Message Object**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `role` | string | Required | One of: "user", "assistant", "system" |
| `content` | string | Required | The message content |

**Returns**

Returns a chat completion object.

```python
{
    "response": "Hello! Yes, I'd be happy to help you...",
    "session_id": "session_xyz789",
    "conversation_id": "conv_abc123"
}
```

### 3.2 Knowledge Bases

Knowledge bases store and process documents that agents can reference during conversations.

#### Create knowledge base

```python
kb = client.knowledge_base.create(
    name="Product Documentation",
    meta={"category": "technical"}
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Required | Name of the knowledge base |
| `meta` | object | Optional | Additional metadata for the knowledge base |

**Returns**

Returns a knowledge base object.

```python
{
    "knowledgeId": "kb_abc123",
    "name": "Product Documentation",
    "meta": {
        "category": "technical"
    }
}
```

#### List knowledge bases

```python
knowledge_bases = client.knowledge_base.list_knowledge_bases()
```

**Parameters**

No parameters required.

**Returns**

Returns a list of knowledge base objects.

```python
{
    "knowledge_bases": [
        {
            "knowledgeId": "kb_abc123",
            "name": "Product Documentation",
            "meta": {"category": "technical"}
        },
        # ... more knowledge bases
    ]
}
```

#### Get knowledge base

```python
kb = client.knowledge_base.get(knowledge_id="kb_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |

**Returns**

Returns a knowledge base object with its sources.

```python
{
    "knowledgeId": "kb_abc123",
    "name": "Product Documentation",
    "meta": {"category": "technical"},
    "sources": [
        {
            "sourceId": "src_xyz789",
            "type": "docs",
            "status": "processed"
        }
        # ... more sources
    ]
}
```

#### Add source to knowledge base

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
| `urls` | array | Optional | Array of URLs to process |
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

#### Get knowledge base status

```python
status = client.knowledge_base.get_status(knowledge_id="kb_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |

**Returns**

Returns the processing status of the knowledge base and its sources.

```python
{
    "status": "processing",
    "progress": 45.5,
    "sources": [
        {
            "sourceId": "src_xyz789",
            "status": "processing",
            "progress": 45.5
        }
    ]
}
```

#### Get source

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

#### List sources

```python
sources = client.knowledge_base.list_sources(knowledge_id="kb_abc123")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `knowledge_id` | string | Required | The knowledge base identifier |

**Returns**

Returns a list of source objects.

```python
[
    {
        "sourceId": "src_xyz789",
        "type": "docs",
        "status": "processed",
        "meta": {"category": "documentation"}
    },
    # ... more sources
]
```

#### Delete sources

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
| `values` | array | Optional | List of source IDs to delete |
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

### 3.3 Files

The Files API allows you to upload and manage files that can be processed by knowledge bases.

#### Upload files

```python
uploaded_files = client.files.upload(
    files=["/path/to/document.pdf"],
    knowledge_id="kb_abc123"  # Optional
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `files` | array | Required | Array of file paths to upload |
| `knowledge_id` | string | Optional | Knowledge base to associate files with |

**Supported File Types**
- Text files (.txt)
- PDF documents (.pdf)
- Microsoft Word documents (.docx)
- Microsoft PowerPoint presentations (.pptx)
- Microsoft Excel spreadsheets (.xlsx)

**Returns**

Returns an array of file objects.

```python
[
    {
        "fileId": "file_abc123",
        "filename": "document.pdf",
        "mimetype": "application/pdf",
        "size": 1234567,
        "status": "uploaded"
    }
]
```

#### List files

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

Returns a paginated list of file objects.

```python
{
    "files": [
        {
            "fileId": "file_abc123",
            "filename": "document.pdf",
            "mimetype": "application/pdf",
            "size": 1234567
        }
    ],
    "total": 45,
    "page": 1,
    "limit": 10
}
```

#### Get file

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
    "fileId": "file_abc123",
    "filename": "document.pdf",
    "mimetype": "application/pdf",
    "size": 1234567,
    "uploadDate": "2024-03-20T10:30:00Z"
}
```

#### Delete file

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
{
    "status": "success",
    "message": "File deleted successfully"
}
```

### 3.4 Notes

The Notes API allows you to add annotations and comments to various resources.

#### Add note

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
| `role` | string | Required | One of: "assistant", "user", "system" |
| `resource` | string | Required | One of: "agent", "knowledgebase", "file" |
| `resource_id` | string | Required | ID of the associated resource |
| `meta` | object | Optional | Additional metadata for the note |

**Returns**

Returns the created note object.

```python
{
    "noteId": "note_xyz789",
    "content": "Important information about this agent",
    "role": "user",
    "resource": "agent",
    "resourceId": "agent_abc123",
    "createdAt": "2024-03-20T10:30:00Z"
}
```

#### Get note

```python
note = client.notes.get(note_id="note_xyz789")
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `note_id` | string | Required | The note identifier |

**Returns**

Returns a note object.

```python
{
    "noteId": "note_xyz789",
    "content": "Important information about this agent",
    "role": "user",
    "resource": "agent",
    "resourceId": "agent_abc123",
    "createdAt": "2024-03-20T10:30:00Z"
}
```

#### Get notes for resource

```python
notes = client.notes.get_for_resource(
    resource="agent",
    resource_id="agent_abc123"
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resource` | string | Required | One of: "agent", "knowledgebase", "file" |
| `resource_id` | string | Required | ID of the resource |

**Returns**

Returns a list of note objects.

```python
[
    {
        "noteId": "note_xyz789",
        "content": "Important information about this agent",
        "role": "user",
        "createdAt": "2024-03-20T10:30:00Z"
    },
    # ... more notes
]
```

#### Update note

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
| `role` | string | Required | One of: "assistant", "user", "system" |
| `meta` | object | Optional | Updated metadata |

**Returns**

Returns the updated note object.

```python
{
    "noteId": "note_xyz789",
    "content": "Updated information",
    "role": "user",
    "updatedAt": "2024-03-20T11:30:00Z"
}
```

#### Delete notes

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
| `resource` | string | Required | One of: "agent", "knowledgebase", "file" |
| `resource_id` | string | Required | ID of the resource |
| `values` | array | Optional | List of note IDs to delete |
| `delete_all` | boolean | Optional | If true, deletes all notes for the resource |

Note: Either `values` or `delete_all` must be specified.

**Returns**

Returns a deletion confirmation.

```python
{
    "status": "success",
    "message": "Notes deleted successfully"
}
```

### 3.5 Utilities

The Utilities API provides additional functionality to enhance agent capabilities.

#### Web search

```python
results = client.utilities.web_search(
    search_terms=["AI Library", "documentation"]
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `search_terms` | array | Required | Array of search terms |

**Returns**

Returns an array of search result objects.

```python
[
    {
        "title": "AI Library Documentation",
        "url": "https://docs.ailibrary.ai",
        "snippet": "Official documentation for AI Library...",
        "source": "ailibrary.ai"
    }
]
```

#### Web parser

```python
parsed_content = client.utilities.web_parser(
    urls=["https://example.com/article"]
)
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `urls` | array | Required | Array of URLs to parse |

**Returns**

Returns an array of parsed page objects.

```python
[
    {
        "url": "https://example.com/article",
        "title": "Example Article",
        "content": "The extracted content of the webpage...",
        "metadata": {
            "author": "John Doe",
            "publishDate": "2024-03-20"
        }
    }
]
```

### Error Handling

The API uses conventional HTTP response codes to indicate the success or failure of requests.

- `200` - Success
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `429` - Too Many Requests
- `500` - Internal Server Error

Error responses include a message providing more details about the error:

```python
{
    "error": {
        "message": "Invalid API key provided",
        "type": "authentication_error",
        "code": 401
    }
}
```

## 4. Examples
- Common use cases and comprehensive examples


## 5. Advanced Features
- Detailed examples using complex scenarios


## 6. Best Practices
- Coding standards and recommended usage


## 7. Troubleshooting
- Common issues and resolution steps


## 8. FAQ
- Frequently asked questions


## 9. Contributing
- Guidelines for contributing to the project
- Code of conduct


## 10. License
- Licensing terms and conditions


## 11. Changelog
- Version history and updates


## 12. Contact & Support
- Support channels
- Contact information
