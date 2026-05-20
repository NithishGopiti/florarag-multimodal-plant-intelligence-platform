def build_context_prompt(disease, retrieved_context):

    return f'''
Detected Disease:
{disease}

Retrieved Agricultural Context:
{retrieved_context}

Generate treatment advisory.
'''
