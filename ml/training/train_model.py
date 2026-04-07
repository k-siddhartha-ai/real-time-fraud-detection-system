"""
Train real fraud detection model using Kaggle PaySim dataset
Industry-ready clean version
"""

import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier


# ---------------- CONFIG ---------------- #

DATA_PATH = Path("data/fraud.csv")   # ✅ changed
MODEL_PATH = Path("ml/models/fraud_model.pkl")
RANDOM_STATE = 42


# ---------------- LOAD DATA ---------------- #

def load_data():
    print("Loading dataset...")

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Optional: use smaller sample if laptop slow
    # df = df.sample(200000, random_state=RANDOM_STATE)

    print("Dataset shape:", df.shape)
    return df


# ---------------- PREPROCESS ---------------- #

def preprocess(df):
    print("Preprocessing...")

    # ✅ PaySim meaningful features
    df = df[[
        "amount",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest",
        "isFraud"
    ]]

    X = df.drop("isFraud", axis=1)
    y = df["isFraud"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y
    )

    return X_train, X_test, y_train, y_test, scaler


# ---------------- TRAIN ---------------- #

def train(X_train, y_train):
    print("Handling imbalance using SMOTE...")

    smote = SMOTE(random_state=RANDOM_STATE)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    print("Training XGBoost model...")

    model = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    model.fit(X_resampled, y_resampled)
    return model


# ---------------- EVALUATE ---------------- #

def evaluate(model, X_test, y_test):
    print("Evaluating...\n")

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    print("Classification Report:\n")
    print(classification_report(y_test, preds))

    print("ROC AUC Score:", roc_auc_score(y_test, probs))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, preds))


# ---------------- SAVE ---------------- #

def save_model(model, scaler):
    print("\nSaving model...")

    bundle = {
        "model": model,
        "scaler": scaler
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(bundle, MODEL_PATH)

    print("Model saved at", MODEL_PATH)


# ---------------- MAIN ---------------- #

def main():
    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
    model = train(X_train, y_train)
    evaluate(model, X_test, y_test)
    save_model(model, scaler)


if __name__ == "__main__":
    main()
