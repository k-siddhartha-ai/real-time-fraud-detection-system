from fastapi import APIRouter, HTTPException, Depends
import numpy as np
from sqlalchemy.orm import Session

from ml.models.model_loader import load_model
from services.api.v1.schemas import FraudRequest, FraudResponse
from services.core.database import SessionLocal
from services.core.models import PredictionLog
from services.utils.logger import get_logger

router = APIRouter()
logger = get_logger("fraud_api")

bundle = load_model()
model = bundle["model"]
scaler = bundle["scaler"]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/predict", response_model=FraudResponse)
def predict(req: FraudRequest, db: Session = Depends(get_db)):

    try:
        # ✔ Build feature vector (5 features)
        X = np.array([[
            req.amount,
            req.oldbalanceOrg,
            req.newbalanceOrig,
            req.oldbalanceDest,
            req.newbalanceDest
        ]])

        # ✔ Scale
        X_scaled = scaler.transform(X)

        # ✔ Predict
        prob = float(model.predict_proba(X_scaled)[0][1])
        prediction = prob > 0.005

        # ✔ Save to DB
        log = PredictionLog(
            features=X.flatten().tolist(),
            fraud_probability=prob,
            is_fraud=prediction,
            model_version="v2_paysim"
        )

        #db.add(log)
        #db.commit()
        #db.refresh(log)

        logger.info(f"Prediction stored | prob={prob:.4f}")

        return FraudResponse(
            fraud_probability=prob,
            is_fraud=prediction
        )

    except Exception as e:
        db.rollback()
        logger.exception("Prediction failed")
        raise HTTPException(500, str(e))
