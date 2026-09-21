'''
Project-> From a plain function to a tool
The core idea of module 2
A normal python function is invisible to an agent. To expose it, add 3 things:
    1. the @tool decorator -> makes it available to agents
    2. type hints          -> tells the agent what data types to except
    3. A proper docstring  -> tells the agent When to use it.
'''
import sys, os
from http.client import responses

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from config import MODEL_ID

@tool
def check_server_status(server_url: str) -> str:
    '''
    check if a server is responding by making am HTTP request.
    Args:
        server_url: The url of the server to check
    Returns:
        A message indicating whether the server is up or down
    '''
    try:
        response = requests.get(server_url, timeout=5)
        return f"Server is up. Status code: {response.status_code}"
    except requests.exceptions.RequestException:
        return "Server is down or unreachable"
agent = Agent(model=BedrockModel(model_id=MODEL_ID), tools=[check_server_status])
response = agent("Is the staging server running? Check Http://httpbin.org/get")