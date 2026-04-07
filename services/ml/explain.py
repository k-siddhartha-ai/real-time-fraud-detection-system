# services/ml/explain.py

import shap
import numpy as np
from ml.models.model_loader import load_model

# load model once
bundle = load_model()
model = bundle["model"]
scaler = bundle["scaler"]

explainer = shap.TreeExplainer(model)


def explain(features: list):
    """
    Return SHAP explanation for one prediction
    """
    X = np.array([features])
    X_scaled = scaler.transform(X)

    shap_values = explainer.shap_values(X_scaled)

    return shap_values[0].tolist()
