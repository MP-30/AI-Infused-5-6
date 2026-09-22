'''
project 2 - Lesson 4- Building a custom tool.
When cummunity tools don't fit (internal API, proprietaty database). You
write your own. Here: an online store checking stock.

The mock dictionary stands in for a real database. The agent-facing part - decorator, type
hints, docstring - is identical either way.
'''
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from config import MODEL_ID

@tool
def check_inventory(product_id: str)-> str:
    '''
    check if a product is in stock.
    '''
    inventory = {
        "PROD-123": 15,
        "PROD-456": 0,
        "PROD-789":9,
    }
    quantity = inventory.get(product_id, 0)
    if quantity > 0:
        return f"Product {product_id} is in stock. We have {quantity} units available."
    else:
        return f"Product {product_id} is currently out of stock."

agent = Agent(model=BedrockModel(model_id=MODEL_ID), tools=[check_inventory])

agent("Is PROD-123 in stock?")
agent("Do we have PROD-456 available?")
agent("Check inventory for PROD-789")
agent("Can I order PROD-123 right now?")