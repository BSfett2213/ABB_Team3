from fastapi import APIRouter, HTTPException
from app.schemas.training_schema import TrainingRequest
from app.services import model_service

router = APIRouter()

@router.post("/")
async def train_model(request: TrainingRequest):
    # starts training process
    try:
        results = model_service.train_and_evaluate(request.dict())
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
