def validate_consistency(prediction, advisory):

    if prediction.lower() in advisory.lower():
        return True

    return False
