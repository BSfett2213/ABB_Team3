from datetime import datetime, timedelta
import pandas as pd

def add_synthetic_timestamps(df: pd.DataFrame, start_time=None) -> pd.DataFrame:
    # adds timestamp to each row, with 1 sec time increment
    if "synthetic_timestamp" not in df.columns:
        if start_time is None:
            start_time = datetime(2021, 1, 1, 0, 0, 0)
        df["synthetic_timestamp"] = [
            start_time + timedelta(seconds=i) for i in range(len(df))
        ]
    return df
