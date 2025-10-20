#!/usr/bin/env -S uv run python
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP


server = MCPServerStreamableHTTP("http://localhost:8000/mcp")
agent = Agent("openai:gpt-4.1", toolsets=[server])


message_history = []
while True:
    current_message = input("You: ")
    if current_message == "exit":
        break
    result = agent.run_sync(current_message, message_history=message_history)
    message_history = result.all_messages()
    print(result.output)
