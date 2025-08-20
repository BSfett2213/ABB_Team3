from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from xgboost import XGBClassifier

app = FastAPI(title="ML Service")

MODEL_PATH = "model.pkl"
FEATURES_PATH = "features.pkl"

class TrainRequest(BaseModel):
    trainStart: str
    trainEnd: str
    testStart: str
    testEnd: str


class PredictRequest(BaseModel):
    data: Dict

DATASET = None

def load_dataset():
    global DATASET
    if DATASET is None:
        raise ValueError("Dataset not available in ML service")
    return DATASET


# endpoint for loading data
@app.post("/load-dataset")
def load_dataset_from_backend(dataset: List[Dict]):
    # load dataset for training after adding timestamp
    global DATASET
    DATASET = pd.DataFrame(dataset)
    return {"status": "Dataset loaded into ML service", "records": len(DATASET)}


# endpoint for training model
@app.post("/train-model")
def train_model(request: TrainRequest):
    try:
        df = load_dataset()

        # set training and testing sets
        train_df = df[(df["synthetic_timestamp"] >= request.trainStart) &
                      (df["synthetic_timestamp"] <= request.trainEnd)]
        test_df = df[(df["synthetic_timestamp"] >= request.testStart) &
                     (df["synthetic_timestamp"] <= request.testEnd)]

        if train_df.empty or test_df.empty:
            raise HTTPException(status_code=400, detail="Invalid date ranges for training/testing")

        X_train = train_df.drop(columns=["Response", "synthetic_timestamp"])
        y_train = train_df["Response"]

        X_test = test_df.drop(columns=["Response", "synthetic_timestamp"])
        y_test = test_df["Response"]

        # Train simple model (XGBoost)
        model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
        model.fit(X_train, y_train)

        # save model
        joblib.dump(model, MODEL_PATH)
        joblib.dump(list(X_train.columns), FEATURES_PATH)

        # eval model performance
        y_pred = model.predict(X_test)

        metrics = {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred)),
            "recall": float(recall_score(y_test, y_pred)),
            "f1_score": float(f1_score(y_test, y_pred)),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }

        return {"status": "success", "metrics": metrics}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# endpoint for predictions
@app.post("/predict")
def predict(req: PredictRequest):
    try:
        if not os.path.exists(MODEL_PATH):
            raise HTTPException(status_code=400, detail="Model not trained yet")

        model = joblib.load(MODEL_PATH)
        features = joblib.load(FEATURES_PATH)

        df = pd.DataFrame([req.data])
        df = df.reindex(columns=features, fill_value=0)

        prediction = model.predict(df)[0]
        proba = model.predict_proba(df)[0][prediction]

        return {
            "timestamp": req.data.get("synthetic_timestamp", ""),
            "sample_id": req.data.get("ID", ""),
            "prediction": "Pass" if prediction == 1 else "Fail",
            "confidence": round(float(proba) * 100, 2),
            "parameters": {k: v for k, v in req.data.items() if k not in ["Response", "synthetic_timestamp"]}
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
