from langchain.agents import create_agent

from llm import llm
from tools import weather_tool

weather_agent = create_agent(
    model=llm,
    tools=[weather_tool],
    system_prompt="""
You are a Weather Specialist.

Rules:
- Answer ONLY weather-related questions.
- Use weather_tool exactly once.
- After receiving the tool output, immediately answer the user.
- Do not call weather_tool multiple times.
- Do not ask follow-up questions unless the location is missing.
- Never make up weather information.
"""
)