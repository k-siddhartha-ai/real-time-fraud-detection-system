from fastapi import APIRouter, HTTPException
import numpy as np

from ml.models.model_loader import load_model

router = APIRouter()

# Load model
bundle = load_model()
model = bundle["model"]
scaler = bundle["scaler"]

# Try SHAP safely
try:
    import shap
    SHAP_AVAILABLE = True
except Exception:
    SHAP_AVAILABLE = False

explainer = None

FEATURE_NAMES = [
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest"
]


def get_explainer():
    global explainer

    if not SHAP_AVAILABLE:
        return None

    if explainer is None:
        try:
            explainer = shap.TreeExplainer(model)
        except Exception:
            explainer = None

    return explainer


@router.post("/explain")
def explain(features: list[float]):

    if len(features) != 5:
        raise HTTPException(status_code=400, detail="Model expects 5 features")

    X = np.array(features).reshape(1, -1)
    X_scaled = scaler.transform(X)

    explainer_obj = get_explainer()

    # 🔴 SAFE FALLBACK (IMPORTANT)
    if explainer_obj is None:
        return {
            "status": "fallback",
            "message": "Explainability disabled due to model incompatibility"
        }

    try:
        shap_values = explainer_obj.shap_values(X_scaled)

        explanation = dict(zip(FEATURE_NAMES, shap_values[0].tolist()))

        return {
            "feature_importance": explanation,
            "status": "success"
        }

    except Exception:
        return {
            "status": "safe-mode",
            "message": "SHAP failed, returning fallback response"
        }