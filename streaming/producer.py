import requests
import time
import random
import logging
from typing import Dict, Any, Optional

# ==============================
# CONFIG
# ==============================
URL = "http://127.0.0.1:8000/api/v1/predict"
DELAY = 2
TIMEOUT = 15
MAX_RETRIES = 3

# ==============================
# LOGGING
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# ==============================
# METRICS
# ==============================
success_count = 0
failure_count = 0
fraud_count = 0


# ==============================
# DATA GENERATOR (SMART)
# ==============================
def generate_transaction() -> Dict[str, int]:
    """
    Generates both normal and fraud-like transactions
    """
    if random.random() < 0.3:
        # NORMAL TRANSACTION
        return {
            "amount": random.randint(100, 2000),
            "oldbalanceOrg": random.randint(5000, 20000),
            "newbalanceOrig": random.randint(3000, 18000),
            "oldbalanceDest": random.randint(1000, 5000),
            "newbalanceDest": random.randint(2000, 6000)
        }
    else:
        # FRAUD-LIKE TRANSACTION
        return {
            "amount": random.randint(50000, 100000),
            "oldbalanceOrg": random.randint(0, 1000),
            "newbalanceOrig": 0,
            "oldbalanceDest": random.randint(0, 1000),
            "newbalanceDest": random.randint(50000, 100000)
        }


# ==============================
# API CALL WITH RETRY
# ==============================
def send_request(data: Dict[str, int]) -> Optional[Dict[str, Any]]:
    global success_count, failure_count, fraud_count

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(URL, json=data, timeout=20)
            response.raise_for_status()

            result = response.json()
            success_count += 1

            if result.get("is_fraud"):
                fraud_count += 1

            return result

        except requests.exceptions.RequestException as e:
            logger.warning(f"Retry {attempt+1}/{MAX_RETRIES} failed: {e}")
            time.sleep(1)

    failure_count += 1
    return None


# ==============================
# METRICS DISPLAY
# ==============================
def print_metrics():
    total = success_count + failure_count
    fraud_rate = (fraud_count / total * 100) if total > 0 else 0

    logger.info(f"📊 Total: {total} | Success: {success_count} | Failed: {failure_count}")
    logger.info(f"🚨 Fraud detected: {fraud_count} | Fraud Rate: {fraud_rate:.2f}%")


# ==============================
# MAIN LOOP
# ==============================
def run():
    logger.info("🚀 Real-Time Fraud Streaming Started")

    while True:
        data = generate_transaction()
        result = send_request(data)

        if result:
            logger.info(f"Prediction: {result}")

        if (success_count + failure_count) % 10 == 0:
            print_metrics()

        time.sleep(3)


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    run()