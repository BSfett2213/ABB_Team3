from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import dataset_service

router = APIRouter()

@router.post("/")
async def upload_dataset(file: UploadFile = File(...)):
    # uploads dataset, validates it's schema and adds timestamps as instructed

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="File must be a CSV")

    try:
        metadata = dataset_service.process_dataset(file)
        return {"status": "success", "metadata": metadata}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
