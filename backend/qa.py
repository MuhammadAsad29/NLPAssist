from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# CPU-safe LLM (TinyLlama)
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
    device_map="cpu"
)


def generate_answer(question, contexts):
    """
    Generate answer using retrieved contexts.
    contexts: list of text chunks from FAISS
    """
    context_text = "\n".join(contexts)

    prompt = f"""
You are a helpful university assistant. Answer the user's question using ONLY the context below.
Do NOT add information not present in the context. Use your own tone and natural language.

Context:
{context_text}

Question:
{question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            temperature=0.25,
            top_p=0.75,
            repetition_penalty=1.2
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # extract after "Answer:" if tokenizer keeps it
    return decoded.split("Answer:")[-1].strip()
