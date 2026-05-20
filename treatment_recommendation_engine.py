treatment_store = {
    "Leaf Blight": "Apply antifungal spray and monitor irrigation.",
    "Rust": "Improve airflow and monitor leaf moisture."
}

def fetch_treatment(disease_name):

    return treatment_store.get(
        disease_name,
        "General crop monitoring required."
    )
