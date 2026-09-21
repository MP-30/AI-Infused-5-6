'''
Lesson 2 -- My first tool-enabled agent: a tip calculator.
Show that the agent understands INTENT, not keywords. All three phrasings
at the bottom work without any extra code -- no regrex, no intent classifer.
'''
import sys, os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from config import MODEL_ID

@tool
def calculate_tip(bill_amount: float, tip_percentage: float, num_people: int=1) -> dict:
    '''
    calculate tip and split the bill among people.
    '''
    tip = bill_amount * (tip_percentage /100)
    total = bill_amount + tip
    per_person = total / num_people

    return {
        "bill": bill_amount,
        "tip": round(tip, 2),
        "total": round(total, 2),
        "per_person": round(per_person,2),
    }
agent = Agent(model=BedrockModel(model_id=MODEL_ID), tools=[calculate_tip])

response = agent(
    "The bill is $85. What's a 20% tip, and how much does each person pay"
    "If we're splitting it 4 ways?"
)
print(response.message["content"][0]["text"])

print("\n--- Try different phrasings ---")
agent("What's a 15% tip on $42?")
agent("Bill is $120, we want to tip 18%, split between 3 people")
agent("Calculate tip for $67.50 at 20%")