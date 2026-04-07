import joblib
from pathlib import Path

MODEL_PATH = Path("ml/models/fraud_model.pkl")

_model = None


def load_model():
    global _model

    if _model is None:
        print("Loading fraud detection model...")
        bundle = joblib.load(MODEL_PATH)
        _model = bundle

    return _model
