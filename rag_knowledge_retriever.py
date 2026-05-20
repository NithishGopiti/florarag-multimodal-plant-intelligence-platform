knowledge_base = {
    "Leaf Blight": "Use antifungal treatment and improve ventilation.",
    "Rust": "Reduce humidity and apply copper fungicides."
}

def retrieve_knowledge(disease_name):

    return knowledge_base.get(
        disease_name,
        "General plant health guidance."
    )
