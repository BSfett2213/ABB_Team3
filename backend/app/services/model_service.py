import requests
from app.config import ML_SERVICE_URL

def train_and_evaluate(request):
    """
    Forward training request to ML service.
    """
    url = f"{ML_SERVICE_URL}/train-model"
    response = requests.post(url, json=request)

    if response.status_code != 200:
        raise ValueError(f"ML service error: {response.text}")

    return response.json()
