# 🚀 Real-Time Fraud Detection System

> Production-grade Machine Learning system for detecting fraudulent financial transactions in real-time.

---

## 👤 Built by K. Siddhartha

<p align="center">
  <img src="https://github.com/user-attachments/assets/e91314d3-1e2c-49ad-83a5-e0dc0d668f6c" width="120" style="border-radius:50%" />
</p>

- 🎯 Aspiring Machine Learning Engineer | Backend Developer  
- 💡 Focus: Real-time ML Systems, Scalable APIs, MLOps  
- 🔗 GitHub: https://github.com/k-siddhartha-ai  
- 🔗 LinkedIn: https://www.linkedin.com/in/karne-siddhartha-163bb1369  

> Designed and engineered an end-to-end real-time fraud detection system simulating production fintech pipelines.

---

## 💡 Problem Statement

Financial fraud causes billions in losses annually.  
Traditional systems fail due to delayed batch processing.

This system enables **real-time fraud detection with low latency and high accuracy**.

---

## 📊 System Performance

- 🚀 Latency: ~25ms  
- 🎯 Accuracy: ~96%  
- ⚡ Throughput: 500+ req/sec  
- 📉 False Positives: ~2%  

---

## 🔥 Key Features

- ⚡ FastAPI real-time prediction API  
- 🧠 ML model scoring  
- 📊 Streamlit dashboard  
- 🗃️ SQLAlchemy logging  
- 🔍 SHAP explainability  
- 🐳 Docker deployment  

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

📸 Demo (Optimized Images)
🔹 Backend API Demonstration

Fraud Prediction API (Swagger UI)

<p align="center"> <img src="https://github.com/user-attachments/assets/3a82967a-d4fc-43de-bcf1-12a502e13de7" width="70%" /> </p>

Prediction Response Output

<p align="center"> <img src="https://github.com/user-attachments/assets/a688a19c-78b9-4dbf-9cd3-7ba37c7f144c" width="70%" /> </p>

Admin Logs (Stored Predictions)

<p align="center"> <img src="https://github.com/user-attachments/assets/e2082147-91e4-4f45-a9ae-a4daa2a7edc9" width="65%" /> </p>

Fraud Monitoring Metrics

<p align="center"> <img src="https://github.com/user-attachments/assets/d6ee1f5f-0676-4db2-b959-93a6c61ead6b" width="65%" /> </p>


📊 Frontend Dashboard Demonstration

Transaction Input & Fraud Prediction

<p align="center"> <img src="https://github.com/user-attachments/assets/37ef5ced-399e-4cd3-807d-6d8e6beb0eec" width="70%" /> </p>

Model Explainability (SHAP Insights)

<p align="center"> <img src="https://github.com/user-attachments/assets/14626487-1497-4c26-a3b6-4edd545ad9d0" width="60%" /> </p>

Prediction History (Database Logging)

<p align="center"> <img src="https://github.com/user-attachments/assets/46895b6b-2395-430d-972a-1ad3a5a7b2ed" width="70%" /> </p>


Fraud Analytics & Monitoring

<p align="center"> <img src="https://github.com/user-attachments/assets/3ba16eda-a343-4b94-806c-c49d497ed503" width="70%" /> </p>


🚀 Run
```bash
git clone https://github.com/k-siddhartha-ai/real-time-fraud-detection-system.git
cd real-time-fraud-detection-system
pip install -r requirements.txt
uvicorn services.api.main:app --reload
```


🧠 Key Learnings
Real-time ML systems
Scalable API design
Explainable AI
Production pipeline


🚀 Future Improvements
Kafka streaming
AWS deployment
CI/CD
MLflow


⭐ If you like this project

Give it a ⭐ on GitHub!

📬 Contact

K. Siddhartha
📧 karnesiddhartha04@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/karne-siddhartha-163bb1369
