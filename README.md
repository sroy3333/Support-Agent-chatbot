CDP Support Chatbot

📌 Project Overview

The CDP Support Chatbot is a FastAPI-based chatbot that helps users by answering questions related to CDP (Customer Data Platform). It utilizes LangChain with OpenAI's GPT-4 model to generate responses based on retrieved documents.

🚀 Features

FastAPI Backend: Handles chatbot queries and serves static files.

LangChain Integration: Uses OpenAI's GPT-4 model for answering questions.

Custom Classifier: Determines if a question is relevant to CDP.

Retriever Module: Fetches related documents to improve answer accuracy.

Static Web UI: A simple HTML + JavaScript frontend to interact with the chatbot.

🏗️ Project Structure

/your_project_directory
│── app.py                # FastAPI backend
│── retriever.py          # Retrieves relevant documents
│── classifier.py         # Classifies relevant questions
│── requirements.txt      # Dependencies
│── static/               # Static files (HTML, JS, etc.)
│   ├── index.html        # Frontend UI
│   ├── script.js         # JavaScript logic for API calls

📦 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/cdp-support-chatbot.git
cd cdp-support-chatbot

2️⃣ Set Up a Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

🔧 Configuration

Set up OpenAI API Key: Ensure your OpenAI API key is set up in your environment variables.

export OPENAI_API_KEY="your_openai_api_key"

▶️ Running the Chatbot

Start the FastAPI server:

uvicorn app:app --host 127.0.0.1 --port 8000 --reload

🌍 Open in Browser

Visit:

http://127.0.0.1:8000/

📜 API Endpoints

Method

Endpoint

Description

POST

/ask

Sends a user query and returns a chatbot response

🛠 Troubleshooting

Issue: RuntimeError: Directory 'static' does not exist

Solution: Create a static folder and move index.html and script.js inside it.

Issue: 501 Unsupported method ('POST')

Solution: Ensure your FastAPI @app.post("/ask") matches the frontend API call in script.js.
