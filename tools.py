from langchain_core.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def weather_tool(location: str) -> str:
    """Get current weather using Tavily."""

    response = client.search(
        query=f"Current weather in {location}",
        max_results=2,
    )
    print("weather tool executed")

    if response.get("results"):
        return response["results"][0]["content"]

    return "Weather information not found."


@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a mathematical expression."""

    print("calculator tool executed")

    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression."