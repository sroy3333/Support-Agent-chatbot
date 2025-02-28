from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from langchain_community.chat_models import ChatOpenAI
from pydantic import BaseModel
from langchain_community.vectorstores import Chroma
from retriever import retrieve_answer
from classifier import is_relevant_question

app = FastAPI()

class QueryRequest(BaseModel):
    query: str  # Ensure this matches frontend JSON

llm = ChatOpenAI(model_name="gpt-4")

@app.post("/ask")  
async def ask_question(request: QueryRequest):  
    query = request.query  

    if not is_relevant_question(query):
        return {"answer": "I'm here to answer CDP-related questions. Can I help with anything else?"}

    docs = retrieve_answer(query)
    response = llm.predict(f"Based on the following docs, answer: {query} {docs}")
    return {"answer": response}

# Serve static files correctly
app.mount("/static", StaticFiles(directory="static"), name="static")

