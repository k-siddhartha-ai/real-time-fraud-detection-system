# dashboard/app.py

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Real-Time Fraud Detection Dashboard",
    layout="wide"
)

st.title("💳 Real-Time Fraud Detection Dashboard")


# ---------------- CHECK BACKEND ---------------- #
def backend_running():
    try:
        r = requests.get(f"{API_URL}/health", timeout=2)
        return r.status_code == 200
    except:
        return False


if not backend_running():
    st.error("❌ FastAPI backend NOT running")
    st.stop()

st.success("✅ Backend Connected")


# ---------------- PREDICTION ---------------- #
st.header("🔍 Run Prediction")
st.write("Enter transaction details")

amount = st.number_input("Amount", value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Sender", value=1000.0)
newbalanceOrig = st.number_input("New Balance Sender", value=0.0)
oldbalanceDest = st.number_input("Old Balance Receiver", value=0.0)
newbalanceDest = st.number_input("New Balance Receiver", value=1000.0)

if st.button("Predict"):
    try:
        payload = {
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }

        res = requests.post(
            f"{API_URL}/api/v1/predict",
            json=payload,
            timeout=5
        )

        if res.status_code == 200:
            data = res.json()

            st.metric("Fraud Probability", round(data["fraud_probability"], 4))
            st.write("Is Fraud:", data["is_fraud"])

            # ----------- EXPLAIN -----------
            explain = requests.post(
                f"{API_URL}/api/v1/explain",
                json=[
                    amount,
                    oldbalanceOrg,
                    newbalanceOrig,
                    oldbalanceDest,
                    newbalanceDest
                ],
                timeout=5
            )

            if explain.status_code == 200:
                st.subheader("Why model predicted this?")
                st.json(explain.json())

        else:
            st.error(res.text)

    except Exception as e:
        st.error(str(e))


# ---------------- LOGS ---------------- #
st.header("📊 Prediction History")

try:
    logs = requests.get(f"{API_URL}/api/v1/admin/logs", timeout=5).json()

    if logs:
        df = pd.DataFrame(logs)
        st.dataframe(df, width="stretch")

        fig = px.histogram(df, x="fraud_probability",
                           title="Fraud Probability Distribution")
        st.plotly_chart(fig, width="stretch")

    else:
        st.info("No logs yet")

except Exception:
    st.warning("Logs not available")


# ---------------- STATS ---------------- #
st.header("📈 Fraud Stats")

try:
    stats = requests.get(f"{API_URL}/api/v1/admin/stats", timeout=5).json()

    col1, col2 = st.columns(2)
    col1.metric("Total Predictions", stats.get("total", 0))
    col2.metric("Fraud Rate %", stats.get("fraud_rate", 0))

except Exception:
    st.warning("Stats API not available")
