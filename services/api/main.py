"""
Main FastAPI Application
Industry-ready structure
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ IMPORTANT — ADD THESE IMPORTS
from services.api.v1.fraud_routes import router as fraud_router
from services.api.v1.admin_routes import router as admin_router
from services.api.v1.explain_routes import router as explain_router

from services.core.database import engine
from services.core.models import Base
from services.utils.logger import get_logger

logger = get_logger("main")

app = FastAPI(
    title="Real-Time Fraud Detection System",
    version="1.0.0",
    description="Production-grade Fraud Detection using ML + FastAPI"
)

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- STARTUP ----------
@app.on_event("startup")
def startup():
    logger.info("Starting API...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database ready")

# ---------- ROOT ----------
@app.get("/")
def root():
    return {"message": "Fraud Detection API running"}

# ---------- HEALTH ----------
@app.get("/health")
def health():
    return {"status": "OK"}

# ---------- ROUTES ----------
app.include_router(fraud_router, prefix="/api/v1", tags=["Fraud Prediction"])
app.include_router(admin_router, prefix="/api/v1", tags=["Admin"])
app.include_router(explain_router, prefix="/api/v1", tags=["Explain AI"])
