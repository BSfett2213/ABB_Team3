from fastapi import APIRouter, HTTPException
from backend.app.schema.daterange_schema import DateRangeRequest
from backend.app.services import validation_service

router = APIRouter()

@router.post("/validate")
async def validate_date_ranges(request: DateRangeRequest):
    #     Validate training/testing/simulation date ranges.
    try:
        result = validation_service.validate_ranges(request.dict())
        return {"status": "success", "validation": result}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
