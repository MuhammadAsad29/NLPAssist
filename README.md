# NLPAssist

**University FAQ Chatbot using RAG and LLM**

## Overview

NLPAssist is a local university FAQ chatbot project developed as a CCP (Capstone Course Project). It combines **Retrieval-Augmented Generation (RAG)** with a local language model to answer university-related questions accurately and in a natural tone.

- **Retrieval:** MiniLM embeddings + FAISS vector search over FAQ dataset.
- **Generation:** Local LLM (TinyLlama) generates answers from retrieved context.
- **Frontend:** HTML/CSS/JavaScript for interactive chat.
- **Backend:** FastAPI serves the API.

## Features

- Accurate semantic retrieval of FAQ content.
- Answers generated in natural language by LLM.
- Hallucination prevention: answers are restricted to retrieved context.
- Sources included for each answer.
- Fully CPU compatible (16 GB RAM recommended).
- Local deployment, no external API needed.

## Project Structure



NLPAssist/
├── backend/
│ ├── main.py
│ ├── rag.py
│ ├── qa.py
│ └── cache.py
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── data/
│ └── university_faq.txt
├── .gitignore
└── README.md

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MuhammadAsad29/NLPAssist.git


Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Run the backend:

uvicorn backend.main:app


Open frontend/index.html in a browser to use the chatbot.

Usage

Type a university-related question into the chatbox.

The bot will respond with an answer based on the FAQ dataset.

Each answer shows the source file it was retrieved from.

Notes

Ensure the FAQ dataset (university_faq.txt) is in the correct data/ directory.

Model generation settings: temperature=0.25, top_p=0.75, max_new_tokens=180.

Fully offline capable after initial setup.

License

MIT License


---

If you want, I can **also provide a ready-to-use `requirements.txt`** with all needed Python packages for this repo, so your GitHub repo will be fully runnable after cloning.  

Do you want me to generate that?
