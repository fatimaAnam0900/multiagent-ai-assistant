from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a single shared LLM instance
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)
#response = llm.invoke("Who are you?")

#rint(response.content)