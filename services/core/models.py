# services/core/models.py

from sqlalchemy import Column, Integer, Float, Boolean, DateTime, String, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)

    # input data snapshot
    features = Column(JSON, nullable=False)

    # prediction result
    fraud_probability = Column(Float, nullable=False)
    is_fraud = Column(Boolean, nullable=False)

    # metadata
    model_version = Column(String, default="v1")
    created_at = Column(DateTime, default=datetime.utcnow)
