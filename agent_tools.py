from langchain_core.tools import tool
from tools import weather_tool
from calculator_agent import calculator_agent


@tool
def weather_agent_tool(query: str) -> str:
    """
     Use ONLY for weather-related questions.

    Examples:
    - Weather in Lahore
    - Temperature of Karachi
    - Is it raining in Islamabad?
    - Weather forecast for Multan

    Never use this tool for mathematics or general conversation.
    """
    print("calculator tool executed")

    location = query.lower()

    for word in [
        "weather",
        "of",
        "in",
        "tell me",
        "what is",
        "what's",
        "display",
        "only",
        "city",
        "name",
    ]:
        location = location.replace(word, "")

    location = location.strip()

    if not location:
        return "Please provide a city name."

    return weather_tool.invoke({"location": location})


@tool
def calculator_agent_tool(query: str) -> str:
    """
     Use ONLY for mathematical calculations.

    Examples:
    - 2+2
    - 15*20
    - Divide 40 by 5
    - Square root of 81
    - Percentage calculations

    Never use this tool for weather or general questions
    """
    print("calculator tool executed")
    response = calculator_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    return response["messages"][-1].content