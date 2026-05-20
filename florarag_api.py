from fastapi import FastAPI

from plant_disease_classifier import classify_disease
from rag_knowledge_retriever import retrieve_knowledge
from contextual_reasoning_pipeline import build_context_prompt
from transformer_advisory_engine import generate_advisory

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "florarag_platform_running"
    }

@app.post("/diagnose-plant")
def diagnose(payload: dict):

    disease = classify_disease(
        payload["feature_score"]
    )

    retrieved_context = retrieve_knowledge(
        disease
    )

    prompt = build_context_prompt(
        disease,
        retrieved_context
    )

    advisory = generate_advisory(prompt)

    return {
        "predicted_disease": disease,
        "advisory": advisory
    }
