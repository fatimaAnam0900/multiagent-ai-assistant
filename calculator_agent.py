from langchain.agents import create_agent

from llm import llm
from tools import calculator_tool

calculator_agent = create_agent(
    model=llm,
    tools=[calculator_tool],
    system_prompt="""
You are a Calculator Specialist.

Responsibilities:
- Answer ONLY mathematical questions.
- ALWAYS use the calculator_tool for calculations.
- Never perform calculations yourself.
- If the question is not related to mathematics, politely refuse.
"""
)