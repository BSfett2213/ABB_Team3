import time
import json
import requests
from app.services.dataset_service import get_dataset
from app.config import ML_SERVICE_URL

def run_simulation(request):
    # gets preds
    df = get_dataset()

    start = request["simulationStart"]
    end = request["simulationEnd"]

    sim_df = df[(df["synthetic_timestamp"] >= start) &
                (df["synthetic_timestamp"] <= end)]

    url = f"{ML_SERVICE_URL}/predict"

    for _, row in sim_df.iterrows():
        # Call ML service for prediction
        payload = row.to_dict()
        response = requests.post(url, json=payload)
        result = response.json()

        yield json.dumps(result) + "\n"  # stream as JSON line
        time.sleep(1)  # 1 record per second
