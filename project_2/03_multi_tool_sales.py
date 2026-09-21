"""Module 2 · Lesson 3 — When one tool isn't enough.
"Pull last quarter's sales data and email a summary to the team" is not one
task. It's three: query, analyse, send.

You give the agent three small tools. You NEVER tell it the order.
It works out: get data -> analyse it -> email the result. That's planning.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from config import MODEL_ID

@tool
def get_sales_data(quater: str) -> dict:
    return {"revenue": 1250000, "deals": 47, "quater": quater}

@tool
def analyze_sales(revenue: int, deals: int, quarter: str) -> str:
    avg_deal = revenue /deals
    return  f"Q{quarter}: ${revenue} revenue, {deals} deals, ${avg_deal:,.0f} avg deal size"

@tool
def send_email(to: str, subject: str, body:str) -> str:
    return f"Email sent to {to}"


agent = Agent(
    model=BedrockModel(model_id=MODEL_ID),
    tools=[get_sales_data, analyze_sales, send_email],
)

response = agent("Pull last quarter's (Q3) sales data and email a summary to the team")