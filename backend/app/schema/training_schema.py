from pydantic import BaseModel
from datetime import date

class TrainingRequest(BaseModel):
    trainStart: date
    trainEnd: date
    testStart: date
    testEnd: date

class TrainingResult(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: dict
    charts: dict  # can hold base64-encoded images
