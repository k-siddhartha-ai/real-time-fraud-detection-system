from pydantic import BaseModel


class FraudRequest(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float


class FraudResponse(BaseModel):
    fraud_probability: float
    is_fraud: bool
