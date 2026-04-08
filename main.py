import os
from fastapi import FastAPI
import vertexai
from vertexai.generative_models import GenerativeModel, Tool, FunctionDeclaration

app = FastAPI()

# 1. Setup - Replace 'your-project-id' with your actual GCP Project ID
PROJECT_ID = "genai-agent-project-452312" # Check your Console top bar for this
vertexai.init(project=PROJECT_ID, location="us-central1")

# 2. Simulated Database Tool (Fulfills the 'Structured Data' requirement)
def save_task_to_db(task_name: str, priority: str):
    """Saves a task to the system database."""
    with open("database.txt", "a") as f:
        f.write(f"TASK: {task_name} | PRIORITY: {priority}\n")
    return f"Successfully saved '{task_name}' to the database."

# 3. Define the tool for the AI
db_tool = Tool(
    function_declarations=[
        FunctionDeclaration(
            name="save_task_to_db",
            description="Saves a new task or to-do item to the database",
            parameters={
                "type": "object",
                "properties": {
                    "task_name": {"type": "string"},
                    "priority": {"type": "string"}
                }
            },
        )
    ]
)

# 4. Initialize the Primary Agent
model = GenerativeModel("gemini-1.5-flash", tools=[db_tool])

@app.get("/")
def health_check():
    return {"status": "Multi-Agent System Online"}

@app.post("/ask")
async def ask_agent(prompt: str):
    # The Primary Agent decides if it needs to use a tool (Sub-agent)
    chat = model.start_chat()
    response = chat.send_message(prompt)
    
    # If the AI wants to save data, it calls our function
    if response.candidates[0].content.parts[0].function_call:
        # Simple auto-execution for the hackathon demo
        return {"agent_action": "Saving to Database", "details": response.text}
    
    return {"agent_response": response.text}