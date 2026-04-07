from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from services.core.database import SessionLocal
from services.core.models import PredictionLog

router = APIRouter()


# ---------- DB ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- LOGS ----------
@router.get("/admin/logs")
def get_logs(db: Session = Depends(get_db)):
    logs = (
        db.query(PredictionLog)
        .order_by(PredictionLog.id.desc())
        .limit(20)
        .all()
    )
    return logs


# ---------- STATS ----------
@router.get("/admin/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(func.count(PredictionLog.id)).scalar()

    fraud_count = (
        db.query(func.count(PredictionLog.id))
        .filter(PredictionLog.is_fraud == True)
        .scalar()
    )

    fraud_rate = (fraud_count / total * 100) if total else 0

    return {
        "total": total,
        "fraud_rate": round(fraud_rate, 2)
    }
