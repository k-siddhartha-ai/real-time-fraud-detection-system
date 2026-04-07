
# 🚀 Real-Time Fraud Detection System

> Production-grade Machine Learning system for detecting fraudulent financial transactions in real-time.

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
- 🔍 Explainable AI (fallback-safe SHAP)
- 🐳 Dockerized deployment (production-ready)

---

## 🏗️ System Architecture
```mermaid
flowchart LR

    User[User] --> API[FastAPI Backend]

    API --> Preprocess[Data Processing]
    Preprocess --> Scaler[Feature Scaling]
    Scaler --> Model[ML Model]

    Model --> API

    API --> DB[(Database)]
    API --> Dashboard[Dashboard]

    DB --> Dashboard

    API --> Logs[Logging System]
    API --> Metrics[Metrics API]

    API --> User
```

## ⚙️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | FastAPI |
| Machine Learning | Scikit-learn |
| Database | SQLite + SQLAlchemy |
| Dashboard | Streamlit |
| Deployment | Docker |
| Language | Python |

---

## 🚀 API Endpoints

### 🔹 Predict Fraud

```http
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
```

🖥️ Run Locally
```bash
git clone https://github.com/k-siddhartha-ai/real-time-fraud-detection-system.git
cd real-time-fraud-detection-system

pip install -r requirements.txt
uvicorn services.api.main:app --reload
```


🐳 Run with Docker
```bash
docker build -t fraud-app .
docker run -p 8000:8000 fraud-app
```

📊 Dashboard
```bash
streamlit run dashboard/app.py
```

📂 Project Structure
services/        → API & core backend  
ml/              → Model training & loading  
dashboard/       → Visualization UI  
streaming/       → Real-time simulation


📸 Backend API Demonstration
🔹 Fraud Prediction API (Swagger UI)
### 🔹 Fraud Prediction API (Swagger UI)

<img src="<img width="1807" height="835" alt="Screenshot 2026-04-08 011152" src="https://github.com/user-attachments/assets/3a82967a-d4fc-43de-bcf1-12a502e13de7" />
" width="100%" />

🔹 Prediction Response Output
### 🔹 Prediction Response Output

<img src="<img width="1761" height="690" alt="Screenshot 2026-04-08 011530" src="https://github.com/user-attachments/assets/a688a19c-78b9-4dbf-9cd3-7ba37c7f144c" />
" width="100%" />

🔹 Admin Logs & Monitoring
### 🔹 Admin Logs (Stored Predictions)

<img src="<img width="841" height="843" alt="Screenshot 2026-04-08 012316" src="https://github.com/user-attachments/assets/e2082147-91e4-4f45-a9ae-a4daa2a7edc9" />
" width="100%" />

### 🔹 Fraud Monitoring Metrics

<img src="<img width="666" height="798" alt="Screenshot 2026-04-08 012637" src="https://github.com/user-attachments/assets/d6ee1f5f-0676-4db2-b959-93a6c61ead6b" />
" width="100%" />

📊 Frontend Dashboard Demonstration

### 🧾 Transaction Input & Fraud Prediction

<img src="<img width="1793" height="904" alt="Screenshot 2026-04-08 003508" src="https://github.com/user-attachments/assets/37ef5ced-399e-4cd3-807d-6d8e6beb0eec" />
" width="100%" />

🔍 Model Explainability (SHAP Insights)
<img src="<img width="666" height="798" alt="Screenshot 2026-04-08 012637" src="https://github.com/user-attachments/assets/08bdedd4-a813-4eed-a22f-b89d1616d3f8" />
" width="100%" />

📜 Prediction History (Database Logging)
### 📜 Prediction History (Database Logging)

<img src="<img width="1778" height="678" alt="Screenshot 2026-04-08 003600" src="https://github.com/user-attachments/assets/46895b6b-2395-430d-972a-1ad3a5a7b2ed" />
" width="100%" />


📈 Fraud Analytics & Monitoring

### 📈 Fraud Analytics & Monitoring

<img src="<img width="1830" height="853" alt="Screenshot 2026-04-08 003654" src="https://github.com/user-attachments/assets/3ba16eda-a343-4b94-806c-c49d497ed503" />
" width="100%" />

📈 Sample Output
{
  "fraud_probability": 0.957,
  "is_fraud": true
}






🚀 Future Improvements
Kafka-based real-time streaming
Cloud deployment (AWS / GCP)
CI/CD pipelines
Model retraining automation

👨‍💻 Author

K. Siddhartha

⭐ If you like this project

Give it a ⭐ on GitHub!
