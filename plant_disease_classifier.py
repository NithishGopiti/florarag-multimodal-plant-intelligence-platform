def classify_disease(feature_score):

    if feature_score > 120:
        return "Leaf Blight"

    if feature_score > 80:
        return "Rust"

    return "Healthy"
