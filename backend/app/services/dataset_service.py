import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta

# in-memory storage
DATASET = None

def process_dataset(file):
    # Process CSV, add timestamp if missing, read/verify if CSV is uploaded
    global DATASET

    contents = file.file.read()
    df = pd.read_csv(BytesIO(contents))

    # Validate schema
    if "Response" not in df.columns:
        raise ValueError("Dataset must contain 'Response' column")

    # Add timestamps if missing
    if "synthetic_timestamp" not in df.columns:
        start_time = datetime(2021, 1, 1, 0, 0, 0)
        df["synthetic_timestamp"] = [
            start_time + timedelta(seconds=i) for i in range(len(df))
        ]
    DATASET = df

    # Prepare metadata
    metadata = {
        "total_records": len(df),
        "total_columns": len(df.columns),
        "pass_rate": round((df["Response"].sum() / len(df)) * 100, 2),
        "start_timestamp": str(df["synthetic_timestamp"].min()),
        "end_timestamp": str(df["synthetic_timestamp"].max())
    }
    return metadata

def get_dataset():
    # read curr data
    if DATASET is None:
        raise ValueError("No dataset uploaded yet")
    return DATASET
