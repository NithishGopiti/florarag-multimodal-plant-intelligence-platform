from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

def generate_advisory(prompt):

    response = generator(
        prompt,
        max_length=150,
        num_return_sequences=1
    )

    return response[0]["generated_text"]
