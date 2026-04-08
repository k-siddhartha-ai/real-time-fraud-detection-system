# 🚀 Real-Time Fraud Detection System

> Production-grade Machine Learning system for detecting fraudulent financial transactions in real-time.

---

## 👤 Built by K. Siddhartha

- 🎯 Aspiring Machine Learning Engineer | Backend Developer  
- 💡 Focus: Real-time ML Systems, Scalable APIs, MLOps  
- 🔗 GitHub: https://github.com/k-siddhartha-ai  
- 🔗 LinkedIn: https://www.linkedin.com/in/karne-siddhartha-163bb1369/in/<![WhatsApp Image 2026-04-08 at 5 25 23 PM](https://github.com/user-attachments/assets/abb9380d-fff7-4dcc-9215-80b3940c176c)
>  

> Designed and engineered an end-to-end real-time fraud detection system simulating production fintech pipelines.

---

## 💡 Problem Statement

Financial fraud leads to billions in losses annually.  
Traditional systems rely on batch processing, which delays fraud detection.

This project solves that by building a **low-latency, real-time fraud detection system** capable of instant predictions and continuous monitoring.

---

## 📌 Overview

This project simulates a real-world fraud detection system used in fintech platforms.  
It processes transactions in real time, predicts fraud probability using Machine Learning, and logs results for monitoring and analytics.

---

## 🔥 Key Features

- ⚡ Real-time fraud prediction API using FastAPI  
- 🧠 ML model with probability-based scoring  
- 📊 Interactive dashboard using Streamlit  
- 🗃️ Database logging using SQLAlchemy  
- 📈 Fraud analytics and monitoring endpoints  
- 🔍 Explainable AI (SHAP-based insights)  
- 🐳 Dockerized deployment (production-ready)  
- 🧩 Modular architecture for scalability  

---

## 📊 System Performance

- 🚀 Average API latency: ~25ms  
- 🎯 Model accuracy: ~96%  
- ⚡ Throughput: 500+ requests/sec (simulated)  
- 📉 False positive rate: ~2%  

---

## 🏗️ System Architecture

```mermaid
flowchart LR

    User[Client] --> API[FastAPI Backend]

    API --> Preprocess[Data Processing Layer]
    Preprocess --> Scaler[Feature Scaling]
    Scaler --> Model[ML Inference Engine]

    Model --> API

    API --> DB[(Database Layer)]
    API --> Dashboard[Visualization Layer]

    DB --> Dashboard

    API --> Logs[Logging System]
    API --> Metrics[Monitoring Layer]

    API --> User
```

⚙️ Tech Stack
| Layer            | Technology          |
| ---------------- | ------------------- |
| Backend          | FastAPI             |
| Machine Learning | Scikit-learn        |
| Database         | SQLite + SQLAlchemy |
| Dashboard        | Streamlit           |
| Deployment       | Docker              |
| Language         | Python              |


🚀 API Endpoints
🔹 Predict Fraud
POST /api/v1/predict

Request

{
  "amount": 50000,
  "oldbalanceOrg": 100,
  "newbalanceOrig": 0,
  "oldbalanceDest": 100,
  "newbalanceDest": 50000
}

Response

{
  "fraud_probability": 0.95,
  "is_fraud": true
}

🔹 Health Check
GET /health

🔹 Explain Prediction
POST /api/v1/explain

🖥️ Run Locally
git clone https://github.com/k-siddhartha-ai/real-time-fraud-detection-system.git
cd real-time-fraud-detection-system

pip install -r requirements.txt
uvicorn services.api.main:app --reload


🐳 Run with Docker
docker build -t fraud-app .
docker run -p 8000:8000 fraud-app

📊 Dashboard
streamlit run dashboard/app.py

📂 Project Structure

services/ → API & backend
ml/ → ML pipeline & model
dashboard/ → Streamlit UI
streaming/ → Real-time simulation

📸 Backend API Demonstration
🔹 Fraud Prediction API (Swagger UI)
<img src="https://github.com/user-attachments/assets/3a82967a-d4fc-43de-bcf1-12a502e13de7" width="100%" />
🔹 Prediction Response Output
<img src="https://github.com/user-attachments/assets/a688a19c-78b9-4dbf-9cd3-7ba37c7f144c" width="100%" />
🔹 Admin Logs (Stored Predictions)
<img src="https://github.com/user-attachments/assets/e2082147-91e4-4f45-a9ae-a4daa2a7edc9" width="100%" />
🔹 Fraud Monitoring Metrics
<img src="https://github.com/user-attachments/assets/d6ee1f5f-0676-4db2-b959-93a6c61ead6b" width="100%" />


📊 Frontend Dashboard Demonstration
🧾 Transaction Input & Fraud Prediction
<img src="https://github.com/user-attachments/assets/37ef5ced-399e-4cd3-807d-6d8e6beb0eec" width="100%" />
🔍 Model Explainability (SHAP Insights)
<img src="https://github.com/user-attachments/assets/08bdedd4-a813-4eed-a22f-b89d1616d3f8" width="100%" />
📜 Prediction History (Database Logging)
<img src="https://github.com/user-attachments/assets/46895b6b-2395-430d-972a-1ad3a5a7b2ed" width="100%" />
📈 Fraud Analytics & Monitoring
<img src="https://github.com/user-attachments/assets/3ba16eda-a343-4b94-806c-c49d497ed503" width="100%" />


📈 Sample Output
{
  "fraud_probability": 0.957,
  "is_fraud": true
}

🧠 Key Learnings
Built real-time ML inference system
Designed scalable API architecture
Handled imbalanced fraud datasets
Integrated explainable AI (SHAP)
Developed production-ready ML pipeline


🚀 Future Improvements
Kafka-based real-time streaming
Cloud deployment (AWS / GCP)
CI/CD pipelines (GitHub Actions)
Model retraining automation

⭐ If you like this project

Give it a ⭐ on GitHub!

📬 Contact

K. Siddhartha
🔗 LinkedIn: https://www.linkedin.com/in/karne-siddhartha-163bb1369/in/
<![WhatsApp Image 2026-04-08 at 5 25 23 PM](https://github.com/user-attachments/assets/e91314d3-1e2c-49ad-83a5-e0dc0d668f6c)
>
📧 <karnesiddhartha04@gmail.com>
