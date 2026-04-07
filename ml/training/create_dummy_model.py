import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Create dummy training data
X = np.array([
    [1000, 5000, 4200],
    [200, 3000, 2800],
    [5000, 10000, 2000],
    [50, 1000, 950]
])

y = np.array([0, 0, 1, 0])  # fraud labels

# Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# Ensure models folder exists
MODEL_PATH = "ml/models/fraud_model.pkl"
os.makedirs("ml/models", exist_ok=True)

# Save model
joblib.dump(model, MODEL_PATH)

print("Dummy model created successfully.")
