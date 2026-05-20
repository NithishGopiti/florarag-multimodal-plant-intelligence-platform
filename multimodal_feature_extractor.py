import numpy as np

def extract_features(image):

    flattened = image.flatten()

    return np.mean(flattened)
