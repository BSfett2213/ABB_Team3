"""
Simple in-memory storage for dataset and models.
Not persistent – resets when the backend restarts.
"""

DATASET = None
TRAINED_MODEL = None
METRICS = None

def save_dataset(df):
    global DATASET
    DATASET = df

def get_dataset():
    if DATASET is None:
        raise ValueError("No dataset stored in memory")
    return DATASET

def save_model(model, metrics=None):
    global TRAINED_MODEL, METRICS
    TRAINED_MODEL = model
    METRICS = metrics

def get_model():
    if TRAINED_MODEL is None:
        raise ValueError("No trained model stored in memory")
    return TRAINED_MODEL

def get_metrics():
    return METRICS
