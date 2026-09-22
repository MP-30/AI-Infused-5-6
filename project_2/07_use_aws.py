'''
Project 2 - Lesson 7 - AWS integration with use_aws.
One tools, many service. use_aws translates plain English into AWS API calls.
You don't write boto3 code, don't handle AWS response, and don't even specify which operation to
use. The agent worls it out.

SAFETY: this script only dones a READ_ONLY request (listing s3 buckets).
on sandbox account.
'''
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import use_aws
from config import MODEL_ID

agent = Agent(
    model=BedrockModel(model_id=MODEL_ID),
    tools=[use_aws],
    system_prompt="You are an AWS assistance that helps manage cloud resources."
)
agent("List all s3 buckets in my account")