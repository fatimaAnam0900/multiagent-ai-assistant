# 🤖 Multi-Agent AI Assistant

An intelligent AI-powered assistant built using **LangChain, LangGraph, FastAPI, and Streamlit**. The system uses multiple specialized agents coordinated by a Supervisor Agent to handle different user queries, including weather information and mathematical calculations.

## 🚀 Project Overview

The Multi-Agent AI Assistant follows a supervisor-based architecture where a central Supervisor Agent receives user queries and delegates tasks to the appropriate specialized agent.

The system provides an interactive chat interface through Streamlit and uses FastAPI as its backend API.

## ✨ Features

- **Supervisor Agent:** Understands user queries and routes them to the appropriate agent.
- **Weather Agent:** Handles weather-related queries using weather tools.
- **Calculator Agent:** Performs mathematical calculations.
- **Multi-Agent Architecture:** Multiple specialized agents work together.
- **FastAPI Backend:** Provides API endpoints for communication.
- **Streamlit Frontend:** Provides a simple and interactive chat interface.
- **LLM Integration:** Uses an LLM to understand and process natural language queries.

## 🛠️ Technologies Used

- Python
- LangChain
- LangGraph
- Groq LLM
- FastAPI
- Streamlit
- Tavily API
- Pydantic

## 🏗️ Project Architecture

```text
Multi-Agent AI Assistant
│
├── Supervisor Agent
│   ├── Weather Agent
│   └── Calculator Agent
│
├── FastAPI Backend
│   └── API Endpoints
│
└── Streamlit Frontend
    └── Interactive Chat Interface
```

## 📂 Project Structure

```text
multiagent/
│
├── agent_tools.py
├── app.py
├── calculator_agent.py
├── llm.py
├── streamlit_app.py
├── supervisor.py
├── test_weather_tool.py
├── tools.py
├── weather_agent.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/multiagent-ai-assistant.git
```

### 2. Navigate to Project Directory

```bash
cd multiagent-ai-assistant
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory and add your API credentials.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Use your own API keys. Never upload your `.env` file to GitHub.

## ▶️ Running the Project

The project requires two terminals to run the backend and frontend separately.

### Terminal 1: Start FastAPI Backend

```bash
uvicorn app:app --reload --port 8000
```

Backend URL:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

### Terminal 2: Start Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Frontend URL:

http://localhost:8501

## 🔮 Future Improvements

- Add more specialized AI agents.
- Improve agent communication and coordination.
- Add conversation memory.
- Enhance error handling and response accuracy.
- Integrate additional external tools and APIs.

## 👩‍💻 Author

**Fatima Anam**

AI / ML Developer | Agentic AI Enthusiast

---

⭐ If you find this project interesting, feel free to explore and contribute!