from fastapi import FastAPI
from pydantic import BaseModel

from supervisor import supervisor
from weather_agent import weather_agent

app = FastAPI(
    title="Multi Agent API",
    version="1.0"
)


class UserQuery(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "Multi-Agent API Running Successfully"
    }


@app.post("/supervisor")
def ask_supervisor(data: UserQuery):

    response = supervisor.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": data.query
                }
            ]
        }
    )

    return {
        "response": response["messages"][-1].content
    }


@app.post("/weather")
def ask_weather(data: UserQuery):

    response = weather_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": data.query
                }
            ]
        }
    )

    return {
        "response": response["messages"][-1].content
    }