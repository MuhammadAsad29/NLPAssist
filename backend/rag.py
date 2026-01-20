import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Config
DATA_PATH = "data/documents/university_faq.txt"
TOP_K = 3  # retrieve top 3 chunks
CHUNK_SIZE = 150  # words per chunk
SIM_THRESHOLD = 0.6  # cosine similarity threshold

# Global variables
chunks = []
chunk_sources = []
faiss_index = None
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_and_chunk():
    global chunks, chunk_sources
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    chunks = []
    chunk_sources = []
    current_q = ""
    current_a = ""

    for line in lines:
        line = line.strip()
        if line.lower().startswith("q:"):
            current_q = line[2:].strip()
        elif line.lower().startswith("a:"):
            current_a = line[2:].strip()
            # split long answer into chunks
            words = current_a.split()
            for i in range(0, len(words), CHUNK_SIZE):
                chunk = " ".join(words[i:i + CHUNK_SIZE])
                chunks.append(chunk)
                chunk_sources.append("university_faq.txt")


def build_index():
    global faiss_index
    embeddings = embedder.encode(chunks, convert_to_numpy=True, normalize_embeddings=True)
    dim = embeddings.shape[1]
    faiss_index = faiss.IndexFlatIP(dim)
    faiss_index.add(embeddings)


def initialize_rag():
    load_and_chunk()
    build_index()


def retrieve_context(question):
    question_embedding = embedder.encode([question], convert_to_numpy=True, normalize_embeddings=True)
    scores, indices = faiss_index.search(question_embedding, TOP_K)

    retrieved_chunks = []
    retrieved_sources = []

    for score, idx in zip(scores[0], indices[0]):
        if score >= SIM_THRESHOLD:
            retrieved_chunks.append(chunks[idx])
            retrieved_sources.append(chunk_sources[idx])

    return retrieved_chunks, retrieved_sources
