import os
import pandas as pd
import joblib

DATA_DIR = "storage_data"
os.makedirs(DATA_DIR, exist_ok=True)

DATASET_PATH = os.path.join(DATA_DIR, "dataset.csv")
MODEL_PATH = os.path.join(DATA_DIR, "model.pkl")
METRICS_PATH = os.path.join(DATA_DIR, "metrics.pkl")

def save_dataset(df: pd.DataFrame):
    df.to_csv(DATASET_PATH, index=False)

def load_dataset() -> pd.DataFrame:
    if not os.path.exists(DATASET_PATH):
        raise ValueError("No dataset saved on disk")
    return pd.read_csv(DATASET_PATH, parse_dates=["synthetic_timestamp"])

def save_model(model, metrics=None):
    joblib.dump(model, MODEL_PATH)
    if metrics:
        joblib.dump(metrics, METRICS_PATH)

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise ValueError("No model saved on disk")
    return joblib.load(MODEL_PATH)

def load_metrics():
    if not os.path.exists(METRICS_PATH):
        return None
    return joblib.load(METRICS_PATH)
