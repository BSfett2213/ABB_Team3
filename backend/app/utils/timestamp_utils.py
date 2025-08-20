from datetime import datetime, timedelta
import pandas as pd

def add_synthetic_timestamps(df: pd.DataFrame, start_time=None) -> pd.DataFrame:
    """
    Add a synthetic timestamp column if not already present.
    Increments by 1 second per row.
    """
    if "synthetic_timestamp" not in df.columns:
        if start_time is None:
            start_time = datetime(2021, 1, 1, 0, 0, 0)
        df["synthetic_timestamp"] = [
            start_time + timedelta(seconds=i) for i in range(len(df))
        ]
    return df
