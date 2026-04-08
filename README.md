Team Name :VSS-Gen AI-Saga

Gemini Multi-Agent Task Orchestrator (GMATO).

🚀 Google Gen AI Academy Hackathon 2026 Submission.

Problem Statement: Build a multi-agent AI system that manages tasks, schedules, and structured information via interacting with multiple tools.

📖 Project Overview
GMATO is an intelligent, API-based orchestration system. It uses a Primary Manager Agent (powered by Gemini 1.5 Flash) to interpret natural language and coordinate with specialized sub-agents/tools to execute real-world workflows.

Core Capabilities:
Intelligent Routing: The primary agent determines if a user request requires database interaction or simple information retrieval.

Structured Data Management: Automatically transforms unstructured chat (e.g., "Remind me to buy milk") into organized data entries.

Multi-Agent Coordination: Demonstrates the seamless handoff between LLM reasoning and functional tool execution.

🛠️ Technical Stack
Core Model: Gemini 1.5 Flash (via Vertex AI)

Orchestration: Python / FastAPI

Deployment: Google Cloud Run (Serverless)

Tooling: Vertex AI Function Calling

Persistence: File-based Structured Database (database.txt)

🏗️ System Architecture
API Layer: FastAPI receives the user's natural language request.

Primary Agent: Gemini analyzes the intent and determines which tool is required.

Task Tool (Sub-Agent): Executes the save_task_to_db function to store structured information.

Database: A persistent storage layer that tracks all scheduled tasks.

🚀 Getting Started
Prerequisites
Google Cloud Platform (GCP) Account

Vertex AI API Enabled

Installation & Local Run
Clone the repo:

Bash
git clone https://github.com/Soniyap16/gen-ai-task-agent.git
cd gen-ai-task-agent
Install dependencies:

Bash
pip install -r requirements.txt
Run locally:

Bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
🔗 Live Links
GitHub Repository: https://github.com/Soniyap16/gen-ai-task-agent

Deployed API URL:  https://hackathon-agent-1073819819689.us-central1.run.app

Interactive Docs: 

🎥 Demo Video
Watch the multi-agent system in action:

Authors

Soniya P 

Vidhya Sagar N 

Gen AI Academy Participant
