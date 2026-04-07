# Converts incoming API data into ML-ready format
import numpy as np


def transform_input(data: dict):
    # For now we simulate features
    # Later we add real feature engineering
    features = np.array([
        data["amount"],
        data["oldbalanceOrg"],
        data["newbalanceOrig"],
    ]).reshape(1, -1)

    return features
