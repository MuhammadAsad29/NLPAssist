from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.rag import initialize_rag, retrieve_context
from backend.qa import generate_answer
from backend.cache import SimpleCache

app = FastAPI(title="University FAQ RAG Chatbot")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache
cache = SimpleCache()

class Query(BaseModel):
    question: str

# Initialize RAG on startup
@app.on_event("startup")
def startup_event():
    initialize_rag()


@app.post("/api/ask")
def ask_question(query: Query):
    question = query.question.strip()
    # check cache
    cached = cache.get(question)
    if cached:
        return cached

    # Retrieve context from RAG
    contexts, sources = retrieve_context(question)

    if not contexts:
        response = {
            "answer": "I currently don't have knowledge about that, sorry!",
            "sources": []
        }
    else:
        # Generate answer using LLM
        answer = generate_answer(question, contexts)
        response = {
            "answer": answer,
            "sources": list(set(sources))  # unique sources
        }

    # Save in cache
    cache.set(question, response)
    return response
