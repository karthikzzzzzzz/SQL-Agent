from dataclasses import dataclass, field
from email.mime import base
from typing import cast
import openai
from openai.types import ChatModel
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import json
from fastapi import FastAPI
import os

app= FastAPI()
load_dotenv()

openai_client = openai.AsyncOpenAI(api_key="ollama",base_url="http://localhost:11434/v1")
server_params = StdioServerParameters(
    command="python", 
    args=["./server.py"],  
    env=None, 
)

@dataclass
class Chat:
    messages: list[ChatModel] = field(default_factory=list)

    system_prompt: str = """You are a master SQL Agent. 
    Your job is to use the tools at your disposal to execute SQL queries and provide the results to the user."""
    async def process_query(self, session: ClientSession, query: str) -> dict:
        response = await session.list_tools()
        available_tools = [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description or "",
                    "parameters": tool.inputSchema,
                },
            }
            for tool in response.tools
        ]

        res = await openai_client.chat.completions.create(
            model="llama3.2",
            messages=self.messages + [{"role": "user", "content": query}],
            tools=available_tools,
        )
    
        
        sql_query = None
        for choice in res.choices:
            if hasattr(choice.message, "tool_calls") and choice.message.tool_calls:
                for tool_call in choice.message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)
                    sql_query = tool_args.get("sql","")
                    result = await session.call_tool(tool_name, cast(dict, tool_args))
                    tool_result = result.content[0].text if result.content else "No response from tool."

                    self.messages.append({"role": "assistant", "content": json.dumps({
                    "tool_name": tool_name,
                    "args": tool_args,
                    "result": tool_result
                })})
                    self.messages.append({"role": "user", "content": tool_result})
        return {
            "query":sql_query,
        }



    async def run_query(self, query: str) -> dict:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await self.process_query(session, query)


chat = Chat()
