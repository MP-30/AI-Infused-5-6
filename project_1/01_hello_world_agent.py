'''
This simplest possible agent (strands + bedrock).
Four lines is a whole agent:
1. Choose a model
2. wrap it in an agent
3. call the agent like a function
4. print the answer

There are no tools here, so the agentic loop runs exactly once.
This is the "before" picture for Module 2.
'''
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strands import  Agent
from strands.models.bedrock import BedrockModel
form config import 